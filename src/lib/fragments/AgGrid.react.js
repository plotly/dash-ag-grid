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
    OMIT_STATE_RENDER,
    OBJ_MAYBE_FUNCTION_OR_MAP_MAYBE_FUNCTIONS,
} from '../utils/propCategories';
import debounce from '../utils/debounce';

import MarkdownRenderer from '../renderers/markdownRenderer';
import RowMenuRenderer from '../renderers/rowMenuRenderer';
import {customFunctions} from '../renderers/customFunctions';

import {AgGridReact} from 'ag-grid-react';

import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';
import 'ag-grid-community/styles/ag-theme-balham.css';
import 'ag-grid-community/styles/ag-theme-material.css';
import 'ag-grid-community/styles/ag-theme-quartz.css';

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

export default class DashAgGrid extends Component {
    constructor(props) {
        super(props);

        this.onGridReady = this.onGridReady.bind(this);
        this.onSelectionChanged = this.onSelectionChanged.bind(this);
        this.onCellClicked = this.onCellClicked.bind(this);
        this.onCellDoubleClicked = this.onCellDoubleClicked.bind(this);
        this.onCellValueChanged = this.onCellValueChanged.bind(this);
        this.afterCellValueChanged = this.afterCellValueChanged.bind(this);
        this.onRowDataUpdated = this.onRowDataUpdated.bind(this);
        this.onFilterChanged = this.onFilterChanged.bind(this);
        this.onSortChanged = this.onSortChanged.bind(this);
        this.onRowGroupOpened = this.onRowGroupOpened.bind(this);
        this.onDisplayedColumnsChanged =
            this.onDisplayedColumnsChanged.bind(this);
        this.onColumnResized = this.onColumnResized.bind(this);
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
        this.scrollTo = this.scrollTo.bind(this);

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
            pauseSelections: false,
            rerender: 0,
            openGroups: {},
            gridApi: null,
            columnState_push: true,
        };

