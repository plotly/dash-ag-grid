from dash import html, register_page
from utils.utils import app_description
from utils.other_components import up_next, make_md, ComponentReference
import dash_ag_grid as dag

register_page(
    __name__, order=2, description=app_description, title="Dash AG Grid")

text1 = """
# Dash AG Grid Reference

AG Grid is highly customizable and has hundreds of props.  Only a subset of these props are defined in the dash-ag-grid
 component. The props defined in dash-ag-grid can be found in the reference section below.  These props are all
 unique to Dash in some way.  For example, they can trigger a Dash callback or they define component defaults. 
 
For all other props, please see the AG Grid docs for the full [AG Grid API reference](https://www.ag-grid.com/react-data-grid/grid-api/).
These props can be used in Dash, they just need to be passed to the grid in a prop such as `dashGridOptions` or `columnDefs`.


>
>__Content__
>
> 1. Props unique to Dash
2. Props that can trigger a Dash callback
3. Prop Defaults
4. JavaScript functions as props
5. Dash AG Grid reference


` `  
` `  


### 1. Props unique to Dash

Here are a few examples of props unique to Dash, and you can find the rest in the reference section below:

 - `cellRendererData` This prop is used with custom components.  See the <dccLink href='/components/cell-renderer' children='Cell Styling' /> section for
more details.


 - `cellStyle`  This is an AG Grid prop, however it also accepts a "dash-only" dict to make it easier to do conditional formatting
without writing JavaScript functions.  See the <dccLink href='/layout/cell-styling' children='Cell Styling' /> section for
more details.


- `dashGridOptions`:

Use the `dashGridOptions` prop for any valid AG Grid prop that's used on the grid level.  
For example, `pagination` is not defined as a prop in dash-ag-grid.  To enable pagination, instead of doing it like this:
 ```
 # don't do it this way:
 dag.AgGrid(     
     pagination=True,
     # other props
 ) 
 ```
 
 Add the `pagination` prop to the `dashGridOptions` dict like this:
 ```
 # correct way:
 dag.AgGrid(
     dashGridOptions={'pagination': True}
     # other props
 ) 
 ```
 
` `  
` `  

 
### 2. Props that trigger callbacks

The following props can be used to trigger a Dash Callback:
```
- autoSizeAllColumns
- cellClicked
- cellValueChanged
- cellRendererData
- columnDefs
- columnState
- defaultColDef
- deleteSelectedRows
- deselectAll
- exportDataAsCsv
- getDetailRequest
- getDetailResponse
- getRowsRequest
- getRowsResponse 
- resetColumnState
- rowData
- rowTransaction
- selectAll
- selectedRows
- updateColumnState 
- virtualRowData

```


` `  
` `  


### 3. Props defaults

```
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
    rowModelType: 'clientSide',
```    

` `  
` `  

### 4. JavaScript functions as props

For more information on using JavaScript functions with Dash see the <dccLink href='/getting-started/beyond-the-basics' children='Beyond The Basics' /> section.  

- __Grid level props__  

The following grid level props props will take functions as inputs.  If the prop does not exist in the Dash AG Grid
 Reference section below, they can be used in the `dashGridOptions` prop.
 
```     
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
```
- __Column Level Prop__  


The following column level props will take functions as inputs.  If the prop does not exist in the Dash AG Grid Reference section
 below, they can be used in the `columnDefs` or `defaultColDefs` props.

```
    'valueGetter',
    'valueFormatter',
    'valueParser',
    'valueSetter',
    'filterValueGetter',
    'headerValueGetter',
    'template',


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

```


` `  
` `  



"""

layout = html.Div(
    [
        make_md(text1),
        make_md("### 5. Dash AG Grid Reference"),
        ComponentReference("AgGrid", dag)
    ],
)


