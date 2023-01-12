# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AgGridColumn(Component):
    """An AgGridColumn component.


Keyword arguments:

- children (boolean | number | string | dict | list; optional):
    The children of this component.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- aggFunc (boolean | number | string | dict | list; optional):
    Name of function to use for aggregation. You can also provide your
    own agg function.

- allowedAggFuncs (boolean | number | string | dict | list; optional):
    Aggregation functions allowed on this column e.g. ['sum', 'avg'].
    If missing, all installed functions are allowed. This will only
    restrict what the GUI allows a user to select, it does not impact
    when you set a function via the API.

- autoHeight (boolean; optional):
    Set to True to have the grid calculate the height of a row based
    on contents of this column. Default Value: False.

- cellClass (boolean | number | string | dict | list; optional):
    The class to give a particular cell. See Cell Class.

- cellClassRules (boolean | number | string | dict | list; optional):
    Rules which can be applied to include certain CSS classes. See
    Cell Class Rules.

- cellEditor (boolean | number | string | dict | list; optional):
    cellEditor to use for this column.

- cellEditorParams (boolean | number | string | dict | list; optional):
    Params to be passed to cell editor component.

- cellRenderer (boolean | number | string | dict | list; optional):
    cellRenderer to use for this column.

- cellRendererParams (boolean | number | string | dict | list; optional):
    Params to be passed to cell renderer component.

- cellRendererSelector (boolean | number | string | dict | list; optional):
    Callback to select which cell renderer / cell editor to be used
    for a given row within the same column.

- cellStyle (boolean | number | string | dict | list; optional):
    The style to give a particular cell. See Cell Style.

- chartDataType (boolean | number | string | dict | list; optional):
    Defines the chart data type that should be used for a column.

- checkboxSelection (boolean; optional):
    boolean or Function. Set to True (or return True from function) to
    render a selection checkbox in the column. Default Value: False.

- colId (boolean | number | string | dict | list; optional):
    The unique ID to give the column. This is optional. If missing,
    the ID will default to the field. If both field and colId are
    missing, a unique ID will be generated. This ID is used to
    identify the column in the API for sorting, filtering etc.

- columnGroupShow (boolean | number | string | dict | list; optional):
    Whether to show the column when the group is open / closed.

- columnsMenuParams (boolean | number | string | dict | list; optional):
    Params used to change the behaviour and appearance of the Columns
    Menu tab. See Customising the Columns Menu Tab.

- defaultWidth (boolean | number | string | dict | list; optional):
    Same as 'width', except only applied when creating a new column.
    Not applied when updating column definitions.

- dndSource (boolean; optional):
    boolean or Function. Set to True (or return True from function) to
    allow dragging for native drag and drop. Default Value: False.

- dndSourceOnRowDrag (boolean | number | string | dict | list; optional):
    Function to allow custom drag functionality for native drag and
    drop.

- editable (boolean; optional):
    Set to True if this column is editable, otherwise False. Can also
    be a function to have different rows editable. Default Value:
    False.

- enableCellChangeFlash (boolean; optional):
    Set to True to flash a cell when it's refreshed. Default Value:
    False.

- enablePivot (boolean; optional):
    (Enterprise only) Set to True if you want to be able to pivot by
    this column via the GUI. This will not block the API or properties
    being used to achieve pivot. Default Value: False.

- enableRowGroup (boolean; optional):
    (Enterprise only) Set to True if you want to be able to row group
    by this column via the GUI. This will not block the API or
    properties being used to achieve row grouping. Default Value:
    False.

- enableValue (boolean; optional):
    (Enterprise only) Set to True if you want to be able to aggregate
    by this column via the GUI. This will not block the API or
    properties being used to achieve aggregation. Default Value:
    False.

- field (boolean | number | string | dict | list; optional):
    The field of the row to get the cells data from.

- filter (boolean | number | string | dict | list; optional):
    Filter component to use for this column. Set to True to use the
    default filter.

- filterParams (boolean | number | string | dict | list; optional):
    Custom params to be passed to filter component.

- flex (boolean | number | string | dict | list; optional):
    Used instead of width when the goal is to fill the remaining empty
    space of the grid. See Column Flex.

- floatingFilter (boolean; optional):
    Whether to show a floating filter for this column. Default Value:
    False.

- floatingFilterComponent (boolean | number | string | dict | list; optional):
    Floating filter component to use for this column.

- floatingFilterComponentParams (boolean | number | string | dict | list; optional):
    Custom params to be passed to floatingFilterComponent or
    floatingFilterComponentFramework.

- getQuickFilterText (boolean | number | string | dict | list; optional):
    A function to tell the grid what quick filter text to use for this
    column if you don't want to use the default (which is calling
    toString on the value).

- groupId (boolean | number | string | dict | list; optional):
    The unique ID to give the column. This is optional. If missing, a
    unique ID will be generated. This ID is used to identify the
    column group in the column API.

- headerCheckboxSelection (boolean; optional):
    boolean. Set to True to show a checkbox in the header of a column.
    Default Value: False.

- headerCheckboxSelectionFilteredOnly (boolean; optional):
    boolean. Set to True for checkbox selections to only affect
    filtered data. Default Value: False.

- headerClass (boolean | number | string | dict | list; optional):
    Class to use for the header cell. Can be a string, array of
    strings, or function.

- headerComponent (boolean | number | string | dict | list; optional):
    Header component to use for this column.

- headerComponentParams (boolean | number | string | dict | list; optional):
    Params to be passed to header component.

- headerGroupComponent (boolean | number | string | dict | list; optional):
    Component to use header group.

- headerGroupComponentParams (boolean | number | string | dict | list; optional):
    Params for the header group component.

- headerName (boolean | number | string | dict | list; optional):
    The name to render in the column header. If not specified and
    field is specified, the field name will be used as the header
    name.

- headerTooltip (boolean | number | string | dict | list; optional):
    Tooltip for the column header.

- hide (boolean; optional):
    Set to True for this column to be hidden. You might think it would
    make more sense to call this field visible and mark it False to
    hide, but we want all default values to be False and we want
    columns to be visible by default. Default Value: False.

- initialAggFunc (boolean | number | string | dict | list; optional):
    Same as 'aggFunc', except only applied when creating a new column.
    Not applied when updating column definitions.

- initialFlex (boolean | number | string | dict | list; optional):
    Same as 'flex', except only applied when creating a new column.
    Not applied when updating column definitions.

- initialHide (boolean | number | string | dict | list; optional):
    Same as 'hide', except only applied when creating a new column.
    Not applied when updating column definitions.

- initialPinned (boolean | number | string | dict | list; optional):
    Same as 'pinned', except only applied when creating a new column.
    Not applied when updating column definitions.

- initialPivot (boolean | number | string | dict | list; optional):
    Same as 'pivot', except only applied when creating a new column.
    Not applied when updating column definitions.

- initialPivotIndex (boolean | number | string | dict | list; optional):
    Same as 'pivotIndex', except only applied when creating a new
    column. Not applied when updating column definitions.

- initialRowGroup (boolean | number | string | dict | list; optional):
    Same as 'rowGroup', except only applied when creating a new
    column. Not applied when updating column definitions.

- initialRowGroupIndex (boolean | number | string | dict | list; optional):
    Same as 'rowGroupIndex', except only applied when creating a new
    column. Not applied when updating column definitions.

- initialSort (boolean | number | string | dict | list; optional):
    Same as 'sort', except only applied when creating a new column.
    Not applied when updating column definitions.

- initialSortIndex (boolean | number | string | dict | list; optional):
    Same as 'sortIndex', except only applied when creating a new
    column. Not applied when updating column definitions.

- lockPinned (boolean; optional):
    Set to True to block pinning column via the UI (API will still
    work). Default Value: False.

- lockPosition (boolean; optional):
    Set to True to always have this column displayed first. Default
    Value: False.

- lockVisible (boolean; optional):
    Set to True to block making column visible / hidden via the UI
    (API will still work). Default Value: False.

- marryChildren (boolean; optional):
    Set to True to keep columns in this group beside each other in the
    grid. Moving the columns outside of the group (and hence breaking
    the group) is not allowed. Default Value: False.

- maxWidth (boolean | number | string | dict | list; optional):
    Maximum width in pixels for the cell.

- menuTabs (boolean | number | string | dict | list; optional):
    Set to an array containing zero, one or many of the following
    options: 'filterMenuTab' | 'generalMenuTab' | 'columnsMenuTab'.
    This is used to figure out which menu tabs are present and in
    which order the tabs are shown.

- minWidth (boolean | number | string | dict | list; optional):
    Minimum width in pixels for the cell.

- openByDefault (boolean; optional):
    Set to True if this group should be opened by default. Default
    Value: False.

- pinned (boolean | number | string | dict | list; optional):
    Pin a column to one side.

- pinnedRowCellRenderer (boolean | number | string | dict | list; optional):
    cellRenderer to use for pinned rows in this column. Pinned cells
    will use pinnedCellRenderer if available, or cellRenderer if not.

- pinnedRowCellRendererParams (boolean | number | string | dict | list; optional):
    Params to be passed to pinned row cell renderer component.

- pivot (boolean | number | string | dict | list; optional):
    Set to True to pivot by this column.

- pivotIndex (boolean | number | string | dict | list; optional):
    Set this in columns you want to pivot by. If only pivoting by one
    column, set this to any number (e.g. 0). If pivoting by multiple
    columns, set this to where you want this column to be in the order
    of pivots (e.g. 0 for first, 1 for second, and so on).

- resizable (boolean; optional):
    Set to True to allow column to be resized. Default Value: False.

- rowDrag (boolean; optional):
    boolean or Function. Set to True (or return True from function) to
    allow row dragging. Default Value: False.

- rowDragText (boolean | number | string | dict | list; optional):
    A callback that should return a string to be displayed by the
    rowDragComp while dragging a row. If this callback is not set, the
    current cell value will be used.function (params: IParams):
    string;.

- rowGroup (boolean | number | string | dict | list; optional):
    Set to True to row group by this column.

- rowGroupIndex (boolean | number | string | dict | list; optional):
    Set this in columns you want to group by. If only grouping by one
    column, set this to any number (e.g. 0). If grouping by multiple
    columns, set this to where you want this column to be in the group
    (e.g. 0 for first, 1 for second, and so on).

- setProps (string; optional):
    Dash-assigned callback that gets fired when the input changes.

- singleClickEdit (boolean; optional):
    Set to True to have cells under this column enter edit mode after
    single click. Default Value: False.

- sort (a value equal to: null, 'asc', 'desc'; optional):
    Set to sort this column. Default Value: [None, 'asc', 'desc'].

- sortIndex (boolean | number | string | dict | list; optional):
    If doing multi-sort by default, the order which column sorts are
    applied.

- sortable (boolean; optional):
    Set to True to allow sorting on this column. Default Value: False.

- sortingOrder (a value equal to: null, 'asc', 'desc'; optional):
    Array defining the order in which sorting occurs (if sorting is
    enabled). Default Value: [None, 'asc', 'desc'].

- style (dict; optional):
    The CSS style for the component.

- suppressCellFlash (boolean; optional):
    Set to True to prevent this column from flashing on changes. Only
    applicable if cell flashing is turned on for the grid. Default
    Value: False.

- suppressColumnsToolPanel (boolean; optional):
    Set to True if you do not want this column or group to appear in
    the Columns Tool Panel. Default Value: False.

- suppressFiltersToolPanel (boolean; optional):
    Set to True if you do not want this column (filter) or group
    (filter group) to appear in the Filters Tool Panel. Default Value:
    False.

- suppressMenu (boolean; optional):
    Set to True if no menu should be shown for this column header.
    Default Value: False.

- suppressMovable (boolean; optional):
    Set to True if you do not want this column to be movable via
    dragging. Default Value: False.

- suppressNavigable (boolean; optional):
    Set to True if this column is not navigable (i.e. cannot be tabbed
    into), otherwise False. Can also be a callback function to have
    different rows navigable. Default Value: False.

- suppressSizeToFit (boolean; optional):
    Set to True if you want this column's width to be fixed during
    'size to fit' operations. Default Value: False.

- toolPanelClass (boolean | number | string | dict | list; optional):
    Class to use for the tool panel cell. Can be a string, array of
    strings, or function.

- tooltipField (boolean | number | string | dict | list; optional):
    The field of the tooltip to apply to the cell.

- tooltipValueGetter (boolean | number | string | dict | list; optional):
    Callback that should return the string used for a tooltip.function
    (params: IParams): string;.

- type (boolean | number | string | dict | list; optional):
    A comma separated string or array of strings containing ColumnType
    keys which can be used as a template for a column. This helps to
    reduce duplication of properties when you have a lot of common
    column properties.

- unSortIcon (boolean; optional):
    Set to True if you want the unsorted icon to be shown when no sort
    is applied to this column. Default Value: False.

- width (boolean | number | string | dict | list; optional):
    Initial width in pixels for the cell.

- wrapText (boolean; optional):
    Set to True to have the text wrap inside the cell. Default Value:
    False."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, headerCheckboxSelection=Component.UNDEFINED, headerCheckboxSelectionFilteredOnly=Component.UNDEFINED, headerName=Component.UNDEFINED, columnGroupShow=Component.UNDEFINED, headerClass=Component.UNDEFINED, toolPanelClass=Component.UNDEFINED, suppressColumnsToolPanel=Component.UNDEFINED, suppressFiltersToolPanel=Component.UNDEFINED, field=Component.UNDEFINED, colId=Component.UNDEFINED, type=Component.UNDEFINED, width=Component.UNDEFINED, defaultWidth=Component.UNDEFINED, minWidth=Component.UNDEFINED, maxWidth=Component.UNDEFINED, flex=Component.UNDEFINED, initialFlex=Component.UNDEFINED, filter=Component.UNDEFINED, filterParams=Component.UNDEFINED, floatingFilter=Component.UNDEFINED, floatingFilterComponent=Component.UNDEFINED, floatingFilterComponentParams=Component.UNDEFINED, hide=Component.UNDEFINED, initialHide=Component.UNDEFINED, pinned=Component.UNDEFINED, initialPinned=Component.UNDEFINED, lockPosition=Component.UNDEFINED, lockVisible=Component.UNDEFINED, lockPinned=Component.UNDEFINED, sortable=Component.UNDEFINED, sort=Component.UNDEFINED, initialSort=Component.UNDEFINED, sortIndex=Component.UNDEFINED, initialSortIndex=Component.UNDEFINED, sortingOrder=Component.UNDEFINED, resizable=Component.UNDEFINED, headerTooltip=Component.UNDEFINED, tooltipField=Component.UNDEFINED, tooltipValueGetter=Component.UNDEFINED, checkboxSelection=Component.UNDEFINED, rowDrag=Component.UNDEFINED, rowDragText=Component.UNDEFINED, dndSource=Component.UNDEFINED, dndSourceOnRowDrag=Component.UNDEFINED, cellStyle=Component.UNDEFINED, cellClass=Component.UNDEFINED, cellClassRules=Component.UNDEFINED, editable=Component.UNDEFINED, cellRenderer=Component.UNDEFINED, cellRendererParams=Component.UNDEFINED, pinnedRowCellRenderer=Component.UNDEFINED, pinnedRowCellRendererParams=Component.UNDEFINED, cellRendererSelector=Component.UNDEFINED, cellEditor=Component.UNDEFINED, cellEditorParams=Component.UNDEFINED, headerComponent=Component.UNDEFINED, headerComponentParams=Component.UNDEFINED, getQuickFilterText=Component.UNDEFINED, aggFunc=Component.UNDEFINED, initialAggFunc=Component.UNDEFINED, allowedAggFuncs=Component.UNDEFINED, rowGroup=Component.UNDEFINED, initialRowGroup=Component.UNDEFINED, rowGroupIndex=Component.UNDEFINED, initialRowGroupIndex=Component.UNDEFINED, pivot=Component.UNDEFINED, initialPivot=Component.UNDEFINED, pivotIndex=Component.UNDEFINED, initialPivotIndex=Component.UNDEFINED, unSortIcon=Component.UNDEFINED, enableRowGroup=Component.UNDEFINED, enablePivot=Component.UNDEFINED, enableValue=Component.UNDEFINED, enableCellChangeFlash=Component.UNDEFINED, menuTabs=Component.UNDEFINED, suppressMenu=Component.UNDEFINED, suppressSizeToFit=Component.UNDEFINED, suppressMovable=Component.UNDEFINED, suppressNavigable=Component.UNDEFINED, suppressCellFlash=Component.UNDEFINED, autoHeight=Component.UNDEFINED, wrapText=Component.UNDEFINED, singleClickEdit=Component.UNDEFINED, chartDataType=Component.UNDEFINED, columnsMenuParams=Component.UNDEFINED, groupId=Component.UNDEFINED, marryChildren=Component.UNDEFINED, openByDefault=Component.UNDEFINED, headerGroupComponent=Component.UNDEFINED, headerGroupComponentParams=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aggFunc', 'allowedAggFuncs', 'autoHeight', 'cellClass', 'cellClassRules', 'cellEditor', 'cellEditorParams', 'cellRenderer', 'cellRendererParams', 'cellRendererSelector', 'cellStyle', 'chartDataType', 'checkboxSelection', 'colId', 'columnGroupShow', 'columnsMenuParams', 'defaultWidth', 'dndSource', 'dndSourceOnRowDrag', 'editable', 'enableCellChangeFlash', 'enablePivot', 'enableRowGroup', 'enableValue', 'field', 'filter', 'filterParams', 'flex', 'floatingFilter', 'floatingFilterComponent', 'floatingFilterComponentParams', 'getQuickFilterText', 'groupId', 'headerCheckboxSelection', 'headerCheckboxSelectionFilteredOnly', 'headerClass', 'headerComponent', 'headerComponentParams', 'headerGroupComponent', 'headerGroupComponentParams', 'headerName', 'headerTooltip', 'hide', 'initialAggFunc', 'initialFlex', 'initialHide', 'initialPinned', 'initialPivot', 'initialPivotIndex', 'initialRowGroup', 'initialRowGroupIndex', 'initialSort', 'initialSortIndex', 'lockPinned', 'lockPosition', 'lockVisible', 'marryChildren', 'maxWidth', 'menuTabs', 'minWidth', 'openByDefault', 'pinned', 'pinnedRowCellRenderer', 'pinnedRowCellRendererParams', 'pivot', 'pivotIndex', 'resizable', 'rowDrag', 'rowDragText', 'rowGroup', 'rowGroupIndex', 'setProps', 'singleClickEdit', 'sort', 'sortIndex', 'sortable', 'sortingOrder', 'style', 'suppressCellFlash', 'suppressColumnsToolPanel', 'suppressFiltersToolPanel', 'suppressMenu', 'suppressMovable', 'suppressNavigable', 'suppressSizeToFit', 'toolPanelClass', 'tooltipField', 'tooltipValueGetter', 'type', 'unSortIcon', 'width', 'wrapText']
        self._type = 'AgGridColumn'
        self._namespace = 'dash_ag_grid'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'aggFunc', 'allowedAggFuncs', 'autoHeight', 'cellClass', 'cellClassRules', 'cellEditor', 'cellEditorParams', 'cellRenderer', 'cellRendererParams', 'cellRendererSelector', 'cellStyle', 'chartDataType', 'checkboxSelection', 'colId', 'columnGroupShow', 'columnsMenuParams', 'defaultWidth', 'dndSource', 'dndSourceOnRowDrag', 'editable', 'enableCellChangeFlash', 'enablePivot', 'enableRowGroup', 'enableValue', 'field', 'filter', 'filterParams', 'flex', 'floatingFilter', 'floatingFilterComponent', 'floatingFilterComponentParams', 'getQuickFilterText', 'groupId', 'headerCheckboxSelection', 'headerCheckboxSelectionFilteredOnly', 'headerClass', 'headerComponent', 'headerComponentParams', 'headerGroupComponent', 'headerGroupComponentParams', 'headerName', 'headerTooltip', 'hide', 'initialAggFunc', 'initialFlex', 'initialHide', 'initialPinned', 'initialPivot', 'initialPivotIndex', 'initialRowGroup', 'initialRowGroupIndex', 'initialSort', 'initialSortIndex', 'lockPinned', 'lockPosition', 'lockVisible', 'marryChildren', 'maxWidth', 'menuTabs', 'minWidth', 'openByDefault', 'pinned', 'pinnedRowCellRenderer', 'pinnedRowCellRendererParams', 'pivot', 'pivotIndex', 'resizable', 'rowDrag', 'rowDragText', 'rowGroup', 'rowGroupIndex', 'setProps', 'singleClickEdit', 'sort', 'sortIndex', 'sortable', 'sortingOrder', 'style', 'suppressCellFlash', 'suppressColumnsToolPanel', 'suppressFiltersToolPanel', 'suppressMenu', 'suppressMovable', 'suppressNavigable', 'suppressSizeToFit', 'toolPanelClass', 'tooltipField', 'tooltipValueGetter', 'type', 'unSortIcon', 'width', 'wrapText']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AgGridColumn, self).__init__(children=children, **args)
