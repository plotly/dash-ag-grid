# AUTO GENERATED FILE - DO NOT EDIT

export aggrid

"""
    aggrid(;kwargs...)
    aggrid(children::Any;kwargs...)
    aggrid(children_maker::Function;kwargs...)


An AgGrid component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The children of this component
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `AsyncTransactionsFlushed` (Bool | Real | String | Dict | Array; optional): Async transactions have been applied. Contains a list of all transaction results.
- `accentedSort` (Bool; optional): Set to true to specify that the sort should take into account accented characters.
If this feature is turned on the sort will perform slower. See Accented Sort.
Default Value: false
- `aggFuncs` (Bool | Real | String | Dict | Array; optional): A map of 'function name' to 'function' for custom aggregation functions. See Custom
Aggregation Functions.
- `aggregateOnlyChangedColumns` (Bool; optional): When using change detection, only the updated column with get re-aggregated.
Default Value: false
- `alignedGrids` (Bool | Real | String | Dict | Array; optional): A list of grids to treat as Aligned Grids. If grids are aligned then the columns
and horizontal scrolling will be kept in sync.
- `allowContextMenuWithControlKey` (Bool | Real | String | Dict | Array; optional): Allows context menu to show, even when Ctrl key is held down.
- `allowDragFromColumnsToolPanel` (Bool; optional): Allow reordering and pinning columns by dragging columns from the columns tool
panel to the grid.
Default Value: false
- `allowShowChangeAfterFilter` (Bool; optional): Set to true to have cells flash after data changes even when the change is due
to filtering. See Flashing Data Changes.
Default Value: false
- `alwaysShowHorizontalScroll` (Bool; optional): Set to true to always show the horizontal scrollbar.
Default Value: false
- `alwaysShowVerticalScroll` (Bool; optional): Set to true to always show the vertical scrollbar.
Default Value: false
- `animateRows` (Bool; optional): Set to true to enable Row Animation.
Default Value: false
- `animationQueueEmpty` (Bool | Real | String | Dict | Array; optional): The grid draws rows and cells using animation frames. This event gets fired when
the animation frame queue is empty. Normally used in conjunction with api.isAnimationFrameQueueEmpty()
so user can check if animation frame is pending, and if so then can be notified
when no animation frames are pending. Useful if your application needs to know
when drawing of the grid is no longer pending, e.g. for sending to a printer.
- `applyColumnDefOrder` (Bool; optional): Sorts the grid columns in the order of Column Definitions after Column Definitions
are updated. See Apply Column Order.
Default Value: false
- `asyncTransactionWaitMillis` (Bool | Real | String | Dict | Array; optional): How many milliseconds to wait before executing a batch of async transactions.
- `autoGroupColumnDef` (Bool | Real | String | Dict | Array; optional): Allows specifying the group 'auto column' if you are not happy with the default.
If grouping, this column def is included as the first column definition in the
grid. If not grouping, this column is not included.
- `autoSizePadding` (Real; optional): Number of pixels to add to a column width after the auto-sizing calculation. Set
this if you want to add extra room to accommodate (for example) sort icons, or
some other dynamic nature of the header.
Default Value: 4
- `blockLoadDebounceMillis` (Bool | Real | String | Dict | Array; optional): How many milliseconds to wait before loading a block. Useful when scrolling over
many rows, spanning many Partial Store blocks, as it prevents blocks loading until
scrolling has settled.
- `bodyScroll` (Bool | Real | String | Dict | Array; optional): The body was scrolled horizontally or vertically.
- `cacheBlockSize` (Real; optional): Partial Store Only - How many rows for each block in the store, i.e. how many
rows returned from the server at a time.
Default Value: 100
- `cacheOverflowSize` (Real; optional): Quantity of extra blank rows to display to the user at the end of the dataset,
which sets the vertical scroll and then allows the grid to request viewing more rows of data.
default is 1, ie show 1 row.
- `cacheQuickFilter` (Bool; optional): Set to true to turn on the  quick filter cache, used for a performance gain when
using the quick filter.
Default Value: false
- `cellClicked` (Bool | Real | String | Dict | Array; optional): Cell is clicked.
- `cellContextMenu` (Bool | Real | String | Dict | Array; optional): Cell is right clicked.
- `cellDoubleClicked` (Bool | Real | String | Dict | Array; optional): Cell is double clicked.
- `cellEditingStarted` (Bool | Real | String | Dict | Array; optional): Editing a cell has started.
- `cellEditingStopped` (Bool | Real | String | Dict | Array; optional): Editing a cell has stopped.
- `cellFadeDelay` (Real; optional): To be used in combination with enableCellChangeFlash, this configuration will
set delay in ms of how long the "flashed
Default Value: 1000
- `cellFlashDelay` (Real; optional): To be used in combination with enableCellChangeFlash, this configuration will
set delay in ms of how long a cell should remain in its "flashed
Default Value: 500
- `cellFocused` (Bool | Real | String | Dict | Array; optional): Cell is focused.
- `cellKeyDown` (Bool | Real | String | Dict | Array; optional): DOM event keyDown happened on a cell. See Keyboard Events.
- `cellKeyPress` (Bool | Real | String | Dict | Array; optional): DOM event keyPress happened on a cell. See Keyboard Events.
- `cellMouseDown` (Bool | Real | String | Dict | Array; optional): Mouse down on cell.
- `cellMouseOut` (Bool | Real | String | Dict | Array; optional): Mouse left cell.
- `cellMouseOver` (Bool | Real | String | Dict | Array; optional): Mouse entered cell.
- `cellStyle` (optional): Object used to perform the cell styling. See AG-Grid Cell Style.. cellStyle has the following type: lists containing elements 'styleConditions', 'defaultStyle'.
Those elements have the following types:
  - `styleConditions` (optional): . styleConditions has the following type: Array of lists containing elements 'condition', 'style'.
Those elements have the following types:
  - `condition` (String; required)
  - `style` (Dict; required)s
  - `defaultStyle` (Dict; optional)
- `cellValueChanged` (Bool | Real | String | Dict | Array; optional): Value has changed after editing.
- `chartThemeOverrides` (Bool | Real | String | Dict | Array; optional): Chart theme overrides applied to all themes, see Overriding Existing Themes.
- `chartThemes` (a value equal to: 'ag-default', 'ag-material', 'ag-pastel', 'ag-vivid', 'ag-solar'; optional): The list of chart themes to be used, see Chart Themes.
Default Value: ['ag-default', 'ag-material', 'ag-pastel', 'ag-vivid', 'ag-solar']
- `clickData` (Bool | Real | String | Dict | Array; optional): Special prop used by renderers.
- `clipboardDeliminator` (Bool | Real | String | Dict | Array; optional): Specify the deliminator to use when copying to clipboard.
- `colResizeDefault` (Bool | Real | String | Dict | Array; optional): Set to 'shift' to have shift-resize as the default resize operation (same as user
holding down Shift while resizing).
- `columnDefs` (Bool | Real | String | Dict | Array; optional): Array of Column Definitions.
- `columnEverythingChanged` (Bool | Real | String | Dict | Array; optional): Shotgun - gets called when either a) new columns are set or b) columnApi.setState()
is used, so everything has changed.
- `columnGroupOpened` (Bool | Real | String | Dict | Array; optional): A column group was opened / closed.
- `columnMoved` (Bool | Real | String | Dict | Array; optional): A column was moved. To find out when the column move is finished you can use the
dragStopped event below.
- `columnPinned` (Bool | Real | String | Dict | Array; optional): A column, or group of columns, was pinned / unpinned.
- `columnPivotChanged` (Bool | Real | String | Dict | Array; optional): A pivot column was added, removed or order changed.
- `columnPivotModeChanged` (Bool | Real | String | Dict | Array; optional): The pivot mode flag was changed.
- `columnResized` (Bool | Real | String | Dict | Array; optional): A column was resized.
- `columnRowGroupChanged` (Bool | Real | String | Dict | Array; optional): A row group column was added or removed.
- `columnSize` (a value equal to: 'sizeToFit', 'autoSizeAll'; optional): Size the columns automatically or to fit their contents
- `columnTypes` (Bool | Real | String | Dict | Array; optional): An object map of custom column types which contain groups of properties that column
definitions can inherit.
- `columnValueChanged` (Bool | Real | String | Dict | Array; optional): A value column was added or removed.
- `columnVisible` (Bool | Real | String | Dict | Array; optional): A column, or group of columns, was hidden / shown.
- `componentStateChanged` (Bool | Real | String | Dict | Array; optional): Only used by React, Angular and VueJS AG Grid components (not used if doing plain
JavaScript or Angular 1.x). If the grid receives changes due to bound properties,
this event fires after the grid has finished processing the change.
- `components` (Bool | Real | String | Dict | Array; optional): A map of component names to plain JavaScript components.
- `context` (Bool | Real | String | Dict | Array; optional): Provides a context object that is provided to different callbacks the grid uses.
Used for passing additional information to the callbacks by your application.
- `copyHeadersToClipboard` (Bool; optional): Set to true to also include headers when copying to clipboard using Ctrl + C clipboard.
Default Value: false
- `csvExportParams` (optional): Object with properties to pass to the exportDataAsCsv() method. csvExportParams has the following type: lists containing elements 'columnSeparator', 'suppressQuotes', 'prependContent', 'appendContent', 'allColumns', 'columnKeys', 'fileName', 'onlySelected', 'onlySelectedAllPages', 'skipColumnGroupHeaders', 'skipColumnHeaders', 'skipRowGroups', 'skipPinnedTop', 'skipPinnedBottom'.
Those elements have the following types:
  - `columnSeparator` (String; optional): Delimiter to insert between cell values.
  - `suppressQuotes` (Bool; optional): Pass true to insert the value into the CSV file without escaping. In this case it is your responsibility to ensure that no cells contain the columnSeparator character.
  - `prependContent` (String; optional): Content to put at the top of the file export. A 2D array of CsvCell objects.
  - `appendContent` (String; optional): Content to put at the bottom of the file export.
  - `allColumns` (Bool; optional): If true, all columns will be exported in the order they appear in the columnDefs.
  - `columnKeys` (Array of Strings; optional): Provide a list (an array) of column keys or Column objects if you want to export specific columns.
  - `fileName` (String; optional): String to use as the file name
  - `onlySelected` (Bool; optional): Export only selected rows.
  - `onlySelectedAllPages` (Bool; optional): Only export selected rows including other pages (only makes sense when using pagination).
  - `skipColumnGroupHeaders` (Bool; optional): Set to true to skip include header column groups.
  - `skipColumnHeaders` (Bool; optional): Set to true if you don't want to export column headers.
  - `skipRowGroups` (Bool; optional): Set to true to skip row group headers if grouping rows. Only relevant when grouping rows.
  - `skipPinnedTop` (Bool; optional): Set to true to suppress exporting rows pinned to the top of the grid.
  - `skipPinnedBottom` (Bool; optional): Set to true to suppress exporting rows pinned to the bottom of the grid.
- `customChartThemes` (Bool | Real | String | Dict | Array; optional): A map containing custom chart themes, see Custom Chart Themes.
- `debounceVerticalScrollbar` (Bool; optional): Set to true to debounce the vertical scrollbar. Can provide smoother scrolling
on older browsers, eg IE.
Default Value: false
- `debug` (Bool; optional): Set this to true to enable debug information from AG Grid and related components.
Will result in additional logging being output, but very useful when investigating
problems.
Default Value: false
- `defaultColDef` (Bool | Real | String | Dict | Array; optional): A default column definition.
- `defaultColGroupDef` (Bool | Real | String | Dict | Array; optional): A default column group definition. All column group definitions will use these
properties. Items defined in the actual column group  definition get precedence.
- `defaultExportParams` (Bool | Real | String | Dict | Array; optional): A default configuration object used to export to CSV or Excel.
- `detailCellRendererParams` (optional): Specifies the params to be used by the default detail Cell Renderer. See Detail
Grids.. detailCellRendererParams has the following type: lists containing elements 'detailGridOptions', 'detailColName', 'suppressCallback'.
Those elements have the following types:
  - `detailGridOptions` (Bool | Real | String | Dict | Array; optional): Grid options for detail grid in master-detail view.
  - `detailColName` (String; optional): Column name where detail grid data is located in main dataset, for master-detail view.
  - `suppressCallback` (Bool; optional): Default: true. If true, suppresses the Dash callback in favor of using the data embedded in rowData at the given detailColName.
- `detailRowAutoHeight` (Bool; optional): Set detail row height automatically based on contents.
- `detailRowHeight` (Real; optional): Set fixed height in pixels for each detail row.
- `displayedColumnsChanged` (Bool | Real | String | Dict | Array; optional): The list of displayed columns changed. This can result from columns open / close,
column move, pivot, group, etc.
- `domLayout` (a value equal to: 'normal', 'autoHeight', 'print'; optional): Switch between layout options. See Printing and Auto Height.
Default Value: ['normal', 'autoHeight', 'print']
- `dragStarted` (Bool | Real | String | Dict | Array; optional): When dragging starts. This could be any action that uses the grid's Drag and Drop
service, e.g. Column Moving, Column Resizing, Range Selection, Fill Handle, etc.
- `dragStopped` (Bool | Real | String | Dict | Array; optional): When dragging stops. This could be any action that uses the grid's Drag and Drop
service, e.g. Column Moving, Column Resizing, Range Selection, Fill Handle, etc.
- `editType` (Bool | Real | String | Dict | Array; optional): Set to 'fullRow' to enable Full Row Editing. Otherwise leave blank to edit one
cell at a time.
- `enableBrowserTooltips` (Bool; optional): Set to true to use the browser's default tooltip instead of using AG Grid's Tooltip
Component.
Default Value: false
- `enableCellChangeFlash` (Bool; optional): Set to true to have cells flash after data changes. See Flashing Data Changes.
Default Value: false
- `enableCellExpressions` (Bool; optional): Set to true to allow cell expressions.
Default Value: false
- `enableCellTextSelection` (Bool; optional): Set to true to be able to select the text within cells.
Default Value: false
- `enableCharts` (Bool; optional): Set to true to Enable Charts.
Default Value: false
- `enableEnterpriseModules` (Bool; optional): If True, enable ag-grid Enterprise modules. Recommended to use with licenseKey.
- `enableExportDataAsCsv` (Bool; optional): If true, the internal method exportDataAsCsv() will be called
- `enableFillHandle` (Bool; optional): Set to true to enable Fill Handle
Default Value: false
- `enableRangeHandle` (Bool; optional): Set to true to enable Range Handle
Default Value: false
- `enableRangeSelection` (Bool; optional): Set to true to enable Range Selection.
Default Value: false
- `enableResetColumnState` (Bool; optional): If true, the internal method resetColumnState() will be called
- `enableRtl` (Bool; optional): Set to true to operate grid in RTL (Right to Left) mode.
Default Value: false
- `ensureDomOrder` (Bool; optional): When true, the order of rows and columns in the DOM are consistent with what is
on screen. See Accessibility - Row and Column Order.
Default Value: false
- `enterMovesDown` (Bool; optional): Set both properties to true to have Excel-style behaviour for the Enter key, i.e.
enter key moves down.
Default Value: false
- `excelStyles` (Bool | Real | String | Dict | Array; optional): The list of Excel styles to be used when exporting to Excel
- `excludeChildrenWhenTreeDataFiltering` (Bool; optional): Set to true to override the default tree data filtering behaviour to instead exclude
child nodes from filter results. See Tree Data Filtering.
Default Value: false
- `expandOrCollapseAll` (Bool | Real | String | Dict | Array; optional): Fired when calling either of the API methods expandAll() or collapseAll().
- `fillHandleDirection` (String; optional): Set to 'x' to force the fill handle direction to horizontal, or set it to 'y'
to force the fill handle direction to vertical
Default Value: xy
- `filterChanged` (Bool | Real | String | Dict | Array; optional): Filter has been modified and applied.
- `filterModified` (Bool | Real | String | Dict | Array; optional): Filter was modified but not applied. Used when filters have 'Apply' buttons.
- `firstDataRendered` (Bool | Real | String | Dict | Array; optional): Fired the first time data is rendered into the grid.
- `floatingFiltersHeight` (Real; optional): The height for the row containing the floating filters. See Header Height.
Default Value: 20
- `frameworkComponents` (Bool | Real | String | Dict | Array; optional): A map of component names to framework (React, Angular etc) components.
- `fullWidthCellRenderer` (Bool | Real | String | Dict | Array; optional): Sets the Cell Renderer to use for Full Width Rows.
- `functionsReadOnly` (Bool; optional): If true, then row group, pivot and value aggregation will be read-only from the
GUI. The grid will display what values are used for each, but will not allow the
user to change the selection. See Read Only Functions.
Default Value: false
- `getDetailRequest` (optional): Request from Dash AgGrid when suppressCallback is disabled and a user opens a row with a detail grid. getDetailRequest has the following type: lists containing elements 'data', 'requestTime'.
Those elements have the following types:
  - `data` (Bool | Real | String | Dict | Array; optional): Details about the row that was opened.
  - `requestTime` (Bool | Real | String | Dict | Array; optional): Datetime representing when the grid was requested.
- `getDetailResponse` (Bool | Real | String | Dict | Array; optional): RowData to populate the detail grid when callbacks are used to populate
- `getRowsRequest` (optional): Infinite Scroll, Datasource interface
See https://www.ag-grid.com/react-grid/infinite-scrolling/#datasource-interface. getRowsRequest has the following type: lists containing elements 'startRow', 'endRow', 'sortModel', 'filterModel', 'context', 'successCallback', 'failCallback'.
Those elements have the following types:
  - `startRow` (Real; optional): The first row index to get.
  - `endRow` (Real; optional): The first row index to NOT get.
  - `sortModel` (Bool | Real | String | Dict | Array; optional): If sorting, what the sort model is
  - `filterModel` (Bool | Real | String | Dict | Array; optional): If filtering, what the filter model is
  - `context` (Bool | Real | String | Dict | Array; optional): The grid context object
  - `successCallback` (optional): Callback to call when the request is successful.
  - `failCallback` (optional): Callback to call when the request fails.
- `getRowsResponse` (optional): Serverside model data response object.
See https://www.ag-grid.com/react-grid/server-side-model-datasource/. getRowsResponse has the following type: lists containing elements 'rowData', 'rowCount', 'storeInfo'.
Those elements have the following types:
  - `rowData` (Array of Bool | Real | String | Dict | Arrays; optional): Data retreived from the server
  - `rowCount` (Real; optional): Current row count, if known
  - `storeInfo` (Bool | Real | String | Dict | Array; optional): Any extra info for the grid to associate with this load
- `gridColumnsChanged` (Bool | Real | String | Dict | Array; optional): The list of grid columns changed.
- `gridReady` (Bool | Real | String | Dict | Array; optional): The grid has initialised. The name 'ready' was influenced by the author's time
programming the Commodore 64. Use this event if, for example, you need to use
the grid's API to fix the columns to size.
- `gridSizeChanged` (Bool | Real | String | Dict | Array; optional): The size of the grid div has changed. In other words, the grid was resized.
- `groupDefaultExpanded` (Real; optional): If grouping, set to the number of levels to expand by default, e.g. 0 for none,
1 for first level only, etc. Set to -1 to expand everything. See Removing Single
Children.
Default Value: 0
- `groupHeaderHeight` (Bool | Real | String | Dict | Array; optional): The height for the rows containing header column groups. If not specified, it
uses headerHeight. See Header Height.
- `groupHideOpenParents` (Bool; optional): Set to true to hide parents that are open. When used with multiple columns for
showing groups, it can give a more pleasing user experience. See Group Hide Open
Parents.
Default Value: false
- `groupIncludeFooter` (Bool; optional): If grouping, whether to show a group footer when the group is expanded. If true,
then by default,  the footer will contain aggregate data (if any) when shown and
the header will be blank. When closed, the header will contain  the aggregate
data regardless of this setting (as the footer is hidden anyway). This is handy
for 'total' rows, that are  displayed below the data when the group is open, and
alongside the group when it is closed See Grouping Footers.
Default Value: false
- `groupIncludeTotalFooter` (Bool; optional): Set to true to show a 'grand' total group footer across all groups. See Grouping
Footers.
Default Value: false
- `groupMultiAutoColumn` (Bool; optional): If using auto column, set to true to have each group in its own separate column,
e.g. if grouping by Country then Year, two auto columns will be created, one for
Country and one for Year. See Multi Auto Column Group.
Default Value: false
- `groupRemoveLowestSingleChildren` (Bool; optional): Set to true to collapse lowest level groups that only have one child. See Remove
Single Children.
Default Value: false
- `groupRemoveSingleChildren` (Bool; optional): Set to true to collapse groups that only have one child. See Remove Single Children.
Default Value: false
- `groupRowInnerRenderer` (Bool | Real | String | Dict | Array; optional): Sets the inner Cell Renderer to use when groupUseEntireRow=true. See Row Grouping.
- `groupRowRenderer` (Bool | Real | String | Dict | Array; optional): Sets the Cell Renderer to use when groupUseEntireRow=true. See Row Grouping.
- `groupSelectsChildren` (Bool; optional): When true, if you select a group, the children of the group will also be selected.
See Group Selection.
Default Value: false
- `groupSelectsFiltered` (Bool; optional): If using groupSelectsChildren, then only the children that pass the current filter
will get selected. See Group Selection.
Default Value: false
- `groupSuppressAutoColumn` (Bool; optional): If true, the grid will not swap in the grouping column when grouping is enabled.
Use this if you want complete control on the column displayed and don't want the
grid's help, in other words if you already have a column in your column definitions
that is responsible for displaying the groups. See Configuring the Auto Group
Column.
Default Value: false
- `groupSuppressBlankHeader` (Bool; optional): If true, and showing footer, aggregate data will be displayed at both the header
and footer levels always. This  stops the possibly undesirable behaviour of the
header details 'jumping' to the footer on expand.
Default Value: false
- `groupUseEntireRow` (Bool; optional): Used when grouping. If true, a group row will span all columns across the entire
width of the table. If false, the cells will be rendered as normal and you will
have the opportunity to include a grouping column (normally the first on the left)
to show the group. See Full Width Group Rows.
Default Value: false
- `headerHeight` (Real; optional): The height in pixels for the row containing the column label header. See Header
Height.
Default Value: 25
- `hoverData` (Bool | Real | String | Dict | Array; optional): Special prop used by renderers.
- `icons` (Bool | Real | String | Dict | Array; optional): Icons to use inside the grid instead of the grid's default icons.
- `immutableData` (Bool | Real | String | Dict | Array; optional): (Client-Side Row Model only) Enables Immutable Data mode, for compatibility with
immutable stores.
- `keepDetailRows` (Bool; optional): Set to true to keep detail rows for when they are displayed again.
Default Value: false
- `keepDetailRowsCount` (Real; optional): Sets the number of details rows to keep.
Default Value: 10
- `layoutInterval` (Real; optional): The interval in milliseconds that the grid uses to periodically check its size
and lay itself out again if the size has changed, such as when your browser changes
size, or your application changes the size of the div element that the grid lives
inside. To stop the periodic layout, set it to -1.
Default Value: 500
- `licenseKey` (String; optional): License key for ag-grid enterprise. If using Enterprise modules,
enableEnterpriseModules must also be true.
- `loadingOverlayComponent` (Bool | Real | String | Dict | Array; optional): Provide a custom loading overlay component.
- `loadingOverlayComponentParams` (Bool | Real | String | Dict | Array; optional): Customise the parameters provided to the loading overlay component.
- `localeText` (Bool | Real | String | Dict | Array; optional): A map of key->value pairs for localising text within the grid. See Localisation.
- `masterDetail` (Bool; optional): Used to enable Master Detail. See Enabling Master Detail.
Default Value: false
- `maxBlocksInCache` (Bool | Real | String | Dict | Array; optional): Partial Store Only - how many blocks to keep in the store. Default is no limit,
so every requested block is kept. Use this if you have memory concerns, and blocks
that were least recently viewed will be purged when the limit is hit. The grid
will additionally make sure it has all the blocks needed to display what is currently
visible - in case this property is set to low.
- `maxConcurrentDatasourceRequests` (Real; optional): How many requests to hit the server with concurrently. If the max is reached,
requests are queued.
Default Value: 1
- `modelUpdated` (Bool | Real | String | Dict | Array; optional): Displayed rows have changed. Triggered after sort, filter or tree expand / collapse
events.
- `multiSortKey` (Bool | Real | String | Dict | Array; optional): Set to 'ctrl' to have multi sorting work using the Ctrl or Command (for Apple)
keys. See Multi Column Sorting.
- `newColumnsLoaded` (Bool | Real | String | Dict | Array; optional): User set new columns.
- `noRowsOverlayComponent` (Bool | Real | String | Dict | Array; optional): Provide a custom no rows overlay component.
- `noRowsOverlayComponentParams` (Bool | Real | String | Dict | Array; optional): Customise the parameters provided to the no rows overlay component.
- `overlayLoadingTemplate` (Bool | Real | String | Dict | Array; optional): Provide a template for 'loading' overlay.
- `overlayNoRowsTemplate` (Bool | Real | String | Dict | Array; optional): Provide a template for 'no rows' overlay.
- `paginateChildRows` (Bool | Real | String | Dict | Array; optional): Set to true to have pages split children of groups when using Row Grouping or
detail rows with Master Detail. See Pagination & Child Rows.
- `pagination` (Bool; optional): Set whether Pagination is enabled.
Default Value: false
- `paginationAutoPageSize` (Bool; optional): Set to true so that the number of rows to load per page is automatically adjusted
by AG Grid so each page shows enough rows to just fill the area designated for
the grid. If false, paginationPageSize is used. See Auto Page Size.
Default Value: false
- `paginationChanged` (Bool | Real | String | Dict | Array; optional): Triggered every time the paging state changes. Some of the most common scenarios
for this event to be triggered are:The page size changesThe current shown page
is changedNew data is loaded onto the grid
- `paginationPageSize` (Real; optional): How many rows to load per page. If paginationAutoPageSize is specified, this property
is ignored. See Customising Pagination.
Default Value: 100
- `pasteEnd` (Bool | Real | String | Dict | Array; optional): Paste operation has ended. See Clipboard Events.
- `pasteStart` (Bool | Real | String | Dict | Array; optional): Paste operation has started. See Clipboard Events.
- `persisted_props` (Array of Strings; optional): Properties whose user interactions will persist after refreshing the
component or the page. Since only `value` is allowed this prop can
normally be ignored.
- `persistence` (Bool | String | Real; optional): Used to allow user interactions in this component to be persisted when
the component - or the page - is refreshed. If `persisted` is truthy and
hasn't changed from its previous value, a `value` that the user has
changed while using the app will keep that change, as long as
the new `value` also matches what was given originally.
Used in conjunction with `persistence_type`.
- `persistence_type` (a value equal to: 'local', 'session', 'memory'; optional): Where persisted user changes will be stored:
memory: only kept in memory, reset on page refresh.
local: window.localStorage, data is kept after the browser quit.
session: window.sessionStorage, data is cleared once the browser quit.
- `pinnedBottomRowData` (Bool | Real | String | Dict | Array; optional): Data to be displayed as Pinned Bottom Rows in the grid.
- `pinnedRowDataChanged` (Bool | Real | String | Dict | Array; optional): The client has set new pinned row data into the grid.
- `pinnedTopRowData` (Bool | Real | String | Dict | Array; optional): Data to be displayed as Pinned Top Rows in the grid.
- `pivotColumnGroupTotals` (Bool | Real | String | Dict | Array; optional): When set and the grid is in pivot mode, automatically calculated totals will appear
within the Pivot Column Groups,in the position specified. See Pivot Column Group
Totals.
- `pivotGroupHeaderHeight` (Bool | Real | String | Dict | Array; optional): The height for the row containing header column groups when in pivot mode. If
not specified, it uses groupHeaderHeight. See Header Height.
- `pivotHeaderHeight` (Bool | Real | String | Dict | Array; optional): The height for the row containing the columns when in pivot mode. If not specified,
it uses headerHeight. See Header Height.
- `pivotMode` (Bool; optional): Set to true to enable pivot mode. See Pivoting.
Default Value: false
- `pivotPanelShow` (a value equal to: 'never', 'always', 'onlyWhenPivoting'; optional): When to show the 'pivot panel' (where you drag rows to pivot) at the top. Note
that the pivot panel will never show if pivotMode is off.
Default Value: ['never', 'always', 'onlyWhenPivoting']
- `pivotRowTotals` (Bool | Real | String | Dict | Array; optional): When set and the grid is in pivot mode, automatically calculated totals will appear
for each value column in the position specified. See Pivot Row Totals.
- `pivotSuppressAutoColumn` (Bool; optional): If true, the grid will not swap in the grouping column when pivoting. Useful if
pivoting using Server Side Row Model or Viewport Row Model and you want full control
of all columns including the group column.
Default Value: false
- `popupParent` (Bool | Real | String | Dict | Array; optional): DOM element to use as popup parent for grid popups (context menu, column menu
etc).
- `preventDefaultOnContextMenu` (Bool; optional): When using suppressContextMenu, you can use the onCellContextMenu function to
provide your own code to handle cell contextmenu events. This flag is useful to
prevent the browser from showing its default context menu.
Default Value: false
- `purgeClosedRowNodes` (Bool | Real | String | Dict | Array; optional): When enabled, closing group rows will remove children of that row. Next time the
row is opened, child rows will be read form the datasoruce again. This property
only applies when there is Row Grouping.
- `quickFilterText` (Bool | Real | String | Dict | Array; optional): Rows are filtered using this text as a quick filter.
- `rangeSelectionChanged` (Bool | Real | String | Dict | Array; optional): A change to range selection has occurred.
- `rowBuffer` (Real; optional): The number of rows rendered outside the scrollable viewable area the grid renders.
Having a buffer means the grid will have rows ready to show as the user slowly
scrolls vertically.
Default Value: 20
- `rowClass` (Bool | Real | String | Dict | Array; optional): The class to give a particular row. See Row Class.
- `rowClassRules` (Bool | Real | String | Dict | Array; optional): Rules which can be applied to include certain CSS classes. See Row Class Rules.
- `rowClicked` (Bool | Real | String | Dict | Array; optional): Row is clicked.
- `rowData` (Bool | Real | String | Dict | Array; optional): (Client-Side Row Model only) Set the data to be displayed as rows in the grid.
- `rowDataChanged` (Bool | Real | String | Dict | Array; optional): The client has set new data into the grid using api.setRowData() or by changing
the rowData bound property.
- `rowDataUpdated` (Bool | Real | String | Dict | Array; optional): The client has updated data for the grid using api.applyTransaction(transaction)
or by changing the rowData bound property with immutableData=true.
- `rowDoubleClicked` (Bool | Real | String | Dict | Array; optional): Row is double clicked.
- `rowDragEnd` (Bool | Real | String | Dict | Array; optional): The drag has finished over the grid.
- `rowDragEnter` (Bool | Real | String | Dict | Array; optional): A drag has started, or dragging was already started and the mouse has re-entered
the grid having previously left the grid.
- `rowDragLeave` (Bool | Real | String | Dict | Array; optional): The mouse has left the grid while dragging.
- `rowDragManaged` (Bool; optional): Set to true to enable Managed Row Dragging.
Default Value: false
- `rowDragMove` (Bool | Real | String | Dict | Array; optional): The mouse has moved while dragging.
- `rowEditingStarted` (Bool | Real | String | Dict | Array; optional): Editing a row has started (when row editing is enabled). When row editing, this
event will be fired once and cellEditingStarted will be fired for each individual
cell. This event corresponds to Full Row Editing only.
- `rowEditingStopped` (Bool | Real | String | Dict | Array; optional): Editing a row has stopped (when row editing is enabled). When row editing, this
event will be fired once and cellEditingStopped will be fired for each individual
cell. This event corresponds to Full Row Editing only.
- `rowGroupOpened` (Bool | Real | String | Dict | Array; optional): A row group was opened or closed.
- `rowGroupPanelShow` (a value equal to: 'never', 'always', 'onlyWhenGrouping'; optional): When to show the 'row group panel' (where you drag rows to group) at the top.
See Column Tool Panel Example.
Default Value: ['never', 'always', 'onlyWhenGrouping']
- `rowHeight` (Real; optional): Default Row Height in pixels.
Default Value: 25
- `rowModelType` (a value equal to: 'clientSide', 'infinite', 'viewport', 'serverSide'; optional): Sets the Row Model type.
Default Value: ['clientSide', 'infinite', 'viewport', 'serverSide']
- `rowMultiSelectWithClick` (Bool; optional): Set to true to allow multiple rows to be selected using single click. See Multi
Select Single Click.
Default Value: false
- `rowSelected` (Bool | Real | String | Dict | Array; optional): Row is selected or deselected.
- `rowSelection` (Bool | Real | String | Dict | Array; optional): Type of Row Selection.
- `rowStyle` (Bool | Real | String | Dict | Array; optional): The style to give a particular row. See Row Style.
- `rowValueChanged` (Bool | Real | String | Dict | Array; optional): A cell's value within a row has changed. This event corresponds to Full Row Editing
only.
- `scrollbarWidth` (Bool | Real | String | Dict | Array; optional): Tell the grid how wide the scrollbar is, which is used in grid width calculations.
Set only if using non-standard browser-provided scrollbars, so the grid can use
the non-standard size in its calculations.
- `selectionChanged` (Bool | Real | String | Dict | Array; optional): Row selection is changed. Use the grid API to get the new row selected.
- `serverSideFilteringAlwaysResets` (Bool | Real | String | Dict | Array; optional): When enabled, always refreshes stores after filter has changed. Use by Full Store
only, to allow Server-Side Filtering.
- `serverSideSortingAlwaysResets` (Bool; optional): When true, a full reset will be performed when sorting using the Server-Side Row
Model.
Default Value: false
- `serverSideStoreType` (a value equal to: 'full', 'partial'; optional): Whether to use Full Store or Partial Store for storing rows. See Row Stores
Default Value: ['full', 'partial']
- `showOpenedGroup` (Bool; optional): Shows the open group in the group column for non-group rows. See Showing Open
Groups.
Default Value: false
- `sideBar` (Bool | a value equal to: 'columns', 'filters' | Dict; optional): SideBar configures the properties of the grid sidebar.
- `singleClickEdit` (Bool; optional): Set to true to enable Single Click Editing for cells, to start editing with a
single click.
Default Value: false
- `skipHeaderOnAutoSize` (Bool; optional): Set this to true to skip the headerName when autoSize is called by default. See
Resizing Example.
Default Value: false
- `sortChanged` (Bool | Real | String | Dict | Array; optional): Sort has changed. The grid also listens for this and updates the model.
- `sortingOrder` (Bool | Real | String | Dict | Array; optional): Array defining the order in which sorting occurs (if sorting is enabled). Values
can be 'asc', 'desc' or null. For example: sortingOrder: ['asc', 'desc']. See
Example Sorting Order and Animation.
- `statusBar` (Bool | Real | String | Dict | Array; optional): Specifies the status bar components to use in the status bar.
- `stopEditingWhenGridLosesFocus` (Bool; optional): Set this to true to  stop cell editing when grid loses focus. The default is the
grid stays editing until focus goes onto another cell. For inline (non-popup)
editors only.
Default Value: false
- `style` (Dict; optional): The CSS style for the component
- `suppressAggAtRootLevel` (Bool; optional): When true, the aggregations won't be computed for root node of the grid. See Big
Data Small Transactions.
Default Value: false
- `suppressAggFilteredOnly` (Bool | Real | String | Dict | Array; optional): Set to true so that aggregations are not impacted by filtering. See Custom Aggregation
Functions.
- `suppressAggFuncInHeader` (Bool; optional): When true, column headers won't include the aggFunc, e.g. 'sum(Bank Balance)'
will just be 'Bank Balance'.
Default Value: false
- `suppressAnimationFrame` (Bool; optional): When true, the grid will not use animation frames when drawing rows while scrolling.
Use this if the grid is working fast enough that you don't need animation frames
and you don't want the grid to flicker.
Default Value: false
- `suppressAsyncEvents` (Bool; optional): Disables the async nature of the events introduced in v10, and makes them synchronous.
This property is only introduced for the purpose of supporting legacy code which
has a dependency to sync events in earlier versions (v9 or earlier) of AG Grid.
It is strongly recommended that you don't change this property unless you have
legacy issues.
Default Value: false
- `suppressAutoSize` (Bool; optional): Suppresses auto-sizing columns for columns. In other words, double clicking a
column's header's edge will not auto-size.
Default Value: false
- `suppressBrowserResizeObserver` (Bool; optional): The grid will check for ResizeObserver and use it if it exists in the browser,
otherwise it will use the grid's alternative implementation. Some users reported
issues with Chrome's ResizeObserver. Use this property to always use the grid's
alternative implementation should such problems exist.
Default Value: false
- `suppressCellSelection` (Bool; optional): If true, cells won't be selectable. This means cells will not get keyboard focus
when you click on them.
Default Value: false
- `suppressClearOnFillReduction` (Bool; optional): Set it to true to prevent cell values from being cleared when the Range Selection
is reduced by the Fill Handle.
Default Value: false
- `suppressClickEdit` (Bool; optional): Set to true so that neither single nor double click starts editing. See Single
Click, Double Click, No Click Editing.
Default Value: false
- `suppressColumnMoveAnimation` (Bool; optional): If true, the ag-column-moving class is not added to the grid while columns are
moving. In the default themes, this results in no animation when moving columns.
Default Value: false
- `suppressColumnVirtualisation` (Bool; optional): Set to true so that the grid doesn't virtualise the columns. For example, if you
have 100 columns, but only 10 visible due to scrolling, all 100 will always be
rendered.
Default Value: false
- `suppressContextMenu` (Bool; optional): Set to true to not show context menu. Use if you don't want to use the default
'right click' context menu.
Default Value: false
- `suppressCopyRowsToClipboard` (Bool; optional): Set to true to only have the range selection, and not row selection, copied to
clipboard.
Default Value: false
- `suppressCsvExport` (Bool; optional): Prevents the user from exporting the grid to CSV.
Default Value: false
- `suppressDragLeaveHidesColumns` (Bool; optional): If true, when you drag a column out of the grid (e.g. to the group zone) the column
is not hidden.
Default Value: false
- `suppressExcelExport` (Bool; optional): Prevents the user from exporting the grid to Excel.
Default Value: false
- `suppressExpandablePivotGroups` (Bool; optional): When enabled pivot column groups will appear 'fixed', without the ability to expand
and collapse the column groups. See Fixed Pivot Column Groups.
Default Value: false
- `suppressFieldDotNotation` (Bool; optional): If true, then dots in field names (e.g. address.firstline) are not treated as
deep references. Allows you to use dots in your field name if you prefer.
Default Value: false
- `suppressFocusAfterRefresh` (Bool; optional): Set to true to not set focus back on the grid after a refresh. This can avoid
issues where you want to keep the focus on another part of the browser.
Default Value: false
- `suppressHorizontalScroll` (Bool; optional): Set to true to never show the horizontal scroll. This is useful if the grid is
aligned with another grid and will scroll when the other grid scrolls. (Show not
be used in combination with alwaysShowHorizontalScroll) See Aligned Grid as Footer.
Default Value: false
- `suppressLastEmptyLineOnPaste` (Bool; optional): Set to true to work around a bug with Excel (Windows) that adds an extra empty
line at the end of ranges copied to the clipboard.
Default Value: false
- `suppressLoadingOverlay` (Bool; optional): Disables the 'loading' overlay.
Default Value: false
- `suppressMaintainUnsortedOrder` (Bool; optional): Set to true to suppress sorting of un-sorted data to match original row data.
See Big Data Small Transactions.
Default Value: false
- `suppressMakeVisibleAfterUnGroup` (Bool; optional): By default, when a column is un-grouped it is made visible. e.g. on main demo:
1) group by country by dragging (action of moving column out of grid means column
is made visible=false); then 2) un-group by clicking 'x' on the country column
in the column drop zone; the column is then made visible=true. This property stops
the column becoming visible again when un-grouping.
Default Value: false
- `suppressMaxRenderedRowRestriction` (Bool; optional): By default the grid has a limit of rendering a maximum of 500 rows at once (remember
the grid only renders rows you can see, so unless your display shows more than
500 rows without vertically scrolling this will never be an issue).
Default Value: false
- `suppressMenuHide` (Bool; optional): Set to true to always show the column menu button, rather than only showing when
the mouse is over the column header.
Default Value: false
- `suppressMiddleClickScrolls` (Bool; optional): If true, then middle clicks will result in click events for cell and row. Otherwise
the browser will use middle click to scroll the grid.
Default Value: false
- `suppressModelUpdateAfterUpdateTransaction` (Bool | Real | String | Dict | Array; optional): ( only) Prevents Transactions changing sort, filter, group or pivot state when
transaction only contains updates.
- `suppressMovableColumns` (Bool; optional): Set to true to suppress column moving, i.e. to make the columns fixed position.
Default Value: false
- `suppressMoveWhenRowDragging` (Bool; optional): Set to true to suppress moving rows while dragging the rowDrag waffle. This option
highlights the position where the row will be placed and it will only move the
row on mouse up. See Row Dragging.
Default Value: false
- `suppressMultiSort` (Bool; optional): Set to true to suppress multi-sort when the user shift-clicks a column header.
Default Value: false
- `suppressNoRowsOverlay` (Bool; optional): Disables the 'no rows' overlay.
Default Value: false
- `suppressPaginationPanel` (Bool; optional): If true, the default AG Grid controls for navigation are hidden. This is useful
if pagination=true and you want to provide your own pagination controls. Otherwise,
when pagination=true the grid automatically shows the necessary controls at the
bottom so that the user can navigate through the different pages. See Custom Pagination
Controls.
Default Value: false
- `suppressParentsInRowNodes` (Bool; optional): If true, rowNodes don't get their parents set. The grid doesn't use the parent
reference, but it is included to help the client code navigate the node tree if
it wants by providing bi-direction navigation up and down the tree. If this is
a problem (e.g. if you need to convert the tree to JSON, which does not allow
cyclic dependencies) then set this to true.
Default Value: false
- `suppressPreventDefaultOnMouseWheel` (Bool; optional): If true, mouse wheel events will be passed to the browser. Useful if your grid
has no vertical scrolls and you want the mouse to scroll the browser page.
Default Value: false
- `suppressPropertyNamesCheck` (Bool; optional): Disables showing a warning message in the console if using a gridOptions or colDef
property that doesn't exist.
Default Value: false
- `suppressRowClickSelection` (Bool; optional): If true, row selection won't happen when rows are clicked. Use when you want checkbox
selection exclusively.
Default Value: false
- `suppressRowDeselection` (Bool; optional): If true then rows will not be deselected if you hold down Ctrl and click the row
or press Space.
Default Value: false
- `suppressRowDrag` (Bool; optional): Set to true to suppress Row Dragging.
Default Value: false
- `suppressRowHoverHighlight` (Bool; optional): Set to true to not highlight rows by adding the ag-row-hover CSS class.
Default Value: false
- `suppressRowTransform` (Bool; optional): Uses CSS top instead of CSS transform for positioning rows. Useful if the transform
function is causing issues such as used in row spanning.
Default Value: false
- `suppressRowVirtualisation` (Bool | Real | String | Dict | Array; optional): There is no such property as suppressRowVirtualisation - if you want to do this,
then set the rowBuffer property to be very large, e.g. 9999. Warning: lots of
rendered rows will mean a very large amount of rendering in the DOM which will
slow things down.
- `suppressScrollOnNewData` (Bool; optional): When true, the grid will not scroll to the top when new row data is provided.
Use this if you don't want the default behaviour of scrolling to the top every
time you load new data.
Default Value: false
- `suppressTouch` (Bool; optional): Disables touch support (but does not remove the browser's efforts to simulate
mouse events on touch).
Default Value: false
- `theme` (a value equal to: 'alpine', 'balham', 'material', 'bootstrap'; optional): The ag-grid provided theme to use. More info here: https://www.ag-grid.com/javascript-grid/themes-provided/
- `toolPanelVisibleChanged` (Bool | Real | String | Dict | Array; optional): The tool panel was hidden or shown. Use api.isToolPanelShowing() to get status.
- `tooltipMouseTrack` (Bool; optional): Set to true to have tooltips follow the cursor once they are displayed.
Default Value: false
- `tooltipShowDelay` (Real; optional): The delay in milliseconds that it takes for tooltips to show up once an element
is hovered.
Default Value: 2000
- `unSortIcon` (Bool; optional): Set to true to show the 'no sort' icon. See Example Custom Sorting.
Default Value: false
- `valueCache` (Bool; optional): Set to true to turn on the value cache.
Default Value: false
- `valueCacheNeverExpires` (Bool; optional): Set to true to set value cache to not expire after data updates.
Default Value: false
- `viewportChanged` (Bool | Real | String | Dict | Array; optional): Which rows are rendered in the DOM has changed.
- `viewportDatasource` (Bool | Real | String | Dict | Array; optional): To use the viewport row model you provide the grid with a viewportDatasource.
See Viewport.
- `viewportRowModelBufferSize` (Bool | Real | String | Dict | Array; optional): When using viewport row model, sets the buffer size for the viewport.
- `viewportRowModelPageSize` (Bool | Real | String | Dict | Array; optional): When using viewport row model, sets the pages size for the viewport.
- `virtualColumnsChanged` (Bool | Real | String | Dict | Array; optional): The list of rendered columns changed (only columns in the visible scrolled viewport
are rendered by default).
- `virtualRowData` (Bool | Real | String | Dict | Array; optional): The rowData in the grid after inline filters are applied.
- `virtualRowRemoved` (Bool | Real | String | Dict | Array; optional): A row was removed from the DOM, for any reason. Use to clean up resources (if
any) used by the row.
"""
function aggrid(; kwargs...)
        available_props = Symbol[:children, :id, :AsyncTransactionsFlushed, :accentedSort, :aggFuncs, :aggregateOnlyChangedColumns, :alignedGrids, :allowContextMenuWithControlKey, :allowDragFromColumnsToolPanel, :allowShowChangeAfterFilter, :alwaysShowHorizontalScroll, :alwaysShowVerticalScroll, :animateRows, :animationQueueEmpty, :applyColumnDefOrder, :asyncTransactionWaitMillis, :autoGroupColumnDef, :autoSizePadding, :blockLoadDebounceMillis, :bodyScroll, :cacheBlockSize, :cacheOverflowSize, :cacheQuickFilter, :cellClicked, :cellContextMenu, :cellDoubleClicked, :cellEditingStarted, :cellEditingStopped, :cellFadeDelay, :cellFlashDelay, :cellFocused, :cellKeyDown, :cellKeyPress, :cellMouseDown, :cellMouseOut, :cellMouseOver, :cellStyle, :cellValueChanged, :chartThemeOverrides, :chartThemes, :clickData, :clipboardDeliminator, :colResizeDefault, :columnDefs, :columnEverythingChanged, :columnGroupOpened, :columnMoved, :columnPinned, :columnPivotChanged, :columnPivotModeChanged, :columnResized, :columnRowGroupChanged, :columnSize, :columnTypes, :columnValueChanged, :columnVisible, :componentStateChanged, :components, :context, :copyHeadersToClipboard, :csvExportParams, :customChartThemes, :debounceVerticalScrollbar, :debug, :defaultColDef, :defaultColGroupDef, :defaultExportParams, :detailCellRendererParams, :detailRowAutoHeight, :detailRowHeight, :displayedColumnsChanged, :domLayout, :dragStarted, :dragStopped, :editType, :enableBrowserTooltips, :enableCellChangeFlash, :enableCellExpressions, :enableCellTextSelection, :enableCharts, :enableEnterpriseModules, :enableExportDataAsCsv, :enableFillHandle, :enableRangeHandle, :enableRangeSelection, :enableResetColumnState, :enableRtl, :ensureDomOrder, :enterMovesDown, :excelStyles, :excludeChildrenWhenTreeDataFiltering, :expandOrCollapseAll, :fillHandleDirection, :filterChanged, :filterModified, :firstDataRendered, :floatingFiltersHeight, :frameworkComponents, :fullWidthCellRenderer, :functionsReadOnly, :getDetailRequest, :getDetailResponse, :getRowsRequest, :getRowsResponse, :gridColumnsChanged, :gridReady, :gridSizeChanged, :groupDefaultExpanded, :groupHeaderHeight, :groupHideOpenParents, :groupIncludeFooter, :groupIncludeTotalFooter, :groupMultiAutoColumn, :groupRemoveLowestSingleChildren, :groupRemoveSingleChildren, :groupRowInnerRenderer, :groupRowRenderer, :groupSelectsChildren, :groupSelectsFiltered, :groupSuppressAutoColumn, :groupSuppressBlankHeader, :groupUseEntireRow, :headerHeight, :hoverData, :icons, :immutableData, :keepDetailRows, :keepDetailRowsCount, :layoutInterval, :licenseKey, :loadingOverlayComponent, :loadingOverlayComponentParams, :localeText, :masterDetail, :maxBlocksInCache, :maxConcurrentDatasourceRequests, :modelUpdated, :multiSortKey, :newColumnsLoaded, :noRowsOverlayComponent, :noRowsOverlayComponentParams, :overlayLoadingTemplate, :overlayNoRowsTemplate, :paginateChildRows, :pagination, :paginationAutoPageSize, :paginationChanged, :paginationPageSize, :pasteEnd, :pasteStart, :persisted_props, :persistence, :persistence_type, :pinnedBottomRowData, :pinnedRowDataChanged, :pinnedTopRowData, :pivotColumnGroupTotals, :pivotGroupHeaderHeight, :pivotHeaderHeight, :pivotMode, :pivotPanelShow, :pivotRowTotals, :pivotSuppressAutoColumn, :popupParent, :preventDefaultOnContextMenu, :purgeClosedRowNodes, :quickFilterText, :rangeSelectionChanged, :rowBuffer, :rowClass, :rowClassRules, :rowClicked, :rowData, :rowDataChanged, :rowDataUpdated, :rowDoubleClicked, :rowDragEnd, :rowDragEnter, :rowDragLeave, :rowDragManaged, :rowDragMove, :rowEditingStarted, :rowEditingStopped, :rowGroupOpened, :rowGroupPanelShow, :rowHeight, :rowModelType, :rowMultiSelectWithClick, :rowSelected, :rowSelection, :rowStyle, :rowValueChanged, :scrollbarWidth, :selectionChanged, :serverSideFilteringAlwaysResets, :serverSideSortingAlwaysResets, :serverSideStoreType, :showOpenedGroup, :sideBar, :singleClickEdit, :skipHeaderOnAutoSize, :sortChanged, :sortingOrder, :statusBar, :stopEditingWhenGridLosesFocus, :style, :suppressAggAtRootLevel, :suppressAggFilteredOnly, :suppressAggFuncInHeader, :suppressAnimationFrame, :suppressAsyncEvents, :suppressAutoSize, :suppressBrowserResizeObserver, :suppressCellSelection, :suppressClearOnFillReduction, :suppressClickEdit, :suppressColumnMoveAnimation, :suppressColumnVirtualisation, :suppressContextMenu, :suppressCopyRowsToClipboard, :suppressCsvExport, :suppressDragLeaveHidesColumns, :suppressExcelExport, :suppressExpandablePivotGroups, :suppressFieldDotNotation, :suppressFocusAfterRefresh, :suppressHorizontalScroll, :suppressLastEmptyLineOnPaste, :suppressLoadingOverlay, :suppressMaintainUnsortedOrder, :suppressMakeVisibleAfterUnGroup, :suppressMaxRenderedRowRestriction, :suppressMenuHide, :suppressMiddleClickScrolls, :suppressModelUpdateAfterUpdateTransaction, :suppressMovableColumns, :suppressMoveWhenRowDragging, :suppressMultiSort, :suppressNoRowsOverlay, :suppressPaginationPanel, :suppressParentsInRowNodes, :suppressPreventDefaultOnMouseWheel, :suppressPropertyNamesCheck, :suppressRowClickSelection, :suppressRowDeselection, :suppressRowDrag, :suppressRowHoverHighlight, :suppressRowTransform, :suppressRowVirtualisation, :suppressScrollOnNewData, :suppressTouch, :theme, :toolPanelVisibleChanged, :tooltipMouseTrack, :tooltipShowDelay, :unSortIcon, :valueCache, :valueCacheNeverExpires, :viewportChanged, :viewportDatasource, :viewportRowModelBufferSize, :viewportRowModelPageSize, :virtualColumnsChanged, :virtualRowData, :virtualRowRemoved]
        wild_props = Symbol[]
        return Component("aggrid", "AgGrid", "dash_ag_grid", available_props, wild_props; kwargs...)
end

aggrid(children::Any; kwargs...) = aggrid(;kwargs..., children = children)
aggrid(children_maker::Function; kwargs...) = aggrid(children_maker(); kwargs...)

