import React, {useCallback, useRef, useState, useMemo, useEffect} from 'react';
import PropTypes from 'prop-types';
import * as evaluate from 'static-eval';
import * as esprima from 'esprima';
import {
    equals,
    has,
    isEmpty,
    map,
    mapObjIndexed,
    memoizeWith,
    pick,
    omit,
    includes,
    assoc,
    assocPath,
} from 'ramda';
import {
    propTypes as _propTypes,
    defaultProps as _defaultProps,
    apiGetters,
} from '../components/AgGrid.react';
import {
    COLUMN_DANGEROUS_FUNCTIONS,
    COLUMN_MAYBE_FUNCTIONS,
    COLUMN_MAYBE_FUNCTIONS_NO_PARAMS,
    COLUMN_ARRAY_NESTED_FUNCTIONS,
    COLUMN_NESTED_FUNCTIONS,
    GRID_MAYBE_FUNCTIONS,
    GRID_MAYBE_FUNCTIONS_NO_PARAMS,
    GRID_ONLY_FUNCTIONS,
    GRID_COLUMN_CONTAINERS,
    GRID_NESTED_FUNCTIONS,
    OBJ_OF_FUNCTIONS,
    COLUMN_NESTED_OR_OBJ_OF_FUNCTIONS,
    PASSTHRU_PROPS,
    PROPS_NOT_FOR_AG_GRID,
    GRID_DANGEROUS_FUNCTIONS,
    OMIT_PROP_RENDER,
    OBJ_MAYBE_FUNCTION_OR_MAP_MAYBE_FUNCTIONS,
} from '../utils/propCategories';
import debounce from '../utils/debounce';

import MarkdownRenderer from '../renderers/markdownRenderer';
import RowMenuRenderer from '../renderers/rowMenuRenderer';
import {customFunctions} from '../renderers/customFunctions';

import {AgGridReact, useGridFilter} from 'ag-grid-react';

// d3 imports
import * as d3Format from 'd3-format';
import * as d3Time from 'd3-time';
import * as d3TimeFormat from 'd3-time-format';

const d3 = {...d3Format, ...d3Time, ...d3TimeFormat};

// Rate-limit for resizing columns when grid div is resized
const RESIZE_DEBOUNCE_MS = 200;

// Rate-limit for updating columnState when interacting with the grid
const COL_RESIZE_DEBOUNCE_MS = 500;

// Time between syncing cell value changes with Dash
const CELL_VALUE_CHANGED_DEBOUNCE_MS = 1;

const xssMessage = (context) => {
    console.error(
        context,
        'Blocked a string that AG Grid would evaluate, to prevent XSS attacks. If you really want this, use dangerously_allow_code'
    );
};

const NO_CONVERT_PROPS = [...PASSTHRU_PROPS, ...PROPS_NOT_FOR_AG_GRID];

const dash_clientside = window.dash_clientside || {};

const agGridRefs = {};

apiGetters.getApi = (id) => agGridRefs[stringifyId(id)]?.api;

const eventBus = {
    listeners: {},
    on(id, targetId, callback) {
        if (!(id in eventBus.listeners)) {
            eventBus.listeners[id] = {};
        }
        eventBus.listeners[id][targetId] = callback;
    },
    dispatch(targetId) {
        for (const id in eventBus.listeners) {
            if (targetId in eventBus.listeners[id]) {
                eventBus.listeners[id][targetId]();
            }
        }
    },
    remove(id) {
        delete eventBus.listeners[id];
    },
};

function stringifyId(id) {
    if (typeof id !== 'object') {
        return id;
    }
    const stringifyVal = (v) => (v && v.wild) || JSON.stringify(v);
    const parts = Object.keys(id)
        .sort()
        .map((k) => JSON.stringify(k) + ':' + stringifyVal(id[k]));
    return '{' + parts.join(',') + '}';
}

function usePrevious(value) {
    const ref = useRef();

    useEffect(() => {
        setTimeout(() => {
            ref.current = value;
        }, 1);
    }, [value]);

    return ref.current;
}

