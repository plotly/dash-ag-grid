# AUTO GENERATED FILE - DO NOT EDIT

export aggridcolumn

"""
    aggridcolumn(;kwargs...)
    aggridcolumn(children::Any;kwargs...)
    aggridcolumn(children_maker::Function;kwargs...)


An AgGridColumn component.

Keyword arguments:
- `children` (Bool | Real | String | Dict | Array; optional): The children of this component
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `aggFunc` (Bool | Real | String | Dict | Array; optional): Name of function to use for aggregation. You can also provide your own agg function.
- `allowedAggFuncs` (Bool | Real | String | Dict | Array; optional): Aggregation functions allowed on this column e.g. ['sum', 'avg']. If missing,
all installed functions are allowed. This will only restrict what the GUI allows
a user to select, it does not impact when you set a function via the API.
- `autoHeight` (Bool; optional): Set to true to have the grid calculate the height of a row based on contents of
this column.
Default Value: false
- `cellClass` (Bool | Real | String | Dict | Array; optional): The class to give a particular cell. See Cell Class.
- `cellClassRules` (Bool | Real | String | Dict | Array; optional): Rules which can be applied to include certain CSS classes. See Cell Class Rules.
- `cellEditor` (Bool | Real | String | Dict | Array; optional): cellEditor to use for this column.
- `cellEditorParams` (Bool | Real | String | Dict | Array; optional): Params to be passed to cell editor component.
- `cellRenderer` (Bool | Real | String | Dict | Array; optional): cellRenderer to use for this column.
- `cellRendererParams` (Bool | Real | String | Dict | Array; optional): Params to be passed to cell renderer component.
- `cellRendererSelector` (Bool | Real | String | Dict | Array; optional): Callback to select which cell renderer / cell editor to be used for a given row
within the same column.
- `cellStyle` (Bool | Real | String | Dict | Array; optional): The style to give a particular cell. See Cell Style.
- `chartDataType` (Bool | Real | String | Dict | Array; optional): Defines the chart data type that should be used for a column.
- `checkboxSelection` (Bool; optional): boolean or Function. Set to true (or return true from function) to render a selection
checkbox in the column.
Default Value: false
- `colId` (Bool | Real | String | Dict | Array; optional): The unique ID to give the column. This is optional. If missing, the ID will default
to the field. If both field and colId are missing, a unique ID will be generated.
This ID is used to identify the column in the API for sorting, filtering etc.
- `columnGroupShow` (Bool | Real | String | Dict | Array; optional): Whether to show the column when the group is open / closed.
- `columnsMenuParams` (Bool | Real | String | Dict | Array; optional): Params used to change the behaviour and appearance of the Columns Menu tab. See
Customising the Columns Menu Tab.
- `defaultWidth` (Bool | Real | String | Dict | Array; optional): Same as 'width', except only applied when creating a new column. Not applied when
updating column definitions.
- `dndSource` (Bool; optional): boolean or Function. Set to true (or return true from function) to allow dragging
for native drag and drop.
Default Value: false
- `dndSourceOnRowDrag` (Bool | Real | String | Dict | Array; optional): Function to allow custom drag functionality for native drag and drop.
- `editable` (Bool; optional): Set to true if this column is editable, otherwise false. Can also be a function
to have different rows editable.
Default Value: false
- `enableCellChangeFlash` (Bool; optional): Set to true to flash a cell when it's refreshed.
Default Value: false
- `enablePivot` (Bool; optional): (Enterprise only) Set to true if you want to be able to pivot by this column via
the GUI. This will not block the API or properties being used to achieve pivot.
Default Value: false
- `enableRowGroup` (Bool; optional): (Enterprise only) Set to true if you want to be able to row group by this column
via the GUI. This will not block the API or properties being used to achieve row
grouping.
Default Value: false
- `enableValue` (Bool; optional): (Enterprise only) Set to true if you want to be able to aggregate by this column
via the GUI. This will not block the API or properties being used to achieve aggregation.
Default Value: false
- `field` (Bool | Real | String | Dict | Array; optional): The field of the row to get the cells data from.
- `filter` (Bool | Real | String | Dict | Array; optional): Filter component to use for this column. Set to true to use the default filter.
- `filterParams` (Bool | Real | String | Dict | Array; optional): Custom params to be passed to filter component.
- `flex` (Bool | Real | String | Dict | Array; optional): Used instead of width when the goal is to fill the remaining empty space of the
grid. See Column Flex.
- `floatingFilter` (Bool; optional): Whether to show a floating filter for this column.
Default Value: false
- `floatingFilterComponent` (Bool | Real | String | Dict | Array; optional): Floating filter component to use for this column.
- `floatingFilterComponentParams` (Bool | Real | String | Dict | Array; optional): Custom params to be passed to floatingFilterComponent or floatingFilterComponentFramework.
- `getQuickFilterText` (Bool | Real | String | Dict | Array; optional): A function to tell the grid what quick filter text to use for this column if you
don't want to use the default (which is calling toString on the value).
- `groupId` (Bool | Real | String | Dict | Array; optional): The unique ID to give the column. This is optional. If missing, a unique ID will
be generated. This ID is used to identify the column group in the column API.
- `headerCheckboxSelection` (Bool; optional): boolean. Set to true to show a checkbox in the header of a column.
Default Value: false
- `headerCheckboxSelectionFilteredOnly` (Bool; optional): boolean. Set to true for checkbox selections to only affect filtered data.
Default Value: false
- `headerClass` (Bool | Real | String | Dict | Array; optional): Class to use for the header cell. Can be a string, array of strings, or function.
- `headerComponent` (Bool | Real | String | Dict | Array; optional): Header component to use for this column.
- `headerComponentParams` (Bool | Real | String | Dict | Array; optional): Params to be passed to header component.
- `headerGroupComponent` (Bool | Real | String | Dict | Array; optional): Component to use header group.
- `headerGroupComponentParams` (Bool | Real | String | Dict | Array; optional): Params for the header group component.
- `headerName` (Bool | Real | String | Dict | Array; optional): The name to render in the column header. If not specified and field is specified,
the field name will be used as the header name.
- `headerTooltip` (Bool | Real | String | Dict | Array; optional): Tooltip for the column header
- `hide` (Bool; optional): Set to true for this column to be hidden. You might think it would make more sense
to call this field visible and mark it false to hide, but we want all default
values to be false and we want columns to be visible by default.
Default Value: false
- `initialAggFunc` (Bool | Real | String | Dict | Array; optional): Same as 'aggFunc', except only applied when creating a new column. Not applied
when updating column definitions.
- `initialFlex` (Bool | Real | String | Dict | Array; optional): Same as 'flex', except only applied when creating a new column. Not applied when
updating column definitions.
- `initialHide` (Bool | Real | String | Dict | Array; optional): Same as 'hide', except only applied when creating a new column. Not applied when
updating column definitions.
- `initialPinned` (Bool | Real | String | Dict | Array; optional): Same as 'pinned', except only applied when creating a new column. Not applied
when updating column definitions.
- `initialPivot` (Bool | Real | String | Dict | Array; optional): Same as 'pivot', except only applied when creating a new column. Not applied when
updating column definitions.
- `initialPivotIndex` (Bool | Real | String | Dict | Array; optional): Same as 'pivotIndex', except only applied when creating a new column. Not applied
when updating column definitions.
- `initialRowGroup` (Bool | Real | String | Dict | Array; optional): Same as 'rowGroup', except only applied when creating a new column. Not applied
when updating column definitions.
- `initialRowGroupIndex` (Bool | Real | String | Dict | Array; optional): Same as 'rowGroupIndex', except only applied when creating a new column. Not applied
when updating column definitions.
- `initialSort` (Bool | Real | String | Dict | Array; optional): Same as 'sort', except only applied when creating a new column. Not applied when
updating column definitions.
- `initialSortIndex` (Bool | Real | String | Dict | Array; optional): Same as 'sortIndex', except only applied when creating a new column. Not applied
when updating column definitions.
- `lockPinned` (Bool; optional): Set to true to block pinning column via the UI (API will still work).
Default Value: false
- `lockPosition` (Bool; optional): Set to true to always have this column displayed first.
Default Value: false
- `lockVisible` (Bool; optional): Set to true to block making column visible / hidden via the UI (API will still
work).
Default Value: false
- `marryChildren` (Bool; optional): Set to true to keep columns in this group beside each other in the grid. Moving
the columns outside of the group (and hence breaking the group) is not allowed.
Default Value: false
- `maxWidth` (Bool | Real | String | Dict | Array; optional): Maximum width in pixels for the cell.
- `menuTabs` (Bool | Real | String | Dict | Array; optional): Set to an array containing zero, one or many of the following options: 'filterMenuTab'
| 'generalMenuTab' | 'columnsMenuTab'. This is used to figure out which menu tabs
are present and in which order the tabs are shown.
- `minWidth` (Bool | Real | String | Dict | Array; optional): Minimum width in pixels for the cell.
- `openByDefault` (Bool; optional): Set to true if this group should be opened by default.
Default Value: false
- `pinned` (Bool | Real | String | Dict | Array; optional): Pin a column to one side.
- `pinnedRowCellRenderer` (Bool | Real | String | Dict | Array; optional): cellRenderer to use for pinned rows in this column. Pinned cells will use pinnedCellRenderer
if available, or cellRenderer if not.
- `pinnedRowCellRendererParams` (Bool | Real | String | Dict | Array; optional): Params to be passed to pinned row cell renderer component.
- `pivot` (Bool | Real | String | Dict | Array; optional): Set to true to pivot by this column
- `pivotIndex` (Bool | Real | String | Dict | Array; optional): Set this in columns you want to pivot by. If only pivoting by one column, set
this to any number (e.g. 0). If pivoting by multiple columns, set this to where
you want this column to be in the order of pivots (e.g. 0 for first, 1 for second,
and so on).
- `resizable` (Bool; optional): Set to true to allow column to be resized.
Default Value: false
- `rowDrag` (Bool; optional): boolean or Function. Set to true (or return true from function) to allow row dragging.
Default Value: false
- `rowDragText` (Bool | Real | String | Dict | Array; optional): A callback that should return a string to be displayed by the rowDragComp while
dragging a row. If this callback is not set, the current cell value will be used.function
(params: IParams): string;
- `rowGroup` (Bool | Real | String | Dict | Array; optional): Set to true to row group by this column
- `rowGroupIndex` (Bool | Real | String | Dict | Array; optional): Set this in columns you want to group by. If only grouping by one column, set
this to any number (e.g. 0). If grouping by multiple columns, set this to where
you want this column to be in the group (e.g. 0 for first, 1 for second, and so
on).
- `setProps` (String; optional): Dash-assigned callback that gets fired when the input changes
- `singleClickEdit` (Bool; optional): Set to true to have cells under this column enter edit mode after single click.
Default Value: false
- `sort` (a value equal to: null, 'asc', 'desc'; optional): Set to sort this column.
Default Value: [null, 'asc', 'desc']
- `sortIndex` (Bool | Real | String | Dict | Array; optional): If doing multi-sort by default, the order which column sorts are applied.
- `sortable` (Bool; optional): Set to true to allow sorting on this column.
Default Value: false
- `sortingOrder` (a value equal to: null, 'asc', 'desc'; optional): Array defining the order in which sorting occurs (if sorting is enabled).
Default Value: [null, 'asc', 'desc']
- `style` (Dict; optional): The CSS style for the component
- `suppressCellFlash` (Bool; optional): Set to true to prevent this column from flashing on changes. Only applicable if
cell flashing is turned on for the grid.
Default Value: false
- `suppressColumnsToolPanel` (Bool; optional): Set to true if you do not want this column or group to appear in the Columns Tool
Panel.
Default Value: false
- `suppressFiltersToolPanel` (Bool; optional): Set to true if you do not want this column (filter) or group (filter group) to
appear in the Filters Tool Panel.
Default Value: false
- `suppressMenu` (Bool; optional): Set to true if no menu should be shown for this column header.
Default Value: false
- `suppressMovable` (Bool; optional): Set to true if you do not want this column to be movable via dragging.
Default Value: false
- `suppressNavigable` (Bool; optional): Set to true if this column is not navigable (i.e. cannot be tabbed into), otherwise
false. Can also be a callback function to have different rows navigable.
Default Value: false
- `suppressSizeToFit` (Bool; optional): Set to true if you want this column's width to be fixed during 'size to fit' operations.
Default Value: false
- `toolPanelClass` (Bool | Real | String | Dict | Array; optional): Class to use for the tool panel cell. Can be a string, array of strings, or function.
- `tooltipField` (Bool | Real | String | Dict | Array; optional): The field of the tooltip to apply to the cell.
- `tooltipValueGetter` (Bool | Real | String | Dict | Array; optional): Callback that should return the string used for a tooltip.function (params: IParams):
string;
- `type` (Bool | Real | String | Dict | Array; optional): A comma separated string or array of strings containing ColumnType keys which
can be used as a template for a column. This helps to reduce duplication of properties
when you have a lot of common column properties.
- `unSortIcon` (Bool; optional): Set to true if you want the unsorted icon to be shown when no sort is applied
to this column.
Default Value: false
- `width` (Bool | Real | String | Dict | Array; optional): Initial width in pixels for the cell.
- `wrapText` (Bool; optional): Set to true to have the text wrap inside the cell.
Default Value: false
"""
function aggridcolumn(; kwargs...)
        available_props = Symbol[:children, :id, :aggFunc, :allowedAggFuncs, :autoHeight, :cellClass, :cellClassRules, :cellEditor, :cellEditorParams, :cellRenderer, :cellRendererParams, :cellRendererSelector, :cellStyle, :chartDataType, :checkboxSelection, :colId, :columnGroupShow, :columnsMenuParams, :defaultWidth, :dndSource, :dndSourceOnRowDrag, :editable, :enableCellChangeFlash, :enablePivot, :enableRowGroup, :enableValue, :field, :filter, :filterParams, :flex, :floatingFilter, :floatingFilterComponent, :floatingFilterComponentParams, :getQuickFilterText, :groupId, :headerCheckboxSelection, :headerCheckboxSelectionFilteredOnly, :headerClass, :headerComponent, :headerComponentParams, :headerGroupComponent, :headerGroupComponentParams, :headerName, :headerTooltip, :hide, :initialAggFunc, :initialFlex, :initialHide, :initialPinned, :initialPivot, :initialPivotIndex, :initialRowGroup, :initialRowGroupIndex, :initialSort, :initialSortIndex, :lockPinned, :lockPosition, :lockVisible, :marryChildren, :maxWidth, :menuTabs, :minWidth, :openByDefault, :pinned, :pinnedRowCellRenderer, :pinnedRowCellRendererParams, :pivot, :pivotIndex, :resizable, :rowDrag, :rowDragText, :rowGroup, :rowGroupIndex, :singleClickEdit, :sort, :sortIndex, :sortable, :sortingOrder, :style, :suppressCellFlash, :suppressColumnsToolPanel, :suppressFiltersToolPanel, :suppressMenu, :suppressMovable, :suppressNavigable, :suppressSizeToFit, :toolPanelClass, :tooltipField, :tooltipValueGetter, :type, :unSortIcon, :width, :wrapText]
        wild_props = Symbol[]
        return Component("aggridcolumn", "AgGridColumn", "dash_ag_grid", available_props, wild_props; kwargs...)
end

aggridcolumn(children::Any; kwargs...) = aggridcolumn(;kwargs..., children = children)
aggridcolumn(children_maker::Function; kwargs...) = aggridcolumn(children_maker(); kwargs...)

