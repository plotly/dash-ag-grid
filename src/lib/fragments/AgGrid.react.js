import React, {Component} from 'react';
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
} from 'ramda';
import {
    propTypes as _propTypes,
    defaultProps as _defaultProps,
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
} from '../utils/propCategories';
import debounce from '../utils/debounce';

import MarkdownRenderer from '../renderers/markdownRenderer';
import RowMenuRenderer from '../renderers/rowMenuRenderer';
import {customFunctions} from '../renderers/customFunctions';

import 'ag-grid-community';
import {AgGridReact} from 'ag-grid-react';

import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';
import 'ag-grid-community/styles/ag-theme-balham.css';
import 'ag-grid-community/styles/ag-theme-material.css';

// d3 imports
import * as d3Format from 'd3-format';
import * as d3Time from 'd3-time';
import * as d3TimeFormat from 'd3-time-format';
import * as d3Array from 'd3-array';
const d3 = {...d3Format, ...d3Time, ...d3TimeFormat, ...d3Array};

// Rate-limit for resizing columns when table div is resized
const RESIZE_DEBOUNCE_MS = 200;

const xssMessage = (context) => {
    console.error(
        context,
        'Blocked a string that AG Grid would evaluate, to prevent XSS attacks. If you really want this, use dangerously_allow_code'
    );
};

const NO_CONVERT_PROPS = [...PASSTHRU_PROPS, ...PROPS_NOT_FOR_AG_GRID];

function findReact(dom, traverseUp = 0) {
    const key = Object.keys(dom).find((key) => {
        return (
            key.startsWith('__reactFiber$') || // react 17+
            key.startsWith('__reactInternalInstance$')
        ); // react <17
    });
    const domFiber = dom[key];
    if (domFiber === null) {
        return null;
    }

    // react <16
    if (domFiber._currentElement) {
        let compFiber = domFiber._currentElement._owner;
        for (let i = 0; i < traverseUp; i++) {
            compFiber = compFiber._currentElement._owner;
        }
        return compFiber._instance;
    }

    // react 16+
    const getCompFiber = (fiber) => {
        // return fiber._debugOwner; // this also works, but is __DEV__ only
        let parentFiber = fiber.return;
        while (typeof parentFiber.type === 'string') {
            parentFiber = parentFiber.return;
        }
        return parentFiber;
    };
    let compFiber = getCompFiber(domFiber);
    for (let i = 0; i < traverseUp; i++) {
        compFiber = getCompFiber(compFiber);
    }
    return compFiber.stateNode;
}

export default class DashAgGrid extends Component {
    constructor(props) {
        super(props);

        this.onGridReady = this.onGridReady.bind(this);
        this.onSelectionChanged = this.onSelectionChanged.bind(this);
        this.onCellClicked = this.onCellClicked.bind(this);
        this.onCellValueChanged = this.onCellValueChanged.bind(this);
        this.onRowDataUpdated = this.onRowDataUpdated.bind(this);
        this.onFilterChanged = this.onFilterChanged.bind(this);
        this.onSortChanged = this.onSortChanged.bind(this);
        this.onRowGroupOpened = this.onRowGroupOpened.bind(this);
        this.onDisplayedColumnsChanged =
            this.onDisplayedColumnsChanged.bind(this);
        this.onGridSizeChanged = this.onGridSizeChanged.bind(this);
        this.updateColumnWidths = this.updateColumnWidths.bind(this);
        this.handleDynamicStyle = this.handleDynamicStyle.bind(this);
        this.generateRenderer = this.generateRenderer.bind(this);
        this.resetColumnState = this.resetColumnState.bind(this);
        this.exportDataAsCsv = this.exportDataAsCsv.bind(this);
        this.setSelection = this.setSelection.bind(this);
        this.memoizeOne = this.memoizeOne.bind(this);
        this.convertFunction = this.convertFunction.bind(this);
        this.convertMaybeFunction = this.convertMaybeFunction.bind(this);
        this.convertCol = this.convertCol.bind(this);
        this.convertOne = this.convertOne.bind(this);
        this.convertAllProps = this.convertAllProps.bind(this);
        this.buildArray = this.buildArray.bind(this);
        this.onAsyncTransactionsFlushed =
            this.onAsyncTransactionsFlushed.bind(this);
        this.onPaginationChanged = this.onPaginationChanged.bind(this);

        // Additional Exposure
        this.selectAll = this.selectAll.bind(this);
        this.deselectAll = this.deselectAll.bind(this);
        this.updateColumnState = this.updateColumnState.bind(this);
        this.deleteSelectedRows = this.deleteSelectedRows.bind(this);
        this.rowTransaction = this.rowTransaction.bind(this);
        this.getRowData = this.getRowData.bind(this);
        this.syncRowData = this.syncRowData.bind(this);
        this.isDatasourceLoadedForInfiniteScrolling =
            this.isDatasourceLoadedForInfiniteScrolling.bind(this);
        this.getDatasource = this.getDatasource.bind(this);
        this.applyRowTransaction = this.applyRowTransaction.bind(this);
        this.parseFunction = this.parseFunction.bind(this);

        const customComponents = window.dashAgGridComponentFunctions || {};
        const newComponents = map(this.generateRenderer, customComponents);

        this.convertedPropCache = {};

        this.state = {
            ...this.props.parentState,
            components: {
                rowMenu: this.generateRenderer(RowMenuRenderer),
                markdown: this.generateRenderer(MarkdownRenderer),
                ...newComponents,
            },
        };

        this.selectionEventFired = false;
        this.reference = React.createRef();
    }

