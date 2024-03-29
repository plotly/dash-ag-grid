from dash import html, register_page
from utils.utils import app_description
from utils.other_components import make_md, make_feature_card


register_page(
    __name__, order=7, description=app_description, title="Dash AG Grid Troubleshooting Guide")


text1 = """
# Troubleshooting Guide


### 1. Dash Error Messages - Invalid Props

> "Invalid prop for this component"

> "TypeError: The `dash_ag_grid.AgGrid` component ....received an unexpected keyword argument:..."

This is normally a helpful error message in Dash.  It means that you have either misspelled a prop name, or you are
 trying to use a prop that is not valid for the component.  However, with dash-ag-grid, this may not be the case.

The [AG Grid API](https://www.ag-grid.com/react-data-grid/grid-options/) has hundreds of props - only a subset are defined as Dash props.  You will see this error if you try
 to use a valid AG Grid prop that is not specifically defined in the dash-ag-grid component.  
 
In most cases, you can still use the prop.  It just needs to be included in the appropriate container to be passed from Dash to the grid. 
 
For example, `rowSelection` is a grid level prop in AG Grid, but `rowSelection` is not defined in dash-ag-grid.  If you try to use it like this, you will get an error message:

```
# Wrong way
dag.AgGrid(
    rowSelection="multiple", 
    # other props
)
```

__Solution:__
Valid grid level props can be passed to the grid in the `dashGridOptions` container like this:
```
# Correct way
dag.AgGrid(
     dashGridOptions={"rowSelection":"multiple"},
     # other props
)
```

It's the same for column level props.  For example, if you try to use `sortable=True` on the grid level, you will see the error:


```
# Wrong way
dag.AgGrid(
    sortable=True, 
    # other props
)
```
__Solution:__
Valid column level props can be passed to the grid in the `defaultColDef` or the `columnDefs` container like this:
```
# Correct way using defaultColDef
dag.AgGrid(
     defaultColDef={"sortable":True},
     # other props
)

# Correct way using columnDefs
dag.AgGrid(
    columnDefs = [
        { 'field': 'athlete' , 'sortable': True },
        { 'field': 'sport' },
        { 'field': 'age' },
    ] 
     # other props
)
```


> If you see the "invalid prop" error message, do the following:
  - Check spelling to make sure the prop is a valid AG Grid prop or Dash prop
  - If you are migrating from an alpha version of dash-ag-grid, check the Migration Guide for prop name and other changes 
  - If it's a valid AG Grid prop, include it in the appropriate container:
     - `dashGridOptions` dict for grid level props
     - `columndDefs` or `defaultColDef` for column level props
    


` `  
` `  




### 2. Check the browser console for error and warning messages 

You often won't get an error message from Dash if something in the grid is not working.  Errors handled by AG Grid
 will be displayed as messages in the browser console.   Be sure to check for both warning messages and error messages.

For example if you use an invalid prop in `columnDefs` or `defaultColDef` you will not get an error message from 
   Dash.  If you open your browser console, you will see a warning message like the image below. Note that invalid 
   props will be ignored, and will seem to "fail silently".

![console_warning](https://user-images.githubusercontent.com/72614349/233742767-efbebbdf-7f81-42cf-8efb-35972eaa7f62.png)

if you are using raw HTML in Markdown or other components that accept raw HTML, or if you are using string
 [expressions](https://www.ag-grid.com/react-data-grid/cell-expressions/) rather than the safer method of validated functions, you must set `dangerously_allow_code=True` 
 otherwise you will see the following message in the browser console:

![console_error](https://user-images.githubusercontent.com/72614349/230785808-8c32d184-29f5-458e-8e78-9ed1d73757d8.png)


__Solution 1:__

Before setting `dangerously_allow_code=True`, please try other ways to make your app more secure.  For more info on
 using functions, see the <dccLink href='/getting-started/beyond-the-basics' children='Beyond the Basics' /> section.  Instead of rendering raw HTML,
  consider using custom <dccLink href='/components/cell-renderer' children='Components.' />


__Solution 2:__
```
dag.AgGrid(
    `dangerously_allow_code=True`,
    # other props
)
```


` `  
` `  


### 3.  The grid is gone!

Does the grid look like this?

![no_grid](https://user-images.githubusercontent.com/72614349/230976812-6025617c-bf3d-47d3-9b95-686288feb73f.png)

__Solution:__ 
The grid must always have a theme class set on its container, whether this is a provided theme or your own. The default
 is `className="ag-theme-alpine"`.  If you set the grid's `className` prop to something else, be sure to include the theme.
 

For more information see the <dccLink href="/layout/themes" children="Themes" /> section of the docs.
```
# Wrong way:
dag.AgGrid(
    className="m-4",
    # other props
)


# Correct way:
dag.AgGrid(
    className="ag-theme-alpine m-4",
    # other props
)

# Another Correct way:
html.Div(
    dag.AgGrid(...),
    className="m-4",
)

```


` `  
` `  
  
### 4. Spaces in field names

If your field names contain spaces, then you cannot use the dot notation  (ie `params.data.date`)

__solution:__  
Use square brackets around the field name. (ie `params.data['invoice date']`)

For example, if your data looks like:

```
rowData = [
    {'invoice date': '12-31-2023', 'price': 100.00}
    # other rows
]
```


```
# wrong way
 "valueGetter": {"function": "d3.timeParse('%Y-%m-%d')(params.data.invoice date)"}

# wrong way
myDate="invoice date"
"valueGetter": {"function": "d3.timeParse('%Y-%m-%d')(params.data.myDate)"}

# right way
"valueGetter": {"function": "d3.timeParse('%Y-%m-%d')(params.data['invoice date'])"}

```



` `  
` `  

### 5. Debugging custom functions with `log()` 

Please see the  <dccLink href='/getting-started/beyond-the-basics' children='Beyond the Basics' /> section for information
on debugging functions with `log()`



` `  
` ` 
### 6. Other

For other issues:
  - Search the [Dash Community Forum](https://community.plotly.com/)
  - Check for dash-ag-grid GitHub [issues](https://github.com/plotly/dash-ag-grid/issues)
  - Check [Ag Grid issues](https://www.ag-grid.com/pipeline/)

If you can't find the answer, please post a question on the Dash community forum and include a complete minimal example with
 sample data that replicates the issue.


"""

layout = html.Div(
    [
        make_md(text1),
    ],
)



