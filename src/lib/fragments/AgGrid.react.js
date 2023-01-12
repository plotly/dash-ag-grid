import React, {Component} from 'react';
import * as evaluate from 'static-eval';
import * as esprima from 'esprima';
import {omit} from 'ramda';
import {propTypes, defaultProps} from '../components/AgGrid.react';

import MarkdownRenderer from '../renderers/markdownRenderer';
import RowMenuRenderer from '../renderers/rowMenuRenderer';

import {AgGridReact, AgGridColumn} from '@ag-grid-community/react';
import {ModuleRegistry} from '@ag-grid-community/core';
import {AllCommunityModules} from '@ag-grid-community/all-modules';
import {AllModules} from '@ag-grid-enterprise/all-modules';
import {LicenseManager} from '@ag-grid-enterprise/core';

import lodash from 'lodash';

import '@ag-grid-community/core/dist/styles/ag-grid.css';
import '@ag-grid-community/core/dist/styles/ag-theme-alpine.css';
import '@ag-grid-community/core/dist/styles/ag-theme-balham.css';
import '@ag-grid-community/core/dist/styles/ag-theme-bootstrap.css';
import '@ag-grid-community/core/dist/styles/ag-theme-material.css';

// Rate-limit for resizing columns when table div is resized
const RESIZE_DEBOUNCE_MS = 200;