    onPaginationChanged() {
        const {setProps} = this.props;
        const {gridApi} = this.state;
        if (gridApi) {
            setProps({
                paginationInfo: {
                    paginationIsLastPageFound:
                        gridApi.paginationIsLastPageFound(),
                    paginationGetPageSize: gridApi.paginationGetPageSize(),
                    paginationGetCurrentPage:
                        gridApi.paginationGetCurrentPage(),
                    paginationGetTotalPages: gridApi.paginationGetTotalPages(),
                    paginationGetRowCount: gridApi.paginationGetRowCount(),
                },
            });
        }
    }

    setSelection(selection) {
        const {gridApi} = this.state;
        if (gridApi && selection) {
            if (!selection.length) {
                gridApi.deselectAll();
            } else {
                gridApi.forEachNode((node) => {
                    const isSelected = selection.some(equals(node.data));
                    node.setSelected(isSelected);
                });
            }
        }
    }

    memoizeOne(converter, obj, target) {
        const cache = this.convertedPropCache[target];
        if (cache && obj === cache[0]) {
            return cache[1];
        }
        const result = converter(obj, target);
        this.convertedPropCache[target] = [obj, result];
        return result;
    }

    convertFunction(func) {
        // TODO: do we want this? ie allow the form `{function: <string>}` even when
        // we're expecting just a string?
        if (has('function', func)) {
            return this.convertFunction(func.function);
        }

        try {
            if (typeof func !== 'string') {
                throw new Error('tried to parse non-string as function', func);
            }
            return this.parseFunction(func);
        } catch (err) {
            console.log(err);
        }
        return '';
    }

    convertFunctionNoParams(func) {
        // TODO: do we want this? ie allow the form `{function: <string>}` even when
        // we're expecting just a string?
        if (has('function', func)) {
            return this.convertFunctionNoParams(func.function);
        }

        try {
            if (typeof func !== 'string') {
                throw new Error('tried to parse non-string as function', func);
            }
            return this.parseFunctionNoParams(func);
        } catch (err) {
            console.log(err);
        }
        return '';
    }

    convertMaybeFunction(maybeFunc, stringsEvalContext) {
        if (has('function', maybeFunc)) {
            return this.convertFunction(maybeFunc.function);
        }

        if (
            stringsEvalContext &&
            typeof maybeFunc === 'string' &&
            !this.props.dangerously_allow_code
        ) {
            xssMessage(stringsEvalContext);
            return null;
        }
        return maybeFunc;
    }

    convertMaybeFunctionNoParams(maybeFunc, stringsEvalContext) {
        if (has('function', maybeFunc)) {
            return this.convertFunctionNoParams(maybeFunc.function);
        }

        if (
            stringsEvalContext &&
            typeof maybeFunc === 'string' &&
            !this.props.dangerously_allow_code
        ) {
            xssMessage(stringsEvalContext);
            return null;
        }
        return maybeFunc;
    }

