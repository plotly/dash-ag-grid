from dash import html, register_page
from utils.utils import app_description
from utils.other_components import make_md


register_page(
    __name__, order=6, description=app_description, title="Dash AG Grid Migration Guide")

text1 = """
# Migration Guide

-----------
Dash AG Grid will continue to evolve through a series of alpha releases until it's ready for the 2.0.0 production release.

Significant changes from 1.3.0 through 2.0.0a4 include:
  - making dash-ag-grid prop names align with the upstream AG Grid API
  - making dash-ag-grid more secure
  - improving performance and fixing bugs
  
Below are the breaking changes in each alpha release, dating from Dash AG Grid 1.3.0. 
  

#### Migrating from Alpha 1 to current release - Breaking Changes Summary


If you are starting from the open source dash-ag-grid alpha releases, here is a brief summary of the breaking changes in each alpha 
version and how to fix them. For more details, please see the example below of migrating an app from alpha 1 to the current version.


__2.0.0a2__


- `selectionChanged` - change prop name to `selectedRows`


- `dangerously_allow html` - change prop name to `dangerously_allow_code`.


- `dangerously_allow_code` - remove from column definitions.  If you are using cell expressions or allowing raw html in
 components like Markdown, then it's only necessary to set `dangerously_allow_code=True` on the grid level. 

__2.0.0a3__


- `clickData` - change prop name to `cellRendererData`

- When using `cell Style`, functions or string expressions, change the AG Grid parameters to start with `params.`  
For example, change `colDef.headerName` to  `params.colDef.headerName`.


__2.0.0a4__


- `cellStyle` - move this prop to the `defaultColDef` or  `columnDefs` dict.


- If you see an error "Invalid prop for this component"  or "TypeError: The `dash_ag_grid.AgGrid` component ....received
 an unexpected keyword argument:...", do the following:
  - check spelling
  - check for prop name changes 
  - if it's `cellStyle`, move it to the column definitions
  - if it's a valid AG Grid prop, include it in the `dashGridOptions` dict
  
__2.0.0a5__

- No breaking changes

-----------------

#### Migrating from Dash Enterprise 1.3.0 - Breaking changes summary

These are additional breaking changes when migrating from the Dash Enterprise dash-ag-grid 1.3.0:


- Note - Currently Dash Design Kit does not update the style of the grid.  This will be fixed before the 2.0.0 release


- `theme` -  Use `className` instead.  See examples in the <dccLink href='https://dashaggrid.pythonanywhere.com/layout/themes' children='Themes' /> section of the docs.


- Set `dangerously_allow_code=True` to any apps that use raw html, such as the Markdown component,  or if you use functions as string expressions.  See more details below.

- `agGridColumns` component - Remove since it was deprecated in AG Grid v29

- `enableResetColumnState` change prop name  to `resetColumnState`
- `enableExportDataAsCsv` change prop name to `exportDataAsCsv`

- Also apply the Alpha version Breaking Changes from above.







-------------------------------


` `  
` `  


### Detailed Example:  Migrating demo app from 2.0.0a1


For an example of migrating from 2.0.0a1 to the current release,  see two versions of the same app in GitHub
- [demo_stock_portfolio - current version](https://github.com/AnnMarieW/dash-ag-grid/blob/dev/docs/demo_stock_portfolio.py)
- [demo_stock_portfolio - v2.0.0a1](https://github.com/AnnMarieW/dash-ag-grid/blob/dev/docs/demo_stock_portfolio_V2.0.0a1.py)


In the latest version you will notice that there is no need to set the grid to `dangerously_allow_code=True` This is because we are not using raw html in a Markdown component, and we are using functions instead of string expressions.


1. The new way to safely pass known JavaScript functions to the Grid:


`{"function": string}` where string is the body of the function as a string, or the variable name of a function defined in the `dashAgGridFunctions` namespace.    See more information in the [Beyond The Basics](https://dashaggrid.pythonanywhere.com/getting-started/beyond-the-basics) section.


For example, in  demo_stock_portfolio app:


```
# New way to use functions as props
columnDefs = [
    "valueFormatter": {"function": "Number(params.value).toFixed(2)"},   
]

# The old way used in 2.0.0a1 -- Don't do it this way.  It executes string expressions and is unsafe. 
columnDefs = [
    "valueFormatter": "Number(value).toFixed(2)",
    "dangerously_allow_html": True,
]
```


2.  When using `cell Style`, functions as props or string expressions, change the AG Grid parameters to start with `params.`  
For example, change `colDef.headerName` to  `params.colDef.headerName`. In the example above, note that `value` is now called `params.value`.



3. Prop name changes:  For example, `selectionChanged` is now called `selectedRows`
```
# New prop name  in current version
@app.callback(
    Output("candlestick", "figure"),
    Input("portfolio-grid", "selectedRows"),
)


# Old prop name in V2.0.0a1 
@app.callback(
    Output("candlestick", "figure"),
    Input("portfolio-grid", "selectionChanged"),
)
```


4.  Move `cellStyle` to column definitions.  The `cellStyle` prop was deleted in a4.  However it is still a valid prop
 and just needs to be moved to the column definitions instead of on the grid level.  

```
# old way
dag.AgGrid(
     cellStyle=cellStyle,
    # other props
)
# new way
dag.AgGrid(
     defaultColDef={"cellStyle": cellStyle},
    # other props
)
```


5.  New Prop:   `dashGridOptions`  

Only a subset of AG Grid props are defined in Dash. Valid AG Grid props can be passed to the grid in the `dashGridOptions` dict. 


In a4, many props that were just passed to AG Grid were removed, so if you see an error "Invalid prop for this component"  or "TypeError: The `dash_ag_grid.AgGrid` component ....received
 an unexpected keyword argument:...", do the following:
  - check spelling
  - check for prop name changes 
  - if it's `cellStyle`, move it to the column definitions
  - if it's a valid AG Grid prop, include it in the `dashGridOptions` dict
  


```
# old way
dag.AgGrid(
     rowSelection="multiple",
    # other props
)
# new way
dag.AgGrid(
     dashGridOptions={"rowSelection": "multiple"},
    # other props
)
```



"""

layout = html.Div(
    [
        make_md(text1),


    ],
)


