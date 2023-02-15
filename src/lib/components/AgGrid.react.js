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
            origColumnDefs: JSON.parse(JSON.stringify(this.props.columnDefs))

        };

        this.buildArray = this.buildArray.bind(this);
    }


    buildArray(arr1, arr2) {
        if (arr1) {
            if (!(JSON.parse(JSON.stringify(arr1)).includes(JSON.parse(JSON.stringify(arr2))))) {
                return [...arr1, arr2];
            }
            return arr1;
        }
        return [JSON.parse(JSON.stringify(arr2))];
    }

    UNSAFE_componentWillReceiveProps(nextProps) {
        if (this.props.rowTransaction && !this.state.mounted) {
            if (nextProps.rowTransaction !== this.props.rowTransaction) {
                this.setState({rowTransaction: this.buildArray(this.state.rowTransaction, this.props.rowTransaction)});
            }
        }
    }

    render() {
        const {enableEnterpriseModules} = this.props

        const RealComponent = getGrid(enableEnterpriseModules)
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
    selectAllFiltered: false,
    deselectAll: false,
    autoSizeAllColumns: false,
    autoSizeAllColumnsSkipHeaders: false,
    enableEnterpriseModules: false,
    updateColumnState: false,
    persisted_props: ['selectedRows'],
    persistence_type: 'local',
    suppressDragLeaveHidesColumns: true,
    dangerously_allow_code: false,
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
     * If true, the internal method selectAll() will be called
     */
    selectAll: PropTypes.bool,

    /**
     * If true, the internal method selectAllFiltered() will be called
     */
    selectAllFiltered: PropTypes.bool,

    /**
     * If true, the internal method deselectAll() will be called
     */
    deselectAll: PropTypes.bool,

    /**
     * If true, the internal method autoSizeAllColumns(false) will be called
     */
    autoSizeAllColumns: PropTypes.bool,

    /**
     * If true, the internal method autoSizeAllColumns(true) will be called
     */
    autoSizeAllColumnsSkipHeaders: PropTypes.bool,

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
     * Size the columns autoSizeAll changes the column sizes to fit the column's content,
     * sizeToFit changes the column sizes to fit the width of the table
     * and null bypasses the altering of the column widths
     */
    columnSize: PropTypes.oneOf(['sizeToFit', 'autoSizeAll', null]),

    /**
     * Use this with Dash Enterprise only.  Sets the ag-grid theme.  Use ddk for dark themes.
     */
    theme: PropTypes.oneOf(['alpine', 'balham', 'material', 'bootstrap']),

    /**
     * Object used to perform the cell styling. See AG-Grid Cell Style.
     */
    cellStyle: PropTypes.shape({
        styleConditions: PropTypes.arrayOf(
            PropTypes.shape({
                condition: PropTypes.string.isRequired,
                style: PropTypes.object.isRequired,
            })
        ),
        defaultStyle: PropTypes.object,
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
        sortModel: PropTypes.any,

        /**
         * If filtering, what the filter model is
         */
        filterModel: PropTypes.any,

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
    getDetailResponse: PropTypes.any,

    /**
     * Special prop used by renderers.
     */
    clickData: PropTypes.any,

    /**
     * Special prop used by renderers.
     */
    hoverData: PropTypes.any,

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
    virtualRowData: PropTypes.any,

    /********************************
     * GRID PROPS
     *******************************/

    /**
     * Array of Column Definitions.
     */
    columnDefs: PropTypes.any,


    /**
     * A default column definition.
     */
    defaultColDef: PropTypes.any,

    /**
     * A default column group definition. All column group definitions will use these
     * properties. Items defined in the actual column group  definition get precedence.
     */
    defaultColGroupDef: PropTypes.any,

    /**
     * An object map of custom column types which contain groups of properties that column
     * definitions can inherit.
     */
    columnTypes: PropTypes.any,

    /**
     * Set to 'shift' to have shift-resize as the default resize operation (same as user
     * holding down Shift while resizing).
     */
    colResizeDefault: PropTypes.any,

    /**
     * Suppresses auto-sizing columns for columns. In other words, double clicking a
     * column's header's edge will not auto-size.
     * Default Value: false
     */
    suppressAutoSize: PropTypes.bool,

    /**
     * Number of pixels to add to a column width after the auto-sizing calculation. Set
     * this if you want to add extra room to accommodate (for example) sort icons, or
     * some other dynamic nature of the header.
     * Default Value: 4
     */
    autoSizePadding: PropTypes.number,

    /**
     * Set this to true to skip the headerName when autoSize is called by default. See
     * Resizing Example.
     * Default Value: false
     */
    skipHeaderOnAutoSize: PropTypes.bool,

    /**
     * If true, the ag-column-moving class is not added to the grid while columns are
     * moving. In the default themes, this results in no animation when moving columns.
     * Default Value: false
     */
    suppressColumnMoveAnimation: PropTypes.bool,

    /**
     * Set to true to suppress column moving, i.e. to make the columns fixed position.
     * Default Value: false
     */
    suppressMovableColumns: PropTypes.bool,

    /**
     * If true, then dots in field names (e.g. address.firstline) are not treated as
     * deep references. Allows you to use dots in your field name if you prefer.
     * Default Value: false
     */
    suppressFieldDotNotation: PropTypes.bool,

    /**
     * Set to true to show the 'no sort' icon. See Example Custom Sorting.
     * Default Value: false
     */
    unSortIcon: PropTypes.bool,

    /**
     * Set to true to suppress multi-sort when the user shift-clicks a column header.
     * Default Value: false
     */
    suppressMultiSort: PropTypes.bool,

    /**
     * Set to true to always show the column menu button, rather than only showing when
     * the mouse is over the column header.
     * Default Value: false
     */
    suppressMenuHide: PropTypes.bool,

    /**
     * Allows specifying the group 'auto column' if you are not happy with the default.
     * If grouping, this column def is included as the first column definition in the
     * grid. If not grouping, this column is not included.
     */
    autoGroupColumnDef: PropTypes.any,

    /**
     * Allow reordering and pinning columns by dragging columns from the columns tool
     * panel to the grid.
     * Default Value: false
     */
    allowDragFromColumnsToolPanel: PropTypes.bool,

    /**
     * Sorts the grid columns in the order of Column Definitions after Column Definitions
     * are updated. See Apply Column Order.
     * Default Value: false
     */
    applyColumnDefOrder: PropTypes.bool,

    /**
     * Rows are filtered using this text as a quick filter.
     */
    quickFilterText: PropTypes.any,

    /**
     * Set to true to turn on the  quick filter cache, used for a performance gain when
     * using the quick filter.
     * Default Value: false
     */
    cacheQuickFilter: PropTypes.bool,

    /**
     * Array defining the order in which sorting occurs (if sorting is enabled). Values
     * can be 'asc', 'desc' or null. For example: sortingOrder: ['asc', 'desc']. See
     * Example Sorting Order and Animation.
     */
    sortingOrder: PropTypes.any,

    /**
     * Set to true to specify that the sort should take into account accented characters.
     * If this feature is turned on the sort will perform slower. See Accented Sort.
     * Default Value: false
     */
    accentedSort: PropTypes.bool,

    /**
     * Set to 'ctrl' to have multi sorting work using the Ctrl or Command (for Apple)
     * keys. See Multi Column Sorting.
     */
    multiSortKey: PropTypes.any,

    /**
     * Set to true to suppress sorting of un-sorted data to match original row data.
     * See Big Data Small Transactions.
     * Default Value: false
     */
    suppressMaintainUnsortedOrder: PropTypes.bool,

    /**
     * Set to true to override the default tree data filtering behaviour to instead exclude
     * child nodes from filter results. See Tree Data Filtering.
     * Default Value: false
     */
    excludeChildrenWhenTreeDataFiltering: PropTypes.bool,

    /**
     * Type of Row Selection.
     */
    rowSelection: PropTypes.any,

    /**
     * Set to true to allow multiple rows to be selected using single click. See Multi
     * Select Single Click.
     * Default Value: false
     */
    rowMultiSelectWithClick: PropTypes.bool,

    /**
     * If true then rows will not be deselected if you hold down Ctrl and click the row
     * or press Space.
     * Default Value: false
     */
    suppressRowDeselection: PropTypes.bool,

    /**
     * If true, row selection won't happen when rows are clicked. Use when you want checkbox
     * selection exclusively.
     * Default Value: false
     */
    suppressRowClickSelection: PropTypes.bool,

    /**
     * If true, cells won't be selectable. This means cells will not get keyboard focus
     * when you click on them.
     * Default Value: false
     */
    suppressCellSelection: PropTypes.bool,

    /**
     * Set to true to enable Range Selection.
     * Default Value: false
     */
    enableRangeSelection: PropTypes.bool,

    /**
     * Set to true to enable Range Handle
     * Default Value: false
     */
    enableRangeHandle: PropTypes.bool,

    /**
     * Set to true to enable Fill Handle
     * Default Value: false
     */
    enableFillHandle: PropTypes.bool,

    /**
     * Set to 'x' to force the fill handle direction to horizontal, or set it to 'y'
     * to force the fill handle direction to vertical
     * Default Value: xy
     */
    fillHandleDirection: PropTypes.string,

    /**
     * Set it to true to prevent cell values from being cleared when the Range Selection
     * is reduced by the Fill Handle.
     * Default Value: false
     */
    suppressClearOnFillReduction: PropTypes.bool,

    /**
     * Set to true to enable Managed Row Dragging.
     * Default Value: false
     */
    rowDragManaged: PropTypes.bool,

    /**
     * Set to true to suppress Row Dragging.
     * Default Value: false
     */
    suppressRowDrag: PropTypes.bool,

    /**
     * Set to true to suppress moving rows while dragging the rowDrag waffle. This option
     * highlights the position where the row will be placed and it will only move the
     * row on mouse up. See Row Dragging.
     * Default Value: false
     */
    suppressMoveWhenRowDragging: PropTypes.bool,

    /**
     * Set to true to enable Single Click Editing for cells, to start editing with a
     * single click.
     * Default Value: false
     */
    singleClickEdit: PropTypes.bool,

    /**
     * Set to true so that neither single nor double click starts editing. See Single
     * Click, Double Click, No Click Editing.
     * Default Value: false
     */
    suppressClickEdit: PropTypes.bool,

    /**
     * Set to 'fullRow' to enable Full Row Editing. Otherwise leave blank to edit one
     * cell at a time.
     */
    editType: PropTypes.any,

    /**
     * Set to true to have cells flash after data changes. See Flashing Data Changes.
     * Default Value: false
     */
    enableCellChangeFlash: PropTypes.bool,

    /**
     * To be used in combination with enableCellChangeFlash, this configuration will
     * set delay in ms of how long a cell should remain in its "flashed
     * Default Value: 500
     */
    cellFlashDelay: PropTypes.number,

    /**
     * To be used in combination with enableCellChangeFlash, this configuration will
     * set delay in ms of how long the "flashed
     * Default Value: 1000
     */
    cellFadeDelay: PropTypes.number,

    /**
     * Set to true to have cells flash after data changes even when the change is due
     * to filtering. See Flashing Data Changes.
     * Default Value: false
     */
    allowShowChangeAfterFilter: PropTypes.bool,

    /**
     * Set this to true to  stop cell editing when grid loses focus. The default is the
     * grid stays editing until focus goes onto another cell. For inline (non-popup)
     * editors only.
     * Default Value: false
     */
    stopEditingWhenGridLosesFocus: PropTypes.bool,

    /**
     * Set both properties to true to have Excel-style behaviour for the Enter key, i.e.
     * enter key moves down.
     * Default Value: false
     */
    enterMovesDown: PropTypes.bool,

    /**
     * The height in pixels for the row containing the column label header. See Header
     * Height.
     * Default Value: 25
     */
    headerHeight: PropTypes.number,

    /**
     * The height for the rows containing header column groups. If not specified, it
     * uses headerHeight. See Header Height.
     */
    groupHeaderHeight: PropTypes.any,

    /**
     * The height for the row containing the floating filters. See Header Height.
     * Default Value: 20
     */
    floatingFiltersHeight: PropTypes.number,

    /**
     * The height for the row containing the columns when in pivot mode. If not specified,
     * it uses headerHeight. See Header Height.
     */
    pivotHeaderHeight: PropTypes.any,

    /**
     * The height for the row containing header column groups when in pivot mode. If
     * not specified, it uses groupHeaderHeight. See Header Height.
     */
    pivotGroupHeaderHeight: PropTypes.any,

    /**
     * Used when grouping. If true, a group row will span all columns across the entire
     * width of the table. If false, the cells will be rendered as normal and you will
     * have the opportunity to include a grouping column (normally the first on the left)
     * to show the group. See Full Width Group Rows.
     * Default Value: false
     */
    groupUseEntireRow: PropTypes.bool,

    /**
     * If grouping, set to the number of levels to expand by default, e.g. 0 for none,
     * 1 for first level only, etc. Set to -1 to expand everything. See Removing Single
     * Children.
     * Default Value: 0
     */
    groupDefaultExpanded: PropTypes.number,

    /**
     * If true, the grid will not swap in the grouping column when grouping is enabled.
     * Use this if you want complete control on the column displayed and don't want the
     * grid's help, in other words if you already have a column in your column definitions
     * that is responsible for displaying the groups. See Configuring the Auto Group
     * Column.
     * Default Value: false
     */
    groupSuppressAutoColumn: PropTypes.bool,

    /**
     * If using auto column, set to true to have each group in its own separate column,
     * e.g. if grouping by Country then Year, two auto columns will be created, one for
     * Country and one for Year. See Multi Auto Column Group.
     * Default Value: false
     */
    groupMultiAutoColumn: PropTypes.bool,

    /**
     * When true, if you select a group, the children of the group will also be selected.
     * See Group Selection.
     * Default Value: false
     */
    groupSelectsChildren: PropTypes.bool,

    /**
     * If grouping, whether to show a group footer when the group is expanded. If true,
     * then by default,  the footer will contain aggregate data (if any) when shown and
     * the header will be blank. When closed, the header will contain  the aggregate
     * data regardless of this setting (as the footer is hidden anyway). This is handy
     * for 'total' rows, that are  displayed below the data when the group is open, and
     * alongside the group when it is closed See Grouping Footers.
     * Default Value: false
     */
    groupIncludeFooter: PropTypes.bool,

    /**
     * Set to true to show a 'grand' total group footer across all groups. See Grouping
     * Footers.
     * Default Value: false
     */
    groupIncludeTotalFooter: PropTypes.bool,

    /**
     * If true, and showing footer, aggregate data will be displayed at both the header
     * and footer levels always. This  stops the possibly undesirable behaviour of the
     * header details 'jumping' to the footer on expand.
     * Default Value: false
     */
    groupSuppressBlankHeader: PropTypes.bool,

    /**
     * If using groupSelectsChildren, then only the children that pass the current filter
     * will get selected. See Group Selection.
     * Default Value: false
     */
    groupSelectsFiltered: PropTypes.bool,

    /**
     * Shows the open group in the group column for non-group rows. See Showing Open
     * Groups.
     * Default Value: false
     */
    showOpenedGroup: PropTypes.bool,

    /**
     * Set to true to collapse groups that only have one child. See Remove Single Children.
     * Default Value: false
     */
    groupRemoveSingleChildren: PropTypes.bool,

    /**
     * Set to true to collapse lowest level groups that only have one child. See Remove
     * Single Children.
     * Default Value: false
     */
    groupRemoveLowestSingleChildren: PropTypes.bool,

    /**
     * Set to true to hide parents that are open. When used with multiple columns for
     * showing groups, it can give a more pleasing user experience. See Group Hide Open
     * Parents.
     * Default Value: false
     */
    groupHideOpenParents: PropTypes.bool,

    /**
     * When to show the 'row group panel' (where you drag rows to group) at the top.
     * See Column Tool Panel Example.
     * Default Value: ['never', 'always', 'onlyWhenGrouping']
     */
    rowGroupPanelShow: PropTypes.oneOf(['never', 'always', 'onlyWhenGrouping']),

    /**
     * Set to true to enable pivot mode. See Pivoting.
     * Default Value: false
     */
    pivotMode: PropTypes.bool,

    /**
     * When to show the 'pivot panel' (where you drag rows to pivot) at the top. Note
     * that the pivot panel will never show if pivotMode is off.
     * Default Value: ['never', 'always', 'onlyWhenPivoting']
     */
    pivotPanelShow: PropTypes.oneOf(['never', 'always', 'onlyWhenPivoting']),

    /**
     * When true, column headers won't include the aggFunc, e.g. 'sum(Bank Balance)'
     * will just be 'Bank Balance'.
     * Default Value: false
     */
    suppressAggFuncInHeader: PropTypes.bool,

    /**
     * When true, the aggregations won't be computed for root node of the grid. See Big
     * Data Small Transactions.
     * Default Value: false
     */
    suppressAggAtRootLevel: PropTypes.bool,

    /**
     * When using change detection, only the updated column with get re-aggregated.
     * Default Value: false
     */
    aggregateOnlyChangedColumns: PropTypes.bool,

    /**
     * If true, then row group, pivot and value aggregation will be read-only from the
     * GUI. The grid will display what values are used for each, but will not allow the
     * user to change the selection. See Read Only Functions.
     * Default Value: false
     */
    functionsReadOnly: PropTypes.bool,

    /**
     * A map of 'function name' to 'function' for custom aggregation functions. See Custom
     * Aggregation Functions.
     */
    aggFuncs: PropTypes.any,

    /**
     * Set to true so that aggregations are not impacted by filtering. See Custom Aggregation
     * Functions.
     */
    suppressAggFilteredOnly: PropTypes.any,

    /**
     * By default, when a column is un-grouped it is made visible. e.g. on main demo:
     * 1) group by country by dragging (action of moving column out of grid means column
     * is made visible=false); then 2) un-group by clicking 'x' on the country column
     * in the column drop zone; the column is then made visible=true. This property stops
     * the column becoming visible again when un-grouping.
     * Default Value: false
     */
    suppressMakeVisibleAfterUnGroup: PropTypes.bool,

    /**
     * When set and the grid is in pivot mode, automatically calculated totals will appear
     * within the Pivot Column Groups,in the position specified. See Pivot Column Group
     * Totals.
     */
    pivotColumnGroupTotals: PropTypes.any,

    /**
     * When set and the grid is in pivot mode, automatically calculated totals will appear
     * for each value column in the position specified. See Pivot Row Totals.
     */
    pivotRowTotals: PropTypes.any,

    /**
     * When enabled pivot column groups will appear 'fixed', without the ability to expand
     * and collapse the column groups. See Fixed Pivot Column Groups.
     * Default Value: false
     */
    suppressExpandablePivotGroups: PropTypes.bool,

    /**
     * If true, the grid will not swap in the grouping column when pivoting. Useful if
     * pivoting using Server Side Row Model or Viewport Row Model and you want full control
     * of all columns including the group column.
     * Default Value: false
     */
    pivotSuppressAutoColumn: PropTypes.bool,

    /**
     * Sets the Row Model type.
     * Default Value: ['clientSide', 'infinite', 'viewport', 'serverSide']
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
    rowData: PropTypes.any,

    /**
     * (Client-Side Row Model only) Enables Immutable Data mode, for compatibility with
     * immutable stores.
     */
    immutableData: PropTypes.any,

    /**
     * ( only) Prevents Transactions changing sort, filter, group or pivot state when
     * transaction only contains updates.
     */
    suppressModelUpdateAfterUpdateTransaction: PropTypes.any,

    /**
     * Data to be displayed as Pinned Top Rows in the grid.
     */
    pinnedTopRowData: PropTypes.any,

    /**
     * Data to be displayed as Pinned Bottom Rows in the grid.
     */
    pinnedBottomRowData: PropTypes.any,

    /**
     * Whether to use Full Store or Partial Store for storing rows. See Row Stores
     * Default Value: ['full', 'partial']
     */
    serverSideStoreType: PropTypes.oneOf(['full', 'partial']),

    /**
     * Partial Store Only - How many rows for each block in the store, i.e. how many
     * rows returned from the server at a time.
     * Default Value: 100
     */
    cacheBlockSize: PropTypes.number,

    /**
     * Quantity of extra blank rows to display to the user at the end of the dataset,
     * which sets the vertical scroll and then allows the grid to request viewing more rows of data.
     * default is 1, ie show 1 row.
     */
    cacheOverflowSize: PropTypes.number,

    /**
     * Partial Store Only - how many blocks to keep in the store. Default is no limit,
     * so every requested block is kept. Use this if you have memory concerns, and blocks
     * that were least recently viewed will be purged when the limit is hit. The grid
     * will additionally make sure it has all the blocks needed to display what is currently
     * visible - in case this property is set to low.
     */
    maxBlocksInCache: PropTypes.any,

    /**
     * How many requests to hit the server with concurrently. If the max is reached,
     * requests are queued.
     * Default Value: 1
     */
    maxConcurrentDatasourceRequests: PropTypes.number,

    /**
     * How many milliseconds to wait before loading a block. Useful when scrolling over
     * many rows, spanning many Partial Store blocks, as it prevents blocks loading until
     * scrolling has settled.
     */
    blockLoadDebounceMillis: PropTypes.any,

    /**
     * When enabled, closing group rows will remove children of that row. Next time the
     * row is opened, child rows will be read form the datasoruce again. This property
     * only applies when there is Row Grouping.
     */
    purgeClosedRowNodes: PropTypes.any,

    /**
     * When enabled, always refreshes stores after filter has changed. Use by Full Store
     * only, to allow Server-Side Filtering.
     */
    serverSideFilteringAlwaysResets: PropTypes.any,

    /**
     * When using viewport row model, sets the pages size for the viewport.
     */
    viewportRowModelPageSize: PropTypes.any,

    /**
     * When using viewport row model, sets the buffer size for the viewport.
     */
    viewportRowModelBufferSize: PropTypes.any,

    /**
     * To use the viewport row model you provide the grid with a viewportDatasource.
     * See Viewport.
     */
    viewportDatasource: PropTypes.any,

    /**
     * Set to true to always show the horizontal scrollbar.
     * Default Value: false
     */
    alwaysShowHorizontalScroll: PropTypes.bool,

    /**
     * Set to true to always show the vertical scrollbar.
     * Default Value: false
     */
    alwaysShowVerticalScroll: PropTypes.bool,

    /**
     * Set to true to debounce the vertical scrollbar. Can provide smoother scrolling
     * on older browsers, eg IE.
     * Default Value: false
     */
    debounceVerticalScrollbar: PropTypes.bool,

    /**
     * Set to true to never show the horizontal scroll. This is useful if the grid is
     * aligned with another grid and will scroll when the other grid scrolls. (Show not
     * be used in combination with alwaysShowHorizontalScroll) See Aligned Grid as Footer.
     * Default Value: false
     */
    suppressHorizontalScroll: PropTypes.bool,

    /**
     * Set to true so that the grid doesn't virtualise the columns. For example, if you
     * have 100 columns, but only 10 visible due to scrolling, all 100 will always be
     * rendered.
     * Default Value: false
     */
    suppressColumnVirtualisation: PropTypes.bool,

    /**
     * There is no such property as suppressRowVirtualisation - if you want to do this,
     * then set the rowBuffer property to be very large, e.g. 9999. Warning: lots of
     * rendered rows will mean a very large amount of rendering in the DOM which will
     * slow things down.
     */
    suppressRowVirtualisation: PropTypes.any,

    /**
     * By default the grid has a limit of rendering a maximum of 500 rows at once (remember
     * the grid only renders rows you can see, so unless your display shows more than
     * 500 rows without vertically scrolling this will never be an issue).
     * Default Value: false
     */
    suppressMaxRenderedRowRestriction: PropTypes.bool,

    /**
     * When true, the grid will not scroll to the top when new row data is provided.
     * Use this if you don't want the default behaviour of scrolling to the top every
     * time you load new data.
     * Default Value: false
     */
    suppressScrollOnNewData: PropTypes.bool,

    /**
     * When true, the grid will not use animation frames when drawing rows while scrolling.
     * Use this if the grid is working fast enough that you don't need animation frames
     * and you don't want the grid to flicker.
     * Default Value: false
     */
    suppressAnimationFrame: PropTypes.bool,

    /**
     * Set whether Pagination is enabled.
     * Default Value: false
     */
    pagination: PropTypes.bool,

    /**
     * How many rows to load per page. If paginationAutoPageSize is specified, this property
     * is ignored. See Customising Pagination.
     * Default Value: 100
     */
    paginationPageSize: PropTypes.number,

    /**
     * Set to true so that the number of rows to load per page is automatically adjusted
     * by AG Grid so each page shows enough rows to just fill the area designated for
     * the grid. If false, paginationPageSize is used. See Auto Page Size.
     * Default Value: false
     */
    paginationAutoPageSize: PropTypes.bool,

    /**
     * If true, the default AG Grid controls for navigation are hidden. This is useful
     * if pagination=true and you want to provide your own pagination controls. Otherwise,
     * when pagination=true the grid automatically shows the necessary controls at the
     * bottom so that the user can navigate through the different pages. See Custom Pagination
     * Controls.
     * Default Value: false
     */
    suppressPaginationPanel: PropTypes.bool,

    /**
     * Set to true to have pages split children of groups when using Row Grouping or
     * detail rows with Master Detail. See Pagination & Child Rows.
     */
    paginateChildRows: PropTypes.any,

    /**
     * Sets the Cell Renderer to use when groupUseEntireRow=true. See Row Grouping.
     */
    groupRowRenderer: PropTypes.any,

    /**
     * Sets the inner Cell Renderer to use when groupUseEntireRow=true. See Row Grouping.
     */
    groupRowInnerRenderer: PropTypes.any,

    /**
     * Sets the Cell Renderer to use for Full Width Rows.
     */
    fullWidthCellRenderer: PropTypes.any,

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
     * Set to true to keep detail rows for when they are displayed again.
     * Default Value: false
     */
    keepDetailRows: PropTypes.bool,

    /**
     * Sets the number of details rows to keep.
     * Default Value: 10
     */
    keepDetailRowsCount: PropTypes.number,

    /**
     * Set fixed height in pixels for each detail row.
     */
    detailRowHeight: PropTypes.number,

    /**
     * Set detail row height automatically based on contents.
     */
    detailRowAutoHeight: PropTypes.bool,

    /**
     * Icons to use inside the grid instead of the grid's default icons.
     */
    icons: PropTypes.any,

    /**
     * Default Row Height in pixels.
     * Default Value: 25
     */
    rowHeight: PropTypes.number,

    /**
     * Set to true to enable Row Animation.
     * Default Value: false
     */
    animateRows: PropTypes.bool,

    /**
     * The style to give a particular row. See Row Style.
     */
    rowStyle: PropTypes.any,

    /**
     * The class to give a particular row. See Row Class.
     */
    rowClass: PropTypes.any,

    /**
     * Rules which can be applied to include certain CSS classes. See Row Class Rules.
     */
    rowClassRules: PropTypes.any,

    /**
     * The list of Excel styles to be used when exporting to Excel
     */
    excelStyles: PropTypes.any,

    /**
     * Tell the grid how wide the scrollbar is, which is used in grid width calculations.
     * Set only if using non-standard browser-provided scrollbars, so the grid can use
     * the non-standard size in its calculations.
     */
    scrollbarWidth: PropTypes.any,

    /**
     * Set to true to not highlight rows by adding the ag-row-hover CSS class.
     * Default Value: false
     */
    suppressRowHoverHighlight: PropTypes.bool,

    /**
     * Set to true to only have the range selection, and not row selection, copied to
     * clipboard.
     * Default Value: false
     */
    suppressCopyRowsToClipboard: PropTypes.bool,

    /**
     * Set to true to also include headers when copying to clipboard using Ctrl + C clipboard.
     * Default Value: false
     */
    copyHeadersToClipboard: PropTypes.bool,

    /**
     * Specify the deliminator to use when copying to clipboard.
     */
    clipboardDeliminator: PropTypes.any,

    /**
     * Set to true to not set focus back on the grid after a refresh. This can avoid
     * issues where you want to keep the focus on another part of the browser.
     * Default Value: false
     */
    suppressFocusAfterRefresh: PropTypes.bool,

    /**
     * Set to true to work around a bug with Excel (Windows) that adds an extra empty
     * line at the end of ranges copied to the clipboard.
     * Default Value: false
     */
    suppressLastEmptyLineOnPaste: PropTypes.bool,

    /**
     * Set to true to be able to select the text within cells.
     * Default Value: false
     */
    enableCellTextSelection: PropTypes.bool,

    /**
     * A map of key->value pairs for localising text within the grid. See Localisation.
     */
    localeText: PropTypes.any,

    /**
     * Disables the 'loading' overlay.
     * Default Value: false
     */
    suppressLoadingOverlay: PropTypes.bool,

    /**
     * Disables the 'no rows' overlay.
     * Default Value: false
     */
    suppressNoRowsOverlay: PropTypes.bool,

    /**
     * Provide a template for 'loading' overlay.
     */
    overlayLoadingTemplate: PropTypes.any,

    /**
     * Provide a template for 'no rows' overlay.
     */
    overlayNoRowsTemplate: PropTypes.any,

    /**
     * Provide a custom loading overlay component.
     */
    loadingOverlayComponent: PropTypes.any,

    /**
     * Customise the parameters provided to the loading overlay component.
     */
    loadingOverlayComponentParams: PropTypes.any,

    /**
     * Provide a custom no rows overlay component.
     */
    noRowsOverlayComponent: PropTypes.any,

    /**
     * Customise the parameters provided to the no rows overlay component.
     */
    noRowsOverlayComponentParams: PropTypes.any,

    /**
     * Set to true to Enable Charts.
     * Default Value: false
     */
    enableCharts: PropTypes.bool,

    /**
     * The list of chart themes to be used, see Chart Themes.
     * Default Value: ['ag-default', 'ag-material', 'ag-pastel', 'ag-vivid', 'ag-solar']
     */
    chartThemes: PropTypes.oneOf([
        'ag-default',
        'ag-material',
        'ag-pastel',
        'ag-vivid',
        'ag-solar',
    ]),

    /**
     * A map containing custom chart themes, see Custom Chart Themes.
     */
    customChartThemes: PropTypes.any,

    /**
     * Chart theme overrides applied to all themes, see Overriding Existing Themes.
     */
    chartThemeOverrides: PropTypes.any,

    /**
     * A map of component names to plain JavaScript components.
     */
    components: PropTypes.any,

    /**
     * A map of component names to framework (React, Angular etc) components.
     */
    frameworkComponents: PropTypes.any,

    /**
     * DOM element to use as popup parent for grid popups (context menu, column menu
     * etc).
     */
    popupParent: PropTypes.any,

    /**
     * Set to true to turn on the value cache.
     * Default Value: false
     */
    valueCache: PropTypes.bool,

    /**
     * Set to true to set value cache to not expire after data updates.
     * Default Value: false
     */
    valueCacheNeverExpires: PropTypes.bool,

    /**
     * A default configuration object used to export to CSV or Excel.
     */
    defaultExportParams: PropTypes.any,

    /**
     * If true, then middle clicks will result in click events for cell and row. Otherwise
     * the browser will use middle click to scroll the grid.
     * Default Value: false
     */
    suppressMiddleClickScrolls: PropTypes.bool,

    /**
     * If true, mouse wheel events will be passed to the browser. Useful if your grid
     * has no vertical scrolls and you want the mouse to scroll the browser page.
     * Default Value: false
     */
    suppressPreventDefaultOnMouseWheel: PropTypes.bool,

    /**
     * Set to true to use the browser's default tooltip instead of using AG Grid's Tooltip
     * Component.
     * Default Value: false
     */
    enableBrowserTooltips: PropTypes.bool,

    /**
     * The delay in milliseconds that it takes for tooltips to show up once an element
     * is hovered.
     * Default Value: 2000
     */
    tooltipShowDelay: PropTypes.number,

    /**
     * Set to true to have tooltips follow the cursor once they are displayed.
     * Default Value: false
     */
    tooltipMouseTrack: PropTypes.bool,

    /**
     * Set to true to allow cell expressions.
     * Default Value: false
     */
    enableCellExpressions: PropTypes.bool,

    /**
     * Switch between layout options. See Printing and Auto Height.
     * Default Value: ['normal', 'autoHeight', 'print']
     */
    domLayout: PropTypes.oneOf(['normal', 'autoHeight', 'print']),

    /**
     * When true, the order of rows and columns in the DOM are consistent with what is
     * on screen. See Accessibility - Row and Column Order.
     * Default Value: false
     */
    ensureDomOrder: PropTypes.bool,

    /**
     * The number of rows rendered outside the scrollable viewable area the grid renders.
     * Having a buffer means the grid will have rows ready to show as the user slowly
     * scrolls vertically.
     * Default Value: 20
     */
    rowBuffer: PropTypes.number,

    /**
     * A list of grids to treat as Aligned Grids. If grids are aligned then the columns
     * and horizontal scrolling will be kept in sync.
     */
    alignedGrids: PropTypes.any,

    /**
     * If true, rowNodes don't get their parents set. The grid doesn't use the parent
     * reference, but it is included to help the client code navigate the node tree if
     * it wants by providing bi-direction navigation up and down the tree. If this is
     * a problem (e.g. if you need to convert the tree to JSON, which does not allow
     * cyclic dependencies) then set this to true.
     * Default Value: false
     */
    suppressParentsInRowNodes: PropTypes.bool,

    /**
     * If true, when you drag a column out of the grid (e.g. to the group zone) the column
     * is not hidden.
     * Default Value: false
     */
    suppressDragLeaveHidesColumns: PropTypes.bool,

    /**
     * The interval in milliseconds that the grid uses to periodically check its size
     * and lay itself out again if the size has changed, such as when your browser changes
     * size, or your application changes the size of the div element that the grid lives
     * inside. To stop the periodic layout, set it to -1.
     * Default Value: 500
     */
    layoutInterval: PropTypes.number,

    /**
     * Set to true to operate grid in RTL (Right to Left) mode.
     * Default Value: false
     */
    enableRtl: PropTypes.bool,

    /**
     * Set this to true to enable debug information from AG Grid and related components.
     * Will result in additional logging being output, but very useful when investigating
     * problems.
     * Default Value: false
     */
    debug: PropTypes.bool,

    /**
     * Provides a context object that is provided to different callbacks the grid uses.
     * Used for passing additional information to the callbacks by your application.
     */
    context: PropTypes.any,

    /**
     * Set to true to not show context menu. Use if you don't want to use the default
     * 'right click' context menu.
     * Default Value: false
     */
    suppressContextMenu: PropTypes.bool,

    /**
     * When using suppressContextMenu, you can use the onCellContextMenu function to
     * provide your own code to handle cell contextmenu events. This flag is useful to
     * prevent the browser from showing its default context menu.
     * Default Value: false
     */
    preventDefaultOnContextMenu: PropTypes.bool,

    /**
     * Allows context menu to show, even when Ctrl key is held down.
     */
    allowContextMenuWithControlKey: PropTypes.any,

    /**
     * Specifies the status bar components to use in the status bar.
     */
    statusBar: PropTypes.any,

    /**
     * Disables touch support (but does not remove the browser's efforts to simulate
     * mouse events on touch).
     * Default Value: false
     */
    suppressTouch: PropTypes.bool,

    /**
     * Disables the async nature of the events introduced in v10, and makes them synchronous.
     * This property is only introduced for the purpose of supporting legacy code which
     * has a dependency to sync events in earlier versions (v9 or earlier) of AG Grid.
     * It is strongly recommended that you don't change this property unless you have
     * legacy issues.
     * Default Value: false
     */
    suppressAsyncEvents: PropTypes.bool,

    /**
     * Prevents the user from exporting the grid to CSV.
     * Default Value: false
     */
    suppressCsvExport: PropTypes.bool,

    /**
     * Prevents the user from exporting the grid to Excel.
     * Default Value: false
     */
    suppressExcelExport: PropTypes.bool,

    /**
     * How many milliseconds to wait before executing a batch of async transactions.
     */
    asyncTransactionWaitMillis: PropTypes.any,

    /**
     * Disables showing a warning message in the console if using a gridOptions or colDef
     * property that doesn't exist.
     * Default Value: false
     */
    suppressPropertyNamesCheck: PropTypes.bool,

    /**
     * Uses CSS top instead of CSS transform for positioning rows. Useful if the transform
     * function is causing issues such as used in row spanning.
     * Default Value: false
     */
    suppressRowTransform: PropTypes.bool,

    /**
     * When true, a full reset will be performed when sorting using the Server-Side Row
     * Model.
     * Default Value: false
     */
    serverSideSortingAlwaysResets: PropTypes.bool,

    /**
     * The grid will check for ResizeObserver and use it if it exists in the browser,
     * otherwise it will use the grid's alternative implementation. Some users reported
     * issues with Chrome's ResizeObserver. Use this property to always use the grid's
     * alternative implementation should such problems exist.
     * Default Value: false
     */
    suppressBrowserResizeObserver: PropTypes.bool,

    /********************************
     * EVENT PROPS
     *******************************/

    /**
     * Cell is clicked.
     */
    cellClicked: PropTypes.any,

    /**
     * Cell is double clicked.
     */
    cellDoubleClicked: PropTypes.any,

    /**
     * Cell is focused.
     */
    cellFocused: PropTypes.any,

    /**
     * Mouse entered cell.
     */
    cellMouseOver: PropTypes.any,

    /**
     * Mouse left cell.
     */
    cellMouseOut: PropTypes.any,

    /**
     * Mouse down on cell.
     */
    cellMouseDown: PropTypes.any,

    /**
     * Row is clicked.
     */
    rowClicked: PropTypes.any,

    /**
     * Row is double clicked.
     */
    rowDoubleClicked: PropTypes.any,

    /**
     * The actively selected rows from the grid (may include filtered rows)
     */
    selectedRows: PropTypes.arrayOf(PropTypes.object),

    /**
     * Cell is right clicked.
     */
    cellContextMenu: PropTypes.any,

    /**
     * A change to range selection has occurred.
     */
    rangeSelectionChanged: PropTypes.any,

    /**
     * Value has changed after editing.
     */
    cellValueChanged: PropTypes.any,

    /**
     * A cell's value within a row has changed. This event corresponds to Full Row Editing
     * only.
     */
    rowValueChanged: PropTypes.any,

    /**
     * Editing a cell has started.
     */
    cellEditingStarted: PropTypes.any,

    /**
     * Editing a cell has stopped.
     */
    cellEditingStopped: PropTypes.any,

    /**
     * Editing a row has started (when row editing is enabled). When row editing, this
     * event will be fired once and cellEditingStarted will be fired for each individual
     * cell. This event corresponds to Full Row Editing only.
     */
    rowEditingStarted: PropTypes.any,

    /**
     * Editing a row has stopped (when row editing is enabled). When row editing, this
     * event will be fired once and cellEditingStopped will be fired for each individual
     * cell. This event corresponds to Full Row Editing only.
     */
    rowEditingStopped: PropTypes.any,

    /**
     * Paste operation has started. See Clipboard Events.
     */
    pasteStart: PropTypes.any,

    /**
     * Paste operation has ended. See Clipboard Events.
     */
    pasteEnd: PropTypes.any,

    /**
     * Sort has changed. The grid also listens for this and updates the model.
     */
    sortChanged: PropTypes.any,

    /**
     * Filter has been modified and applied.
     */
    filterChanged: PropTypes.any,

    /**
     * Filter was modified but not applied. Used when filters have 'Apply' buttons.
     */
    filterModified: PropTypes.any,

    /**
     * A drag has started, or dragging was already started and the mouse has re-entered
     * the grid having previously left the grid.
     */
    rowDragEnter: PropTypes.any,

    /**
     * The mouse has moved while dragging.
     */
    rowDragMove: PropTypes.any,

    /**
     * The mouse has left the grid while dragging.
     */
    rowDragLeave: PropTypes.any,

    /**
     * The drag has finished over the grid.
     */
    rowDragEnd: PropTypes.any,

    /**
     * A column, or group of columns, was hidden / shown.
     */
    columnVisible: PropTypes.any,

    /**
     * A column, or group of columns, was pinned / unpinned.
     */
    columnPinned: PropTypes.any,

    /**
     * A column was resized.
     */
    columnResized: PropTypes.any,

    /**
     * A column was moved. To find out when the column move is finished you can use the
     * dragStopped event below.
     */
    columnMoved: PropTypes.any,

    /**
     * A row group column was added or removed.
     */
    columnRowGroupChanged: PropTypes.any,

    /**
     * A value column was added or removed.
     */
    columnValueChanged: PropTypes.any,

    /**
     * The pivot mode flag was changed.
     */
    columnPivotModeChanged: PropTypes.any,

    /**
     * A pivot column was added, removed or order changed.
     */
    columnPivotChanged: PropTypes.any,

    /**
     * A column group was opened / closed.
     */
    columnGroupOpened: PropTypes.any,

    /**
     * User set new columns.
     */
    newColumnsLoaded: PropTypes.any,

    /**
     * The list of grid columns changed.
     */
    gridColumnsChanged: PropTypes.any,

    /**
     * The list of displayed columns changed. This can result from columns open / close,
     * column move, pivot, group, etc.
     */
    displayedColumnsChanged: PropTypes.any,

    /**
     * The list of rendered columns changed (only columns in the visible scrolled viewport
     * are rendered by default).
     */
    virtualColumnsChanged: PropTypes.any,

    /**
     * Shotgun - gets called when either a) new columns are set or b) columnApi.setState()
     * is used, so everything has changed.
     */
    columnEverythingChanged: PropTypes.any,

    /**
     * The grid has initialised. The name 'ready' was influenced by the author's time
     * programming the Commodore 64. Use this event if, for example, you need to use
     * the grid's API to fix the columns to size.
     */
    gridReady: PropTypes.any,

    /**
     * The size of the grid div has changed. In other words, the grid was resized.
     */
    gridSizeChanged: PropTypes.any,

    /**
     * Displayed rows have changed. Triggered after sort, filter or tree expand / collapse
     * events.
     */
    modelUpdated: PropTypes.any,

    /**
     * Fired the first time data is rendered into the grid.
     */
    firstDataRendered: PropTypes.any,

    /**
     * A row group was opened or closed.
     */
    rowGroupOpened: PropTypes.any,

    /**
     * Fired when calling either of the API methods expandAll() or collapseAll().
     */
    expandOrCollapseAll: PropTypes.any,

    /**
     * Triggered every time the paging state changes. Some of the most common scenarios
     * for this event to be triggered are:The page size changesThe current shown page
     * is changedNew data is loaded onto the grid
     */
    paginationChanged: PropTypes.any,

    /**
     * The client has set new pinned row data into the grid.
     */
    pinnedRowDataChanged: PropTypes.any,

    /**
     * A row was removed from the DOM, for any reason. Use to clean up resources (if
     * any) used by the row.
     */
    virtualRowRemoved: PropTypes.any,

    /**
     * Which rows are rendered in the DOM has changed.
     */
    viewportChanged: PropTypes.any,

    /**
     * The body was scrolled horizontally or vertically.
     */
    bodyScroll: PropTypes.any,

    /**
     * When dragging starts. This could be any action that uses the grid's Drag and Drop
     * service, e.g. Column Moving, Column Resizing, Range Selection, Fill Handle, etc.
     */
    dragStarted: PropTypes.any,

    /**
     * When dragging stops. This could be any action that uses the grid's Drag and Drop
     * service, e.g. Column Moving, Column Resizing, Range Selection, Fill Handle, etc.
     */
    dragStopped: PropTypes.any,

    /**
     * The client has set new data into the grid using api.setRowData() or by changing
     * the rowData bound property.
     */
    rowDataChanged: PropTypes.any,

    /**
     * The client has updated data for the grid using api.applyTransaction(transaction)
     * or by changing the rowData bound property with immutableData=true.
     */
    rowDataUpdated: PropTypes.any,

    /**
     * The tool panel was hidden or shown. Use api.isToolPanelShowing() to get status.
     */
    toolPanelVisibleChanged: PropTypes.any,

    /**
     * Only used by React, Angular and VueJS AG Grid components (not used if doing plain
     * JavaScript or Angular 1.x). If the grid receives changes due to bound properties,
     * this event fires after the grid has finished processing the change.
     */
    componentStateChanged: PropTypes.any,

    /**
     * The grid draws rows and cells using animation frames. This event gets fired when
     * the animation frame queue is empty. Normally used in conjunction with api.isAnimationFrameQueueEmpty()
     * so user can check if animation frame is pending, and if so then can be notified
     * when no animation frames are pending. Useful if your application needs to know
     * when drawing of the grid is no longer pending, e.g. for sending to a printer.
     */
    animationQueueEmpty: PropTypes.any,

    /**
     * Async transactions have been applied. Contains a list of all transaction results.
     */
    AsyncTransactionsFlushed: PropTypes.any,

    /**
     * DOM event keyDown happened on a cell. See Keyboard Events.
     */
    cellKeyDown: PropTypes.any,

    /**
     * DOM event keyPress happened on a cell. See Keyboard Events.
     */
    cellKeyPress: PropTypes.any,

    /**
     * SideBar configures the properties of the grid sidebar.
     */
    sideBar: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.oneOf(['columns', 'filters']),
        PropTypes.object,
    ]),

    /**
     * Other ag-grid options
     */
    dashGridOptions: PropTypes.object,
};

export const propTypes = DashAgGrid.propTypes;
export const defaultProps = DashAgGrid.defaultProps;