    suppressGetDetail(colName) {
        return (params) => {
            params.successCallback(params.data[colName]);
        };
    }

    callbackGetDetail = (params) => {
        const {setProps} = this.props;
        const {data} = params;
        this.getDetailParams = params;
        // Adding the current time in ms forces Dash to trigger a callback
        // when the same row is closed and re-opened.
        setProps({getDetailRequest: {data: data, requestTime: Date.now()}});
    };

    convertCol(columnDef) {
        if (typeof columnDef === 'function') {
            return columnDef;
        }
        const field = columnDef.field || columnDef.headerName;

        return mapObjIndexed((value, target) => {
            if (
                target === 'cellStyle' &&
                (has('styleConditions', value) || has('defaultStyle', value))
            ) {
                return this.handleDynamicStyle(value);
            }
            if (OBJ_OF_FUNCTIONS[target]) {
                return map(this.convertFunction, value);
            }
            if (COLUMN_DANGEROUS_FUNCTIONS[target]) {
                // the second argument tells convertMaybeFunction
                // that a plain string is dangerous,
                // and provides the context for error reporting
                return this.convertMaybeFunction(value, {target, field});
            }
            if (COLUMN_MAYBE_FUNCTIONS[target]) {
                return this.convertMaybeFunction(value);
            }
            if (COLUMN_MAYBE_FUNCTIONS_NO_PARAMS[target]) {
                return this.convertMaybeFunctionNoParams(value);
            }
            if (COLUMN_ARRAY_NESTED_FUNCTIONS[target] && Array.isArray(value)) {
                return value.map(this.convertCol);
            }
            if (COLUMN_NESTED_FUNCTIONS[target] && typeof value === 'object') {
                return this.convertCol(value);
            }
            if (COLUMN_NESTED_OR_OBJ_OF_FUNCTIONS[target]) {
                if (has('function', value)) {
                    return this.convertMaybeFunction(value);
                }
                return this.convertCol(value);
            }
            // not one of those categories - pass it straight through
            return value;
        }, columnDef);
    }

    convertOne(value, target) {
        if (value) {
            if (target === 'columnDefs') {
                return value.map(this.convertCol);
            }
            if (GRID_COLUMN_CONTAINERS[target]) {
                return this.convertCol(value);
            }
            if (GRID_NESTED_FUNCTIONS[target]) {
                if ('suppressCallback' in value) {
                    value.getDetailRowData = value.suppressCallback
                        ? this.suppressGetDetail(value.detailColName)
                        : this.callbackGetDetail;
                }
                return this.convertAllProps(value);
            }
            if (GRID_DANGEROUS_FUNCTIONS[target]) {
                return this.convertMaybeFunctionNoParams(value, {prop: target});
            }
            if (target === 'getRowId') {
                return this.convertFunction(value);
            }
            if (target === 'getRowStyle') {
                return this.handleDynamicStyle(value);
            }
            if (OBJ_OF_FUNCTIONS[target]) {
                return map(this.convertFunction, value);
            }
            if (GRID_ONLY_FUNCTIONS[target]) {
                return this.convertFunction(value);
            }
            if (GRID_MAYBE_FUNCTIONS[target]) {
                return this.convertMaybeFunction(value);
            }
            if (GRID_MAYBE_FUNCTIONS_NO_PARAMS[target]) {
                return this.convertMaybeFunctionNoParams(value);
            }
            if (target === 'alignedGrids') {
                return (
                    document.getElementById(value) && [
                        findReact(document.getElementById(value)).reference
                            .current,
                    ]
                );
            }

            return value;
        }
        return value;
    }

    convertAllProps(props) {
        return mapObjIndexed(
            (value, target) => this.memoizeOne(this.convertOne, value, target),
            props
        );
    }

    onFilterChanged() {
        const {setProps, rowModelType} = this.props;
        const filterModel = this.state.gridApi.getFilterModel();
        const propsToSet = {filterModel};
        if (rowModelType === 'clientSide') {
            const virtualRowData = [];
            this.state.gridApi.forEachNodeAfterFilter((node) => {
                virtualRowData.push(node.data);
            });
            propsToSet.virtualRowData = virtualRowData;
        }

        setProps(propsToSet);
    }

