import React, {Component} from 'react';
import PropTypes from 'prop-types';
import * as evaluate from 'static-eval';
import * as esprima from 'esprima';
import {omit} from 'ramda';
import {propTypes, defaultProps} from '../components/AgGrid.react';
import {expressWarn, gridFunctions, columnFunctions} from '../utils/functionVars'

import MarkdownRenderer from '../renderers/markdownRenderer';
import RowMenuRenderer from '../renderers/rowMenuRenderer';
import {customFunctions} from '../renderers/customFunctions';

import 'ag-grid-community';
import { AgGridReact } from 'ag-grid-react';

import lodash from 'lodash';

import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';
import 'ag-grid-community/styles/ag-theme-balham.css';
import 'ag-grid-community/styles/ag-theme-material.css';

// d3 imports
import * as d3Format from "d3-format"
import * as d3Time from "d3-time"
import * as d3TimeFormat from "d3-time-format"
import * as d3Array from "d3-array"
const d3 = {...d3Format, ...d3Time, ...d3TimeFormat, ...d3Array};

// Rate-limit for resizing columns when table div is resized
const RESIZE_DEBOUNCE_MS = 200;

export default class DashAgGrid extends Component {
    constructor(props) {
        super(props);

        this.state = {...this.props.parentState}
        this.state.components = {
            rowMenu: this.generateRenderer(RowMenuRenderer),
            markdown: this.generateRenderer(MarkdownRenderer),
        }

        const customComponents = window.dashAgGridComponentFunctions
        if (customComponents) {
            Object.keys(customComponents).forEach(function(key, index) {
                if (typeof customComponents[key] != 'function') {
                    customComponents[key] = this.generateRenderer(JSON.parse(JSON.stringify(customComponents[key])))
                }
            })

            this.state.components = Object.assign(this.state.components, {...customComponents})
        }

        this.onGridReady = this.onGridReady.bind(this);
        this.onSelectionChanged = this.onSelectionChanged.bind(this);
        this.onCellClicked = this.onCellClicked.bind(this);
        this.onCellValueChanged = this.onCellValueChanged.bind(this);
        this.onRowDataUpdated = this.onRowDataUpdated.bind(this);
        this.onFilterChanged = this.onFilterChanged.bind(this);
        this.onSortChanged = this.onSortChanged.bind(this);
        this.onRowGroupOpened = this.onRowGroupOpened.bind(this);
        this.onDisplayedColumnsChanged = this.onDisplayedColumnsChanged.bind(
            this
        );
        this.onGridSizeChanged = this.onGridSizeChanged.bind(this);
        this.updateColumnWidths = this.updateColumnWidths.bind(this);
        this.handleDynamicCellStyle = this.handleDynamicCellStyle.bind(this);
        this.handleDynamicRowStyle = this.handleDynamicRowStyle.bind(this);
        this.generateRenderer = this.generateRenderer.bind(this);
        this.resetColumnState = this.resetColumnState.bind(this);
        this.exportDataAsCsv = this.exportDataAsCsv.bind(this);
        this.setSelection = this.setSelection.bind(this);
        this.parseParamFunction = this.parseParamFunction.bind(this);
        this.buildArray = this.buildArray.bind(this);
        this.fixCols = this.fixCols.bind(this);

        //Additional Exposure
        this.setUpCols = this.setUpCols.bind(this);
        this.selectAll = this.selectAll.bind(this);
        this.selectAllFiltered = this.selectAllFiltered.bind(this);
        this.deselectAll = this.deselectAll.bind(this);
        this.autoSizeAllColumns = this.autoSizeAllColumns.bind(this);
        this.updateColumnState = this.updateColumnState.bind(this);
        this.deleteSelectedRows = this.deleteSelectedRows.bind(this);
        this.rowTransaction = this.rowTransaction.bind(this);
        this.getRowData = this.getRowData.bind(this);

        this.selectionEventFired = false;

    }

