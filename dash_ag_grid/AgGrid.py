# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AgGrid(Component):
    """An AgGrid component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this component.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- AsyncTransactionsFlushed (boolean | number | string | dict | list; optional):
    Async transactions have been applied. Contains a list of all
    transaction results.

- accentedSort (boolean; optional):
    Set to True to specify that the sort should take into account
    accented characters. If this feature is turned on the sort will
    perform slower. See Accented Sort. Default Value: False.

- aggFuncs (boolean | number | string | dict | list; optional):
    A map of 'function name' to 'function' for custom aggregation
    functions. See Custom Aggregation Functions.

- aggregateOnlyChangedColumns (boolean; optional):
    When using change detection, only the updated column with get
    re-aggregated. Default Value: False.

- alignedGrids (boolean | number | string | dict | list; optional):
    A list of grids to treat as Aligned Grids. If grids are aligned
    then the columns and horizontal scrolling will be kept in sync.

- allowContextMenuWithControlKey (boolean | number | string | dict | list; optional):
    Allows context menu to show, even when Ctrl key is held down.

- allowDragFromColumnsToolPanel (boolean; optional):
    Allow reordering and pinning columns by dragging columns from the
    columns tool panel to the grid. Default Value: False.

- allowShowChangeAfterFilter (boolean; optional):
    Set to True to have cells flash after data changes even when the
    change is due to filtering. See Flashing Data Changes. Default
    Value: False.

- alwaysShowHorizontalScroll (boolean; optional):
    Set to True to always show the horizontal scrollbar. Default
    Value: False.

- alwaysShowVerticalScroll (boolean; optional):
    Set to True to always show the vertical scrollbar. Default Value:
    False.

- animateRows (boolean; optional):
    Set to True to enable Row Animation. Default Value: False.

- animationQueueEmpty (boolean | number | string | dict | list; optional):
    The grid draws rows and cells using animation frames. This event
    gets fired when the animation frame queue is empty. Normally used
    in conjunction with api.isAnimationFrameQueueEmpty() so user can
    check if animation frame is pending, and if so then can be
    notified when no animation frames are pending. Useful if your
    application needs to know when drawing of the grid is no longer
    pending, e.g. for sending to a printer.

- applyColumnDefOrder (boolean; optional):
    Sorts the grid columns in the order of Column Definitions after
    Column Definitions are updated. See Apply Column Order. Default
    Value: False.

- asyncTransactionWaitMillis (boolean | number | string | dict | list; optional):
    How many milliseconds to wait before executing a batch of async
    transactions.

- autoGroupColumnDef (boolean | number | string | dict | list; optional):
    Allows specifying the group 'auto column' if you are not happy
    with the default. If grouping, this column def is included as the
    first column definition in the grid. If not grouping, this column
    is not included.

- autoSizePadding (number; optional):
    Number of pixels to add to a column width after the auto-sizing
    calculation. Set this if you want to add extra room to accommodate
    (for example) sort icons, or some other dynamic nature of the
    header. Default Value: 4.

- blockLoadDebounceMillis (boolean | number | string | dict | list; optional):
    How many milliseconds to wait before loading a block. Useful when
    scrolling over many rows, spanning many Partial Store blocks, as
    it prevents blocks loading until scrolling has settled.

- bodyScroll (boolean | number | string | dict | list; optional):
    The body was scrolled horizontally or vertically.

- cacheBlockSize (number; optional):
    Partial Store Only - How many rows for each block in the store,
    i.e. how many rows returned from the server at a time. Default
    Value: 100.

- cacheOverflowSize (number; optional):
    Quantity of extra blank rows to display to the user at the end of
    the dataset, which sets the vertical scroll and then allows the
    grid to request viewing more rows of data. default is 1, ie show 1
    row.

- cacheQuickFilter (boolean; optional):
    Set to True to turn on the  quick filter cache, used for a
    performance gain when using the quick filter. Default Value:
    False.

- cellClicked (boolean | number | string | dict | list; optional):
    Cell is clicked.

- cellContextMenu (boolean | number | string | dict | list; optional):
    Cell is right clicked.

- cellDoubleClicked (boolean | number | string | dict | list; optional):
    Cell is double clicked.

- cellEditingStarted (boolean | number | string | dict | list; optional):
    Editing a cell has started.

- cellEditingStopped (boolean | number | string | dict | list; optional):
    Editing a cell has stopped.

- cellFadeDelay (number; optional):
    To be used in combination with enableCellChangeFlash, this
    configuration will set delay in ms of how long the \"flashed
    Default Value: 1000.

- cellFlashDelay (number; optional):
    To be used in combination with enableCellChangeFlash, this
    configuration will set delay in ms of how long a cell should
    remain in its \"flashed Default Value: 500.

- cellFocused (boolean | number | string | dict | list; optional):
    Cell is focused.

- cellKeyDown (boolean | number | string | dict | list; optional):
    DOM event keyDown happened on a cell. See Keyboard Events.

- cellKeyPress (boolean | number | string | dict | list; optional):
    DOM event keyPress happened on a cell. See Keyboard Events.

- cellMouseDown (boolean | number | string | dict | list; optional):
    Mouse down on cell.

- cellMouseOut (boolean | number | string | dict | list; optional):
    Mouse left cell.

- cellMouseOver (boolean | number | string | dict | list; optional):
    Mouse entered cell.

- cellStyle (dict; optional):
    Object used to perform the cell styling. See AG-Grid Cell Style.

    `cellStyle` is a dict with keys:

    - defaultStyle (dict; optional)

    - styleConditions (list of dicts; optional)

        `styleConditions` is a list of dicts with keys:

        - condition (string; required)

        - style (dict; required)

- cellValueChanged (boolean | number | string | dict | list; optional):
    Value has changed after editing.

- chartThemeOverrides (boolean | number | string | dict | list; optional):
    Chart theme overrides applied to all themes, see Overriding
    Existing Themes.

- chartThemes (a value equal to: 'ag-default', 'ag-material', 'ag-pastel', 'ag-vivid', 'ag-solar'; optional):
    The list of chart themes to be used, see Chart Themes. Default
    Value: ['ag-default', 'ag-material', 'ag-pastel', 'ag-vivid',
    'ag-solar'].

- clickData (boolean | number | string | dict | list; optional):
    Special prop used by renderers.

- clipboardDeliminator (boolean | number | string | dict | list; optional):
    Specify the deliminator to use when copying to clipboard.

- colResizeDefault (boolean | number | string | dict | list; optional):
    Set to 'shift' to have shift-resize as the default resize
    operation (same as user holding down Shift while resizing).

- columnDefs (boolean | number | string | dict | list; optional):
    Array of Column Definitions.

- columnEverythingChanged (boolean | number | string | dict | list; optional):
    Shotgun - gets called when either a) new columns are set or b)
    columnApi.setState() is used, so everything has changed.

- columnGroupOpened (boolean | number | string | dict | list; optional):
    A column group was opened / closed.

- columnMoved (boolean | number | string | dict | list; optional):
    A column was moved. To find out when the column move is finished
    you can use the dragStopped event below.

- columnPinned (boolean | number | string | dict | list; optional):
    A column, or group of columns, was pinned / unpinned.

- columnPivotChanged (boolean | number | string | dict | list; optional):
    A pivot column was added, removed or order changed.

- columnPivotModeChanged (boolean | number | string | dict | list; optional):
    The pivot mode flag was changed.

- columnResized (boolean | number | string | dict | list; optional):
    A column was resized.

- columnRowGroupChanged (boolean | number | string | dict | list; optional):
    A row group column was added or removed.

- columnSize (a value equal to: 'sizeToFit', 'autoSizeAll'; optional):
    Size the columns automatically or to fit their contents.

- columnTypes (boolean | number | string | dict | list; optional):
    An object map of custom column types which contain groups of
    properties that column definitions can inherit.

- columnValueChanged (boolean | number | string | dict | list; optional):
    A value column was added or removed.

- columnVisible (boolean | number | string | dict | list; optional):
    A column, or group of columns, was hidden / shown.

- componentStateChanged (boolean | number | string | dict | list; optional):
    Only used by React, Angular and VueJS AG Grid components (not used
    if doing plain JavaScript or Angular 1.x). If the grid receives
    changes due to bound properties, this event fires after the grid
    has finished processing the change.

- components (boolean | number | string | dict | list; optional):
    A map of component names to plain JavaScript components.

- context (boolean | number | string | dict | list; optional):
    Provides a context object that is provided to different callbacks
    the grid uses. Used for passing additional information to the
    callbacks by your application.

- copyHeadersToClipboard (boolean; optional):
    Set to True to also include headers when copying to clipboard
    using Ctrl + C clipboard. Default Value: False.

- csvExportParams (dict; optional):
    Object with properties to pass to the exportDataAsCsv() method.

    `csvExportParams` is a dict with keys:

    - allColumns (boolean; optional):
        If True, all columns will be exported in the order they appear
        in the columnDefs.

    - appendContent (string; optional):
        Content to put at the bottom of the file export.

    - columnKeys (list of strings; optional):
        Provide a list (an array) of column keys or Column objects if
        you want to export specific columns.

    - columnSeparator (string; optional):
        Delimiter to insert between cell values.

    - fileName (string; optional):
        String to use as the file name.

    - onlySelected (boolean; optional):
        Export only selected rows.

    - onlySelectedAllPages (boolean; optional):
        Only export selected rows including other pages (only makes
        sense when using pagination).

    - prependContent (string; optional):
        Content to put at the top of the file export. A 2D array of
        CsvCell objects.

    - skipColumnGroupHeaders (boolean; optional):
        Set to True to skip include header column groups.

    - skipColumnHeaders (boolean; optional):
        Set to True if you don't want to export column headers.

    - skipPinnedBottom (boolean; optional):
        Set to True to suppress exporting rows pinned to the bottom of
        the grid.

    - skipPinnedTop (boolean; optional):
        Set to True to suppress exporting rows pinned to the top of
        the grid.

    - skipRowGroups (boolean; optional):
        Set to True to skip row group headers if grouping rows. Only
        relevant when grouping rows.

    - suppressQuotes (boolean; optional):
        Pass True to insert the value into the CSV file without
        escaping. In this case it is your responsibility to ensure
        that no cells contain the columnSeparator character.

- customChartThemes (boolean | number | string | dict | list; optional):
    A map containing custom chart themes, see Custom Chart Themes.

- debounceVerticalScrollbar (boolean; optional):
    Set to True to debounce the vertical scrollbar. Can provide
    smoother scrolling on older browsers, eg IE. Default Value: False.

- debug (boolean; optional):
    Set this to True to enable debug information from AG Grid and
    related components. Will result in additional logging being
    output, but very useful when investigating problems. Default
    Value: False.

- defaultColDef (boolean | number | string | dict | list; optional):
    A default column definition.

- defaultColGroupDef (boolean | number | string | dict | list; optional):
    A default column group definition. All column group definitions
    will use these properties. Items defined in the actual column
    group  definition get precedence.

- defaultExportParams (boolean | number | string | dict | list; optional):
    A default configuration object used to export to CSV or Excel.

- detailCellRendererParams (dict; optional):
    Specifies the params to be used by the default detail Cell
    Renderer. See Detail Grids.

    `detailCellRendererParams` is a dict with keys:

    - detailColName (string; optional):
        Column name where detail grid data is located in main dataset,
        for master-detail view.

    - detailGridOptions (boolean | number | string | dict | list; optional):
        Grid options for detail grid in master-detail view.

    - suppressCallback (boolean; optional):
        Default: True. If True, suppresses the Dash callback in favor
        of using the data embedded in rowData at the given
        detailColName.

- detailRowAutoHeight (boolean; optional):
    Set detail row height automatically based on contents.

- detailRowHeight (number; optional):
    Set fixed height in pixels for each detail row.

- displayedColumnsChanged (boolean | number | string | dict | list; optional):
    The list of displayed columns changed. This can result from
    columns open / close, column move, pivot, group, etc.

- domLayout (a value equal to: 'normal', 'autoHeight', 'print'; optional):
    Switch between layout options. See Printing and Auto Height.
    Default Value: ['normal', 'autoHeight', 'print'].

- dragStarted (boolean | number | string | dict | list; optional):
    When dragging starts. This could be any action that uses the
    grid's Drag and Drop service, e.g. Column Moving, Column Resizing,
    Range Selection, Fill Handle, etc.

- dragStopped (boolean | number | string | dict | list; optional):
    When dragging stops. This could be any action that uses the grid's
    Drag and Drop service, e.g. Column Moving, Column Resizing, Range
    Selection, Fill Handle, etc.

- editType (boolean | number | string | dict | list; optional):
    Set to 'fullRow' to enable Full Row Editing. Otherwise leave blank
    to edit one cell at a time.

- enableBrowserTooltips (boolean; optional):
    Set to True to use the browser's default tooltip instead of using
    AG Grid's Tooltip Component. Default Value: False.

- enableCellChangeFlash (boolean; optional):
    Set to True to have cells flash after data changes. See Flashing
    Data Changes. Default Value: False.

- enableCellExpressions (boolean; optional):
    Set to True to allow cell expressions. Default Value: False.

- enableCellTextSelection (boolean; optional):
    Set to True to be able to select the text within cells. Default
    Value: False.

- enableCharts (boolean; optional):
    Set to True to Enable Charts. Default Value: False.

- enableEnterpriseModules (boolean; optional):
    If True, enable ag-grid Enterprise modules. Recommended to use
    with licenseKey.

- enableExportDataAsCsv (boolean; default False):
    If True, the internal method exportDataAsCsv() will be called.

- enableFillHandle (boolean; optional):
    Set to True to enable Fill Handle Default Value: False.

- enableRangeHandle (boolean; optional):
    Set to True to enable Range Handle Default Value: False.

- enableRangeSelection (boolean; optional):
    Set to True to enable Range Selection. Default Value: False.

- enableResetColumnState (boolean; default False):
    If True, the internal method resetColumnState() will be called.

- enableRtl (boolean; optional):
    Set to True to operate grid in RTL (Right to Left) mode. Default
    Value: False.

- ensureDomOrder (boolean; optional):
    When True, the order of rows and columns in the DOM are consistent
    with what is on screen. See Accessibility - Row and Column Order.
    Default Value: False.

- enterMovesDown (boolean; optional):
    Set both properties to True to have Excel-style behaviour for the
    Enter key, i.e. enter key moves down. Default Value: False.

- excelStyles (boolean | number | string | dict | list; optional):
    The list of Excel styles to be used when exporting to Excel.

- excludeChildrenWhenTreeDataFiltering (boolean; optional):
    Set to True to override the default tree data filtering behaviour
    to instead exclude child nodes from filter results. See Tree Data
    Filtering. Default Value: False.

- expandOrCollapseAll (boolean | number | string | dict | list; optional):
    Fired when calling either of the API methods expandAll() or
    collapseAll().

- fillHandleDirection (string; optional):
    Set to 'x' to force the fill handle direction to horizontal, or
    set it to 'y' to force the fill handle direction to vertical
    Default Value: xy.

- filterChanged (boolean | number | string | dict | list; optional):
    Filter has been modified and applied.

- filterModified (boolean | number | string | dict | list; optional):
    Filter was modified but not applied. Used when filters have
    'Apply' buttons.

- firstDataRendered (boolean | number | string | dict | list; optional):
    Fired the first time data is rendered into the grid.

- floatingFiltersHeight (number; optional):
    The height for the row containing the floating filters. See Header
    Height. Default Value: 20.

- frameworkComponents (boolean | number | string | dict | list; optional):
    A map of component names to framework (React, Angular etc)
    components.

- fullWidthCellRenderer (boolean | number | string | dict | list; optional):
    Sets the Cell Renderer to use for Full Width Rows.

- functionsReadOnly (boolean; optional):
    If True, then row group, pivot and value aggregation will be
    read-only from the GUI. The grid will display what values are used
    for each, but will not allow the user to change the selection. See
    Read Only Functions. Default Value: False.

- getDetailRequest (dict; optional):
    Request from Dash AgGrid when suppressCallback is disabled and a
    user opens a row with a detail grid.

    `getDetailRequest` is a dict with keys:

    - data (boolean | number | string | dict | list; optional):
        Details about the row that was opened.

    - requestTime (boolean | number | string | dict | list; optional):
        Datetime representing when the grid was requested.

- getDetailResponse (boolean | number | string | dict | list; optional):
    RowData to populate the detail grid when callbacks are used to
    populate.

- getRowsRequest (dict; optional):
    Infinite Scroll, Datasource interface See
    https://www.ag-grid.com/react-grid/infinite-scrolling/#datasource-interface.

    `getRowsRequest` is a dict with keys:

    - context (boolean | number | string | dict | list; optional):
        The grid context object.

    - endRow (number; optional):
        The first row index to NOT get.

    - failCallback (optional):
        Callback to call when the request fails.

    - filterModel (boolean | number | string | dict | list; optional):
        If filtering, what the filter model is.

    - sortModel (boolean | number | string | dict | list; optional):
        If sorting, what the sort model is.

    - startRow (number; optional):
        The first row index to get.

    - successCallback (optional):
        Callback to call when the request is successful.

- getRowsResponse (dict; optional):
    Serverside model data response object. See
    https://www.ag-grid.com/react-grid/server-side-model-datasource/.

    `getRowsResponse` is a dict with keys:

    - rowCount (number; optional):
        Current row count, if known.

    - rowData (list of boolean | number | string | dict | lists; optional):
        Data retreived from the server.

    - storeInfo (boolean | number | string | dict | list; optional):
        Any extra info for the grid to associate with this load.

- gridColumnsChanged (boolean | number | string | dict | list; optional):
    The list of grid columns changed.

- gridReady (boolean | number | string | dict | list; optional):
    The grid has initialised. The name 'ready' was influenced by the
    author's time programming the Commodore 64. Use this event if, for
    example, you need to use the grid's API to fix the columns to
    size.

- gridSizeChanged (boolean | number | string | dict | list; optional):
    The size of the grid div has changed. In other words, the grid was
    resized.

- groupDefaultExpanded (number; optional):
    If grouping, set to the number of levels to expand by default,
    e.g. 0 for none, 1 for first level only, etc. Set to -1 to expand
    everything. See Removing Single Children. Default Value: 0.

- groupHeaderHeight (boolean | number | string | dict | list; optional):
    The height for the rows containing header column groups. If not
    specified, it uses headerHeight. See Header Height.

- groupHideOpenParents (boolean; optional):
    Set to True to hide parents that are open. When used with multiple
    columns for showing groups, it can give a more pleasing user
    experience. See Group Hide Open Parents. Default Value: False.

- groupIncludeFooter (boolean; optional):
    If grouping, whether to show a group footer when the group is
    expanded. If True, then by default,  the footer will contain
    aggregate data (if any) when shown and the header will be blank.
    When closed, the header will contain  the aggregate data
    regardless of this setting (as the footer is hidden anyway). This
    is handy for 'total' rows, that are  displayed below the data when
    the group is open, and alongside the group when it is closed See
    Grouping Footers. Default Value: False.

- groupIncludeTotalFooter (boolean; optional):
    Set to True to show a 'grand' total group footer across all
    groups. See Grouping Footers. Default Value: False.

- groupMultiAutoColumn (boolean; optional):
    If using auto column, set to True to have each group in its own
    separate column, e.g. if grouping by Country then Year, two auto
    columns will be created, one for Country and one for Year. See
    Multi Auto Column Group. Default Value: False.

- groupRemoveLowestSingleChildren (boolean; optional):
    Set to True to collapse lowest level groups that only have one
    child. See Remove Single Children. Default Value: False.

- groupRemoveSingleChildren (boolean; optional):
    Set to True to collapse groups that only have one child. See
    Remove Single Children. Default Value: False.

- groupRowInnerRenderer (boolean | number | string | dict | list; optional):
    Sets the inner Cell Renderer to use when groupUseEntireRow=True.
    See Row Grouping.

- groupRowRenderer (boolean | number | string | dict | list; optional):
    Sets the Cell Renderer to use when groupUseEntireRow=True. See Row
    Grouping.

- groupSelectsChildren (boolean; optional):
    When True, if you select a group, the children of the group will
    also be selected. See Group Selection. Default Value: False.

- groupSelectsFiltered (boolean; optional):
    If using groupSelectsChildren, then only the children that pass
    the current filter will get selected. See Group Selection. Default
    Value: False.

- groupSuppressAutoColumn (boolean; optional):
    If True, the grid will not swap in the grouping column when
    grouping is enabled. Use this if you want complete control on the
    column displayed and don't want the grid's help, in other words if
    you already have a column in your column definitions that is
    responsible for displaying the groups. See Configuring the Auto
    Group Column. Default Value: False.

- groupSuppressBlankHeader (boolean; optional):
    If True, and showing footer, aggregate data will be displayed at
    both the header and footer levels always. This  stops the possibly
    undesirable behaviour of the header details 'jumping' to the
    footer on expand. Default Value: False.

- groupUseEntireRow (boolean; optional):
    Used when grouping. If True, a group row will span all columns
    across the entire width of the table. If False, the cells will be
    rendered as normal and you will have the opportunity to include a
    grouping column (normally the first on the left) to show the
    group. See Full Width Group Rows. Default Value: False.

- headerHeight (number; optional):
    The height in pixels for the row containing the column label
    header. See Header Height. Default Value: 25.

- hoverData (boolean | number | string | dict | list; optional):
    Special prop used by renderers.

- icons (boolean | number | string | dict | list; optional):
    Icons to use inside the grid instead of the grid's default icons.

- immutableData (boolean | number | string | dict | list; optional):
    (Client-Side Row Model only) Enables Immutable Data mode, for
    compatibility with immutable stores.

- keepDetailRows (boolean; optional):
    Set to True to keep detail rows for when they are displayed again.
    Default Value: False.

- keepDetailRowsCount (number; optional):
    Sets the number of details rows to keep. Default Value: 10.

- layoutInterval (number; optional):
    The interval in milliseconds that the grid uses to periodically
    check its size and lay itself out again if the size has changed,
    such as when your browser changes size, or your application
    changes the size of the div element that the grid lives inside. To
    stop the periodic layout, set it to -1. Default Value: 500.

- licenseKey (string; optional):
    License key for ag-grid enterprise. If using Enterprise modules,
    enableEnterpriseModules must also be True.

- loadingOverlayComponent (boolean | number | string | dict | list; optional):
    Provide a custom loading overlay component.

- loadingOverlayComponentParams (boolean | number | string | dict | list; optional):
    Customise the parameters provided to the loading overlay
    component.

- localeText (boolean | number | string | dict | list; optional):
    A map of key->value pairs for localising text within the grid. See
    Localisation.

- masterDetail (boolean; optional):
    Used to enable Master Detail. See Enabling Master Detail. Default
    Value: False.

- maxBlocksInCache (boolean | number | string | dict | list; optional):
    Partial Store Only - how many blocks to keep in the store. Default
    is no limit, so every requested block is kept. Use this if you
    have memory concerns, and blocks that were least recently viewed
    will be purged when the limit is hit. The grid will additionally
    make sure it has all the blocks needed to display what is
    currently visible - in case this property is set to low.

- maxConcurrentDatasourceRequests (number; optional):
    How many requests to hit the server with concurrently. If the max
    is reached, requests are queued. Default Value: 1.

- modelUpdated (boolean | number | string | dict | list; optional):
    Displayed rows have changed. Triggered after sort, filter or tree
    expand / collapse events.

- multiSortKey (boolean | number | string | dict | list; optional):
    Set to 'ctrl' to have multi sorting work using the Ctrl or Command
    (for Apple) keys. See Multi Column Sorting.

- newColumnsLoaded (boolean | number | string | dict | list; optional):
    User set new columns.

- noRowsOverlayComponent (boolean | number | string | dict | list; optional):
    Provide a custom no rows overlay component.

- noRowsOverlayComponentParams (boolean | number | string | dict | list; optional):
    Customise the parameters provided to the no rows overlay
    component.

- overlayLoadingTemplate (boolean | number | string | dict | list; optional):
    Provide a template for 'loading' overlay.

- overlayNoRowsTemplate (boolean | number | string | dict | list; optional):
    Provide a template for 'no rows' overlay.

- paginateChildRows (boolean | number | string | dict | list; optional):
    Set to True to have pages split children of groups when using Row
    Grouping or detail rows with Master Detail. See Pagination & Child
    Rows.

- pagination (boolean; optional):
    Set whether Pagination is enabled. Default Value: False.

- paginationAutoPageSize (boolean; optional):
    Set to True so that the number of rows to load per page is
    automatically adjusted by AG Grid so each page shows enough rows
    to just fill the area designated for the grid. If False,
    paginationPageSize is used. See Auto Page Size. Default Value:
    False.

- paginationChanged (boolean | number | string | dict | list; optional):
    Triggered every time the paging state changes. Some of the most
    common scenarios for this event to be triggered are:The page size
    changesThe current shown page is changedNew data is loaded onto
    the grid.

- paginationPageSize (number; optional):
    How many rows to load per page. If paginationAutoPageSize is
    specified, this property is ignored. See Customising Pagination.
    Default Value: 100.

- pasteEnd (boolean | number | string | dict | list; optional):
    Paste operation has ended. See Clipboard Events.

- pasteStart (boolean | number | string | dict | list; optional):
    Paste operation has started. See Clipboard Events.

- persisted_props (list of strings; default ['selectionChanged']):
    Properties whose user interactions will persist after refreshing
    the component or the page. Since only `value` is allowed this prop
    can normally be ignored.

- persistence (boolean | string | number; optional):
    Used to allow user interactions in this component to be persisted
    when the component - or the page - is refreshed. If `persisted` is
    truthy and hasn't changed from its previous value, a `value` that
    the user has changed while using the app will keep that change, as
    long as the new `value` also matches what was given originally.
    Used in conjunction with `persistence_type`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    Where persisted user changes will be stored: memory: only kept in
    memory, reset on page refresh. local: window.localStorage, data is
    kept after the browser quit. session: window.sessionStorage, data
    is cleared once the browser quit.

- pinnedBottomRowData (boolean | number | string | dict | list; optional):
    Data to be displayed as Pinned Bottom Rows in the grid.

- pinnedRowDataChanged (boolean | number | string | dict | list; optional):
    The client has set new pinned row data into the grid.

- pinnedTopRowData (boolean | number | string | dict | list; optional):
    Data to be displayed as Pinned Top Rows in the grid.

- pivotColumnGroupTotals (boolean | number | string | dict | list; optional):
    When set and the grid is in pivot mode, automatically calculated
    totals will appear within the Pivot Column Groups,in the position
    specified. See Pivot Column Group Totals.

- pivotGroupHeaderHeight (boolean | number | string | dict | list; optional):
    The height for the row containing header column groups when in
    pivot mode. If not specified, it uses groupHeaderHeight. See
    Header Height.

- pivotHeaderHeight (boolean | number | string | dict | list; optional):
    The height for the row containing the columns when in pivot mode.
    If not specified, it uses headerHeight. See Header Height.

- pivotMode (boolean; optional):
    Set to True to enable pivot mode. See Pivoting. Default Value:
    False.

- pivotPanelShow (a value equal to: 'never', 'always', 'onlyWhenPivoting'; optional):
    When to show the 'pivot panel' (where you drag rows to pivot) at
    the top. Note that the pivot panel will never show if pivotMode is
    off. Default Value: ['never', 'always', 'onlyWhenPivoting'].

- pivotRowTotals (boolean | number | string | dict | list; optional):
    When set and the grid is in pivot mode, automatically calculated
    totals will appear for each value column in the position
    specified. See Pivot Row Totals.

- pivotSuppressAutoColumn (boolean; optional):
    If True, the grid will not swap in the grouping column when
    pivoting. Useful if pivoting using Server Side Row Model or
    Viewport Row Model and you want full control of all columns
    including the group column. Default Value: False.

- popupParent (boolean | number | string | dict | list; optional):
    DOM element to use as popup parent for grid popups (context menu,
    column menu etc).

- preventDefaultOnContextMenu (boolean; optional):
    When using suppressContextMenu, you can use the onCellContextMenu
    function to provide your own code to handle cell contextmenu
    events. This flag is useful to prevent the browser from showing
    its default context menu. Default Value: False.

- purgeClosedRowNodes (boolean | number | string | dict | list; optional):
    When enabled, closing group rows will remove children of that row.
    Next time the row is opened, child rows will be read form the
    datasoruce again. This property only applies when there is Row
    Grouping.

- quickFilterText (boolean | number | string | dict | list; optional):
    Rows are filtered using this text as a quick filter.

- rangeSelectionChanged (boolean | number | string | dict | list; optional):
    A change to range selection has occurred.

- rowBuffer (number; optional):
    The number of rows rendered outside the scrollable viewable area
    the grid renders. Having a buffer means the grid will have rows
    ready to show as the user slowly scrolls vertically. Default
    Value: 20.

- rowClass (boolean | number | string | dict | list; optional):
    The class to give a particular row. See Row Class.

- rowClassRules (boolean | number | string | dict | list; optional):
    Rules which can be applied to include certain CSS classes. See Row
    Class Rules.

- rowClicked (boolean | number | string | dict | list; optional):
    Row is clicked.

- rowData (boolean | number | string | dict | list; optional):
    (Client-Side Row Model only) Set the data to be displayed as rows
    in the grid.

- rowDataChanged (boolean | number | string | dict | list; optional):
    The client has set new data into the grid using api.setRowData()
    or by changing the rowData bound property.

- rowDataUpdated (boolean | number | string | dict | list; optional):
    The client has updated data for the grid using
    api.applyTransaction(transaction) or by changing the rowData bound
    property with immutableData=True.

- rowDoubleClicked (boolean | number | string | dict | list; optional):
    Row is double clicked.

- rowDragEnd (boolean | number | string | dict | list; optional):
    The drag has finished over the grid.

- rowDragEnter (boolean | number | string | dict | list; optional):
    A drag has started, or dragging was already started and the mouse
    has re-entered the grid having previously left the grid.

- rowDragLeave (boolean | number | string | dict | list; optional):
    The mouse has left the grid while dragging.

- rowDragManaged (boolean; optional):
    Set to True to enable Managed Row Dragging. Default Value: False.

- rowDragMove (boolean | number | string | dict | list; optional):
    The mouse has moved while dragging.

- rowEditingStarted (boolean | number | string | dict | list; optional):
    Editing a row has started (when row editing is enabled). When row
    editing, this event will be fired once and cellEditingStarted will
    be fired for each individual cell. This event corresponds to Full
    Row Editing only.

- rowEditingStopped (boolean | number | string | dict | list; optional):
    Editing a row has stopped (when row editing is enabled). When row
    editing, this event will be fired once and cellEditingStopped will
    be fired for each individual cell. This event corresponds to Full
    Row Editing only.

- rowGroupOpened (boolean | number | string | dict | list; optional):
    A row group was opened or closed.

- rowGroupPanelShow (a value equal to: 'never', 'always', 'onlyWhenGrouping'; optional):
    When to show the 'row group panel' (where you drag rows to group)
    at the top. See Column Tool Panel Example. Default Value:
    ['never', 'always', 'onlyWhenGrouping'].

- rowHeight (number; optional):
    Default Row Height in pixels. Default Value: 25.

- rowModelType (a value equal to: 'clientSide', 'infinite', 'viewport', 'serverSide'; optional):
    Sets the Row Model type. Default Value: ['clientSide', 'infinite',
    'viewport', 'serverSide'].

- rowMultiSelectWithClick (boolean; optional):
    Set to True to allow multiple rows to be selected using single
    click. See Multi Select Single Click. Default Value: False.

- rowSelected (boolean | number | string | dict | list; optional):
    Row is selected or deselected.

- rowSelection (boolean | number | string | dict | list; optional):
    Type of Row Selection.

- rowStyle (boolean | number | string | dict | list; optional):
    The style to give a particular row. See Row Style.

- rowValueChanged (boolean | number | string | dict | list; optional):
    A cell's value within a row has changed. This event corresponds to
    Full Row Editing only.

- scrollbarWidth (boolean | number | string | dict | list; optional):
    Tell the grid how wide the scrollbar is, which is used in grid
    width calculations. Set only if using non-standard
    browser-provided scrollbars, so the grid can use the non-standard
    size in its calculations.

- selectionChanged (boolean | number | string | dict | list; optional):
    Row selection is changed. Use the grid API to get the new row
    selected.

- serverSideFilteringAlwaysResets (boolean | number | string | dict | list; optional):
    When enabled, always refreshes stores after filter has changed.
    Use by Full Store only, to allow Server-Side Filtering.

- serverSideSortingAlwaysResets (boolean; optional):
    When True, a full reset will be performed when sorting using the
    Server-Side Row Model. Default Value: False.

- serverSideStoreType (a value equal to: 'full', 'partial'; optional):
    Whether to use Full Store or Partial Store for storing rows. See
    Row Stores Default Value: ['full', 'partial'].

- showOpenedGroup (boolean; optional):
    Shows the open group in the group column for non-group rows. See
    Showing Open Groups. Default Value: False.

- sideBar (boolean | a value equal to: 'columns', 'filters' | dict; optional):
    SideBar configures the properties of the grid sidebar.

- singleClickEdit (boolean; optional):
    Set to True to enable Single Click Editing for cells, to start
    editing with a single click. Default Value: False.

- skipHeaderOnAutoSize (boolean; optional):
    Set this to True to skip the headerName when autoSize is called by
    default. See Resizing Example. Default Value: False.

- sortChanged (boolean | number | string | dict | list; optional):
    Sort has changed. The grid also listens for this and updates the
    model.

- sortingOrder (boolean | number | string | dict | list; optional):
    Array defining the order in which sorting occurs (if sorting is
    enabled). Values can be 'asc', 'desc' or None. For example:
    sortingOrder: ['asc', 'desc']. See Example Sorting Order and
    Animation.

- statusBar (boolean | number | string | dict | list; optional):
    Specifies the status bar components to use in the status bar.

- stopEditingWhenGridLosesFocus (boolean; optional):
    Set this to True to  stop cell editing when grid loses focus. The
    default is the grid stays editing until focus goes onto another
    cell. For inline (non-popup) editors only. Default Value: False.

- style (dict; default {height: '400px', width: '100%'}):
    The CSS style for the component.

- suppressAggAtRootLevel (boolean; optional):
    When True, the aggregations won't be computed for root node of the
    grid. See Big Data Small Transactions. Default Value: False.

- suppressAggFilteredOnly (boolean | number | string | dict | list; optional):
    Set to True so that aggregations are not impacted by filtering.
    See Custom Aggregation Functions.

- suppressAggFuncInHeader (boolean; optional):
    When True, column headers won't include the aggFunc, e.g.
    'sum(Bank Balance)' will just be 'Bank Balance'. Default Value:
    False.

- suppressAnimationFrame (boolean; optional):
    When True, the grid will not use animation frames when drawing
    rows while scrolling. Use this if the grid is working fast enough
    that you don't need animation frames and you don't want the grid
    to flicker. Default Value: False.

- suppressAsyncEvents (boolean; optional):
    Disables the async nature of the events introduced in v10, and
    makes them synchronous. This property is only introduced for the
    purpose of supporting legacy code which has a dependency to sync
    events in earlier versions (v9 or earlier) of AG Grid. It is
    strongly recommended that you don't change this property unless
    you have legacy issues. Default Value: False.

- suppressAutoSize (boolean; optional):
    Suppresses auto-sizing columns for columns. In other words, double
    clicking a column's header's edge will not auto-size. Default
    Value: False.

- suppressBrowserResizeObserver (boolean; optional):
    The grid will check for ResizeObserver and use it if it exists in
    the browser, otherwise it will use the grid's alternative
    implementation. Some users reported issues with Chrome's
    ResizeObserver. Use this property to always use the grid's
    alternative implementation should such problems exist. Default
    Value: False.

- suppressCellSelection (boolean; optional):
    If True, cells won't be selectable. This means cells will not get
    keyboard focus when you click on them. Default Value: False.

- suppressClearOnFillReduction (boolean; optional):
    Set it to True to prevent cell values from being cleared when the
    Range Selection is reduced by the Fill Handle. Default Value:
    False.

- suppressClickEdit (boolean; optional):
    Set to True so that neither single nor double click starts
    editing. See Single Click, Double Click, No Click Editing. Default
    Value: False.

- suppressColumnMoveAnimation (boolean; optional):
    If True, the ag-column-moving class is not added to the grid while
    columns are moving. In the default themes, this results in no
    animation when moving columns. Default Value: False.

- suppressColumnVirtualisation (boolean; optional):
    Set to True so that the grid doesn't virtualise the columns. For
    example, if you have 100 columns, but only 10 visible due to
    scrolling, all 100 will always be rendered. Default Value: False.

- suppressContextMenu (boolean; optional):
    Set to True to not show context menu. Use if you don't want to use
    the default 'right click' context menu. Default Value: False.

- suppressCopyRowsToClipboard (boolean; optional):
    Set to True to only have the range selection, and not row
    selection, copied to clipboard. Default Value: False.

- suppressCsvExport (boolean; optional):
    Prevents the user from exporting the grid to CSV. Default Value:
    False.

- suppressDragLeaveHidesColumns (boolean; optional):
    If True, when you drag a column out of the grid (e.g. to the group
    zone) the column is not hidden. Default Value: False.

- suppressExcelExport (boolean; optional):
    Prevents the user from exporting the grid to Excel. Default Value:
    False.

- suppressExpandablePivotGroups (boolean; optional):
    When enabled pivot column groups will appear 'fixed', without the
    ability to expand and collapse the column groups. See Fixed Pivot
    Column Groups. Default Value: False.

- suppressFieldDotNotation (boolean; optional):
    If True, then dots in field names (e.g. address.firstline) are not
    treated as deep references. Allows you to use dots in your field
    name if you prefer. Default Value: False.

- suppressFocusAfterRefresh (boolean; optional):
    Set to True to not set focus back on the grid after a refresh.
    This can avoid issues where you want to keep the focus on another
    part of the browser. Default Value: False.

- suppressHorizontalScroll (boolean; optional):
    Set to True to never show the horizontal scroll. This is useful if
    the grid is aligned with another grid and will scroll when the
    other grid scrolls. (Show not be used in combination with
    alwaysShowHorizontalScroll) See Aligned Grid as Footer. Default
    Value: False.

- suppressLastEmptyLineOnPaste (boolean; optional):
    Set to True to work around a bug with Excel (Windows) that adds an
    extra empty line at the end of ranges copied to the clipboard.
    Default Value: False.

- suppressLoadingOverlay (boolean; optional):
    Disables the 'loading' overlay. Default Value: False.

- suppressMaintainUnsortedOrder (boolean; optional):
    Set to True to suppress sorting of un-sorted data to match
    original row data. See Big Data Small Transactions. Default Value:
    False.

- suppressMakeVisibleAfterUnGroup (boolean; optional):
    By default, when a column is un-grouped it is made visible. e.g.
    on main demo: 1) group by country by dragging (action of moving
    column out of grid means column is made visible=False); then 2)
    un-group by clicking 'x' on the country column in the column drop
    zone; the column is then made visible=True. This property stops
    the column becoming visible again when un-grouping. Default Value:
    False.

- suppressMaxRenderedRowRestriction (boolean; optional):
    By default the grid has a limit of rendering a maximum of 500 rows
    at once (remember the grid only renders rows you can see, so
    unless your display shows more than 500 rows without vertically
    scrolling this will never be an issue). Default Value: False.

- suppressMenuHide (boolean; optional):
    Set to True to always show the column menu button, rather than
    only showing when the mouse is over the column header. Default
    Value: False.

- suppressMiddleClickScrolls (boolean; optional):
    If True, then middle clicks will result in click events for cell
    and row. Otherwise the browser will use middle click to scroll the
    grid. Default Value: False.

- suppressModelUpdateAfterUpdateTransaction (boolean | number | string | dict | list; optional):
    ( only) Prevents Transactions changing sort, filter, group or
    pivot state when transaction only contains updates.

- suppressMovableColumns (boolean; optional):
    Set to True to suppress column moving, i.e. to make the columns
    fixed position. Default Value: False.

- suppressMoveWhenRowDragging (boolean; optional):
    Set to True to suppress moving rows while dragging the rowDrag
    waffle. This option highlights the position where the row will be
    placed and it will only move the row on mouse up. See Row
    Dragging. Default Value: False.

- suppressMultiSort (boolean; optional):
    Set to True to suppress multi-sort when the user shift-clicks a
    column header. Default Value: False.

- suppressNoRowsOverlay (boolean; optional):
    Disables the 'no rows' overlay. Default Value: False.

- suppressPaginationPanel (boolean; optional):
    If True, the default AG Grid controls for navigation are hidden.
    This is useful if pagination=True and you want to provide your own
    pagination controls. Otherwise, when pagination=True the grid
    automatically shows the necessary controls at the bottom so that
    the user can navigate through the different pages. See Custom
    Pagination Controls. Default Value: False.

- suppressParentsInRowNodes (boolean; optional):
    If True, rowNodes don't get their parents set. The grid doesn't
    use the parent reference, but it is included to help the client
    code navigate the node tree if it wants by providing bi-direction
    navigation up and down the tree. If this is a problem (e.g. if you
    need to convert the tree to JSON, which does not allow cyclic
    dependencies) then set this to True. Default Value: False.

- suppressPreventDefaultOnMouseWheel (boolean; optional):
    If True, mouse wheel events will be passed to the browser. Useful
    if your grid has no vertical scrolls and you want the mouse to
    scroll the browser page. Default Value: False.

- suppressPropertyNamesCheck (boolean; optional):
    Disables showing a warning message in the console if using a
    gridOptions or colDef property that doesn't exist. Default Value:
    False.

- suppressRowClickSelection (boolean; optional):
    If True, row selection won't happen when rows are clicked. Use
    when you want checkbox selection exclusively. Default Value:
    False.

- suppressRowDeselection (boolean; optional):
    If True then rows will not be deselected if you hold down Ctrl and
    click the row or press Space. Default Value: False.

- suppressRowDrag (boolean; optional):
    Set to True to suppress Row Dragging. Default Value: False.

- suppressRowHoverHighlight (boolean; optional):
    Set to True to not highlight rows by adding the ag-row-hover CSS
    class. Default Value: False.

- suppressRowTransform (boolean; optional):
    Uses CSS top instead of CSS transform for positioning rows. Useful
    if the transform function is causing issues such as used in row
    spanning. Default Value: False.

- suppressRowVirtualisation (boolean | number | string | dict | list; optional):
    There is no such property as suppressRowVirtualisation - if you
    want to do this, then set the rowBuffer property to be very large,
    e.g. 9999. Warning: lots of rendered rows will mean a very large
    amount of rendering in the DOM which will slow things down.

- suppressScrollOnNewData (boolean; optional):
    When True, the grid will not scroll to the top when new row data
    is provided. Use this if you don't want the default behaviour of
    scrolling to the top every time you load new data. Default Value:
    False.

- suppressTouch (boolean; optional):
    Disables touch support (but does not remove the browser's efforts
    to simulate mouse events on touch). Default Value: False.

- theme (a value equal to: 'alpine', 'balham', 'material', 'bootstrap'; default 'alpine'):
    The ag-grid provided theme to use. More info here:
    https://www.ag-grid.com/javascript-grid/themes-provided/.

- toolPanelVisibleChanged (boolean | number | string | dict | list; optional):
    The tool panel was hidden or shown. Use api.isToolPanelShowing()
    to get status.

- tooltipMouseTrack (boolean; optional):
    Set to True to have tooltips follow the cursor once they are
    displayed. Default Value: False.

- tooltipShowDelay (number; optional):
    The delay in milliseconds that it takes for tooltips to show up
    once an element is hovered. Default Value: 2000.

- unSortIcon (boolean; optional):
    Set to True to show the 'no sort' icon. See Example Custom
    Sorting. Default Value: False.

- valueCache (boolean; optional):
    Set to True to turn on the value cache. Default Value: False.

- valueCacheNeverExpires (boolean; optional):
    Set to True to set value cache to not expire after data updates.
    Default Value: False.

- viewportChanged (boolean | number | string | dict | list; optional):
    Which rows are rendered in the DOM has changed.

- viewportDatasource (boolean | number | string | dict | list; optional):
    To use the viewport row model you provide the grid with a
    viewportDatasource. See Viewport.

- viewportRowModelBufferSize (boolean | number | string | dict | list; optional):
    When using viewport row model, sets the buffer size for the
    viewport.

- viewportRowModelPageSize (boolean | number | string | dict | list; optional):
    When using viewport row model, sets the pages size for the
    viewport.

- virtualColumnsChanged (boolean | number | string | dict | list; optional):
    The list of rendered columns changed (only columns in the visible
    scrolled viewport are rendered by default).

- virtualRowData (boolean | number | string | dict | list; optional):
    The rowData in the grid after inline filters are applied.

- virtualRowRemoved (boolean | number | string | dict | list; optional):
    A row was removed from the DOM, for any reason. Use to clean up
    resources (if any) used by the row."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, enableResetColumnState=Component.UNDEFINED, enableExportDataAsCsv=Component.UNDEFINED, csvExportParams=Component.UNDEFINED, columnSize=Component.UNDEFINED, theme=Component.UNDEFINED, cellStyle=Component.UNDEFINED, getRowsRequest=Component.UNDEFINED, getDetailRequest=Component.UNDEFINED, getDetailResponse=Component.UNDEFINED, clickData=Component.UNDEFINED, hoverData=Component.UNDEFINED, getRowsResponse=Component.UNDEFINED, licenseKey=Component.UNDEFINED, enableEnterpriseModules=Component.UNDEFINED, virtualRowData=Component.UNDEFINED, columnDefs=Component.UNDEFINED, defaultColDef=Component.UNDEFINED, defaultColGroupDef=Component.UNDEFINED, columnTypes=Component.UNDEFINED, colResizeDefault=Component.UNDEFINED, suppressAutoSize=Component.UNDEFINED, autoSizePadding=Component.UNDEFINED, skipHeaderOnAutoSize=Component.UNDEFINED, suppressColumnMoveAnimation=Component.UNDEFINED, suppressMovableColumns=Component.UNDEFINED, suppressFieldDotNotation=Component.UNDEFINED, unSortIcon=Component.UNDEFINED, suppressMultiSort=Component.UNDEFINED, suppressMenuHide=Component.UNDEFINED, autoGroupColumnDef=Component.UNDEFINED, allowDragFromColumnsToolPanel=Component.UNDEFINED, applyColumnDefOrder=Component.UNDEFINED, quickFilterText=Component.UNDEFINED, cacheQuickFilter=Component.UNDEFINED, sortingOrder=Component.UNDEFINED, accentedSort=Component.UNDEFINED, multiSortKey=Component.UNDEFINED, suppressMaintainUnsortedOrder=Component.UNDEFINED, excludeChildrenWhenTreeDataFiltering=Component.UNDEFINED, rowSelection=Component.UNDEFINED, rowMultiSelectWithClick=Component.UNDEFINED, suppressRowDeselection=Component.UNDEFINED, suppressRowClickSelection=Component.UNDEFINED, suppressCellSelection=Component.UNDEFINED, enableRangeSelection=Component.UNDEFINED, enableRangeHandle=Component.UNDEFINED, enableFillHandle=Component.UNDEFINED, fillHandleDirection=Component.UNDEFINED, suppressClearOnFillReduction=Component.UNDEFINED, rowDragManaged=Component.UNDEFINED, suppressRowDrag=Component.UNDEFINED, suppressMoveWhenRowDragging=Component.UNDEFINED, singleClickEdit=Component.UNDEFINED, suppressClickEdit=Component.UNDEFINED, editType=Component.UNDEFINED, enableCellChangeFlash=Component.UNDEFINED, cellFlashDelay=Component.UNDEFINED, cellFadeDelay=Component.UNDEFINED, allowShowChangeAfterFilter=Component.UNDEFINED, stopEditingWhenGridLosesFocus=Component.UNDEFINED, enterMovesDown=Component.UNDEFINED, headerHeight=Component.UNDEFINED, groupHeaderHeight=Component.UNDEFINED, floatingFiltersHeight=Component.UNDEFINED, pivotHeaderHeight=Component.UNDEFINED, pivotGroupHeaderHeight=Component.UNDEFINED, groupUseEntireRow=Component.UNDEFINED, groupDefaultExpanded=Component.UNDEFINED, groupSuppressAutoColumn=Component.UNDEFINED, groupMultiAutoColumn=Component.UNDEFINED, groupSelectsChildren=Component.UNDEFINED, groupIncludeFooter=Component.UNDEFINED, groupIncludeTotalFooter=Component.UNDEFINED, groupSuppressBlankHeader=Component.UNDEFINED, groupSelectsFiltered=Component.UNDEFINED, showOpenedGroup=Component.UNDEFINED, groupRemoveSingleChildren=Component.UNDEFINED, groupRemoveLowestSingleChildren=Component.UNDEFINED, groupHideOpenParents=Component.UNDEFINED, rowGroupPanelShow=Component.UNDEFINED, pivotMode=Component.UNDEFINED, pivotPanelShow=Component.UNDEFINED, suppressAggFuncInHeader=Component.UNDEFINED, suppressAggAtRootLevel=Component.UNDEFINED, aggregateOnlyChangedColumns=Component.UNDEFINED, functionsReadOnly=Component.UNDEFINED, aggFuncs=Component.UNDEFINED, suppressAggFilteredOnly=Component.UNDEFINED, suppressMakeVisibleAfterUnGroup=Component.UNDEFINED, pivotColumnGroupTotals=Component.UNDEFINED, pivotRowTotals=Component.UNDEFINED, suppressExpandablePivotGroups=Component.UNDEFINED, pivotSuppressAutoColumn=Component.UNDEFINED, rowModelType=Component.UNDEFINED, rowData=Component.UNDEFINED, immutableData=Component.UNDEFINED, suppressModelUpdateAfterUpdateTransaction=Component.UNDEFINED, pinnedTopRowData=Component.UNDEFINED, pinnedBottomRowData=Component.UNDEFINED, serverSideStoreType=Component.UNDEFINED, cacheBlockSize=Component.UNDEFINED, cacheOverflowSize=Component.UNDEFINED, maxBlocksInCache=Component.UNDEFINED, maxConcurrentDatasourceRequests=Component.UNDEFINED, blockLoadDebounceMillis=Component.UNDEFINED, purgeClosedRowNodes=Component.UNDEFINED, serverSideFilteringAlwaysResets=Component.UNDEFINED, viewportRowModelPageSize=Component.UNDEFINED, viewportRowModelBufferSize=Component.UNDEFINED, viewportDatasource=Component.UNDEFINED, alwaysShowHorizontalScroll=Component.UNDEFINED, alwaysShowVerticalScroll=Component.UNDEFINED, debounceVerticalScrollbar=Component.UNDEFINED, suppressHorizontalScroll=Component.UNDEFINED, suppressColumnVirtualisation=Component.UNDEFINED, suppressRowVirtualisation=Component.UNDEFINED, suppressMaxRenderedRowRestriction=Component.UNDEFINED, suppressScrollOnNewData=Component.UNDEFINED, suppressAnimationFrame=Component.UNDEFINED, pagination=Component.UNDEFINED, paginationPageSize=Component.UNDEFINED, paginationAutoPageSize=Component.UNDEFINED, suppressPaginationPanel=Component.UNDEFINED, paginateChildRows=Component.UNDEFINED, groupRowRenderer=Component.UNDEFINED, groupRowInnerRenderer=Component.UNDEFINED, fullWidthCellRenderer=Component.UNDEFINED, masterDetail=Component.UNDEFINED, detailCellRendererParams=Component.UNDEFINED, keepDetailRows=Component.UNDEFINED, keepDetailRowsCount=Component.UNDEFINED, detailRowHeight=Component.UNDEFINED, detailRowAutoHeight=Component.UNDEFINED, icons=Component.UNDEFINED, rowHeight=Component.UNDEFINED, animateRows=Component.UNDEFINED, rowStyle=Component.UNDEFINED, rowClass=Component.UNDEFINED, rowClassRules=Component.UNDEFINED, excelStyles=Component.UNDEFINED, scrollbarWidth=Component.UNDEFINED, suppressRowHoverHighlight=Component.UNDEFINED, suppressCopyRowsToClipboard=Component.UNDEFINED, copyHeadersToClipboard=Component.UNDEFINED, clipboardDeliminator=Component.UNDEFINED, suppressFocusAfterRefresh=Component.UNDEFINED, suppressLastEmptyLineOnPaste=Component.UNDEFINED, enableCellTextSelection=Component.UNDEFINED, localeText=Component.UNDEFINED, suppressLoadingOverlay=Component.UNDEFINED, suppressNoRowsOverlay=Component.UNDEFINED, overlayLoadingTemplate=Component.UNDEFINED, overlayNoRowsTemplate=Component.UNDEFINED, loadingOverlayComponent=Component.UNDEFINED, loadingOverlayComponentParams=Component.UNDEFINED, noRowsOverlayComponent=Component.UNDEFINED, noRowsOverlayComponentParams=Component.UNDEFINED, enableCharts=Component.UNDEFINED, chartThemes=Component.UNDEFINED, customChartThemes=Component.UNDEFINED, chartThemeOverrides=Component.UNDEFINED, components=Component.UNDEFINED, frameworkComponents=Component.UNDEFINED, popupParent=Component.UNDEFINED, valueCache=Component.UNDEFINED, valueCacheNeverExpires=Component.UNDEFINED, defaultExportParams=Component.UNDEFINED, suppressMiddleClickScrolls=Component.UNDEFINED, suppressPreventDefaultOnMouseWheel=Component.UNDEFINED, enableBrowserTooltips=Component.UNDEFINED, tooltipShowDelay=Component.UNDEFINED, tooltipMouseTrack=Component.UNDEFINED, enableCellExpressions=Component.UNDEFINED, domLayout=Component.UNDEFINED, ensureDomOrder=Component.UNDEFINED, rowBuffer=Component.UNDEFINED, alignedGrids=Component.UNDEFINED, suppressParentsInRowNodes=Component.UNDEFINED, suppressDragLeaveHidesColumns=Component.UNDEFINED, layoutInterval=Component.UNDEFINED, enableRtl=Component.UNDEFINED, debug=Component.UNDEFINED, context=Component.UNDEFINED, suppressContextMenu=Component.UNDEFINED, preventDefaultOnContextMenu=Component.UNDEFINED, allowContextMenuWithControlKey=Component.UNDEFINED, statusBar=Component.UNDEFINED, suppressTouch=Component.UNDEFINED, suppressAsyncEvents=Component.UNDEFINED, suppressCsvExport=Component.UNDEFINED, suppressExcelExport=Component.UNDEFINED, asyncTransactionWaitMillis=Component.UNDEFINED, suppressPropertyNamesCheck=Component.UNDEFINED, suppressRowTransform=Component.UNDEFINED, serverSideSortingAlwaysResets=Component.UNDEFINED, suppressBrowserResizeObserver=Component.UNDEFINED, cellClicked=Component.UNDEFINED, cellDoubleClicked=Component.UNDEFINED, cellFocused=Component.UNDEFINED, cellMouseOver=Component.UNDEFINED, cellMouseOut=Component.UNDEFINED, cellMouseDown=Component.UNDEFINED, rowClicked=Component.UNDEFINED, rowDoubleClicked=Component.UNDEFINED, rowSelected=Component.UNDEFINED, selectionChanged=Component.UNDEFINED, cellContextMenu=Component.UNDEFINED, rangeSelectionChanged=Component.UNDEFINED, cellValueChanged=Component.UNDEFINED, rowValueChanged=Component.UNDEFINED, cellEditingStarted=Component.UNDEFINED, cellEditingStopped=Component.UNDEFINED, rowEditingStarted=Component.UNDEFINED, rowEditingStopped=Component.UNDEFINED, pasteStart=Component.UNDEFINED, pasteEnd=Component.UNDEFINED, sortChanged=Component.UNDEFINED, filterChanged=Component.UNDEFINED, filterModified=Component.UNDEFINED, rowDragEnter=Component.UNDEFINED, rowDragMove=Component.UNDEFINED, rowDragLeave=Component.UNDEFINED, rowDragEnd=Component.UNDEFINED, columnVisible=Component.UNDEFINED, columnPinned=Component.UNDEFINED, columnResized=Component.UNDEFINED, columnMoved=Component.UNDEFINED, columnRowGroupChanged=Component.UNDEFINED, columnValueChanged=Component.UNDEFINED, columnPivotModeChanged=Component.UNDEFINED, columnPivotChanged=Component.UNDEFINED, columnGroupOpened=Component.UNDEFINED, newColumnsLoaded=Component.UNDEFINED, gridColumnsChanged=Component.UNDEFINED, displayedColumnsChanged=Component.UNDEFINED, virtualColumnsChanged=Component.UNDEFINED, columnEverythingChanged=Component.UNDEFINED, gridReady=Component.UNDEFINED, gridSizeChanged=Component.UNDEFINED, modelUpdated=Component.UNDEFINED, firstDataRendered=Component.UNDEFINED, rowGroupOpened=Component.UNDEFINED, expandOrCollapseAll=Component.UNDEFINED, paginationChanged=Component.UNDEFINED, pinnedRowDataChanged=Component.UNDEFINED, virtualRowRemoved=Component.UNDEFINED, viewportChanged=Component.UNDEFINED, bodyScroll=Component.UNDEFINED, dragStarted=Component.UNDEFINED, dragStopped=Component.UNDEFINED, rowDataChanged=Component.UNDEFINED, rowDataUpdated=Component.UNDEFINED, toolPanelVisibleChanged=Component.UNDEFINED, componentStateChanged=Component.UNDEFINED, animationQueueEmpty=Component.UNDEFINED, AsyncTransactionsFlushed=Component.UNDEFINED, cellKeyDown=Component.UNDEFINED, cellKeyPress=Component.UNDEFINED, sideBar=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'AsyncTransactionsFlushed', 'accentedSort', 'aggFuncs', 'aggregateOnlyChangedColumns', 'alignedGrids', 'allowContextMenuWithControlKey', 'allowDragFromColumnsToolPanel', 'allowShowChangeAfterFilter', 'alwaysShowHorizontalScroll', 'alwaysShowVerticalScroll', 'animateRows', 'animationQueueEmpty', 'applyColumnDefOrder', 'asyncTransactionWaitMillis', 'autoGroupColumnDef', 'autoSizePadding', 'blockLoadDebounceMillis', 'bodyScroll', 'cacheBlockSize', 'cacheOverflowSize', 'cacheQuickFilter', 'cellClicked', 'cellContextMenu', 'cellDoubleClicked', 'cellEditingStarted', 'cellEditingStopped', 'cellFadeDelay', 'cellFlashDelay', 'cellFocused', 'cellKeyDown', 'cellKeyPress', 'cellMouseDown', 'cellMouseOut', 'cellMouseOver', 'cellStyle', 'cellValueChanged', 'chartThemeOverrides', 'chartThemes', 'clickData', 'clipboardDeliminator', 'colResizeDefault', 'columnDefs', 'columnEverythingChanged', 'columnGroupOpened', 'columnMoved', 'columnPinned', 'columnPivotChanged', 'columnPivotModeChanged', 'columnResized', 'columnRowGroupChanged', 'columnSize', 'columnTypes', 'columnValueChanged', 'columnVisible', 'componentStateChanged', 'components', 'context', 'copyHeadersToClipboard', 'csvExportParams', 'customChartThemes', 'debounceVerticalScrollbar', 'debug', 'defaultColDef', 'defaultColGroupDef', 'defaultExportParams', 'detailCellRendererParams', 'detailRowAutoHeight', 'detailRowHeight', 'displayedColumnsChanged', 'domLayout', 'dragStarted', 'dragStopped', 'editType', 'enableBrowserTooltips', 'enableCellChangeFlash', 'enableCellExpressions', 'enableCellTextSelection', 'enableCharts', 'enableEnterpriseModules', 'enableExportDataAsCsv', 'enableFillHandle', 'enableRangeHandle', 'enableRangeSelection', 'enableResetColumnState', 'enableRtl', 'ensureDomOrder', 'enterMovesDown', 'excelStyles', 'excludeChildrenWhenTreeDataFiltering', 'expandOrCollapseAll', 'fillHandleDirection', 'filterChanged', 'filterModified', 'firstDataRendered', 'floatingFiltersHeight', 'frameworkComponents', 'fullWidthCellRenderer', 'functionsReadOnly', 'getDetailRequest', 'getDetailResponse', 'getRowsRequest', 'getRowsResponse', 'gridColumnsChanged', 'gridReady', 'gridSizeChanged', 'groupDefaultExpanded', 'groupHeaderHeight', 'groupHideOpenParents', 'groupIncludeFooter', 'groupIncludeTotalFooter', 'groupMultiAutoColumn', 'groupRemoveLowestSingleChildren', 'groupRemoveSingleChildren', 'groupRowInnerRenderer', 'groupRowRenderer', 'groupSelectsChildren', 'groupSelectsFiltered', 'groupSuppressAutoColumn', 'groupSuppressBlankHeader', 'groupUseEntireRow', 'headerHeight', 'hoverData', 'icons', 'immutableData', 'keepDetailRows', 'keepDetailRowsCount', 'layoutInterval', 'licenseKey', 'loadingOverlayComponent', 'loadingOverlayComponentParams', 'localeText', 'masterDetail', 'maxBlocksInCache', 'maxConcurrentDatasourceRequests', 'modelUpdated', 'multiSortKey', 'newColumnsLoaded', 'noRowsOverlayComponent', 'noRowsOverlayComponentParams', 'overlayLoadingTemplate', 'overlayNoRowsTemplate', 'paginateChildRows', 'pagination', 'paginationAutoPageSize', 'paginationChanged', 'paginationPageSize', 'pasteEnd', 'pasteStart', 'persisted_props', 'persistence', 'persistence_type', 'pinnedBottomRowData', 'pinnedRowDataChanged', 'pinnedTopRowData', 'pivotColumnGroupTotals', 'pivotGroupHeaderHeight', 'pivotHeaderHeight', 'pivotMode', 'pivotPanelShow', 'pivotRowTotals', 'pivotSuppressAutoColumn', 'popupParent', 'preventDefaultOnContextMenu', 'purgeClosedRowNodes', 'quickFilterText', 'rangeSelectionChanged', 'rowBuffer', 'rowClass', 'rowClassRules', 'rowClicked', 'rowData', 'rowDataChanged', 'rowDataUpdated', 'rowDoubleClicked', 'rowDragEnd', 'rowDragEnter', 'rowDragLeave', 'rowDragManaged', 'rowDragMove', 'rowEditingStarted', 'rowEditingStopped', 'rowGroupOpened', 'rowGroupPanelShow', 'rowHeight', 'rowModelType', 'rowMultiSelectWithClick', 'rowSelected', 'rowSelection', 'rowStyle', 'rowValueChanged', 'scrollbarWidth', 'selectionChanged', 'serverSideFilteringAlwaysResets', 'serverSideSortingAlwaysResets', 'serverSideStoreType', 'showOpenedGroup', 'sideBar', 'singleClickEdit', 'skipHeaderOnAutoSize', 'sortChanged', 'sortingOrder', 'statusBar', 'stopEditingWhenGridLosesFocus', 'style', 'suppressAggAtRootLevel', 'suppressAggFilteredOnly', 'suppressAggFuncInHeader', 'suppressAnimationFrame', 'suppressAsyncEvents', 'suppressAutoSize', 'suppressBrowserResizeObserver', 'suppressCellSelection', 'suppressClearOnFillReduction', 'suppressClickEdit', 'suppressColumnMoveAnimation', 'suppressColumnVirtualisation', 'suppressContextMenu', 'suppressCopyRowsToClipboard', 'suppressCsvExport', 'suppressDragLeaveHidesColumns', 'suppressExcelExport', 'suppressExpandablePivotGroups', 'suppressFieldDotNotation', 'suppressFocusAfterRefresh', 'suppressHorizontalScroll', 'suppressLastEmptyLineOnPaste', 'suppressLoadingOverlay', 'suppressMaintainUnsortedOrder', 'suppressMakeVisibleAfterUnGroup', 'suppressMaxRenderedRowRestriction', 'suppressMenuHide', 'suppressMiddleClickScrolls', 'suppressModelUpdateAfterUpdateTransaction', 'suppressMovableColumns', 'suppressMoveWhenRowDragging', 'suppressMultiSort', 'suppressNoRowsOverlay', 'suppressPaginationPanel', 'suppressParentsInRowNodes', 'suppressPreventDefaultOnMouseWheel', 'suppressPropertyNamesCheck', 'suppressRowClickSelection', 'suppressRowDeselection', 'suppressRowDrag', 'suppressRowHoverHighlight', 'suppressRowTransform', 'suppressRowVirtualisation', 'suppressScrollOnNewData', 'suppressTouch', 'theme', 'toolPanelVisibleChanged', 'tooltipMouseTrack', 'tooltipShowDelay', 'unSortIcon', 'valueCache', 'valueCacheNeverExpires', 'viewportChanged', 'viewportDatasource', 'viewportRowModelBufferSize', 'viewportRowModelPageSize', 'virtualColumnsChanged', 'virtualRowData', 'virtualRowRemoved']
        self._type = 'AgGrid'
        self._namespace = 'dash_ag_grid'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'AsyncTransactionsFlushed', 'accentedSort', 'aggFuncs', 'aggregateOnlyChangedColumns', 'alignedGrids', 'allowContextMenuWithControlKey', 'allowDragFromColumnsToolPanel', 'allowShowChangeAfterFilter', 'alwaysShowHorizontalScroll', 'alwaysShowVerticalScroll', 'animateRows', 'animationQueueEmpty', 'applyColumnDefOrder', 'asyncTransactionWaitMillis', 'autoGroupColumnDef', 'autoSizePadding', 'blockLoadDebounceMillis', 'bodyScroll', 'cacheBlockSize', 'cacheOverflowSize', 'cacheQuickFilter', 'cellClicked', 'cellContextMenu', 'cellDoubleClicked', 'cellEditingStarted', 'cellEditingStopped', 'cellFadeDelay', 'cellFlashDelay', 'cellFocused', 'cellKeyDown', 'cellKeyPress', 'cellMouseDown', 'cellMouseOut', 'cellMouseOver', 'cellStyle', 'cellValueChanged', 'chartThemeOverrides', 'chartThemes', 'clickData', 'clipboardDeliminator', 'colResizeDefault', 'columnDefs', 'columnEverythingChanged', 'columnGroupOpened', 'columnMoved', 'columnPinned', 'columnPivotChanged', 'columnPivotModeChanged', 'columnResized', 'columnRowGroupChanged', 'columnSize', 'columnTypes', 'columnValueChanged', 'columnVisible', 'componentStateChanged', 'components', 'context', 'copyHeadersToClipboard', 'csvExportParams', 'customChartThemes', 'debounceVerticalScrollbar', 'debug', 'defaultColDef', 'defaultColGroupDef', 'defaultExportParams', 'detailCellRendererParams', 'detailRowAutoHeight', 'detailRowHeight', 'displayedColumnsChanged', 'domLayout', 'dragStarted', 'dragStopped', 'editType', 'enableBrowserTooltips', 'enableCellChangeFlash', 'enableCellExpressions', 'enableCellTextSelection', 'enableCharts', 'enableEnterpriseModules', 'enableExportDataAsCsv', 'enableFillHandle', 'enableRangeHandle', 'enableRangeSelection', 'enableResetColumnState', 'enableRtl', 'ensureDomOrder', 'enterMovesDown', 'excelStyles', 'excludeChildrenWhenTreeDataFiltering', 'expandOrCollapseAll', 'fillHandleDirection', 'filterChanged', 'filterModified', 'firstDataRendered', 'floatingFiltersHeight', 'frameworkComponents', 'fullWidthCellRenderer', 'functionsReadOnly', 'getDetailRequest', 'getDetailResponse', 'getRowsRequest', 'getRowsResponse', 'gridColumnsChanged', 'gridReady', 'gridSizeChanged', 'groupDefaultExpanded', 'groupHeaderHeight', 'groupHideOpenParents', 'groupIncludeFooter', 'groupIncludeTotalFooter', 'groupMultiAutoColumn', 'groupRemoveLowestSingleChildren', 'groupRemoveSingleChildren', 'groupRowInnerRenderer', 'groupRowRenderer', 'groupSelectsChildren', 'groupSelectsFiltered', 'groupSuppressAutoColumn', 'groupSuppressBlankHeader', 'groupUseEntireRow', 'headerHeight', 'hoverData', 'icons', 'immutableData', 'keepDetailRows', 'keepDetailRowsCount', 'layoutInterval', 'licenseKey', 'loadingOverlayComponent', 'loadingOverlayComponentParams', 'localeText', 'masterDetail', 'maxBlocksInCache', 'maxConcurrentDatasourceRequests', 'modelUpdated', 'multiSortKey', 'newColumnsLoaded', 'noRowsOverlayComponent', 'noRowsOverlayComponentParams', 'overlayLoadingTemplate', 'overlayNoRowsTemplate', 'paginateChildRows', 'pagination', 'paginationAutoPageSize', 'paginationChanged', 'paginationPageSize', 'pasteEnd', 'pasteStart', 'persisted_props', 'persistence', 'persistence_type', 'pinnedBottomRowData', 'pinnedRowDataChanged', 'pinnedTopRowData', 'pivotColumnGroupTotals', 'pivotGroupHeaderHeight', 'pivotHeaderHeight', 'pivotMode', 'pivotPanelShow', 'pivotRowTotals', 'pivotSuppressAutoColumn', 'popupParent', 'preventDefaultOnContextMenu', 'purgeClosedRowNodes', 'quickFilterText', 'rangeSelectionChanged', 'rowBuffer', 'rowClass', 'rowClassRules', 'rowClicked', 'rowData', 'rowDataChanged', 'rowDataUpdated', 'rowDoubleClicked', 'rowDragEnd', 'rowDragEnter', 'rowDragLeave', 'rowDragManaged', 'rowDragMove', 'rowEditingStarted', 'rowEditingStopped', 'rowGroupOpened', 'rowGroupPanelShow', 'rowHeight', 'rowModelType', 'rowMultiSelectWithClick', 'rowSelected', 'rowSelection', 'rowStyle', 'rowValueChanged', 'scrollbarWidth', 'selectionChanged', 'serverSideFilteringAlwaysResets', 'serverSideSortingAlwaysResets', 'serverSideStoreType', 'showOpenedGroup', 'sideBar', 'singleClickEdit', 'skipHeaderOnAutoSize', 'sortChanged', 'sortingOrder', 'statusBar', 'stopEditingWhenGridLosesFocus', 'style', 'suppressAggAtRootLevel', 'suppressAggFilteredOnly', 'suppressAggFuncInHeader', 'suppressAnimationFrame', 'suppressAsyncEvents', 'suppressAutoSize', 'suppressBrowserResizeObserver', 'suppressCellSelection', 'suppressClearOnFillReduction', 'suppressClickEdit', 'suppressColumnMoveAnimation', 'suppressColumnVirtualisation', 'suppressContextMenu', 'suppressCopyRowsToClipboard', 'suppressCsvExport', 'suppressDragLeaveHidesColumns', 'suppressExcelExport', 'suppressExpandablePivotGroups', 'suppressFieldDotNotation', 'suppressFocusAfterRefresh', 'suppressHorizontalScroll', 'suppressLastEmptyLineOnPaste', 'suppressLoadingOverlay', 'suppressMaintainUnsortedOrder', 'suppressMakeVisibleAfterUnGroup', 'suppressMaxRenderedRowRestriction', 'suppressMenuHide', 'suppressMiddleClickScrolls', 'suppressModelUpdateAfterUpdateTransaction', 'suppressMovableColumns', 'suppressMoveWhenRowDragging', 'suppressMultiSort', 'suppressNoRowsOverlay', 'suppressPaginationPanel', 'suppressParentsInRowNodes', 'suppressPreventDefaultOnMouseWheel', 'suppressPropertyNamesCheck', 'suppressRowClickSelection', 'suppressRowDeselection', 'suppressRowDrag', 'suppressRowHoverHighlight', 'suppressRowTransform', 'suppressRowVirtualisation', 'suppressScrollOnNewData', 'suppressTouch', 'theme', 'toolPanelVisibleChanged', 'tooltipMouseTrack', 'tooltipShowDelay', 'unSortIcon', 'valueCache', 'valueCacheNeverExpires', 'viewportChanged', 'viewportDatasource', 'viewportRowModelBufferSize', 'viewportRowModelPageSize', 'virtualColumnsChanged', 'virtualRowData', 'virtualRowRemoved']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AgGrid, self).__init__(children=children, **args)