    getRowData() {
        const newRowData = [];
        this.state.gridApi.forEachNode((node) => {
            newRowData.push(node.data);
        });
        return newRowData;
    }

    syncRowData() {
        const {rowData, setProps, rowModelType} = this.props;
        if (rowData) {
            const virtualRowData = [];
            if (rowModelType === 'clientSide') {
                this.state.gridApi.forEachNodeAfterFilter((node) => {
                    virtualRowData.push(node.data);
                });
            }
            if (rowData !== this.getRowData()) {
                setProps({rowData: this.getRowData(), virtualRowData});
            } else {
                setProps({virtualRowData});
            }
        }
    }

    onSortChanged() {
        const {setProps, rowModelType} = this.props;
        const propsToSet = {};
        if (rowModelType === 'clientSide') {
            const virtualRowData = [];
            this.state.gridApi.forEachNodeAfterFilterAndSort((node) => {
                virtualRowData.push(node.data);
            });

            propsToSet.virtualRowData = virtualRowData;
        }
        propsToSet.columnState = this.state.gridColumnApi.getColumnState();
        setProps(propsToSet);
    }

    componentDidMount() {
        this.setState({mounted: true});
    }

    componentDidUpdate(prevProps) {
        const {
            selectedRows,
            getDetailResponse,
            detailCellRendererParams,
            masterDetail,
            setProps,
            columnSize,
        } = this.props;

        if (this.isDatasourceLoadedForInfiniteScrolling()) {
            const {rowData, rowCount} = this.props.getRowsResponse;
            this.getRowsParams.successCallback(rowData, rowCount);
            setProps({getRowsResponse: null});
        }

        if (
            masterDetail &&
            !detailCellRendererParams.suppressCallback &&
            getDetailResponse
        ) {
            this.getDetailParams.successCallback(getDetailResponse);
            setProps({getDetailResponse: null});
        }
        // Call the API to select rows unless the update was triggered by a selection made in the UI
        if (
            !equals(selectedRows, prevProps.selectedRows) &&
            !this.selectionEventFired
        ) {
            this.setSelection(selectedRows);
        }

        if (
            JSON.stringify(this.props.columnDefs) !==
                JSON.stringify(prevProps.columnDefs) ||
            prevProps.columnSize !== columnSize
        ) {
            this.updateColumnWidths();
        }

        // Reset selection event flag
        this.selectionEventFired = false;
    }

    onRowDataUpdated() {
        // Handles preserving existing selections when rowData is updated in a callback
        const {selectedRows, setProps, rowData, rowModelType, filterModel} =
            this.props;
        const {openGroups, gridApi} = this.state;

        // Call the API to select rows
        this.setSelection(selectedRows);

        if (gridApi) {
            if (rowData && rowModelType === 'clientSide') {
                const virtualRowData = [];
                gridApi.forEachNodeAfterFilter((node) => {
                    virtualRowData.push(node.data);
                });

                setProps({virtualRowData});
            }

            // When the rowData is updated, reopen any row groups if they previously existed in the table
            // Iterate through all nodes in the grid. Unfortunately there's no way to iterate through only nodes representing groups
            if (openGroups.size > 0) {
                gridApi.forEachNode((node) => {
                    // Check if it's a group row based on whether it has the __hasChildren prop
                    if (node.__hasChildren) {
                        // If the key for the node (i.e. the group name) is the same as an
                        if (openGroups.has(node.key)) {
                            gridApi.setRowNodeExpanded(node, true);
                        }
                    }
                });
            }
            if (!isEmpty(filterModel)) {
                gridApi.setFilterModel(filterModel);
            }
        }
    }

    onRowGroupOpened(e) {
        const {openGroups} = this.state;

        if (e.expanded) {
            // If the node was just expanded, add it to the list of open nodes
            openGroups.add(e.node.key);
        } else {
            // If it's collapsed, remove it from the list of open nodes
            openGroups.delete(e.node.key);
        }
        this.setState({openGroups});
    }

    onSelectionChanged() {
        // Flag that the selection event was fired
        this.selectionEventFired = true;
        const selectedRows = this.state.gridApi.getSelectedRows();
        this.props.setProps({selectedRows});
    }

