/**
* Dangerous elements that can be used to execute strings as JS code:
* https://www.ag-grid.com/react-data-grid/cell-expressions/#column-definition-expressions
**/
export const expressWarn = [
    'valueGetter',
    'valueFormatter',
    'valueParser',
    'valueSetter',
    'filterValueGetter',
    'headerValueGetter',
    'template',
];

/**
* These props will always be replaced because the values inside the objects can only be strings to be evaluated
**/
export const replaceFunctions = ['cellClassRules', 'rowClassRules']

/**
* Functions from grid props https://www.ag-grid.com/react-data-grid/grid-options/
**/
export const gridFunctions = [
    // Accessories
    'getMainMenuItems',
    'postProcessPopup',

    // Clipboard
    'processCellForClipboard',
    'processHeaderForClipboard',
    'processGroupHeaderForClipboard',
    'processCellFromClipboard',
    'sendToClipboard',
    'processDataFromClipboard',

    // Filtering
    'isExternalFilterPresent',
    'doesExternalFilterPass',

    // Integrated Charts
    'getChartToolbarItems',
    'createChartContainer',

    // Keyboard Navigation
    'navigateToNextHeader',
    'tabToNextHeader',
    'navigateToNextCell',
    'tabToNextCell',

    // Localisation
    'getLocaleText',

    // Miscellaneous
    'getDocument',

    // Pagination
    'paginationNumberFormatter',

    // Pivot and Aggregation
    'processPivotResultColDef',
    'processPivotResultColGroupDef',
    'aggFuncs',
    'getGroupRowAgg',

    // Rendering
    'getBusinessKeyForNode',
    'processRowPostCreate',

    // Row Drag and Drop
    'rowDragText',

    // Row Grouping
    'isGroupOpenByDefault',
    'initialGroupOrderComparator',

    // RowModel: Server-Side
    'getChildCount',
    'getServerSideGroupLevelParams',
    'isServerSideGroupOpenByDefault',
    'isApplyServerSideTransaction',
    'isServerSideGroup',
    'getServerSideGroupKey',

    // Selection
    'isRowSelectable',
    'fillOperation',

    // Sorting
    'postSortRows',

    // Styling
    'getRowHeight',
    'getRowStyle',
    'getRowClass',
    'rowClassRules',
    'isFullWidthRow',

 ];

/**
* Functions from columnDef props https://www.ag-grid.com/react-data-grid/column-properties/
**/
export const columnFunctions = [
    // Columns
    'keyCreator',
    'equals',
    'checkboxSelection',
    'icons',
    'suppressNavigable',
    'suppressKeyboardEvent',
    'filterParams',

    // Columns: Editing
    'editable',
    'cellEditor',
    'cellEditorSelector',

    // Columns: Events
    'onCellDoubleClicked',
    'onCellContextMenu',

    // Columns: Filter
    'getQuickFilterText',


    // Columns: Headers
    'suppressHeaderKeyboardEvent',
    'headerCheckboxSelection',

    // Columns: Pivoting
    'pivotComparator',

    // Columns: Rendering and Styling
    'cellStyle',
    'cellClass',
    'cellClassRules',
    'tooltipComponent',
    'cellRendererSelector',

    // Columns: Row Dragging
    'rowDrag',
    'rowDragText',
    'dndSource',
    'dndSourceOnRowDrag',

    // Columns: Row Grouping
    'aggFunc',
    'initialAggFunc',

    // Columns: Sort
    'comparator',

    // Columns: Spanning
    'colSpan',
    'rowSpan',

    // Columns: Tooltips
    'tooltipValueGetter',

    // Groups
    'toolPanelClass',

    // Groups: Header
    'headerClass',

    // Header Component Parameters
    'showColumnMenu',
    'progressSort',
    'setSort',

    // Header Group Component Parameters
    'setExpanded',
];

