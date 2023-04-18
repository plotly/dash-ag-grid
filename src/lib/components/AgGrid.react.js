import PropTypes from 'prop-types';
import LazyLoader from '../LazyLoader';
import React, {Component, lazy, Suspense} from 'react';

const RealAgGrid = lazy(LazyLoader.agGrid);
const RealAgGridEnterprise = lazy(LazyLoader.agGridEnterprise);

function getGrid(enable) {
    return enable ? RealAgGridEnterprise : RealAgGrid;
}

export default class DashAgGrid extends Component {
    constructor(props) {
        super(props);

        this.state = {
            gridApi: null,
            columnApi: null,
            openGroups: new Set(),
            filterModel: {},
        };

        this.buildArray = this.buildArray.bind(this);
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

    UNSAFE_componentWillReceiveProps(nextProps) {
        if (this.props.rowTransaction && !this.state.mounted) {
            if (nextProps.rowTransaction !== this.props.rowTransaction) {
                this.setState({
                    rowTransaction: this.buildArray(
                        this.state.rowTransaction,
                        this.props.rowTransaction
                    ),
                });
            }
        }
    }

    render() {
        const {enableEnterpriseModules} = this.props;

        const RealComponent = getGrid(enableEnterpriseModules);
        return (
            <Suspense fallback={null}>
                <RealComponent parentState={this.state} {...this.props} />
            </Suspense>
        );
    }
}

DashAgGrid.defaultProps = {
    style: {height: '400px', width: '100%'},
    className: 'ag-theme-alpine',
    resetColumnState: false,
    exportDataAsCsv: false,
    selectAll: false,
    deselectAll: false,
    enableEnterpriseModules: false,
    updateColumnState: false,
    persisted_props: ['selectedRows'],
    persistence_type: 'local',
    suppressDragLeaveHidesColumns: true,
    dangerously_allow_code: false,
    rowModelType: 'clientSide',
    dashGridOptions: {},
    filterModel: {},
    paginationGoTo: null,
    gridReady: false,
};
DashAgGrid.propTypes = {
    /********************************
     * DASH PROPS
     *******************************/

    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Initial prop is false, will be updated to True once the grid is ready.
     */
    gridReady: PropTypes.bool,

    /**
     * Dash-assigned callback that gets fired when the input changes
     */
    setProps: PropTypes.func,

    /**
     * The CSS style for the component
     */
    style: PropTypes.object,

    /**
     * The class for the ag-grid.  Can specify the ag-grid theme here.
     */
    className: PropTypes.string,

    /**
     * Used to allow user interactions in this component to be persisted when
     * the component - or the page - is refreshed. If `persisted` is truthy and
     * hasn't changed from its previous value, a `value` that the user has
     * changed while using the app will keep that change, as long as
     * the new `value` also matches what was given originally.
     * Used in conjunction with `persistence_type`.
     */
    persistence: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.string,
        PropTypes.number,
    ]),

    /**
     * Properties whose user interactions will persist after refreshing the
     * component or the page. Since only `value` is allowed this prop can
     * normally be ignored.
     */
    persisted_props: PropTypes.arrayOf(PropTypes.string),

    /**
     * Where persisted user changes will be stored:
     * memory: only kept in memory, reset on page refresh.
     * local: window.localStorage, data is kept after the browser quit.
     * session: window.sessionStorage, data is cleared once the browser quit.
     */
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),

    /**
     * Allow strings containing JavaScript code or HTML in certain props.
     * If your app stores Dash layouts for later retrieval this is dangerous
     * because it can lead to cross-site-scripting attacks.
     */
    dangerously_allow_code: PropTypes.bool,

    /********************************
     * CUSTOM PROPS
     *******************************/

    /**
     * If true, the internal method resetColumnState() will be called
     */
    resetColumnState: PropTypes.bool,

    /**
     * If true, the internal method exportDataAsCsv() will be called
     */
    exportDataAsCsv: PropTypes.bool,

    /**
     * Set to true to cause all rows to be selected,
     * Or pass an object of options for which rows to select.
     * Currently supports `filtered`, set to true to only select filtered rows.
     */
    selectAll: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.exact({
            filtered: PropTypes.bool,
        }),
    ]),

    /**
     * If true, the internal method deselectAll() will be called
     */
    deselectAll: PropTypes.bool,

    /**
     * If true, the internal method updateColumnState() will be called
     */
    updateColumnState: PropTypes.bool,

    /**
     * If true, the internal method deleteSelectedRows() will be called
     */
    deleteSelectedRows: PropTypes.bool,

    /**
     * If true, the internal method rowTransaction() will be used,
     * if async provided as false, applyTransaction() will be called, else applyTransactionAsync()
     */
    rowTransaction: PropTypes.shape({
        async: PropTypes.bool,
        add: PropTypes.array,
        update: PropTypes.array,
        remove: PropTypes.array,
        addIndex: PropTypes.number,
    }),

    /**
     * This is required for change detection in rowData
     */
    getRowId: PropTypes.string,

    /**
     * Current state of the columns
     */
    columnState: PropTypes.array,

    /**
     * Object with properties to pass to the exportDataAsCsv() method
     */
    csvExportParams: PropTypes.shape({
        /**
         * Delimiter to insert between cell values.
         */
        columnSeparator: PropTypes.string,

        /**
         * Pass true to insert the value into the CSV file without escaping. In this case it is your responsibility to ensure that no cells contain the columnSeparator character.
         */
        suppressQuotes: PropTypes.bool,

        /**
         * Content to put at the top of the file export. A 2D array of CsvCell objects.
         */
        prependContent: PropTypes.string,

        /**
         * Content to put at the bottom of the file export.
         */
        appendContent: PropTypes.string,

        /**
         * If true, all columns will be exported in the order they appear in the columnDefs.
         */
        allColumns: PropTypes.bool,

        /**
         * Provide a list (an array) of column keys or Column objects if you want to export specific columns.
         */
        columnKeys: PropTypes.arrayOf(PropTypes.string),

        /**
         * String to use as the file name
         */
        fileName: PropTypes.string,

        /**
         * Export only selected rows.
         */
        onlySelected: PropTypes.bool,

        /**
         * Only export selected rows including other pages (only makes sense when using pagination).
         */
        onlySelectedAllPages: PropTypes.bool,

        /**
         * Set to true to skip include header column groups.
         */
        skipColumnGroupHeaders: PropTypes.bool,

        /**
         * Set to true if you don't want to export column headers.
         */
        skipColumnHeaders: PropTypes.bool,

        /**
         * Set to true to skip row group headers if grouping rows. Only relevant when grouping rows.
         */
        skipRowGroups: PropTypes.bool,

        /**
         * Set to true to suppress exporting rows pinned to the top of the grid.
         */
        skipPinnedTop: PropTypes.bool,

        /**
         * Set to true to suppress exporting rows pinned to the bottom of the grid.
         */
        skipPinnedBottom: PropTypes.bool,
    }),

    /**
     * Size the columns autoSize changes the column sizes to fit the column's content,
     * sizeToFit changes the column sizes to fit the width of the table
     * responsiveSizeToFit changes the column sizes to fit the width of the table and also resizing upon grid or column changes
     * and null bypasses the altering of the column widths
     */
    columnSize: PropTypes.oneOf([
        'sizeToFit',
        'autoSize',
        'responsiveSizeToFit',
        null,
    ]),

    /**
     * Options to customize the columnSize operation.
     * autoSize calls either autoSizeColumns or autoSizeAllColumns, see:
     * https://www.ag-grid.com/react-data-grid/column-sizing/#autosize-column-api,
     * and sizeToFit and responsiveSizeToFit call sizeColumnsToFit, see:
     * https://www.ag-grid.com/react-data-grid/column-sizing/#size-columns-to-fit
     */
    columnSizeOptions: PropTypes.exact({
        /**
         * for (responsive)sizeToFit: per-column minimum and maximum width, in pixels.
         */
        columnLimits: PropTypes.arrayOf(
            PropTypes.exact({
                key: PropTypes.string,
                minWidth: PropTypes.number,
                maxWidth: PropTypes.number,
            })
        ),
        /**
         * for (responsive)sizeToFit: default minimum width, in pixels, if not overridden by columnLimits
         */
        defaultMinWidth: PropTypes.number,
        /**
         * for (responsive)sizeToFit: default maximum width, in pixels, if not overridden by columnLimits
         */
        defaultMaxWidth: PropTypes.number,
        /**
         * for autoSize: list of column keys to autosize. If omitted, all columns will be autosized.
         */
        keys: PropTypes.arrayOf(PropTypes.string),
        /**
         * for autoSize: If skipHeader=True, the header won't be included when calculating the column widths.
         * default: False
         */
        skipHeader: PropTypes.bool,
    }),

    /**
     * Object used to perform the row styling. See AG-Grid Row Style.
     */
    getRowStyle: PropTypes.shape({
        styleConditions: PropTypes.arrayOf(
            PropTypes.shape({
                condition: PropTypes.string.isRequired,
                style: PropTypes.object.isRequired,
            })
        ),
        defaultStyle: PropTypes.object,
    }),

    /**
     * Infinite Scroll, Datasource interface
     * See https://www.ag-grid.com/react-grid/infinite-scrolling/#datasource-interface
     */
    getRowsRequest: PropTypes.shape({
        /**
         * The first row index to get.
         */
        startRow: PropTypes.number,

        /**
         * The first row index to NOT get.
         */
        endRow: PropTypes.number,

        /**
         * If sorting, what the sort model is
         */
        sortModel: PropTypes.arrayOf(PropTypes.object),

        /**
         * If filtering, what the filter model is
         */
        filterModel: PropTypes.object,

        /**
         * The grid context object
         */
        context: PropTypes.any,

        /**
         * Callback to call when the request is successful.
         */
        successCallback: PropTypes.func,

        /**
         * Callback to call when the request fails.
         */
        failCallback: PropTypes.func,
    }),

    /**
     * If in pagination mode, this will be populated with info from the pagination API:
     * https://www.ag-grid.com/react-data-grid/grid-api/#reference-pagination
     */
    paginationInfo: PropTypes.object,

    /**
     * If in pagination mode, this will navigate to: ['next', 'previous', 'last', 'first', number]
     * https://www.ag-grid.com/react-data-grid/grid-api/#reference-pagination
     */
    paginationGoTo: PropTypes.oneOfType([
        PropTypes.oneOf(['first', 'last', 'next', 'previous', null]),
        PropTypes.number,
    ]),

    /**
     * If filtering client-side rowModel, what the filter model is.
     * Passing a model back to this prop will apply it to the grid.
     */
    filterModel: PropTypes.object,

    /**
     * Request from Dash AgGrid when suppressCallback is disabled and a user opens a row with a detail grid
     */
    getDetailRequest: PropTypes.shape({
        /**
         * Details about the row that was opened.
         */
        data: PropTypes.any,
        /**
         * Datetime representing when the grid was requested.
         */
        requestTime: PropTypes.any,
    }),

    /**
     * RowData to populate the detail grid when callbacks are used to populate
     */
    getDetailResponse: PropTypes.arrayOf(PropTypes.object),

    /**
     * Special prop to allow feedback from cell renderer to the grid.
     */
    cellRendererData: PropTypes.shape({
        /**
         * Value set from the function
         */
        value: PropTypes.any,

        /**
         * Column ID from where the event was fired
         */
        colId: PropTypes.string,

        /**
         * Row Index from the grid, this is associated with the row count
         */
        rowIndex: PropTypes.number,

        /**
         * Row Id from the grid, this could be a number automatically, or set via getRowId
         */
        rowId: PropTypes.any,

        /**
         * Timestamp of when the event was fired
         */
        timestamp: PropTypes.any,
    }),

    /**
     * Serverside model data response object.
     * See https://www.ag-grid.com/react-grid/server-side-model-datasource/
     */
    getRowsResponse: PropTypes.shape({
        /**
         * Data retreived from the server
         */
        rowData: PropTypes.arrayOf(PropTypes.object),

        /**
         * Current row count, if known
         */
        rowCount: PropTypes.number,

        /**
         * Any extra info for the grid to associate with this load
         */
        storeInfo: PropTypes.any,
    }),

    /**
     * License key for ag-grid enterprise. If using Enterprise modules,
     * enableEnterpriseModules must also be true.
     */
    licenseKey: PropTypes.string,

    /**
     * If True, enable ag-grid Enterprise modules. Recommended to use with licenseKey.
     */
    enableEnterpriseModules: PropTypes.bool,

    /**
     * The rowData in the grid after inline filters are applied.
     */
    virtualRowData: PropTypes.arrayOf(PropTypes.object),

    /********************************
     * GRID PROPS
     *******************************/

    /**
     * Array of Column Definitions.
     */
    columnDefs: PropTypes.arrayOf(PropTypes.object),

    /**
     * A default column definition.
     */
    defaultColDef: PropTypes.object,

    /**
     * Sets the Row Model type.
     * Default Value: 'clientSide'
     */
    rowModelType: PropTypes.oneOf([
        'clientSide',
        'infinite',
        'viewport',
        'serverSide',
    ]),

    /**
     * (Client-Side Row Model only) Set the data to be displayed as rows in the grid.
     */
    rowData: PropTypes.arrayOf(PropTypes.object),

    /**
     * Used to enable Master Detail. See Enabling Master Detail.
     * Default Value: false
     */
    masterDetail: PropTypes.bool,

    /**
     * Specifies the params to be used by the default detail Cell Renderer. See Detail
     * Grids.
     */
    detailCellRendererParams: PropTypes.shape({
        /**
         * Grid options for detail grid in master-detail view.
         */
        detailGridOptions: PropTypes.any,

        /**
         * Column name where detail grid data is located in main dataset, for master-detail view.
         */
        detailColName: PropTypes.string,

        /**
         * Default: true. If true, suppresses the Dash callback in favor of using the data embedded in rowData at the given detailColName.
         */
        suppressCallback: PropTypes.bool,
    }),

    /**
     * The style to give a particular row. See Row Style.
     */
    rowStyle: PropTypes.object,

    /**
     * The class to give a particular row. See Row Class.
     */
    rowClass: PropTypes.string,

    /**
     * Rules which can be applied to include certain CSS classes. See Row Class Rules.
     */
    rowClassRules: PropTypes.object,

    /**
     * If true, when you drag a column out of the grid (e.g. to the group zone) the column
     * is not hidden.
     */
    suppressDragLeaveHidesColumns: PropTypes.bool,

    /********************************
     * EVENT PROPS
     *******************************/

    /**
     * Cell is clicked.
     */
    cellClicked: PropTypes.shape({
        /**
         * value of the clicked cell
         */
        value: PropTypes.any,

        /**
         * column where the cell was clicked
         */
        colId: PropTypes.any,

        /**
         * rowIndex, typically a row number
         */
        rowIndex: PropTypes.number,

        /**
         * Row Id from the grid, this could be a number automatically, or set via getRowId
         */
        rowId: PropTypes.any,

        /**
         * timestamp of last action
         */
        timestamp: PropTypes.any,
    }),

    /**
     * The actively selected rows from the grid (may include filtered rows)
     */
    selectedRows: PropTypes.arrayOf(PropTypes.object),

    /**
     * Value has changed after editing.
     */
    cellValueChanged: PropTypes.shape({
        /**
         * rowIndex, typically a row number
         */
        rowIndex: PropTypes.number,

        /**
         * Row Id from the grid, this could be a number automatically, or set via getRowId
         */
        rowId: PropTypes.any,

        /**
         * data, data object from the row
         */
        data: PropTypes.object,

        /**
         * old value of the cell
         */
        oldValue: PropTypes.any,

        /**
         * new value of the cell
         */
        newValue: PropTypes.any,

        /**
         * column where the cell was changed
         */
        colId: PropTypes.any,
    }),

    /**
     * Other ag-grid options
     */
    dashGridOptions: PropTypes.object,
};

export const propTypes = DashAgGrid.propTypes;
export const defaultProps = DashAgGrid.defaultProps;