    isDatasourceLoadedForInfiniteScrolling() {
        return (
            this.props.rowModelType === 'infinite' &&
            this.getRowsParams &&
            this.props.getRowsResponse
        );
    }

    getDatasource() {
        const self = this;

        return {
            getRows(params) {
                self.getRowsParams = params;
                self.props.setProps({getRowsRequest: params});
            },

            destroy() {
                self.getRowsParams = null;
            },
        };
    }

    applyRowTransaction(data, gridApi = this.state.gridApi) {
        if (data.async === false) {
            gridApi.applyTransaction(data);
        } else {
            gridApi.applyTransactionAsync(data);
        }
    }

    onGridReady(params) {
        // Applying Infinite Row Model
        // see: https://www.ag-grid.com/javascript-grid/infinite-scrolling/
        const {
            rowModelType,
            selectedRows,
            resetColumnState,
            csvExportParams,
            exportDataAsCsv,
            selectAll,
            deselectAll,
            deleteSelectedRows,
            filterModel,
            setProps,
            columnState,
            paginationGoTo,
        } = this.props;

        const propsToSet = {};
        if (rowModelType === 'infinite') {
            params.api.setDatasource(this.getDatasource());
        }

        this.setState({
            gridApi: params.api,
            gridColumnApi: params.columnApi,
        });

        if (this.reference.current.props.pagination) {
            this.onPaginationChanged();
        }

        if (!isEmpty(filterModel)) {
            this.state.gridApi.setFilterModel(filterModel);
        }

        if (columnState) {
            this.setColumnState();
        }

        if (paginationGoTo) {
            this.paginationGoTo(false);
            propsToSet.paginationGoTo = null;
        }

        if (resetColumnState) {
            this.resetColumnState(false);
            propsToSet.resetColumnState = false;
        }

        if (exportDataAsCsv) {
            this.exportDataAsCsv(csvExportParams, false);
            propsToSet.exportDataAsCsv = false;
        }

        if (selectAll) {
            this.selectAll(selectAll, false);
            propsToSet.selectAll = false;
        }

        if (deselectAll) {
            this.deselectAll(false);
            propsToSet.deselectAll = false;
        }

        if (deleteSelectedRows) {
            this.deleteSelectedRows(false);
            propsToSet.deleteSelectedRows = false;
        }

        if (!isEmpty(propsToSet)) {
            setProps(propsToSet);
        }

        if (this.state.rowTransaction) {
            this.state.rowTransaction.map((data) =>
                this.applyRowTransaction(data, params.api)
            );
            this.setState({rowTransaction: null});
            this.syncRowData();
        }

        // Handles applying selections when a selection was persisted by Dash
        this.setSelection(selectedRows);
        // Hydrate virtualRowData
        this.onFilterChanged(true);

        this.updateColumnWidths();
    }

    onCellClicked({value, column: {colId}, rowIndex, node}) {
        const timestamp = Date.now();
        this.props.setProps({
            cellClicked: {value, colId, rowIndex, rowId: node.id, timestamp},
        });
    }

    onCellValueChanged({
        oldValue,
        value,
        column: {colId},
        rowIndex,
        data,
        node,
    }) {
        const virtualRowData = [];
        if (this.props.rowModelType === 'clientSide' && this.state.gridApi) {
            this.state.gridApi.forEachNodeAfterFilter((node) => {
                virtualRowData.push(node.data);
            });
        }
        this.props.setProps({
            cellValueChanged: {
                rowIndex,
                rowId: node.id,
                data,
                oldValue,
                value,
                colId,
            },
            virtualRowData,
        });
        this.syncRowData();
    }

    onDisplayedColumnsChanged() {
        if (this.props.columnSize === 'responsiveSizeToFit') {
            this.updateColumnWidths();
        }
    }

    onGridSizeChanged() {
        if (this.props.columnSize === 'responsiveSizeToFit') {
            this.updateColumnWidths();
        }
    }