        this.selectionEventFired = false;
        this.reference = React.createRef();
        this.pendingChanges = null;
    }

    onPaginationChanged() {
        const {setProps} = this.props;
        const {gridApi} = this.state;
        if (gridApi && !gridApi?.isDestroyed()) {
            setProps({
                paginationInfo: {
                    isLastPageFound: gridApi.paginationIsLastPageFound(),
                    pageSize: gridApi.paginationGetPageSize(),
                    currentPage: gridApi.paginationGetCurrentPage(),
                    totalPages: gridApi.paginationGetTotalPages(),
                    rowCount: gridApi.paginationGetRowCount(),
                },
            });
        }
    }

    setSelection(selection) {
        const {gridApi} = this.state;
        const {getRowId} = this.props;
        if (gridApi && selection && !gridApi?.isDestroyed()) {
            this.setState({pauseSelections: true});
            const nodeData = [];
            if (has('function', selection)) {
                const test = this.parseFunction(selection.function);

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
            gridApi.setNodesSelected({nodes: nodeData, newValue: true});
            this.setState({pauseSelections: false});
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
                const field = columnDef.field || columnDef.headerName;
                return this.convertMaybeFunction(value, {target, field});
            }
            if (COLUMN_MAYBE_FUNCTIONS[target]) {
                return this.convertMaybeFunction(value);
            }
            if (COLUMN_MAYBE_FUNCTIONS_NO_PARAMS[target]) {
                return this.convertMaybeFunctionNoParams(value);
            }
            if (COLUMN_ARRAY_NESTED_FUNCTIONS[target] && Array.isArray(value)) {
                return value.map((c) => {
                    if (typeof c === 'object') {
                        return this.convertCol(c);
                    }
                    return c;
                });
            }
            if (OBJ_MAYBE_FUNCTION_OR_MAP_MAYBE_FUNCTIONS[target]) {
                if ('function' in value) {
                    if (typeof value.function === 'string') {
                        return this.convertMaybeFunctionNoParams(value);
                    }
                }
                return map((v) => {
                    if (typeof v === 'object') {
                        if (typeof v.function === 'string') {
                            return this.convertMaybeFunctionNoParams(v);
                        }
                        return this.convertCol(v);
                    }
                    return v;
                }, value);
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
            if (OBJ_MAYBE_FUNCTION_OR_MAP_MAYBE_FUNCTIONS[target]) {
                if ('function' in value) {
                    if (typeof value.function === 'string') {
                        return this.convertMaybeFunctionNoParams(value);
                    }
                }
                return mapObjIndexed((v) => {
                    if (typeof v === 'object') {
                        if ('function' in v) {
                            if (typeof v.function === 'string') {
                                return this.convertMaybeFunctionNoParams(v);
                            }
                        } else {
                            return this.convertCol(v);
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
                            ? this.suppressGetDetail(value.detailColName)
                            : this.callbackGetDetail,
                    };
                }
                if ('detailGridOptions' in value) {
                    adjustedVal = assocPath(
                        ['detailGridOptions', 'components'],
                        this.state.components,
                        adjustedVal
                    );
                }
                return this.convertAllProps(adjustedVal);
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
        if (!this.state.gridApi) {
            return;
        }
        const filterModel = this.state.gridApi.getFilterModel();
        const propsToSet = {filterModel};
        if (rowModelType === 'clientSide') {
            propsToSet.virtualRowData = this.virtualRowData();
        }

        setProps(propsToSet);
    }

    getRowData() {
        const newRowData = [];
        this.state.gridApi.forEachLeafNode((node) => {
            newRowData.push(node.data);
        });
        return newRowData;
    }

    virtualRowData() {
        const {rowModelType} = this.props;
        const {gridApi} = this.state;
        const virtualRowData = [];
        if (rowModelType === 'clientSide' && gridApi) {
            gridApi.forEachNodeAfterFilterAndSort((node) => {
                if (node.data) {
                    virtualRowData.push(node.data);
                }
            });
        }
        return virtualRowData;
    }

    syncRowData() {
        const {rowData, setProps} = this.props;
        if (rowData) {
            const virtualRowData = this.virtualRowData();
            const newRowData = this.getRowData();
            if (rowData !== newRowData) {
                setProps({rowData: newRowData, virtualRowData});
            } else {
                setProps({virtualRowData});
            }
        }
    }

    onSortChanged() {
        const {setProps, rowModelType} = this.props;
        const propsToSet = {};
        if (rowModelType === 'clientSide') {
            propsToSet.virtualRowData = this.virtualRowData();
        }
        propsToSet.columnState = JSON.parse(
            JSON.stringify(this.state.gridApi.getColumnState())
        );
        setProps(propsToSet);
    }

    componentDidMount() {
        const {id} = this.props;
        if (id) {
            agGridRefs[id] = this.reference.current;
            eventBus.dispatch(id);
        }
    }

    componentWillUnmount() {
        this.setState({mounted: false, gridApi: null});
        if (this.props.id) {
            delete agGridRefs[this.props.id];
            eventBus.remove(this.props.id);
        }
    }

    shouldComponentUpdate(nextProps, nextState) {
        const {gridApi} = this.state;
        const {columnState, filterModel, selectedRows} = nextProps;

        if (
            !equals(
                {...omit(OMIT_PROP_RENDER, nextProps)},
                {...omit(OMIT_PROP_RENDER, this.props)}
            )
        ) {
            return true;
        }
        if (
            !equals(
                {...omit(OMIT_STATE_RENDER, nextState)},
                {...omit(OMIT_STATE_RENDER, this.state)}
            )
        ) {
            return true;
        }
        if (gridApi && !gridApi?.isDestroyed()) {
            if (columnState) {
                if (columnState !== this.props.columnState) {
                    return true;
                }
            }
            if (filterModel) {
                if (!equals(filterModel, gridApi.getFilterModel())) {
                    return true;
                }
            }
            if (selectedRows) {
                if (!equals(selectedRows, gridApi.getSelectedRows())) {
                    return true;
                }
            }
            return false;
        }
        return false;
    }

    componentDidUpdate(prevProps, prevState) {
        const {
            selectedRows,
            getDetailResponse,
            detailCellRendererParams,
            masterDetail,
            setProps,
            id,
            resetColumnState,
            csvExportParams,
            exportDataAsCsv,
            selectAll,
            deselectAll,
            deleteSelectedRows,
            filterModel,
            columnState,
            columnSize,
            paginationGoTo,
            scrollTo,
            rowTransaction,
            updateColumnState,
        } = this.props;

        if (this.state.gridApi && prevProps.loading_state.is_loading) {
            if (
                this.props.columnState !== prevProps.columnState &&
                !this.state.columnState_push
            ) {
                this.setState({columnState_push: true});
            }
        }

        if (id !== prevProps.id) {
            if (id) {
                agGridRefs[id] = this.reference.current;
                eventBus.dispatch(id);
            }
            if (prevProps.id) {
                delete agGridRefs[prevProps.id];
                eventBus.remove(prevProps.id);
            }
        }

        if (this.state.gridApi && this.state.gridApi !== prevState.gridApi) {
            const propsToSet = {};
            this.updateColumnWidths(false);

            const groups = {};
            this.state.gridApi.forEachNode((node) => {
                if (node.expanded) {
                    groups[node.key] = 1;
                }
            });

            if (this.state.rowTransaction) {
                this.state.rowTransaction.map((data) =>
                    this.applyRowTransaction(data, this.state.gridApi)
                );
                this.setState({rowTransaction: null});
                this.syncRowData();
            }

            // Handles applying selections when a selection was persisted by Dash
            this.setSelection(selectedRows);

            if (this.reference.current.props.pagination) {
                this.onPaginationChanged();
            }

            if (!isEmpty(filterModel)) {
                this.state.gridApi.setFilterModel(filterModel);
            }

            if (columnState) {
                this.setColumnState();
            }

            if (paginationGoTo || paginationGoTo === 0) {
                this.paginationGoTo(false);
                propsToSet.paginationGoTo = null;
            }

            if (scrollTo) {
                this.scrollTo(scrollTo);
                propsToSet.scrollTo = null;
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
            // Hydrate virtualRowData
            this.onFilterChanged(true);
            this.setState({
                mounted: true,
                openGroups: groups,
                columnState_push: false,
            });
            this.updateColumnState();
        }

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

        if (this.state.gridApi && this.state.gridApi === prevState.gridApi) {
            if (filterModel) {
                if (this.state.gridApi) {
                    if (this.state.gridApi.getFilterModel() !== filterModel) {
                        this.state.gridApi.setFilterModel(filterModel);
                    }
                }
            }

            if (paginationGoTo || paginationGoTo === 0) {
                this.paginationGoTo();
            }

            if (scrollTo) {
                this.scrollTo();
            }

            if (columnSize) {
                this.updateColumnWidths();
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

            if (deleteSelectedRows) {
                this.deleteSelectedRows();
            }

            if (rowTransaction) {
                this.rowTransaction(rowTransaction);
            }
            if (updateColumnState) {
                this.updateColumnState();
            } else if (this.state.columnState_push) {
                this.setColumnState();
            }
        }

        // Reset selection event flag
        this.selectionEventFired = false;
    }

    onRowDataUpdated() {
        // Handles preserving existing selections when rowData is updated in a callback
        const {selectedRows, setProps, rowData, rowModelType, filterModel} =
            this.props;
        const {openGroups, gridApi} = this.state;

        if (gridApi && !gridApi?.isDestroyed()) {
            // Call the API to select rows
            this.setSelection(selectedRows);

            if (rowData && rowModelType === 'clientSide') {
                const virtualRowData = this.virtualRowData();

                setProps({virtualRowData});
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
        }
    }

    onRowGroupOpened(e) {
        this.setState(({openGroups}) => ({
            openGroups: e.expanded
                ? assoc(e.node.key, 1, openGroups)
                : omit([e.node.key], openGroups),
        }));
    }

    onSelectionChanged() {
        if (!this.state.pauseSelections) {
            // Flag that the selection event was fired
            this.selectionEventFired = true;
            const selectedRows = this.state.gridApi.getSelectedRows();
            this.props.setProps({selectedRows});
        }
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
        const {selectedRows} = this.props;
        if (data.async === false) {
            gridApi.applyTransaction(data);
            if (selectedRows) {
                this.setSelection(selectedRows);
            }
        } else {
            gridApi.applyTransactionAsync(data);
        }
    }

    onGridReady(params) {
        // Applying Infinite Row Model
        // see: https://www.ag-grid.com/javascript-grid/infinite-scrolling/
        const {rowModelType, eventListeners} = this.props;

        if (rowModelType === 'infinite') {
            params.api.setDatasource(this.getDatasource());
        }

        if (eventListeners) {
            Object.entries(eventListeners).map(([key, v]) => {
                v.map((func) => {
                    params.api.addEventListener(
                        key,
                        this.parseFunctionEvent(func)
                    );
                });
            });
        }

        this.setState({
            gridApi: params.api,
        });
    }

    onCellClicked({value, column: {colId}, rowIndex, node}) {
        const timestamp = Date.now();
        this.props.setProps({
            cellClicked: {value, colId, rowIndex, rowId: node.id, timestamp},
        });
    }

    onCellDoubleClicked({value, column: {colId}, rowIndex, node}) {
        const timestamp = Date.now();
        this.props.setProps({
            cellDoubleClicked: {
                value,
                colId,
                rowIndex,
                rowId: node.id,
                timestamp,
            },
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
        if (!this.pendingCellValueChanges) {
            this.pendingCellValueChanges = [newChange];
        } else {
            this.pendingCellValueChanges.push(newChange);
        }
    }

    afterCellValueChanged() {
        // Guard against multiple invocations of the same change session.
        if (!this.pendingCellValueChanges) {
            return;
        }
        // Send update(s) for current change session to Dash.
        const virtualRowData = this.virtualRowData();
        this.props.setProps({
            cellValueChanged: this.pendingCellValueChanges,
            virtualRowData,
        });
        this.syncRowData();
        // Mark current change session as ended.
        this.pendingCellValueChanges = null;
    }

    onDisplayedColumnsChanged() {
        if (this.props.columnSize === 'responsiveSizeToFit') {
            this.updateColumnWidths();
        }
        if (this.state.mounted) {
            this.updateColumnState();
        }
    }

    onColumnResized() {
        if (
            this.state.mounted &&
            this.props.columnSize !== 'responsiveSizeToFit'
        ) {
            this.updateColumnState();
        }
    }

    onGridSizeChanged() {
        if (this.props.columnSize === 'responsiveSizeToFit') {
            this.updateColumnWidths();
        }
    }

    updateColumnWidths(setColumns = true) {
        const {columnSize, columnSizeOptions, setProps} = this.props;
        const {gridApi} = this.state;
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
                setProps({columnSize: null});
            }
            if (setColumns) {
                this.updateColumnState();
            }
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

    parseFunctionEvent = memoizeWith(String, (funcString) => {
        const parsedCondition = esprima.parse(funcString).body[0].expression;
        const context = {
            d3,
            ...customFunctions,
            ...window.dashAgGridFunctions,
            setGridProps: this.props.setProps,
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
        if (!this.state.gridApi || this.props.updateColumnState) {
            return;
        }

        if (this.state.columnState_push) {
            this.state.gridApi.applyColumnState({
                state: this.props.columnState,
                applyOrder: true,
            });
            this.setState({columnState_push: false});
        }
    }

    // Event actions that reset
    exportDataAsCsv(csvExportParams, reset = true) {
        if (!this.state.gridApi) {
            return;
        }
        this.state.gridApi.exportDataAsCsv(
            this.convertAllProps(csvExportParams)
        );
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

    scrollTo(reset = false) {
        const {gridApi} = this.state;
        const {scrollTo, setProps, getRowId} = this.props;
        if (!gridApi) {
            return;
        }
        const rowPosition = scrollTo.rowPosition ? scrollTo.rowPosition : 'top';
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
            setProps({
                scrollTo: null,
            });
        }
    }

    resetColumnState(reset = true) {
        if (!this.state.gridApi) {
            return;
        }
        this.state.gridApi.resetColumnState();
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
            });
            this.syncRowData();
        }
    }

    // end event actions

    updateColumnState() {
        if (!this.state.gridApi || !this.state.mounted) {
            return;
        }

        var columnState = JSON.parse(
            JSON.stringify(this.state.gridApi.getColumnState())
        );

        this.props.setProps({
            columnState,
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
        const {rowTransaction, gridApi, mounted} = this.state;
        if (mounted) {
            if (gridApi && !gridApi?.isDestroyed()) {
                if (rowTransaction) {
                    rowTransaction.forEach(this.applyRowTransaction);
                    this.setState({rowTransaction: null});
                }
                this.applyRowTransaction(data);
                this.props.setProps({
                    rowTransaction: null,
                });
                this.syncRowData();
            } else {
                this.setState({
                    rowTransaction: rowTransaction
                        ? this.buildArray(rowTransaction, data)
                        : [JSON.parse(JSON.stringify(data))],
                });
            }
        }
    }

    onAsyncTransactionsFlushed() {
        const {selectedRows} = this.props;
        if (selectedRows) {
            this.setSelection(selectedRows);
        }
        this.syncRowData();
    }

    render() {
        const {id, style, className, dashGridOptions, ...restProps} =
            this.props;

        const passingProps = pick(PASSTHRU_PROPS, restProps);

        const convertedProps = this.convertAllProps(
            omit(NO_CONVERT_PROPS, {...dashGridOptions, ...restProps})
        );

        let alignedGrids;
        if (dashGridOptions) {
            if ('alignedGrids' in dashGridOptions) {
                alignedGrids = [];
                const addGrid = (id) => {
                    const strId = stringifyId(id);
                    eventBus.on(this.props.id, strId, () => {
                        this.setState(({rerender}) => ({
                            rerender: rerender + 1,
                        }));
                    });
                    if (!agGridRefs[strId]) {
                        agGridRefs[strId] = {api: null};
                    }
                    alignedGrids.push(agGridRefs[strId]);
                };
                eventBus.remove(this.props.id);
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
                        convertedProps.domLayout === 'autoHeight'
                            ? null
                            : '400px',
                    width: '100%',
                    ...style,
                }}
            >
                <AgGridReact
                    ref={this.reference}
                    alignedGrids={alignedGrids}
                    onGridReady={this.onGridReady}
                    onSelectionChanged={this.onSelectionChanged}
                    onCellClicked={this.onCellClicked}
                    onCellDoubleClicked={this.onCellDoubleClicked}
                    onCellValueChanged={debounce(
                        this.afterCellValueChanged,
                        CELL_VALUE_CHANGED_DEBOUNCE_MS,
                        this.onCellValueChanged
                    )}
                    onFilterChanged={this.onFilterChanged}
                    onSortChanged={this.onSortChanged}
                    onRowDragEnd={this.onSortChanged}
                    onRowDataUpdated={this.onRowDataUpdated}
                    onRowGroupOpened={this.onRowGroupOpened}
                    onDisplayedColumnsChanged={debounce(
                        this.onDisplayedColumnsChanged,
                        COL_RESIZE_DEBOUNCE_MS
                    )}
                    onColumnResized={debounce(
                        this.onColumnResized,
                        COL_RESIZE_DEBOUNCE_MS
                    )}
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