export function DashAgGrid(props) {
    const active = useRef(true);

    // const customSetProps = props.setProps;
    const customSetProps = useCallback(
        (propsToSet) => {
            if (active.current) {
                props.setProps(propsToSet);
            }
        },
        [props.setProps]
    );

    const setEventData = useCallback(
        (data) => {
            const timestamp = Date.now();
            customSetProps({
                eventData: {
                    data,
                    timestamp,
                },
            });
        },
        [customSetProps]
    );

    const parseFunction = useMemo(
        () =>
            memoizeWith(String, (funcString) => {
                const parsedCondition =
                    esprima.parse(funcString).body[0].expression;
                const context = {
                    d3,
                    dash_clientside,
                    ...customFunctions,
                    ...window.dashAgGridFunctions,
                };
                return (params) =>
                    evaluate(parsedCondition, {params, ...context});
            }),
        []
    );

    const parseFunctionEvent = useMemo(
        () =>
            memoizeWith(String, (funcString) => {
                const parsedCondition =
                    esprima.parse(funcString).body[0].expression;
                const context = {
                    d3,
                    dash_clientside,
                    ...customFunctions,
                    ...window.dashAgGridFunctions,
                    setGridProps: customSetProps,
                    setEventData: setEventData,
                };
                return (params) =>
                    evaluate(parsedCondition, {params, ...context});
            }),
        [customSetProps, setEventData]
    );

    const parseFunctionNoParams = useMemo(
        () =>
            memoizeWith(String, (funcString) => {
                const parsedCondition =
                    esprima.parse(funcString).body[0].expression;
                const context = {
                    d3,
                    ...customFunctions,
                    ...window.dashAgGridFunctions,
                };
                return evaluate(parsedCondition, context);
            }),
        []
    );

    /**
     * @params AG-Grid Styles rules attribute.
     * Cells: https://www.ag-grid.com/react-grid/cell-styles/#cell-style-cell-class--cell-class-rules-params
     * Rows: https://www.ag-grid.com/react-grid/row-styles/#row-style-row-class--row-class-rules-params
     */
    const handleDynamicStyle = useCallback(
        (cellStyle) => {
            const {styleConditions, defaultStyle} = cellStyle;
            const _defaultStyle = defaultStyle || null;

            if (styleConditions && styleConditions.length) {
                const tests = styleConditions.map(({condition, style}) => ({
                    test: parseFunction(condition),
                    style,
                }));
                return (params) => {
                    for (const {test, style} of tests) {
                        if (params) {
                            if (params.node.id && params.node.id !== null) {
                                if (test(params)) {
                                    return style;
                                }
                            }
                        }
                    }
                    return _defaultStyle;
                };
            }

            return _defaultStyle;
        },
        [parseFunction]
    );

    const generateRenderer = useCallback(
        (Renderer) => {
            const {dangerously_allow_code} = props;

            return (cellProps) => (
                <Renderer
                    setData={(value) => {
                        customSetProps({
                            cellRendererData: {
                                value,
                                colId: cellProps.column.colId,
                                rowIndex: cellProps.node.sourceRowIndex,
                                rowId: cellProps.node.id,
                                timestamp: Date.now(),
                            },
                        });
                    }}
                    dangerously_allow_code={dangerously_allow_code}
                    {...cellProps}
                ></Renderer>
            );
        },
        [props.dangerously_allow_code, customSetProps]
    );

    const customComponents = window.dashAgGridComponentFunctions || {};
    const newComponents = map(generateRenderer, customComponents);

    const [gridApi, setGridApi] = useState(null);
    const [, forceRerender] = useState({});
    const [openGroups, setOpenGroups] = useState({});
    const [columnState_push, setColumnState_push] = useState(true);
    const [rowTransactionState, setRowTransactionState] = useState(null);

    const components = useMemo(
        () => ({
            rowMenu: generateRenderer(RowMenuRenderer),
            markdown: generateRenderer(MarkdownRenderer),
            ...newComponents,
        }),
        [generateRenderer, newComponents]
    );

    const prevProps = usePrevious(props);
    const prevGridApi = usePrevious(gridApi);

    const convertedPropCache = useRef({});

    const selectionEventFired = useRef(false);
    const pauseSelections = useRef(false);
    const reference = useRef();
    const dataUpdates = useRef(false);
    const getDetailParams = useRef();
    const getRowsParams = useRef(null);
    const pendingCellValueChanges = useRef(null);

    const onPaginationChanged = useCallback(() => {
        if (gridApi && !gridApi?.isDestroyed()) {
            customSetProps({
                paginationInfo: {
                    isLastPageFound: gridApi.paginationIsLastPageFound(),
                    pageSize: gridApi.paginationGetPageSize(),
                    currentPage: gridApi.paginationGetCurrentPage(),
                    totalPages: gridApi.paginationGetTotalPages(),
                    rowCount: gridApi.paginationGetRowCount(),
                },
            });
        }
    }, [gridApi, customSetProps]);

    const setSelection = useCallback(
        (selection) => {
            const {getRowId} = props;
            if (gridApi && selection && !gridApi?.isDestroyed()) {
                pauseSelections.current = true;
                const nodeData = [];
                if (has('function', selection)) {
                    const test = parseFunction(selection.function);

                    gridApi.forEachNode((node) => {
                        if (test(node)) {
                            nodeData.push(node);
                        }
                    });
                } else if (has('ids', selection)) {
                    const mapId = {};
                    selection.ids.forEach((id) => {
                        mapId[id] = true;
                    });
                    gridApi.forEachNode((node) => {
                        if (mapId[node.id]) {
                            nodeData.push(node);
                        }
                    });
                } else {
                    if (selection.length) {
                        if (getRowId) {
                            const parsedCondition = esprima.parse(
                                getRowId.replaceAll('params.data.', '')
                            ).body[0].expression;
                            const mapId = {};
                            selection.forEach((params) => {
                                mapId[evaluate(parsedCondition, params)] = true;
                            });
                            gridApi.forEachNode((node) => {
                                if (mapId[node.id]) {
                                    nodeData.push(node);
                                }
                            });
                        } else {
                            gridApi.forEachNode((node) => {
                                if (includes(node.data, selection)) {
                                    nodeData.push(node);
                                }
                            });
                        }
                    }
                }
                gridApi.deselectAll();
                gridApi.setNodesSelected({
                    nodes: nodeData,
                    newValue: true,
                });
                setTimeout(() => {
                    pauseSelections.current = false;
                }, 1);
            }
        },
        [gridApi, props.getRowId, parseFunction]
    );

    const memoizeOne = useCallback(
        (converter, obj, target) => {
            const cache = convertedPropCache.current[target];
            if (cache && obj === cache[0]) {
                return cache[1];
            }
            const result = converter(obj, target);
            convertedPropCache.current[target] = [obj, result];
            return result;
        },
        [convertedPropCache]
    );

    const convertFunction = useCallback(
        (func) => {
            // TODO: do we want this? ie allow the form `{function: <string>}` even when
            // we're expecting just a string?
            if (has('function', func)) {
                return convertFunction(func.function);
            }

            try {
                if (typeof func !== 'string') {
                    throw new Error(
                        'tried to parse non-string as function',
                        func
                    );
                }
                return parseFunction(func);
            } catch (err) {
                console.log(err);
            }
            return '';
        },
        [parseFunction]
    );

    const convertFunctionNoParams = useCallback(
        (func) => {
            // TODO: do we want this? ie allow the form `{function: <string>}` even when
            // we're expecting just a string?
            if (has('function', func)) {
                return convertFunctionNoParams(func.function);
            }

            try {
                if (typeof func !== 'string') {
                    throw new Error(
                        'tried to parse non-string as function',
                        func
                    );
                }
                return parseFunctionNoParams(func);
            } catch (err) {
                console.log(err);
            }
            return '';
        },
        [parseFunctionNoParams]
    );

    const convertMaybeFunction = useCallback(
        (maybeFunc, stringsEvalContext) => {
            if (has('function', maybeFunc)) {
                return convertFunction(maybeFunc.function);
            }

            if (
                stringsEvalContext &&
                typeof maybeFunc === 'string' &&
                !props.dangerously_allow_code
            ) {
                xssMessage(stringsEvalContext);
                return null;
            }
            return maybeFunc;
        },
        [props.dangerously_allow_code, convertFunction]
    );

    const convertMaybeFunctionNoParams = useCallback(
        (maybeFunc, stringsEvalContext) => {
            if (has('function', maybeFunc)) {
                return convertFunctionNoParams(maybeFunc.function);
            }

            if (
                stringsEvalContext &&
                typeof maybeFunc === 'string' &&
                !props.dangerously_allow_code
            ) {
                xssMessage(stringsEvalContext);
                return null;
            }
            return maybeFunc;
        },
        [props.dangerously_allow_code, convertFunctionNoParams]
    );

    const suppressGetDetail = useCallback((colName) => {
        return (params) => {
            params.successCallback(params.data[colName]);
        };
    }, []);

    const callbackGetDetail = useCallback((params) => {
        const {data} = params;
        getDetailParams.current = params;
        // Adding the current time in ms forces Dash to trigger a callback
        // when the same row is closed and re-opened.
        customSetProps({
            getDetailRequest: {data: data, requestTime: Date.now()},
        });
    }, []);

    const convertCol = useCallback(
        (columnDef) => {
            if (typeof columnDef === 'function') {
                return columnDef;
            }

            return mapObjIndexed((value, target) => {
                if (
                    target === 'cellStyle' &&
                    (has('styleConditions', value) ||
                        has('defaultStyle', value))
                ) {
                    return handleDynamicStyle(value);
                }
                if (OBJ_OF_FUNCTIONS[target]) {
                    return map(convertFunction, value);
                }
                if (COLUMN_DANGEROUS_FUNCTIONS[target]) {
                    // the second argument tells convertMaybeFunction
                    // that a plain string is dangerous,
                    // and provides the context for error reporting
                    const field = columnDef.field || columnDef.headerName;
                    return convertMaybeFunction(value, {target, field});
                }
                if (COLUMN_MAYBE_FUNCTIONS[target]) {
                    return convertMaybeFunction(value);
                }
                if (COLUMN_MAYBE_FUNCTIONS_NO_PARAMS[target]) {
                    return convertMaybeFunctionNoParams(value);
                }
                if (
                    COLUMN_ARRAY_NESTED_FUNCTIONS[target] &&
                    Array.isArray(value)
                ) {
                    return value.map((c) => {
                        if (typeof c === 'object') {
                            return convertCol(c);
                        }
                        return c;
                    });
                }
                if (OBJ_MAYBE_FUNCTION_OR_MAP_MAYBE_FUNCTIONS[target]) {
                    if ('function' in value) {
                        if (typeof value.function === 'string') {
                            return convertMaybeFunctionNoParams(value);
                        }
                    }
                    return map((v) => {
                        if (typeof v === 'object') {
                            if (typeof v.function === 'string') {
                                return convertMaybeFunctionNoParams(v);
                            }
                            return convertCol(v);
                        }
                        return v;
                    }, value);
                }
                if (
                    COLUMN_NESTED_FUNCTIONS[target] &&
                    typeof value === 'object'
                ) {
                    return convertCol(value);
                }
                if (COLUMN_NESTED_OR_OBJ_OF_FUNCTIONS[target]) {
                    if (has('function', value)) {
                        return convertMaybeFunction(value);
                    }
                    return convertCol(value);
                }
                // not one of those categories - pass it straight through
                return value;
            }, columnDef);
        },
        [
            handleDynamicStyle,
            convertFunction,
            convertMaybeFunction,
            convertMaybeFunctionNoParams,
        ]
    );

    const convertOneRef = useRef();
    const convertAllPropsRef = useRef();

    const convertOne = useCallback(
        (value, target) => {
            if (value) {
                if (target === 'columnDefs') {
                    return value.map(convertCol);
                }
                if (GRID_COLUMN_CONTAINERS[target]) {
                    return convertCol(value);
                }
                if (OBJ_MAYBE_FUNCTION_OR_MAP_MAYBE_FUNCTIONS[target]) {
                    if ('function' in value) {
                        if (typeof value.function === 'string') {
                            return convertMaybeFunctionNoParams(value);
                        }
                    }
                    return mapObjIndexed((v) => {
                        if (typeof v === 'object') {
                            if ('function' in v) {
                                if (typeof v.function === 'string') {
                                    return convertMaybeFunctionNoParams(v);
                                }
                            } else {
                                return convertCol(v);
                            }
                        }
                        return v;
                    }, value);
                }
                if (GRID_NESTED_FUNCTIONS[target]) {
                    let adjustedVal = value;
                    if ('suppressCallback' in value) {
                        adjustedVal = {
                            ...adjustedVal,
                            getDetailRowData: value.suppressCallback
                                ? suppressGetDetail(value.detailColName)
                                : callbackGetDetail,
                        };
                    }
                    if ('detailGridOptions' in value) {
                        adjustedVal = assocPath(
                            ['detailGridOptions', 'components'],
                            components,
                            adjustedVal
                        );
                    }
                    return convertAllPropsRef.current(adjustedVal);
                }
                if (GRID_DANGEROUS_FUNCTIONS[target]) {
                    return convertMaybeFunctionNoParams(value, {prop: target});
                }
                if (target === 'getRowId') {
                    return convertFunction(value);
                }
                if (
                    target === 'getRowStyle' &&
                    (has('styleConditions', value) ||
                        has('defaultStyle', value))
                ) {
                    return handleDynamicStyle(value);
                }
                if (OBJ_OF_FUNCTIONS[target]) {
                    return map(convertFunction, value);
                }
                if (GRID_ONLY_FUNCTIONS[target]) {
                    return convertFunction(value);
                }
                if (GRID_MAYBE_FUNCTIONS[target]) {
                    return convertMaybeFunction(value);
                }
                if (GRID_MAYBE_FUNCTIONS_NO_PARAMS[target]) {
                    return convertMaybeFunctionNoParams(value);
                }

                return value;
            }
            return value;
        },
        [
            convertCol,
            convertMaybeFunctionNoParams,
            suppressGetDetail,
            callbackGetDetail,
            components,
            convertAllPropsRef.current,
            convertFunction,
            handleDynamicStyle,
            convertMaybeFunction,
        ]
    );

    const convertAllProps = useCallback(
        (props) => {
            return mapObjIndexed(
                (value, target) =>
                    memoizeOne(convertOneRef.current, value, target),
                props
            );
        },
        [memoizeOne, convertOneRef.current]
    );

    convertOneRef.current = convertOne;
    convertAllPropsRef.current = convertAllProps;

    const virtualRowData = useCallback(() => {
        const {rowModelType} = props;
        const virtualRowData = [];
        if (rowModelType === 'clientSide' && gridApi) {
            gridApi.forEachNodeAfterFilterAndSort((node) => {
                if (node.data) {
                    virtualRowData.push(node.data);
                }
            });
        }
        return virtualRowData;
    }, [props.rowModelType, gridApi]);

    const onFilterChanged = useCallback(() => {
        const {rowModelType} = props;
        if (!gridApi) {
            return;
        }
        const filterModel = gridApi.getFilterModel();
        const propsToSet = {filterModel};
        if (rowModelType === 'clientSide') {
            propsToSet.virtualRowData = virtualRowData();
        }

        customSetProps(propsToSet);
    }, [props.rowModelType, gridApi, virtualRowData, customSetProps]);

    const getRowData = useCallback(() => {
        const newRowData = [];
        gridApi.forEachLeafNode((node) => {
            newRowData.push(node.data);
        });
        return newRowData;
    }, [gridApi]);

    const syncRowData = useCallback(() => {
        const {rowData} = props;
        if (rowData) {
            const virtualRowDataResult = virtualRowData();
            const newRowData = getRowData();
            if (rowData !== newRowData) {
                customSetProps({
                    rowData: newRowData,
                    virtualRowData: virtualRowDataResult,
                });
            } else {
                customSetProps({virtualRowData: virtualRowDataResult});
            }
        }
    }, [props.rowData, virtualRowData, getRowData, customSetProps]);

    const onSortChanged = useCallback(() => {
        const {rowModelType} = props;
        const propsToSet = {};
        if (rowModelType === 'clientSide') {
            propsToSet.virtualRowData = virtualRowData();
        }
        if (!gridApi.isDestroyed()) {
            propsToSet.columnState = JSON.parse(
                JSON.stringify(gridApi.getColumnState())
            );
        }
        customSetProps(propsToSet);
    }, [props.rowModelType, virtualRowData, gridApi, customSetProps]);

    const onRowDataUpdated = useCallback(() => {
        // Handles preserving existing selections when rowData is updated in a callback
        const {selectedRows, rowData, rowModelType, filterModel} = props;

        if (gridApi && !gridApi?.isDestroyed()) {
            dataUpdates.current = true;
            pauseSelections.current = true;
            setSelection(selectedRows);

            if (rowData && rowModelType === 'clientSide') {
                const virtualRowDataResult = virtualRowData();

                customSetProps({virtualRowData: virtualRowDataResult});
            }

            // When the rowData is updated, reopen any row groups if they previously existed in the table
            // Iterate through all nodes in the grid. Unfortunately there's no way to iterate through only nodes representing groups
            if (!isEmpty(openGroups)) {
                gridApi.forEachNode((node) => {
                    // Check if it's a group row based on whether it has the __hasChildren prop
                    if (node.__hasChildren) {
                        // If the key for the node (i.e. the group name) is the same as an
                        if (openGroups[node.key]) {
                            gridApi.setRowNodeExpanded(node, true);
                        }
                    }
                });
            }
            if (!isEmpty(filterModel)) {
                gridApi.setFilterModel(filterModel);
            }
            setTimeout(() => {
                dataUpdates.current = false;
            }, 1);
        }
    }, [
        props.selectedRows,
        props.rowData,
        props.rowModelType,
        props.filterModel,
        gridApi,
        openGroups,
        setSelection,
        virtualRowData,
        customSetProps,
    ]);

    const onRowGroupOpened = useCallback((e) => {
        setOpenGroups((prevOpenGroups) =>
            e.expanded
                ? assoc(e.node.key, 1, prevOpenGroups)
                : omit([e.node.key], prevOpenGroups)
        );
    }, []);

    const onSelectionChanged = useCallback(() => {
        setTimeout(() => {
            if (!pauseSelections.current) {
                const selectedRows = gridApi.getSelectedRows();
                if (!equals(selectedRows, props.selectedRows)) {
                    // Flag that the selection event was fired
                    selectionEventFired.current = true;
                    customSetProps({selectedRows});
                }
            }
        }, 1);
    }, [gridApi, props.selectedRows, customSetProps]);

    const isDatasourceLoadedForInfiniteScrolling = useCallback(() => {
        return (
            props.rowModelType === 'infinite' &&
            getRowsParams.current &&
            props.getRowsResponse
        );
    }, [props.rowModelType, getRowsParams.current, props.getRowsResponse]);

    const getDatasource = useCallback(() => {
        return {
            getRows(params) {
                getRowsParams.current = params;
                customSetProps({getRowsRequest: params});
            },

            destroy() {
                getRowsParams.current = null;
            },
        };
    }, [getRowsParams.current, customSetProps]);

    const applyRowTransaction = useCallback(
        (data, gridApiParam = gridApi) => {
            const {selectedRows} = props;
            if (data.async === false) {
                gridApiParam.applyTransaction(data);
                if (selectedRows) {
                    setSelection(selectedRows);
                }
            } else {
                gridApiParam.applyTransactionAsync(data);
            }
        },
        [gridApi, props.selectedRows, setSelection]
    );

    const onGridReady = useCallback(
        (params) => {
            // Applying Infinite Row Model
            // see: https://www.ag-grid.com/javascript-grid/infinite-scrolling/
            const {rowModelType, eventListeners} = props;

            if (rowModelType === 'infinite') {
                params.api.setGridOption('datasource', getDatasource());
            }

            if (eventListeners) {
                Object.entries(eventListeners).map(([key, v]) => {
                    v.map((func) => {
                        params.api.addEventListener(
                            key,
                            parseFunctionEvent(func)
                        );
                    });
                });
            }
            setGridApi(params.api);
        },
        [
            props.rowModelType,
            props.eventListeners,
            getDatasource,
            parseFunctionEvent,
            setGridApi,
        ]
    );

    const onCellClicked = useCallback(
        ({value, column: {colId}, rowIndex, node}) => {
            const timestamp = Date.now();
            customSetProps({
                cellClicked: {
                    value,
                    colId,
                    rowIndex,
                    rowId: node.id,
                    timestamp,
                },
            });
        },
        [customSetProps]
    );

    const onCellDoubleClicked = useCallback(
        ({value, column: {colId}, rowIndex, node}) => {
            const timestamp = Date.now();
            customSetProps({
                cellDoubleClicked: {
                    value,
                    colId,
                    rowIndex,
                    rowId: node.id,
                    timestamp,
                },
            });
        },
        [customSetProps]
    );

    const onCellValueChanged = useCallback(
        ({oldValue, value, column: {colId}, rowIndex, data, node}) => {
            const timestamp = Date.now();
            // Collect new change.
            const newChange = {
                rowIndex,
                rowId: node.id,
                data,
                oldValue,
                value,
                colId,
                timestamp,
            };
            // Append it to current change session.
            if (!pendingCellValueChanges.current) {
                pendingCellValueChanges.current = [newChange];
            } else {
                pendingCellValueChanges.current.push(newChange);
            }
        },
        [pendingCellValueChanges.current]
    );

    const afterCellValueChanged = useCallback(() => {
        // Guard against multiple invocations of the same change session.
        if (!pendingCellValueChanges.current) {
            return;
        }
        // Send update(s) for current change session to Dash.
        const virtualRowDataResult = virtualRowData();
        customSetProps({
            cellValueChanged: pendingCellValueChanges.current,
            virtualRowData: virtualRowDataResult,
        });
        syncRowData();
        // Mark current change session as ended.
        pendingCellValueChanges.current = null;
    }, [
        pendingCellValueChanges.current,
        virtualRowData,
        customSetProps,
        syncRowData,
    ]);

    const updateColumnState = useCallback(() => {
        if (!gridApi) {
            return;
        }
        if (!gridApi.isDestroyed()) {
            var columnState = JSON.parse(
                JSON.stringify(gridApi.getColumnState())
            );

            customSetProps({
                columnState,
                updateColumnState: false,
            });
        } else {
            customSetProps({
                updateColumnState: false,
            });
        }
    }, [gridApi, customSetProps]);

    const updateColumnWidths = useCallback(
        (setColumns = true) => {
            const {columnSize, columnSizeOptions} = props;
            if (gridApi && !gridApi?.isDestroyed()) {
                const {
                    keys,
                    skipHeader,
                    defaultMinWidth,
                    defaultMaxWidth,
                    columnLimits,
                } = columnSizeOptions || {};
                if (columnSize === 'autoSize') {
                    if (keys) {
                        gridApi.autoSizeColumns(keys, skipHeader);
                    } else {
                        gridApi.autoSizeAllColumns(skipHeader);
                    }
                } else if (
                    columnSize === 'sizeToFit' ||
                    columnSize === 'responsiveSizeToFit'
                ) {
                    gridApi.sizeColumnsToFit({
                        defaultMinWidth,
                        defaultMaxWidth,
                        columnLimits,
                    });
                }
                if (columnSize !== 'responsiveSizeToFit') {
                    customSetProps({columnSize: null});
                }
                if (setColumns) {
                    updateColumnState();
                }
            }
        },
        [
            props.columnSize,
            props.columnSizeOptions,
            gridApi,
            customSetProps,
            updateColumnState,
        ]
    );

    const onDisplayedColumnsChanged = useCallback(() => {
        if (props.columnSize === 'responsiveSizeToFit') {
            updateColumnWidths();
        }
        updateColumnState();
    }, [props.columnSize, updateColumnWidths, updateColumnState]);

    const onColumnResized = useCallback(() => {
        if (props.columnSize !== 'responsiveSizeToFit') {
            updateColumnState();
        }
    }, [props.columnSize, updateColumnState]);

    const onGridSizeChanged = useCallback(() => {
        if (props.columnSize === 'responsiveSizeToFit') {
            updateColumnWidths();
        }
    }, [props.columnSize, updateColumnWidths]);

    const setColumnState = useCallback(() => {
        if (!gridApi || props.updateColumnState) {
            return;
        }

        if (columnState_push) {
            gridApi.applyColumnState({
                state: props.columnState,
                applyOrder: true,
            });
            setColumnState_push(false);
        }
    }, [gridApi, props.updateColumnState, columnState_push]);

    const exportDataAsCsv = useCallback(
        (csvExportParams, reset = true) => {
            if (!gridApi) {
                return;
            }
            gridApi.exportDataAsCsv(convertAllProps(csvExportParams));
            if (reset) {
                customSetProps({
                    exportDataAsCsv: false,
                });
            }
        },
        [gridApi, convertAllProps, customSetProps]
    );

    const paginationGoTo = useCallback(
        (reset = true) => {
            if (!gridApi) {
                return;
            }
            switch (props.paginationGoTo) {
                case 'next':
                    gridApi.paginationGoToNextPage();
                    break;
                case 'previous':
                    gridApi.paginationGoToPreviousPage();
                    break;
                case 'last':
                    gridApi.paginationGoToLastPage();
                    break;
                case 'first':
                    gridApi.paginationGoToFirstPage();
                    break;
                default:
                    gridApi.paginationGoToPage(props.paginationGoTo);
            }
            if (reset) {
                customSetProps({
                    paginationGoTo: null,
                });
            }
        },
        [gridApi, props.paginationGoTo, customSetProps]
    );

    const scrollTo = useCallback(
        (reset = true) => {
            const {scrollTo, getRowId} = props;
            if (!gridApi) {
                return;
            }
            const rowPosition = scrollTo.rowPosition
                ? scrollTo.rowPosition
                : 'top';
            if (scrollTo.rowIndex || scrollTo.rowIndex === 0) {
                gridApi.ensureIndexVisible(scrollTo.rowIndex, rowPosition);
            } else if (typeof scrollTo.rowId !== 'undefined') {
                const node = gridApi.getRowNode(scrollTo.rowId);
                gridApi.ensureNodeVisible(node, rowPosition);
            } else if (scrollTo.data) {
                if (getRowId) {
                    const parsedCondition = esprima.parse(
                        getRowId.replaceAll('params.data.', '')
                    ).body[0].expression;
                    const node = gridApi.getRowNode(
                        evaluate(parsedCondition, scrollTo.data)
                    );
                    gridApi.ensureNodeVisible(node, rowPosition);
                } else {
                    let scrolled = false;
                    gridApi.forEachNodeAfterFilterAndSort((node) => {
                        if (!scrolled && equals(node.data, scrollTo.data)) {
                            gridApi.ensureNodeVisible(node, rowPosition);
                            scrolled = true;
                        }
                    });
                }
            }
            if (scrollTo.column) {
                const columnPosition = scrollTo.columnPosition
                    ? scrollTo.columnPosition
                    : 'auto';
                gridApi.ensureColumnVisible(scrollTo.column, columnPosition);
            }
            if (reset) {
                customSetProps({
                    scrollTo: null,
                });
            }
        },
        [gridApi, props.scrollTo, props.getRowId, customSetProps]
    );

    const resetColumnState = useCallback(
        (reset = true) => {
            if (!gridApi) {
                return;
            }
            gridApi.resetColumnState();
            if (reset) {
                customSetProps({
                    resetColumnState: false,
                });
                updateColumnState();
            }
        },
        [gridApi, customSetProps, updateColumnState]
    );

    const selectAll = useCallback(
        (opts, reset = true) => {
            if (!gridApi) {
                return;
            }
            if (opts?.filtered) {
                gridApi.selectAllFiltered();
            } else {
                gridApi.selectAll();
            }
            if (reset) {
                customSetProps({
                    selectAll: false,
                });
            }
        },
        [gridApi, customSetProps]
    );

    const deselectAll = useCallback(
        (reset = true) => {
            if (!gridApi) {
                return;
            }
            gridApi.deselectAll();
            if (reset) {
                customSetProps({
                    deselectAll: false,
                });
            }
        },
        [gridApi, customSetProps]
    );

    const deleteSelectedRows = useCallback(
        (reset = true) => {
            if (!gridApi) {
                return;
            }
            const sel = gridApi.getSelectedRows();
            gridApi.applyTransaction({remove: sel});
            if (reset) {
                customSetProps({
                    deleteSelectedRows: false,
                });
                syncRowData();
            }
        },
        [gridApi, customSetProps, syncRowData]
    );

    const buildArray = useCallback((arr1, arr2) => {
        if (arr1) {
            if (!arr1.includes(arr2)) {
                return [...arr1, arr2];
            }
            return arr1;
        }
        return [JSON.parse(JSON.stringify(arr2))];
    }, []);

    const rowTransaction = useCallback(
        (data) => {
            const rowTransaction = rowTransactionState;
            if (gridApi && !gridApi?.isDestroyed()) {
                if (rowTransaction) {
                    rowTransaction.forEach(applyRowTransaction);
                    setRowTransactionState(null);
                }
                applyRowTransaction(data);
                customSetProps({
                    rowTransaction: null,
                });
                syncRowData();
            } else {
                setRowTransactionState(
                    rowTransaction
                        ? buildArray(rowTransaction, data)
                        : [JSON.parse(JSON.stringify(data))]
                );
            }
        },
        [
            rowTransactionState,
            gridApi,
            applyRowTransaction,
            setRowTransactionState,
            customSetProps,
            syncRowData,
            buildArray,
        ]
    );

    const onAsyncTransactionsFlushed = useCallback(() => {
        const {selectedRows} = props;
        if (selectedRows) {
            setSelection(selectedRows);
        }
        syncRowData();
    }, [props.selectedRows, setSelection, syncRowData]);

    // Mount and unmount effect
    useEffect(() => {
        const {id} = props;
        if (id) {
            agGridRefs[id] = reference.current;
            eventBus.dispatch(id);
        }

        return () => {
            setGridApi(null);
            active.current = false;
            if (props.id) {
                delete agGridRefs[props.id];
                eventBus.remove(props.id);
            }
        };
    }, []);

    useEffect(() => {
        // Apply selections
        if (gridApi) {
            const selectedRows = gridApi.getSelectedRows();
            if (!equals(selectedRows, props.selectedRows)) {
                setSelection(props.selectedRows);
            }
        }
    }, [props.selectedRows, gridApi]);

    // Handle gridApi initialization - basic setup
    useEffect(() => {
        if (gridApi && gridApi !== prevGridApi) {
            updateColumnWidths(false);

            // Handle pagination initialization
            if (reference.current.props.pagination) {
                onPaginationChanged();
            }
        }
    }, [gridApi, prevGridApi, updateColumnWidths, onPaginationChanged]);

    // Handle gridApi initialization - expanded groups tracking
    useEffect(() => {
        if (gridApi && gridApi !== prevGridApi) {
            const groups = {};
            gridApi.forEachNode((node) => {
                if (node.expanded) {
                    groups[node.key] = 1;
                }
            });
            setOpenGroups(groups);
        }
    }, [gridApi, prevGridApi, setOpenGroups]);

    // Handle gridApi initialization - row transactions
    useEffect(() => {
        if (gridApi && gridApi !== prevGridApi && rowTransactionState) {
            rowTransactionState.map((data) =>
                applyRowTransaction(data, gridApi)
            );
            setRowTransactionState(null);
            syncRowData();
        }
    }, [
        gridApi,
        prevGridApi,
        rowTransactionState,
        applyRowTransaction,
        setRowTransactionState,
        syncRowData,
    ]);

    // Handle gridApi initialization - filter model application
    useEffect(() => {
        if (gridApi && gridApi !== prevGridApi && !isEmpty(props.filterModel)) {
            gridApi.setFilterModel(props.filterModel);
        }
    }, [gridApi, prevGridApi, props.filterModel]);

    // Handle gridApi initialization - column state application
    useEffect(() => {
        if (gridApi && gridApi !== prevGridApi && props.columnState) {
            setColumnState();
        }
    }, [gridApi, prevGridApi, props.columnState, setColumnState]);

    // Handle gridApi initialization - finalization
    useEffect(() => {
        if (gridApi && gridApi !== prevGridApi) {
            // Hydrate virtualRowData and finalize setup
            onFilterChanged(true);
            updateColumnState();
            setColumnState_push(false);
        }
    }, [
        gridApi,
        prevGridApi,
        onFilterChanged,
        setColumnState_push,
        updateColumnState,
    ]);

    // Handle columnState push changes
    useEffect(() => {
        if (
            gridApi &&
            (!props.loading_state || prevProps?.loading_state?.is_loading)
        ) {
            const existingColumnState = gridApi.getColumnState();
            const realStateChange =
                props.columnState &&
                !equals(props.columnState, existingColumnState);

            if (realStateChange && !columnState_push) {
                setColumnState_push(true);
            }
        }
    }, [props.columnState, props.loading_state, columnState_push]);

    // Handle ID changes
    useEffect(() => {
        if (props.id !== prevProps?.id) {
            if (props.id) {
                agGridRefs[props.id] = reference.current;
                eventBus.dispatch(props.id);
            }
            if (prevProps?.id) {
                delete agGridRefs[prevProps.id];
                eventBus.remove(prevProps.id);
            }
        }
    }, [props.id]);

    // Handle infinite scrolling datasource
    useEffect(() => {
        if (isDatasourceLoadedForInfiniteScrolling()) {
            const {rowData, rowCount} = props.getRowsResponse;
            getRowsParams.current.successCallback(rowData, rowCount);
            customSetProps({getRowsResponse: null});
        }
    }, [props.getRowsResponse]);

    // Handle master detail response
    useEffect(() => {
        if (
            props.masterDetail &&
            !props.detailCellRendererParams.suppressCallback &&
            props.getDetailResponse
        ) {
            getDetailParams.current.successCallback(props.getDetailResponse);
            customSetProps({getDetailResponse: null});
        }
    }, [
        props.getDetailResponse,
        props.masterDetail,
        props.detailCellRendererParams,
    ]);

    // Handle dataUpdates reset
    useEffect(() => {
        dataUpdates.current = false;
    });

    // Handle filter model updates
    useEffect(() => {
        if (
            gridApi &&
            gridApi === prevGridApi &&
            props.filterModel &&
            gridApi.getFilterModel() !== props.filterModel
        ) {
            gridApi.setFilterModel(props.filterModel);
        }
    }, [props.filterModel, gridApi, prevGridApi]);

    // Handle pagination actions
    useEffect(() => {
        if (gridApi && (props.paginationGoTo || props.paginationGoTo === 0)) {
            paginationGoTo();
        }
    }, [props.paginationGoTo, gridApi, prevGridApi, paginationGoTo]);

    // Handle scroll actions
    useEffect(() => {
        if (gridApi && props.scrollTo) {
            scrollTo();
        }
    }, [props.scrollTo, gridApi, prevGridApi, scrollTo]);

    // Handle column size updates
    useEffect(() => {
        if (gridApi && props.columnSize) {
            updateColumnWidths();
        }
    }, [props.columnSize, gridApi, prevGridApi, updateColumnWidths]);

    // Handle column state reset
    useEffect(() => {
        if (gridApi && props.resetColumnState) {
            resetColumnState();
        }
    }, [props.resetColumnState, gridApi, prevGridApi, resetColumnState]);

    // Handle CSV export
    useEffect(() => {
        if (gridApi && props.exportDataAsCsv) {
            exportDataAsCsv(props.csvExportParams);
        }
    }, [
        props.exportDataAsCsv,
        props.csvExportParams,
        gridApi,
        prevGridApi,
        exportDataAsCsv,
    ]);

    // Handle row selection actions
    useEffect(() => {
        if (gridApi) {
            if (props.selectAll) {
                selectAll(props.selectAll);
            }
            if (props.deselectAll) {
                deselectAll();
            }
            if (props.deleteSelectedRows) {
                deleteSelectedRows();
            }
        }
    }, [
        props.selectAll,
        props.deselectAll,
        props.deleteSelectedRows,
        gridApi,
        prevGridApi,
        selectAll,
        deselectAll,
        deleteSelectedRows,
    ]);

    // Handle row transactions
    useEffect(() => {
        if (gridApi && props.rowTransaction) {
            rowTransaction(props.rowTransaction);
        }
    }, [props.rowTransaction, gridApi, prevGridApi, rowTransaction]);

    // Handle column state updates
    useEffect(() => {
        if (gridApi) {
            if (props.updateColumnState) {
                updateColumnState();
            } else if (columnState_push) {
                setColumnState();
            }
        }
    }, [
        props.updateColumnState,
        columnState_push,
        gridApi,
        prevGridApi,
        updateColumnState,
        setColumnState,
    ]);

    const {id, style, className, dashGridOptions, ...restProps} = props;
    const passingProps = pick(PASSTHRU_PROPS, restProps);
    const convertedProps = convertAllProps(
        omit(NO_CONVERT_PROPS, {...dashGridOptions, ...restProps})
    );

    let alignedGrids;
    if (dashGridOptions) {
        if ('alignedGrids' in dashGridOptions) {
            alignedGrids = [];
            const addGrid = (id) => {
                const strId = stringifyId(id);
                eventBus.on(props.id, strId, () => {
                    forceRerender({});
                });
                if (!agGridRefs[strId]) {
                    agGridRefs[strId] = {api: null};
                }
                alignedGrids.push(agGridRefs[strId]);
            };
            eventBus.remove(props.id);
            if (Array.isArray(dashGridOptions.alignedGrids)) {
                dashGridOptions.alignedGrids.map(addGrid);
            } else {
                addGrid(dashGridOptions.alignedGrids);
            }
        }
    }

    return (
        <div
            id={id}
            className={className}
            style={{
                height:
                    convertedProps.domLayout === 'autoHeight' ? null : '400px',
                width: '100%',
                ...style,
            }}
        >
            <AgGridReact
                ref={reference}
                alignedGrids={alignedGrids}
                onGridReady={onGridReady}
                onSelectionChanged={onSelectionChanged}
                onCellClicked={onCellClicked}
                onCellDoubleClicked={onCellDoubleClicked}
                onCellValueChanged={debounce(
                    afterCellValueChanged,
                    CELL_VALUE_CHANGED_DEBOUNCE_MS,
                    onCellValueChanged
                )}
                onFilterChanged={onFilterChanged}
                onSortChanged={onSortChanged}
                onRowDragEnd={onSortChanged}
                onRowDataUpdated={onRowDataUpdated}
                onRowGroupOpened={onRowGroupOpened}
                onDisplayedColumnsChanged={debounce(
                    onDisplayedColumnsChanged,
                    COL_RESIZE_DEBOUNCE_MS
                )}
                onColumnResized={debounce(
                    onColumnResized,
                    COL_RESIZE_DEBOUNCE_MS
                )}
                onAsyncTransactionsFlushed={onAsyncTransactionsFlushed}
                onPaginationChanged={onPaginationChanged}
                onGridSizeChanged={debounce(
                    onGridSizeChanged,
                    RESIZE_DEBOUNCE_MS
                )}
                components={components}
                {...passingProps}
                {...convertedProps}
            ></AgGridReact>
        </div>
    );
}