    setSelection(selection) {
        if (this.state.gridApi && selection) {
            if (!selection.length) {
                this.state.gridApi.deselectAll();
            } else {
                this.state.gridApi.forEachNode((node) => {
                    let isSelected = selection.some((i) => {
                        // Return true if the node data is the same as i, false if it is different
                        return lodash.isEqual(i, node.data);
                    });
                    node.setSelected(isSelected);
                });
            }
        }
    }

    fixCols(columnDef, templateMessage) {

        const test = (target) => {
            if (target in columnDef) {
                if (!(this.state.dangerously_allow_code) && expressWarn.includes(target)) {
                    if (typeof columnDef[target] !== 'function') {
                        if (!(Object.keys(columnDef[target]).includes('function'))) {
                            columnDef[target] = (params) => {return ''}
                            console.error({field: columnDef['field'] || columnDef['headerName'], message: templateMessage})
                        }
                    }
                }
                if (typeof columnDef[target] !== 'function') {
                    if (Object.keys(columnDef[target]).includes('function')) {
                        const newFunc = JSON.parse(JSON.stringify(columnDef[target]['function']))
                        columnDef[target] = (params) => this.parseParamFunction(params, newFunc)
                    }
                }
            }
        }

        if ("headerComponentParams" in columnDef) {
            if ('template' in columnDef['headerComponentParams'] && !(this.state.dangerously_allow_code)) {
                columnDef['headerComponentParams']['template'] = '<div></div>'
                console.error({field: columnDef['field'], message: templateMessage})
            }
        }

        columnFunctions.concat(expressWarn).map(test)

        return columnDef
    }

    setUpCols(cellStyle) {
        const templateMessage = 'you are trying to use a dangerous element that could lead to XSS'
        if (this.props.columnDefs) {
            this.props.setProps(
                {columnDefs: this.props.columnDefs.map((columnDef) => {
                    if ('children' in columnDef) {
                        columnDef['children'] = columnDef['children'].map((child) => {
                                child = this.fixCols(child, templateMessage)

                                if ('cellStyle' in child) {
                                    return child
                                }
                                return {
                                        ...omit(['id'], child),
                                        cellStyle: (params) =>
                                            this.handleDynamicCellStyle({params, cellStyle}),
                                    }
                            })
                        }

                    columnDef = this.fixCols(columnDef, templateMessage)

                    if ('cellStyle' in columnDef) {
                        return columnDef
                    }
                    return {
                            ...omit(['id'], columnDef),
                            cellStyle: (params) =>
                                this.handleDynamicCellStyle({params, cellStyle}),
                        }

                    })
                }
            )
        }
    }

    onFilterChanged(e) {
        const {setProps} = this.props;
        let virtualRowData = [];
        this.state.gridApi.forEachNodeAfterFilter((node) => {
            virtualRowData.push(node.data);
        });

        const filterModel = this.state.gridApi.getFilterModel();
        this.setState({filterModel: filterModel});
        setProps({virtualRowData: virtualRowData});
    }

    getRowData() {
        let newRowData = [];
        this.state.gridApi.forEachNode((node) => {
            newRowData.push(node.data);
        })
        return newRowData;
    }

    onSortChanged(e) {
        const {setProps, columnState} = this.props;
        let virtualRowData = [];
        this.state.gridApi.forEachNodeAfterFilterAndSort((node) => {
            virtualRowData.push(node.data);
        });

        setProps({
            virtualRowData: virtualRowData,
            columnState: this.state.gridColumnApi.getColumnState(),
        });
    }

    shouldComponentUpdate(nextProps, nextState) {
        if (JSON.stringify(nextProps) === JSON.stringify(this.props)) {
            return false;
        }
        return true
    }

    componentDidMount() {
        this.state.mounted = true
    }

