import React, {Component} from 'react';
import PropTypes from 'prop-types';
import * as evaluate from 'static-eval';
import * as esprima from 'esprima';
import {equals, has, isEmpty, map, mapObjIndexed, omit} from 'ramda';
import {
    propTypes as _propTypes,
    defaultProps as _defaultProps,
} from '../components/AgGrid.react';
import {
    columnDangerousFunctions,
    columnMaybeFunctions,
    columnArrayNestedFunctions,
    columnNestedFunctions,
    gridMaybeFunctions,
    gridOnlyFunctions,
    gridColumnContainers,
    gridNestedFunctions,
    objOfFunctions,
    columnNestedOrObjOfFunctions,
} from '../utils/functionVars';
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
        this.convertFunction = this.convertFunction.bind(this);
        this.convertMaybeFunction = this.convertMaybeFunction.bind(this);
        this.convertCol = this.convertCol.bind(this);
        this.convertAllProps = this.convertAllProps.bind(this);
        this.buildArray = this.buildArray.bind(this);
        this.onAsyncTransactionsFlushed =
            this.onAsyncTransactionsFlushed.bind(this);

        // Additional Exposure
        this.selectAll = this.selectAll.bind(this);
        this.deselectAll = this.deselectAll.bind(this);
        this.autoSizeAllColumns = this.autoSizeAllColumns.bind(this);
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

        this.state = {
            ...this.props.parentState,
            components: {
                rowMenu: this.generateRenderer(RowMenuRenderer),
                markdown: this.generateRenderer(MarkdownRenderer),
                ...newComponents,
            },
        };

        this.selectionEventFired = false;
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
            if (objOfFunctions[target]) {
                return map(this.convertFunction, value);
            }
            if (columnDangerousFunctions[target]) {
                // the second argument tells convertMaybeFunction
                // that a plain string is dangerous,
                // and provides the context for error reporting
                return this.convertMaybeFunction(value, {target, field});
            }
            if (columnMaybeFunctions[target]) {
                return this.convertMaybeFunction(value);
            }
            if (columnNestedFunctions[target]) {
                return this.convertCol(value);
            }
            if (columnArrayNestedFunctions[target]) {
                return value.map(this.convertCol);
            }
            if (columnNestedOrObjOfFunctions[target]) {
                if (has('function', value)) {
                    return this.convertMaybeFunction(value);
                }
                return value.map(this.convertCol);
            }
            // not one of those categories - pass it straight through
            return value;
        }, columnDef);
    }

    convertAllProps(props) {
        return mapObjIndexed((value, target) => {
            if (target === 'columnDefs') {
                return value.map(this.convertCol);
            }
            if (gridColumnContainers[target]) {
                return this.convertCol(value);
            }
            if (gridNestedFunctions[target]) {
                return this.convertAllProps(value);
            }
            if (target === 'getRowId') {
                return this.convertFunction(value);
            }
            if (target === 'getRowStyle') {
                return this.handleDynamicStyle(value);
            }
            if (objOfFunctions[target]) {
                return map(this.convertFunction, value);
            }
            if (gridOnlyFunctions[target]) {
                return this.convertFunction(value);
            }
            if (gridMaybeFunctions[target]) {
                return this.convertMaybeFunction(value);
            }
            return value;
        }, props);
    }

    onFilterChanged() {
        const {setProps, rowModelType} = this.props;
        if (rowModelType === 'clientSide') {
            const virtualRowData = [];
            this.state.gridApi.forEachNodeAfterFilter((node) => {
                virtualRowData.push(node.data);
            });

            const filterModel = this.state.gridApi.getFilterModel();
            this.setState({filterModel});
            setProps({virtualRowData});
        }
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
            setProps({rowData: this.getRowData(), virtualRowData});
        }
    }

    onSortChanged() {
        const {setProps, rowModelType} = this.props;
        if (rowModelType === 'clientSide') {
            const virtualRowData = [];
            this.state.gridApi.forEachNodeAfterFilterAndSort((node) => {
                virtualRowData.push(node.data);
            });

            setProps({
                virtualRowData: virtualRowData,
                columnState: this.state.gridColumnApi.getColumnState(),
            });
        }
    }

    shouldComponentUpdate(nextProps) {
        if (JSON.stringify(nextProps) === JSON.stringify(this.props)) {
            return false;
        }
        return true;
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
        const {selectedRows, setProps, rowData, rowModelType} = this.props;
        const {openGroups, filterModel} = this.state;

        if (rowData && rowModelType === 'clientSide' && this.state.gridApi) {
            const virtualRowData = [];
            this.state.gridApi.forEachNodeAfterFilter((node) => {
                virtualRowData.push(node.data);
            });

            setProps({virtualRowData});
        }

        // Call the API to select rows
        this.setSelection(selectedRows);
        // When the rowData is updated, reopen any row groups if they previously existed in the table
        // Iterate through all nodes in the grid. Unfortunately there's no way to iterate through only nodes representing groups
        if (openGroups.size > 0) {
            this.state.gridApi.forEachNode((node) => {
                // Check if it's a group row based on whether it has the __hasChildren prop
                if (node.__hasChildren) {
                    // If the key for the node (i.e. the group name) is the same as an
                    if (openGroups.has(node.key)) {
                        this.state.gridApi.setRowNodeExpanded(node, true);
                    }
                }
            });
        }
        if (!isEmpty(filterModel)) {
            this.state.gridApi.setFilterModel(filterModel);
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
        const {rowModelType, selectedRows} = this.props;
        if (rowModelType === 'infinite') {
            params.api.setDatasource(this.getDatasource());
        }

        this.setState({
            gridApi: params.api,
            gridColumnApi: params.columnApi,
        });

        this.updateColumnWidths();
        this.updateColumnState();

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
    }

    onCellClicked({value, column: {colId}, rowIndex, node}) {
        const timestamp = Date.now();
        this.props.setProps({
            cellClicked: {value, colId, rowIndex, rowId: node.id, timestamp},
        });
    }

    onCellValueChanged({
        oldValue,
        newValue,
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
                newValue,
                colId,
            },
            virtualRowData,
        });
    }

    onDisplayedColumnsChanged() {
        // this.updateColumnWidths();
    }

    onGridSizeChanged() {
        // this.updateColumnWidths();
    }

    updateColumnWidths() {
        if (this.state.gridApi || this.state.gridColumnApi) {
            if (this.props.columnSize === 'autoSizeAll') {
                this.state.gridColumnApi.autoSizeAllColumns(false);
            } else if (this.props.columnSize === 'sizeToFit') {
                this.state.gridApi.sizeColumnsToFit();
            }
        }
    }

    parseFunction(funcString) {
        const parsedCondition = esprima.parse(funcString).body[0].expression;
        const context = {
            d3,
            ...customFunctions,
            ...window.dashAgGridFunctions,
            ...window.dashSharedVariables,
        };
        return (params) => evaluate(parsedCondition, {params, ...context});
    }

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

    resetColumnState() {
        this.state.gridColumnApi.resetColumnState();
        this.props.setProps({
            resetColumnState: false,
        });
    }

    exportDataAsCsv(csvExportParams) {
        this.state.gridApi.exportDataAsCsv(csvExportParams);
        this.props.setProps({
            exportDataAsCsv: false,
        });
    }

    selectAll(opts) {
        if (opts?.filtered) {
            this.state.gridApi.selectAllFiltered();
        } else {
            this.state.gridApi.selectAll();
        }
        this.props.setProps({
            selectAll: false,
        });
    }

    deselectAll() {
        this.state.gridApi.deselectAll();
        this.props.setProps({
            deselectAll: false,
        });
    }

    deleteSelectedRows() {
        const sel = this.state.gridApi.getSelectedRows();
        this.state.gridApi.applyTransaction({remove: sel});
        this.props.setProps({
            deleteSelectedRows: false,
            rowData: this.getRowData(),
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

    autoSizeAllColumns(opts) {
        const {getColumnState, autoSizeColumns} = this.state.gridColumnApi;
        const allColumnIds = getColumnState().map((column) => column.colId);
        const skipHeaders = Boolean(opts?.skipHeaders);
        autoSizeColumns(allColumnIds, skipHeaders);
        this.props.setProps({
            autoSizeAllColumns: false,
        });
    }

    updateColumnState() {
        this.props.setProps({
            columnState: JSON.parse(
                JSON.stringify(this.state.gridColumnApi.getColumnState())
            ),
            updateColumnState: false,
        });
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
            autoSizeAllColumns,
            deleteSelectedRows,
            rowTransaction,
            updateColumnState,
            csvExportParams,
            detailCellRendererParams,
            setProps,
            // eslint-disable-next-line no-unused-vars
            dangerously_allow_code,
            dashGridOptions,
            ...restProps
        } = this.props;

        const convertedProps = this.convertAllProps({
            ...dashGridOptions,
            ...restProps,
        });

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

        if (autoSizeAllColumns) {
            this.autoSizeAllColumns(autoSizeAllColumns);
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

        const callbackGetDetail = (params) => {
            const {data} = params;
            this.getDetailParams = params;
            // Adding the current time in ms forces Dash to trigger a callback
            // when the same row is closed and re-opened.
            setProps({getDetailRequest: {data: data, requestTime: Date.now()}});
        };

        function suppressGetDetail(colName) {
            return (params) => {
                params.successCallback(params.data[colName]);
            };
        }

        let newDetailCellRendererParams = null;
        if (this.props.masterDetail) {
            newDetailCellRendererParams = {
                ...omit(
                    ['detailColName', 'suppressCallback'],
                    detailCellRendererParams
                ),
                getDetailRowData: detailCellRendererParams.suppressCallback
                    ? suppressGetDetail(detailCellRendererParams.detailColName)
                    : callbackGetDetail,
            };
        }

        return (
            <div
                id={id}
                className={className}
                style={{
                    ...style,
                }}
            >
                <AgGridReact
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
                    onGridSizeChanged={debounce(
                        this.onGridSizeChanged,
                        RESIZE_DEBOUNCE_MS
                    )}
                    components={this.state.components}
                    detailCellRendererParams={newDetailCellRendererParams}
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
