/**
 * Dangerous elements inside column defs: If you pass a string,
 * AG Grid will execute it as raw JS. We accept these strings if
 * `dangerously_allow_code=true`, otherwise we require
 * {function: <string>} and we'll eval & exec it safely.
 * https://www.ag-grid.com/react-data-grid/cell-expressions/#column-definition-expressions
 **/
export const COLUMN_DANGEROUS_FUNCTIONS = {
    valueGetter: 1,
    valueFormatter: 1,
    valueParser: 1,
    valueSetter: 1,
    filterValueGetter: 1,
    headerValueGetter: 1,
    template: 1,
    dateParser: 1,
    dateFormatter: 1,
};

/**
 * Dangerous elements on the grid: If you pass a string,
 * AG Grid will execute it as raw JS. We accept these strings if
 * `dangerously_allow_code=true`, otherwise we require
 * {function: <string>} and we'll eval & exec it safely.
 * https://www.ag-grid.com/react-data-grid/cell-expressions/#column-definition-expressions
 **/
export const GRID_DANGEROUS_FUNCTIONS = {
    overlayLoadingTemplate: 1,
    overlayNoRowsTemplate: 1,
};

/**
 * Objects in either columns or top-level props with arbitrary keys
 * whose values can only be function strings, which we will eval safely
 **/
export const OBJ_OF_FUNCTIONS = {
    cellClassRules: 1,
    rowClassRules: 1,
};

/**
 * Possible functions from top-level grid props
 * Props in this list can be string constants (NOT eval'd by AG Grid) or functions,
 * in which case we require {function: <string>} and we will eval them safely
 * https://www.ag-grid.com/react-data-grid/grid-options/
 **/
export const GRID_MAYBE_FUNCTIONS = {
    // Accessories
    getMainMenuItems: 1,
    postProcessPopup: 1,
    getContextMenuItems: 1,

    // Clipboard
    processCellForClipboard: 1,
    processHeaderForClipboard: 1,
    processGroupHeaderForClipboard: 1,
    processCellFromClipboard: 1,
    sendToClipboard: 1,
    processDataFromClipboard: 1,

    // Exporting
    getCustomContentBelowRow: 1,
    shouldRowBeSkipped: 1,
    processCellCallback: 1,
    processHeaderCallback: 1,
    processGroupHeaderCallback: 1,
    processRowGroupCallback: 1,

    // Filtering
    isExternalFilterPresent: 1,
    doesExternalFilterPass: 1,
    quickFilterParser: 1,

    // Integrated Charts
    getChartToolbarItems: 1,
    createChartContainer: 1,

    // Keyboard Navigation
    navigateToNextHeader: 1,
    tabToNextHeader: 1,
    navigateToNextCell: 1,
    tabToNextCell: 1,

    // Localisation
    getLocaleText: 1,

    // Miscellaneous
    getDocument: 1,
    isRowMaster: 1,

    // Pagination
    paginationNumberFormatter: 1,

    // Pivot and Aggregation
    processPivotResultColDef: 1,
    processPivotResultColGroupDef: 1,
    aggFuncs: 1,
    getGroupRowAgg: 1,

    // Rendering
    getBusinessKeyForNode: 1,
    processRowPostCreate: 1,

    // Row Drag and Drop
    rowDragText: 1,

    // Row Grouping
    isGroupOpenByDefault: 1,
    initialGroupOrderComparator: 1,

    // RowModel: Server-Side
    getChildCount: 1,
    getServerSideGroupLevelParams: 1,
    isServerSideGroupOpenByDefault: 1,
    isApplyServerSideTransaction: 1,
    isServerSideGroup: 1,
    getServerSideGroupKey: 1,

    // Selection
    isRowSelectable: 1,
    fillOperation: 1,

    // Sorting
    postSortRows: 1,

    // Styling
    getRowHeight: 1,
    getRowStyle: 1,
    getRowClass: 1,
    isFullWidthRow: 1,
};

/**
 * Possible functions from top-level grid props
 * Props in this list can be string constants (NOT eval'd by AG Grid) or functions,
 * in which case we require {function: <string>} and we will eval them safely
 * https://www.ag-grid.com/react-data-grid/grid-options/
 **/
export const GRID_MAYBE_FUNCTIONS_NO_PARAMS = {
    components: 1,
    frameworkComponents: 1,
    setPopupParent: 1,
    popupParent: 1,
    quickFilterMatcher: 1,
};

/**
 * Functions from top-level grid props. Props in this list can ONLY be
 * functions, so we accept a string and eval it safely
 * https://www.ag-grid.com/react-data-grid/grid-options/
 **/
export const GRID_ONLY_FUNCTIONS = {
    getRowId: 1,
    getDataPath: 1,
};

/**
 * Other top-level containers that look like a column def
 */
export const GRID_COLUMN_CONTAINERS = {
    defaultColDef: 1,
    autoGroupColumnDef: 1,
    defaultColGroupDef: 1,
};

/**
 * Top-level containers that contain other functions or entire grids
 */
export const GRID_NESTED_FUNCTIONS = {
    detailCellRendererParams: 1,
    detailGridOptions: 1,
    csvExportParams: 1,
    defaultCsvExportParams: 1,
};