export default class DashAgGrid extends Component {
    constructor(props) {
        super(props);

        if (props.enableEnterpriseModules) {
            ModuleRegistry.registerModules(AllModules);
            if (props.licenseKey) {
                LicenseManager.setLicenseKey(props.licenseKey);
            }
        } else {
            ModuleRegistry.registerModules(AllCommunityModules);
        }

        this.onGridReady = this.onGridReady.bind(this);
        this.onSelectionChanged = this.onSelectionChanged.bind(this);
        this.onCellClicked = this.onCellClicked.bind(this);
        this.onCellValueChanged = this.onCellValueChanged.bind(this);
        this.onRowDataChanged = this.onRowDataChanged.bind(this);
        this.onFilterChanged = this.onFilterChanged.bind(this);
        this.onRowGroupOpened = this.onRowGroupOpened.bind(this);
        this.onDisplayedColumnsChanged = this.onDisplayedColumnsChanged.bind(
            this
        );
        this.onGridSizeChanged = this.onGridSizeChanged.bind(this);
        this.updateColumnWidths = this.updateColumnWidths.bind(this);
        this.handleDynamicCellStyle = this.handleDynamicCellStyle.bind(this);
        this.generateRenderer = this.generateRenderer.bind(this);
        this.resetColumnState = this.resetColumnState.bind(this);
        this.exportDataAsCsv = this.exportDataAsCsv.bind(this);
        this.setSelection = this.setSelection.bind(this);

        this.selectionEventFired = false;
        this.state = {
            gridApi: null,
            columnApi: null,
            frameworkComponents: {
                rowMenu: this.generateRenderer(RowMenuRenderer),
                markdown: this.generateRenderer(MarkdownRenderer)
            },
            openGroups: new Set(),
            filterModel: {},
        };
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

    componentDidUpdate(prevProps) {
        const {
            selectionChanged,
            getDetailResponse,
            detailCellRendererParams,
            masterDetail,
            setProps,
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

        // Reset selection event flag
        this.selectionEventFired = false;
    }

    onRowDataChanged() {
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

        // Handles applying selections when a selection was persisted by Dash
        this.setSelection(selectionChanged);
        this.props.setProps({gridReady: true});
        // Hydrate virtualRowData
        this.onFilterChanged(true);
    }

    onCellClicked({value, column: {colId}, rowIndex}) {
        this.props.setProps({cellClicked: {value, colId, rowIndex}});
    }

    onCellValueChanged({oldValue, newValue, column: {colId}, rowIndex}) {
        this.props.setProps({
            cellValueChanged: {oldValue, newValue, colId, rowIndex},
        });
    }

    onDisplayedColumnsChanged(e) {
        this.updateColumnWidths();
    }

    onGridSizeChanged(e) {
        this.updateColumnWidths();
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
     * @params AG-Grid Cell Style rules attribute.
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

    generateRenderer(Renderer) {
        const {setProps} = this.props;

        const setCellProps = (props) => {
            setProps({clickData: props.clickData, hoverData: props.hoverData});
        };

        return (props) => (
            <Renderer setProps={setCellProps} {...props}></Renderer>
        );
    }

    resetColumnState() {
        this.state.gridColumnApi.resetColumnState();
        this.props.setProps({
            enableResetColumnState: false,
        });
    }

    exportDataAsCsv(csvExportParams) {
        this.state.gridApi.exportDataAsCsv(csvExportParams);
        this.props.setProps({
            enableExportDataAsCsv: false,
        });
    }

    render() {
        const {
            id,
            children = null,
            cellStyle,
            columnDefs,
            style,
            theme,
            enableResetColumnState,
            enableExportDataAsCsv,
            csvExportParams,
            detailCellRendererParams,
            setProps,
            ...restProps
        } = this.props;

        const styledColumnDefs =
            columnDefs &&
            columnDefs.map((columnDef) => {
                if ('cellStyle' in columnDef) {
                    return columnDef;
                }

                return {
                    ...omit(['id'], columnDef),
                    cellStyle: (params) =>
                        this.handleDynamicCellStyle({params, cellStyle}),
                };
            });

        const cols = [];

        if (children) {
            React.Children.map(children, (child) => {
                if ('_dashprivate_layout' in child.props) {
                    const childProps = child.props._dashprivate_layout.props;

                    cols.push(
                        <AgGridColumn
                            {...omit(['id'], childProps)}
                            cellStyle={(params) =>
                                this.handleDynamicCellStyle({
                                    params,
                                    cellStyle,
                                })
                            }
                        ></AgGridColumn>
                    );
                }
            });
        }

        if (enableResetColumnState) {
            this.resetColumnState();
        }

        if (enableExportDataAsCsv) {
            this.exportDataAsCsv(csvExportParams);
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
                className={'ag-theme-' + theme}
                style={{
                    ...style,
                    ...{
                        '--ag-data-color': 'var(--text)',
                        '--ag-foreground-color': 'var(--text)',
                        '--ag-background-color': 'var(--background_content)',
                        '--ag-odd-row-background-color':
                            'var(--background_page)',
                        '--ag-header-background-color':
                            'var(--background_page)',
                        '--ag-border-color': 'var(--border)',
                        '--ag-secondary-border-color': 'var(--border)',
                        '--ag-checkbox-checked-color': 'var(--accent)',
                        '--ag-control-panel-background-color':
                            'var(--background_page)',
                        'font-family': 'var(--font_family, Arial)',
                    },
                }}
            >
                <AgGridReact
                    onGridReady={this.onGridReady}
                    onSelectionChanged={this.onSelectionChanged}
                    onCellClicked={this.onCellClicked}
                    onCellValueChanged={this.onCellValueChanged}
                    onFilterChanged={this.onFilterChanged}
                    onRowDataChanged={this.onRowDataChanged}
                    onRowGroupOpened={this.onRowGroupOpened}
                    onDisplayedColumnsChanged={this.onDisplayedColumnsChanged}
                    onGridSizeChanged={lodash.debounce(
                        this.onGridSizeChanged,
                        RESIZE_DEBOUNCE_MS
                    )}
                    columnDefs={styledColumnDefs}
                    frameworkComponents={this.state.frameworkComponents}
                    detailCellRendererParams={newDetailCellRendererParams}
                    {...omit(['theme'], restProps)}
                >
                    {cols}
                </AgGridReact>
            </div>
        );
    }
}

DashAgGrid.defaultProps = defaultProps;
DashAgGrid.propTypes = propTypes;