DashAgGrid.defaultProps = _defaultProps;
DashAgGrid.propTypes = {parentState: PropTypes.any, ..._propTypes};

export const propTypes = DashAgGrid.propTypes;
export const defaultProps = DashAgGrid.defaultProps;

var dagfuncs = (window.dash_ag_grid = window.dash_ag_grid || {});
dagfuncs.useGridFilter = useGridFilter;

const MemoizedAgGrid = React.memo(DashAgGrid, (prevProps, nextProps) => {
    // Check if props are equal (excluding render-specific props)
    const relevantNextProps = {...omit(OMIT_PROP_RENDER, nextProps)};
    const relevantPrevProps = {...omit(OMIT_PROP_RENDER, prevProps)};

    const isInternalChange = nextProps?.dashRenderType === 'internal';
    const propsHaveChanged = !equals(relevantNextProps, relevantPrevProps);
    const rowDataChanged = !equals(nextProps.rowData, prevProps.rowData);
    const selectedRowsChanged = !equals(
        nextProps.selectedRows,
        prevProps.selectedRows
    );

    if (
        propsHaveChanged &&
        (!isInternalChange || rowDataChanged || selectedRowsChanged)
    ) {
        return false; // Props changed, re-render
    }

    return true;
});

export default MemoizedAgGrid;