/**
 * Possible functions from columnDef props
 * Props in this list can be string constants (NOT eval'd by AG Grid) or functions,
 * in which case we require {function: <string>} and we will eval them safely
 * https://www.ag-grid.com/react-data-grid/column-properties/
 **/
export const COLUMN_MAYBE_FUNCTIONS_NO_PARAMS = {
    cellEditor: 1,
    filter: 1,

    // Columns: Sort
    comparator: 1,

    // filter params custom option
    predicate: 1,
};

/**
 * Possible functions from columnDef props
 * Props in this list can be string constants (NOT eval'd by AG Grid) or functions,
 * in which case we require {function: <string>} and we will eval them safely
 * https://www.ag-grid.com/react-data-grid/column-properties/
 **/
export const COLUMN_MAYBE_FUNCTIONS = {
    // Columns
    keyCreator: 1,
    equals: 1,
    checkboxSelection: 1,
    icons: 1,
    suppressNavigable: 1,
    suppressKeyboardEvent: 1,

    // Columns: Editing
    editable: 1,
    cellEditorSelector: 1,

    // Columns: Events
    onCellDoubleClicked: 1,
    onCellContextMenu: 1,

    // Columns: Filter
    getQuickFilterText: 1,
    textFormatter: 1,
    textMatcher: 1,
    numberFormatter: 1,
    numberParser: 1,

    // Columns: Headers
    suppressHeaderKeyboardEvent: 1,
    headerCheckboxSelection: 1,

    // Columns: Pivoting
    pivotComparator: 1,

    // Columns: Rendering and Styling
    cellStyle: 1,
    cellClass: 1,
    tooltipComponent: 1,
    cellRendererSelector: 1,

    // Columns: Row Dragging
    rowDrag: 1,
    rowDragText: 1,
    dndSource: 1,
    dndSourceOnRowDrag: 1,

    // Columns: Row Grouping
    aggFunc: 1,
    initialAggFunc: 1,

    // Columns: Spanning
    colSpan: 1,
    rowSpan: 1,

    // Columns: Tooltips
    tooltipValueGetter: 1,

    // Groups
    toolPanelClass: 1,

    // Groups: Header
    headerClass: 1,

    // Header Component Parameters
    showColumnMenu: 1,
    progressSort: 1,
    setSort: 1,

    // Header Group Component Parameters
    setExpanded: 1,

    // In filterParams
    filterPlaceholder: 1,

    // In dataTypeDefinitions
    dataTypeMatcher: 1,
};

/**
 * Container objects inside columnDefs that may have other functions
 * inside them, listed in other categories
 **/
export const COLUMN_NESTED_FUNCTIONS = {
    headerComponentParams: 1,
    headerGroupComponentParams: 1,
};

/**
 * Container objects inside columnDefs that may have other functions
 * or may be functions themselves
 **/
export const COLUMN_NESTED_OR_OBJ_OF_FUNCTIONS = {
    filterParams: 1,
    cellRendererParams: 1,
    cellEditorParams: 1,
    tooltipComponentParams: 1,
};

/**
 * Container arrays of objects inside columnDefs that may have functions
 * inside them, listed in other categories
 */
export const COLUMN_ARRAY_NESTED_FUNCTIONS = {
    children: 1,
    filterOptions: 1,
};

/**
 * Container function, object of functions, or object of objects inside a property that may have functions
 * inside them, listed in other categories
 */
export const OBJ_MAYBE_FUNCTION_OR_MAP_MAYBE_FUNCTIONS = {
    dataTypeDefinitions: 1,
};

/**
 * Props to pass straight from Dash to AG Grid with no caching or conversion
 */
export const PASSTHRU_PROPS = ['rowData'];

/**
 * Props to not send to AG Grid at all
 * There are others too, that are already pulled out of `restProps`
 * in the render() method, so they don't need to be listed here
 */
export const PROPS_NOT_FOR_AG_GRID = [
    'setProps',
    'loading_state',
    'enableEnterpriseModules',
    'parentState',
    'persisted_props',
    'persistence_type',
    'virtualRowData',
    'cellValueChanged',
    'cellClicked',
    'getRowRequest',
    'getRowResponse',
    'getDetailRequest',
    'getDetailResponse',
    'dangerously_allow_code',
    'alignedGrids',
    'resetColumnState',
    'exportDataAsCsv',
    'selectAll',
    'deselectAll',
    'deleteSelectedRows',
    'rowTransaction',
    'updateColumnState',
    'csvExportParams',
    'filterModel',
    'columnState',
    'paginationGoTo',
    'columnSize',
    'scrollTo',
];

/**
 * Props to not trigger a render update
 */
export const OMIT_PROP_RENDER = [
    'virtualRowData',
    'columnState',
    'filterModel',
    'selectedRows',
    'getRowRequest',
    'getDetailRequest',
    'cellValueChanged',
    'cellClicked',
    'paginationInfo',
    'cellRendererData',
];

/**
 * States to not trigger a render update
 */
export const OMIT_STATE_RENDER = ['gridColumnApi', 'mounted', 'openGroups'];
