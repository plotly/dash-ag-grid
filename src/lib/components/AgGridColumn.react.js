import React from 'react';
import PropTypes from 'prop-types';

export default function DashAgGridColumn() {
    return <div />;
}
DashAgGridColumn.propTypes = {
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
    setProps: PropTypes.string,

    /**
     * The children of this component
     */
    children: PropTypes.node,

    /**
     * The CSS style for the component
     */
    style: PropTypes.object,

    /********************************
     * CUSTOM PROPS
     *******************************/

    /**
     * boolean. Set to true to show a checkbox in the header of a column.
     * Default Value: false
     */
    headerCheckboxSelection: PropTypes.bool,

    /**
     * boolean. Set to true for checkbox selections to only affect filtered data.
     * Default Value: false
     */
    headerCheckboxSelectionFilteredOnly: PropTypes.bool,

    /********************************
     * COLDEF PROPS
     *******************************/

    /********************************
     * Columns and Column Groups
     *******************************/

    /**
     * The name to render in the column header. If not specified and field is specified,
     * the field name will be used as the header name.
     */
    headerName: PropTypes.any,

    /**
     * Whether to show the column when the group is open / closed.
     */
    columnGroupShow: PropTypes.any,

    /**
     * Class to use for the header cell. Can be a string, array of strings, or function.
     */
    headerClass: PropTypes.any,

    /**
     * Class to use for the tool panel cell. Can be a string, array of strings, or function.
     */
    toolPanelClass: PropTypes.any,

    /**
     * Set to true if you do not want this column or group to appear in the Columns Tool
     * Panel.
     * Default Value: false
     */
    suppressColumnsToolPanel: PropTypes.bool,

    /**
     * Set to true if you do not want this column (filter) or group (filter group) to
     * appear in the Filters Tool Panel.
     * Default Value: false
     */
    suppressFiltersToolPanel: PropTypes.bool,

    /********************************
     * Columns Only
     *******************************/

    /**
     * The field of the row to get the cells data from.
     */
    field: PropTypes.any,

    /**
     * The unique ID to give the column. This is optional. If missing, the ID will default
     * to the field. If both field and colId are missing, a unique ID will be generated.
     * This ID is used to identify the column in the API for sorting, filtering etc.
     */
    colId: PropTypes.any,

    /**
     * A comma separated string or array of strings containing ColumnType keys which
     * can be used as a template for a column. This helps to reduce duplication of properties
     * when you have a lot of common column properties.
     */
    type: PropTypes.any,

    /**
     * Initial width in pixels for the cell.
     */
    width: PropTypes.any,

    /**
     * Same as 'width', except only applied when creating a new column. Not applied when
     * updating column definitions.
     */
    defaultWidth: PropTypes.any,

    /**
     * Minimum width in pixels for the cell.
     */
    minWidth: PropTypes.any,

    /**
     * Maximum width in pixels for the cell.
     */
    maxWidth: PropTypes.any,

    /**
     * Used instead of width when the goal is to fill the remaining empty space of the
     * grid. See Column Flex.
     */
    flex: PropTypes.any,

    /**
     * Same as 'flex', except only applied when creating a new column. Not applied when
     * updating column definitions.
     */
    initialFlex: PropTypes.any,

    /**
     * Filter component to use for this column. Set to true to use the default filter.
     */
    filter: PropTypes.any,

    /**
     * Custom params to be passed to filter component.
     */
    filterParams: PropTypes.any,

    /**
     * Whether to show a floating filter for this column.
     * Default Value: false
     */
    floatingFilter: PropTypes.bool,

    /**
     * Floating filter component to use for this column.
     */
    floatingFilterComponent: PropTypes.any,

    /**
     * Custom params to be passed to floatingFilterComponent or floatingFilterComponentFramework.
     */
    floatingFilterComponentParams: PropTypes.any,

    /**
     * Set to true for this column to be hidden. You might think it would make more sense
     * to call this field visible and mark it false to hide, but we want all default
     * values to be false and we want columns to be visible by default.
     * Default Value: false
     */
    hide: PropTypes.bool,

    /**
     * Same as 'hide', except only applied when creating a new column. Not applied when
     * updating column definitions.
     */
    initialHide: PropTypes.any,

    /**
     * Pin a column to one side.
     */
    pinned: PropTypes.any,

    /**
     * Same as 'pinned', except only applied when creating a new column. Not applied
     * when updating column definitions.
     */
    initialPinned: PropTypes.any,

    /**
     * Set to true to always have this column displayed first.
     * Default Value: false
     */
    lockPosition: PropTypes.bool,

    /**
     * Set to true to block making column visible / hidden via the UI (API will still
     * work).
     * Default Value: false
     */
    lockVisible: PropTypes.bool,

    /**
     * Set to true to block pinning column via the UI (API will still work).
     * Default Value: false
     */
    lockPinned: PropTypes.bool,

    /**
     * Set to true to allow sorting on this column.
     * Default Value: false
     */
    sortable: PropTypes.bool,

    /**
     * Set to sort this column.
     * Default Value: [null, 'asc', 'desc']
     */
    sort: PropTypes.oneOf([null, 'asc', 'desc']),

    /**
     * Same as 'sort', except only applied when creating a new column. Not applied when
     * updating column definitions.
     */
    initialSort: PropTypes.any,

    /**
     * If doing multi-sort by default, the order which column sorts are applied.
     */
    sortIndex: PropTypes.any,

    /**
     * Same as 'sortIndex', except only applied when creating a new column. Not applied
     * when updating column definitions.
     */
    initialSortIndex: PropTypes.any,

    /**
     * Array defining the order in which sorting occurs (if sorting is enabled).
     * Default Value: [null, 'asc', 'desc']
     */
    sortingOrder: PropTypes.oneOf([null, 'asc', 'desc']),

    /**
     * Set to true to allow column to be resized.
     * Default Value: false
     */
    resizable: PropTypes.bool,

    /**
     * Tooltip for the column header
     */
    headerTooltip: PropTypes.any,

    /**
     * The field of the tooltip to apply to the cell.
     */
    tooltipField: PropTypes.any,

    /**
     * Callback that should return the string used for a tooltip.function (params: IParams):
     * string;
     */
    tooltipValueGetter: PropTypes.any,

    /**
     * boolean or Function. Set to true (or return true from function) to render a selection
     * checkbox in the column.
     * Default Value: false
     */
    checkboxSelection: PropTypes.bool,

    /**
     * boolean or Function. Set to true (or return true from function) to allow row dragging.
     * Default Value: false
     */
    rowDrag: PropTypes.bool,

    /**
     * A callback that should return a string to be displayed by the rowDragComp while
     * dragging a row. If this callback is not set, the current cell value will be used.function
     * (params: IParams): string;
     */
    rowDragText: PropTypes.any,

    /**
     * boolean or Function. Set to true (or return true from function) to allow dragging
     * for native drag and drop.
     * Default Value: false
     */
    dndSource: PropTypes.bool,

    /**
     * Function to allow custom drag functionality for native drag and drop.
     */
    dndSourceOnRowDrag: PropTypes.any,

    /**
     * The style to give a particular cell. See Cell Style.
     */
    cellStyle: PropTypes.any,

    /**
     * The class to give a particular cell. See Cell Class.
     */
    cellClass: PropTypes.any,

    /**
     * Rules which can be applied to include certain CSS classes. See Cell Class Rules.
     */
    cellClassRules: PropTypes.any,

    /**
     * Set to true if this column is editable, otherwise false. Can also be a function
     * to have different rows editable.
     * Default Value: false
     */
    editable: PropTypes.bool,

    /**
     * cellRenderer to use for this column.
     */
    cellRenderer: PropTypes.any,

    /**
     * Params to be passed to cell renderer component.
     */
    cellRendererParams: PropTypes.any,

    /**
     * cellRenderer to use for pinned rows in this column. Pinned cells will use pinnedCellRenderer
     * if available, or cellRenderer if not.
     */
    pinnedRowCellRenderer: PropTypes.any,

    /**
     * Params to be passed to pinned row cell renderer component.
     */
    pinnedRowCellRendererParams: PropTypes.any,

    /**
     * Callback to select which cell renderer / cell editor to be used for a given row
     * within the same column.
     */
    cellRendererSelector: PropTypes.any,

    /**
     * cellEditor to use for this column.
     */
    cellEditor: PropTypes.any,

    /**
     * Params to be passed to cell editor component.
     */
    cellEditorParams: PropTypes.any,

    /**
     * Header component to use for this column.
     */
    headerComponent: PropTypes.any,

    /**
     * Params to be passed to header component.
     */
    headerComponentParams: PropTypes.any,

    /**
     * A function to tell the grid what quick filter text to use for this column if you
     * don't want to use the default (which is calling toString on the value).
     */
    getQuickFilterText: PropTypes.any,

    /**
     * Name of function to use for aggregation. You can also provide your own agg function.
     */
    aggFunc: PropTypes.any,

    /**
     * Same as 'aggFunc', except only applied when creating a new column. Not applied
     * when updating column definitions.
     */
    initialAggFunc: PropTypes.any,

    /**
     * Aggregation functions allowed on this column e.g. ['sum', 'avg']. If missing,
     * all installed functions are allowed. This will only restrict what the GUI allows
     * a user to select, it does not impact when you set a function via the API.
     */
    allowedAggFuncs: PropTypes.any,

    /**
     * Set to true to row group by this column
     */
    rowGroup: PropTypes.any,

    /**
     * Same as 'rowGroup', except only applied when creating a new column. Not applied
     * when updating column definitions.
     */
    initialRowGroup: PropTypes.any,

    /**
     * Set this in columns you want to group by. If only grouping by one column, set
     * this to any number (e.g. 0). If grouping by multiple columns, set this to where
     * you want this column to be in the group (e.g. 0 for first, 1 for second, and so
     * on).
     */
    rowGroupIndex: PropTypes.any,

    /**
     * Same as 'rowGroupIndex', except only applied when creating a new column. Not applied
     * when updating column definitions.
     */
    initialRowGroupIndex: PropTypes.any,

    /**
     * Set to true to pivot by this column
     */
    pivot: PropTypes.any,

    /**
     * Same as 'pivot', except only applied when creating a new column. Not applied when
     * updating column definitions.
     */
    initialPivot: PropTypes.any,

    /**
     * Set this in columns you want to pivot by. If only pivoting by one column, set
     * this to any number (e.g. 0). If pivoting by multiple columns, set this to where
     * you want this column to be in the order of pivots (e.g. 0 for first, 1 for second,
     * and so on).
     */
    pivotIndex: PropTypes.any,

    /**
     * Same as 'pivotIndex', except only applied when creating a new column. Not applied
     * when updating column definitions.
     */
    initialPivotIndex: PropTypes.any,

    /**
     * Set to true if you want the unsorted icon to be shown when no sort is applied
     * to this column.
     * Default Value: false
     */
    unSortIcon: PropTypes.bool,

    /**
     * (Enterprise only) Set to true if you want to be able to row group by this column
     * via the GUI. This will not block the API or properties being used to achieve row
     * grouping.
     * Default Value: false
     */
    enableRowGroup: PropTypes.bool,

    /**
     * (Enterprise only) Set to true if you want to be able to pivot by this column via
     * the GUI. This will not block the API or properties being used to achieve pivot.
     * Default Value: false
     */
    enablePivot: PropTypes.bool,

    /**
     * (Enterprise only) Set to true if you want to be able to aggregate by this column
     * via the GUI. This will not block the API or properties being used to achieve aggregation.
     * Default Value: false
     */
    enableValue: PropTypes.bool,

    /**
     * Set to true to flash a cell when it's refreshed.
     * Default Value: false
     */
    enableCellChangeFlash: PropTypes.bool,

    /**
     * Set to an array containing zero, one or many of the following options: 'filterMenuTab'
     * | 'generalMenuTab' | 'columnsMenuTab'. This is used to figure out which menu tabs
     * are present and in which order the tabs are shown.
     */
    menuTabs: PropTypes.any,

    /**
     * Set to true if no menu should be shown for this column header.
     * Default Value: false
     */
    suppressMenu: PropTypes.bool,

    /**
     * Set to true if you want this column's width to be fixed during 'size to fit' operations.
     * Default Value: false
     */
    suppressSizeToFit: PropTypes.bool,

    /**
     * Set to true if you do not want this column to be movable via dragging.
     * Default Value: false
     */
    suppressMovable: PropTypes.bool,

    /**
     * Set to true if this column is not navigable (i.e. cannot be tabbed into), otherwise
     * false. Can also be a callback function to have different rows navigable.
     * Default Value: false
     */
    suppressNavigable: PropTypes.bool,

    /**
     * Set to true to prevent this column from flashing on changes. Only applicable if
     * cell flashing is turned on for the grid.
     * Default Value: false
     */
    suppressCellFlash: PropTypes.bool,

    /**
     * Set to true to have the grid calculate the height of a row based on contents of
     * this column.
     * Default Value: false
     */
    autoHeight: PropTypes.bool,

    /**
     * Set to true to have the text wrap inside the cell.
     * Default Value: false
     */
    wrapText: PropTypes.bool,

    /**
     * Set to true to have cells under this column enter edit mode after single click.
     * Default Value: false
     */
    singleClickEdit: PropTypes.bool,

    /**
     * Defines the chart data type that should be used for a column.
     */
    chartDataType: PropTypes.any,

    /**
     * Params used to change the behaviour and appearance of the Columns Menu tab. See
     * Customising the Columns Menu Tab.
     */
    columnsMenuParams: PropTypes.any,

    /********************************
     * Column Groups Only
     *******************************/

    /**
     * The unique ID to give the column. This is optional. If missing, a unique ID will
     * be generated. This ID is used to identify the column group in the column API.
     */
    groupId: PropTypes.any,

    /**
     * A list containing a mix of columns and column groups.
     */
    children: PropTypes.any,

    /**
     * Set to true to keep columns in this group beside each other in the grid. Moving
     * the columns outside of the group (and hence breaking the group) is not allowed.
     * Default Value: false
     */
    marryChildren: PropTypes.bool,

    /**
     * Set to true if this group should be opened by default.
     * Default Value: false
     */
    openByDefault: PropTypes.bool,

    /**
     * Component to use header group.
     */
    headerGroupComponent: PropTypes.any,

    /**
     * Params for the header group component.
     */
    headerGroupComponentParams: PropTypes.any,
};