    updateColumnWidths() {
        const {columnSize, columnSizeOptions, setProps} = this.props;
        const {gridApi, gridColumnApi} = this.state;
        if (gridApi || gridColumnApi) {
            const {
                keys,
                skipHeader,
                defaultMinWidth,
                defaultMaxWidth,
                columnLimits,
            } = columnSizeOptions || {};
            if (columnSize === 'autoSize') {
                if (keys) {
                    gridColumnApi.autoSizeColumns(keys, skipHeader);
                } else {
                    gridColumnApi.autoSizeAllColumns(skipHeader);
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
                setProps({columnSize: null});
            }
            this.updateColumnState();
        }
    }

    parseFunction = memoizeWith(String, (funcString) => {
        const parsedCondition = esprima.parse(funcString).body[0].expression;
        const context = {
            d3,
            ...customFunctions,
            ...window.dashAgGridFunctions,
        };
        return (params) => evaluate(parsedCondition, {params, ...context});
    });

    parseFunctionNoParams = memoizeWith(String, (funcString) => {
        const parsedCondition = esprima.parse(funcString).body[0].expression;
        const context = {
            d3,
            ...customFunctions,
            ...window.dashAgGridFunctions,
        };
        return evaluate(parsedCondition, context);
    });

    /**
     * @params AG-Grid Styles rules attribute.
     * Cells: https://www.ag-grid.com/react-grid/cell-styles/#cell-style-cell-class--cell-class-rules-params
     * Rows: https://www.ag-grid.com/react-grid/row-styles/#row-style-row-class--row-class-rules-params
     */
    handleDynamicStyle(cellStyle) {
        const {styleConditions, defaultStyle} = cellStyle;
        const _defaultStyle = defaultStyle || null;

        if (styleConditions && styleConditions.length) {
            const tests = styleConditions.map(({condition, style}) => ({
                test: this.parseFunction(condition),
                style,
            }));
            return (params) => {
                for (const {test, style} of tests) {
                    if (test(params)) {
                        return style;
                    }
                }
                return _defaultStyle;
            };
        }

        return _defaultStyle;
    }

    generateRenderer(Renderer) {
        const {setProps, dangerously_allow_code} = this.props;

        return (props) => (
            <Renderer
                setData={(value) => {
                    setProps({
                        cellRendererData: {
                            value,
                            colId: props.column.colId,
                            rowIndex: props.rowIndex,
                            rowId: props.node.id,
                            timestamp: Date.now(),
                        },
                    });
                }}
                dangerously_allow_code={dangerously_allow_code}
                {...props}
            ></Renderer>
        );
    }

    setColumnState() {
        if (!this.state.gridApi) {
            return;
        }
        this.state.gridColumnApi.applyColumnState({
            state: this.props.columnState,
        });
    }

    // Event actions that reset
    exportDataAsCsv(csvExportParams, reset = true) {
        if (!this.state.gridApi) {
            return;
        }
        this.state.gridApi.exportDataAsCsv(csvExportParams);
        if (reset) {
            this.props.setProps({
                exportDataAsCsv: false,
            });
        }
    }

    paginationGoTo(reset = true) {
        const {gridApi} = this.state;
        if (!gridApi) {
            return;
        }
        switch (this.props.paginationGoTo) {
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
                gridApi.paginationGoToPage(this.props.paginationGoTo);
        }
        if (reset) {
            this.props.setProps({
                paginationGoTo: null,
            });
        }
    }

    resetColumnState(reset = true) {
        if (!this.state.gridApi) {
            return;
        }
        this.state.gridColumnApi.resetColumnState();
        if (reset) {
            this.props.setProps({
                resetColumnState: false,
            });
            this.updateColumnState();
        }
    }

    selectAll(opts, reset = true) {
        if (!this.state.gridApi) {
            return;
        }
        if (opts?.filtered) {
            this.state.gridApi.selectAllFiltered();
        } else {
            this.state.gridApi.selectAll();
        }
        if (reset) {
            this.props.setProps({
                selectAll: false,
            });
        }
    }

    deselectAll(reset = true) {
        if (!this.state.gridApi) {
            return;
        }
        this.state.gridApi.deselectAll();
        if (reset) {
            this.props.setProps({
                deselectAll: false,
            });
        }
    }

    deleteSelectedRows(reset = true) {
        if (!this.state.gridApi) {
            return;
        }
        const sel = this.state.gridApi.getSelectedRows();
        this.state.gridApi.applyTransaction({remove: sel});
        if (reset) {
            this.props.setProps({
                deleteSelectedRows: false,
                rowData: this.getRowData(),
            });
        }
    }

    // end event actions

    updateColumnState() {
        if (!this.state.gridApi) {
            return;
        }
        this.props.setProps({
            columnState: JSON.parse(
                JSON.stringify(this.state.gridColumnApi.getColumnState())
            ),
            updateColumnState: false,
        });
    }

    buildArray(arr1, arr2) {
        if (arr1) {
            if (!arr1.includes(arr2)) {
                return [...arr1, arr2];
            }
            return arr1;
        }
        return [JSON.parse(JSON.stringify(arr2))];
    }

    rowTransaction(data) {
        if (this.state.mounted) {
            if (this.state.gridApi) {
                if (this.state.rowTransaction) {
                    this.state.rowTransaction.forEach(this.applyRowTransaction);
                    this.setState({rowTransaction: null});
                }
                this.applyRowTransaction(data);
                this.props.setProps({
                    rowTransaction: null,
                    rowData: this.getRowData(),
                });
            } else {
                this.setState({
                    rowTransaction: this.state.rowTransaction
                        ? this.buildArray(this.state.rowTransaction, data)
                        : [JSON.parse(JSON.stringify(data))],
                });
            }
        }
    }

    onAsyncTransactionsFlushed() {
        this.syncRowData();
    }

    render() {
        const {
            id,
            style,
            className,
            resetColumnState,
            exportDataAsCsv,
            selectAll,
            deselectAll,
            deleteSelectedRows,
            rowTransaction,
            updateColumnState,
            csvExportParams,
            dashGridOptions,
            filterModel,
            columnSize,
            columnState,
            paginationGoTo,
            ...restProps
        } = this.props;

        const passingProps = pick(PASSTHRU_PROPS, restProps);

        const convertedProps = this.convertAllProps(
            omit(NO_CONVERT_PROPS, {...dashGridOptions, ...restProps})
        );

        if (filterModel) {
            if (this.state.gridApi) {
                if (this.state.gridApi.getFilterModel() !== filterModel) {
                    this.state.gridApi.setFilterModel(filterModel);
                }
            }
        }

        if (paginationGoTo) {
            this.paginationGoTo();
        }

        if (columnSize) {
            this.updateColumnWidths();
        }

        if (columnState) {
            this.setColumnState();
        }

        if (resetColumnState) {
            this.resetColumnState();
        }

        if (exportDataAsCsv) {
            this.exportDataAsCsv(csvExportParams);
        }

        if (selectAll) {
            this.selectAll(selectAll);
        }

        if (deselectAll) {
            this.deselectAll();
        }

        if (updateColumnState) {
            this.updateColumnState();
        }

        if (deleteSelectedRows) {
            this.deleteSelectedRows();
        }

        if (rowTransaction) {
            this.rowTransaction(rowTransaction);
        }

        return (
            <div id={id} className={className} style={style}>
                <AgGridReact
                    ref={this.reference}
                    onGridReady={this.onGridReady}
                    onSelectionChanged={this.onSelectionChanged}
                    onCellClicked={this.onCellClicked}
                    onCellValueChanged={this.onCellValueChanged}
                    onFilterChanged={this.onFilterChanged}
                    onSortChanged={this.onSortChanged}
                    onRowDataUpdated={this.onRowDataUpdated}
                    onRowGroupOpened={this.onRowGroupOpened}
                    onDisplayedColumnsChanged={this.onDisplayedColumnsChanged}
                    onAsyncTransactionsFlushed={this.onAsyncTransactionsFlushed}
                    onPaginationChanged={this.onPaginationChanged}
                    onGridSizeChanged={debounce(
                        this.onGridSizeChanged,
                        RESIZE_DEBOUNCE_MS
                    )}
                    components={this.state.components}
                    {...passingProps}
                    {...convertedProps}
                ></AgGridReact>
            </div>
        );
    }
}

DashAgGrid.defaultProps = _defaultProps;
DashAgGrid.propTypes = {parentState: PropTypes.any, ..._propTypes};

export const propTypes = DashAgGrid.propTypes;
export const defaultProps = DashAgGrid.defaultProps;