    componentDidUpdate(prevProps, prevState) {
        const {
            selectionChanged,
            getDetailResponse,
            detailCellRendererParams,
            masterDetail,
            setProps,
            cellStyle,
            dashGridOptions,
            rowData,
            columnSize,
        } = this.props;

        if (this.isDatasourceLoadedForInfiniteScrolling()) {
            const {rowData, rowCount} = this.props.getRowsResponse;
            this.getRowsParams.successCallback(rowData, rowCount);
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
            !lodash.isEqual(selectionChanged, prevProps.selectionChanged) &&
            !this.selectionEventFired
        ) {
            this.setSelection(selectionChanged);
        }

        if (JSON.stringify(cellStyle) != JSON.stringify(prevProps.cellStyle) ||
         JSON.stringify(this.props.columnDefs) != JSON.stringify(prevProps.columnDefs) ||
        prevProps.columnSize != columnSize) {
            this.props.setProps({columnDefs: JSON.parse(JSON.stringify(this.props.columnDefs))})
            this.setState({origColumnDefs: JSON.parse(JSON.stringify(this.props.columnDefs))})
            this.setUpCols(cellStyle)
            this.updateColumnWidths()
        }

        if (dashGridOptions != prevProps.dashGridOptions) {
            this.props.setProps(JSON.parse(JSON.stringify({...omit(['cellClassRules', 'rowClassRules'], this.props.dashGridOptions)})))
        }

        // Reset selection event flag
        this.selectionEventFired = false;

    }

    onRowDataUpdated({api, columnApi, context, type}) {
        // Handles preserving existing selections when rowData is updated in a callback
        const {selectionChanged} = this.props;
        const {openGroups, filterModel} = this.state;

        // Call the API to select rows
        this.setSelection(selectionChanged);
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
        if (!lodash.isEmpty(filterModel)) {
            this.state.gridApi.setFilterModel(filterModel);
        }
    }

    onRowGroupOpened(e) {
        let {openGroups} = this.state;

        if (e.expanded) {
            // If the node was just expanded, add it to the list of open nodes
            openGroups.add(e.node.key);
        } else {
            // If it's collapsed, remove it from the list of open nodes
            openGroups.delete(e.node.key);
        }
        this.setState({openGroups: openGroups});
    }

    onSelectionChanged() {
        // Flag that the selection event was fired
        this.selectionEventFired = true;
        const selectedRows = this.state.gridApi.getSelectedRows();
        this.props.setProps({selectionChanged: selectedRows});
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
        if ('async' in data) {
            if (data['async']) {gridApi.applyTransactionAsync(data)}
            else {gridApi.applyTransaction(data)}
            }
            else {gridApi.applyTransactionAsync(data)}
    }

    onGridReady(params) {
        // Applying Infinite Row Model
        // see: https://www.ag-grid.com/javascript-grid/infinite-scrolling/
        const {rowModelType, selectionChanged} = this.props;
        if (rowModelType === 'infinite') {
            params.api.setDatasource(this.getDatasource());
        }

        this.setState({
            gridApi: params.api,
            gridColumnApi: params.columnApi,
        });

        this.updateColumnWidths()

        if (this.state.rowTransaction) {
            this.state.rowTransaction.map((data) => this.applyRowTransaction(data, params.api))
            this.state.rowTransaction = null;
            this.props.setProps({rowData: this.getRowData()})
        }

        // Handles applying selections when a selection was persisted by Dash
        this.setSelection(selectionChanged);
        this.props.setProps({gridReady: true});
        // Hydrate virtualRowData
        this.onFilterChanged(true);

    }

    onCellClicked({value, column: {colId}, rowIndex}) {
        const timestamp = Date.now()
        this.props.setProps({cellClicked: {value, colId, rowIndex, timestamp}});
    }

    onCellValueChanged({oldValue, newValue, column: {colId}, rowIndex, data, node}) {
        const nodeId = JSON.parse(JSON.stringify(node.id))
        this.props.setProps({
            cellValueChanged: {rowIndex, nodeId, data, oldValue, newValue, colId},
        });
    }

    onDisplayedColumnsChanged(e) {
//        this.updateColumnWidths();
    }

    onGridSizeChanged(e) {
//        this.updateColumnWidths();
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

    /**
     * @params AG-Grid Styles rules attribute.
     * See: https://www.ag-grid.com/react-grid/cell-styles/#cell-style-cell-class--cell-class-rules-params
     */
    handleDynamicCellStyle({params, cellStyle = {}}) {
        const {styleConditions, defaultStyle} = cellStyle;

        if (styleConditions && styleConditions.length > 0) {
            for (const styleCondition of styleConditions) {
                const {condition, style} = styleCondition;
                const parsedCondition = esprima.parse(condition).body[0]
                    .expression;

                if (evaluate(parsedCondition, {...params})) {
                    return style;
                }
            }
        }

        return defaultStyle ? defaultStyle : null;
    }

    evaluateFunction = (tempFunction, params) => {
        const parsedCondition = esprima.parse(tempFunction).body[0]
                    .expression;
        const value = evaluate(parsedCondition, {params, d3, ...customFunctions, ...window.dashAgGridFunctions,
        ...window.dashSharedVariables})
        return value
    }

    /**
     * @params AG-Grid Styles rules attribute.
     * See: https://www.ag-grid.com/react-grid/row-styles/#row-style-row-class--row-class-rules-params
     */
    handleDynamicRowStyle({params, getRowStyle = {}}) {
        const {styleConditions, defaultStyle} = getRowStyle;

        if (styleConditions && styleConditions.length > 0) {
            for (const styleCondition of styleConditions) {
                const {condition, style} = styleCondition;

                if (this.evaluateFunction(condition, params)) {
                    return style;
                }
            }
        }

        return defaultStyle ? defaultStyle : null;
    }

    parseParamFunction(params, tempFunction) {
        try {
            return this.evaluateFunction(tempFunction, params)
        } catch (err) {
            console.log(err)
        }
        return ''
    }

    generateRenderer(Renderer) {
        const {setProps} = this.props;
        const {dangerously_allow_code} = this.state;

        const setCellProps = (props) => {
            setProps({clickData: props.clickData, hoverData: props.hoverData});
        };

        return (props) => (
            <Renderer setProps={setCellProps} dangerously_allow_code={dangerously_allow_code} {...props}></Renderer>
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

    selectAll() {
        this.state.gridApi.selectAll()
        this.props.setProps({
            selectAll: false,
        });
    }

    selectAllFiltered() {
        this.state.gridApi.selectAllFiltered()
        this.props.setProps({
            selectAllFiltered: false,
        });
    }

    deselectAll() {
        this.state.gridApi.deselectAll()
        this.props.setProps({
            deselectAll: false,
        });
    }

    deleteSelectedRows() {
        const sel = this.state.gridApi.getSelectedRows();
        this.state.gridApi.applyTransaction({remove: sel});
        this.props.setProps({
            deleteSelectedRows: false,
            rowData: this.getRowData()
        });
    }

    buildArray(arr1, arr2) {
        if (arr1) {
            if (!(JSON.parse(JSON.stringify(arr1)).includes(JSON.parse(JSON.stringify(arr2))))) {
                arr1.push(arr2)
            }
        } else {
            arr1 = [JSON.parse(JSON.stringify(arr2))]
        }
        return arr1
    }

    rowTransaction(data) {
        if (this.state.mounted) {
            if (this.state.gridApi) {
                if (this.state.rowTransaction) {
                    this.state.rowTransaction.map((data) => this.applyRowTransaction(data))
                    this.state.rowTransaction = null;
                }
                this.applyRowTransaction(data)
                this.props.setProps({
                    rowTransaction: null,
                    rowData: this.getRowData()
                })
            } else {
                if (this.state.rowTransaction) {
                    this.state.rowTransaction = this.buildArray(this.state.rowTransaction, data)
                } else {
                    this.state.rowTransaction = [JSON.parse(JSON.stringify(data))]
                }
            }
        }
    }

    autoSizeAllColumns(skipHeader) {
        const allColumnIds = [];
        this.state.gridColumnApi.getColumnState().forEach((column) => {
          allColumnIds.push(column.colId);
        });
        this.state.gridColumnApi.autoSizeColumns(allColumnIds, skipHeader);
        this.props.setProps({
            autoSizeAllColumns: false,
            autoSizeAllColumnsSkipHeaders: false,
        });
    };

    updateColumnState () {
        this.props.setProps({
            columnState: JSON.parse(JSON.stringify(this.state.gridColumnApi.getColumnState())),
            updateColumnState: false
        })
    }

    render() {
        const {
            id,
            cellStyle,
            getRowStyle,
            style,
            theme,
            className,
            resetColumnState,
            exportDataAsCsv,
            selectAll,
            selectAllFiltered,
            deselectAll,
            autoSizeAllColumns,
            autoSizeAllColumnsSkipHeaders,
            deleteSelectedRows,
            rowTransaction,
            updateColumnState,
            csvExportParams,
            detailCellRendererParams,
            setProps,
            dangerously_allow_code,
            ...restProps
        } = this.props;

        const replaceFunc = (keyPair) => {
            const target = Object.keys(keyPair)[0]
            const varType = keyPair[target]
//            if (!varType || varType == 'params') {   <---- unused currently
                if (target in this.props) {
                    if (!(this.state.dangerously_allow_code) && expressWarn.includes(target)) {
                        if (typeof this.props[target] !== 'function') {
                            if (!(Object.keys(this.props[target]).includes('function'))) {
                                this.props[target] = (params) => {return ''}
                                console.error({prop: target, message: 'you are trying to use an unsafe prop without dangerously_allow_code'})
                            }
                        }
                    }
                    if (typeof this.props[target] !== 'function') {
                        if (Object.keys(this.props[target]).includes('function')) {
                            const newFunc = JSON.parse(JSON.stringify(this.props[target]['function']))
                            this.props[target] = (params) => this.parseParamFunction(params, newFunc)
                        }
                    }
                }
                if (this.props.dashGridOptions) {
                    if (target in this.props.dashGridOptions) {
                        if (!(this.state.dangerously_allow_code) && expressWarn.includes(target)) {
                            if (typeof this.props.dashGridOptions[target] !== 'function') {
                                if (!(Object.keys(this.props.dashGridOptions[target]).includes('function'))) {
                                    this.props.dashGridOptions[target] = (params) => {return ''}
                                    console.error({prop: target, message: 'you are trying to use an unsafe prop without dangerously_allow_code'})
                                }
                            }
                        }
                        if (typeof this.props.dashGridOptions[target] !== 'function') {
                            if (Object.keys(this.props.dashGridOptions[target]).includes('function')) {
                                const newFunc = JSON.parse(JSON.stringify(this.props.dashGridOptions[target]['function']))
                                this.props.dashGridOptions[target] = (params) => this.parseParamFunction(params, newFunc)
                            }
                        }
                    }
                }
//            }
//            else if (varType == 'rowNode') { <---- unused currently
//                if (target in this.props) {
//                    if (!(this.state.dangerously_allow_code) && expressWarn.includes(target)) {
//                        if (typeof this.props[target] !== 'function') {
//                            if (!(Object.keys(this.props[target]).includes('function'))) {
//                                this.props[target] = (rowNode) => {return ''}
//                                console.error({prop: target, message: 'you are trying to use an unsafe prop without dangerously_allow_code'})
//                            }
//                        }
//                    }
//                    if (typeof this.props[target] !== 'function') {
//                        if (Object.keys(this.props[target]).includes('function')) {
//                            const newFunc = JSON.parse(JSON.stringify(this.props[target]['function']))
//                            this.props[target] = (rowNode) => this.parseParamFunction(rowNode, newFunc)
//                        }
//                    }
//                }
//                if (target in this.props.dashGridOptions) {
//                    if (!(this.state.dangerously_allow_code) && expressWarn.includes(target)) {
//                        if (typeof this.props.dashGridOptions[target] !== 'function') {
//                            if (!(Object.keys(this.props.dashGridOptions[target]).includes('function'))) {
//                                this.props.dashGridOptions[target] = (rowNode) => {return ''}
//                                console.error({prop: target, message: 'you are trying to use an unsafe prop without dangerously_allow_code'})
//                            }
//                        }
//                    }
//                    if (typeof this.props.dashGridOptions[target] !== 'function') {
//                        if (Object.keys(this.props.dashGridOptions[target]).includes('function')) {
//                            const newFunc = JSON.parse(JSON.stringify(this.props.dashGridOptions[target]['function']))
//                            this.props.dashGridOptions[target] = (rowNode) => this.parseParamFunction(rowNode, newFunc)
//                        }
//                    }
//                }
//            }
        }

        gridFunctions.map(replaceFunc)

        //Disable cellClassRules and rowClassRules if dangerously_allow_code is disabled
        let cellClassRules;
        let rowClassRules;
        if (!this.state.dangerously_allow_code) {
            cellClassRules = null;
            rowClassRules = null;
        } else {
            cellClassRules = this.props.cellClassRules;
            rowClassRules = this.props.rowClassRules;
        }

        let getRowId;
        if (this.props.getRowId) {
            getRowId = (params) => this.parseParamFunction(params, JSON.parse(JSON.stringify(this.props.getRowId)))
        }

        this.setUpCols(cellStyle)

        let newRowStyle;
        if (getRowStyle) {
            newRowStyle = (params) => this.handleDynamicRowStyle({params, getRowStyle})
        }

        if (resetColumnState) {
            this.resetColumnState();
        }

        if (exportDataAsCsv) {
            this.exportDataAsCsv(csvExportParams);
        }

        if (selectAll) {
            this.selectAll();
        }

        if (selectAllFiltered) {
            this.selectAllFiltered();
        }

        if (deselectAll) {
            this.deselectAll();
        }

        if (autoSizeAllColumns) {
            this.autoSizeAllColumns(false);
        }

        if (autoSizeAllColumnsSkipHeaders) {
            this.autoSizeAllColumns(true);
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
            const {data, node} = params;
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
                className={theme ? 'ag-theme-' + theme : className}
                style={{
                    ...style,
                }}
            >
                <AgGridReact
                    getRowId={getRowId}
                    getRowStyle={newRowStyle}
                    onGridReady={this.onGridReady}
                    onSelectionChanged={this.onSelectionChanged}
                    onCellClicked={this.onCellClicked}
                    onCellValueChanged={this.onCellValueChanged}
                    onFilterChanged={this.onFilterChanged}
                    onSortChanged={this.onSortChanged}
                    onRowDataUpdated={this.onRowDataUpdated}
                    onRowGroupOpened={this.onRowGroupOpened}
                    onDisplayedColumnsChanged={this.onDisplayedColumnsChanged}
                    onGridSizeChanged={lodash.debounce(
                        this.onGridSizeChanged,
                        RESIZE_DEBOUNCE_MS
                    )}
                    components={this.state.components}
                    detailCellRendererParams={newDetailCellRendererParams}
                    cellClassRules={cellClassRules}
                    rowClassRules={rowClassRules}
                    {...omit(['cellClassRules', 'rowClassRules'], this.props.dashGridOptions)}
                    {...omit(['theme', 'cellClassRules', 'rowClassRules', 'getRowId'], restProps)}

                >
                </AgGridReact>
            </div>
        );
    };
}

DashAgGrid.defaultProps = defaultProps;
DashAgGrid.propTypes = {parentState: PropTypes.any, ...propTypes};
