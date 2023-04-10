from dash import html, register_page
from utils.utils import app_description
from utils.other_components import make_md, make_feature_card


register_page(
    __name__, order=7, description=app_description, title="Dash AG Grid Troubleshooting Guide")


text1 = """
# Troubleshooting Guide


### 1. Error Messages - Invalid Props

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

Solution:
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
Solution:
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




### 2. It's not working -- check the browser console for error messages 

if you are using raw HTML in Markdown or other components that accept raw HTML, or if you are using string
 [expressions](https://www.ag-grid.com/react-data-grid/cell-expressions/) rather than the safer method of validated functions, you must set `dangerously_allow_code=True` 
 otherwise you will see the following message in the browser console:

![console_error](https://user-images.githubusercontent.com/72614349/230785808-8c32d184-29f5-458e-8e78-9ed1d73757d8.png)


Solution 1:

Before setting `dangerously_allow_code=True`, please try other ways to make your app more secure.  For more info on
 using functions, see the <dccLink href='/getting-started/beyond-the-basics' children='Beyond the Basics' /> section.  Instead of rendering raw HTML,
  consider using custom <dccLink href='/components/cell-renderer' children='Components.' />


Solution 2:
```
dag.AgGrid(
    `dangerously_allow_code=True`,
    # other props
)
```


` `  
` `  


### 3. It's not working --  no error message

In Dash we depend on the dev tools to alert us to errors  However if prop is misspelled in one of the dicts that pass
 props to the grid such as `columnDefs`, then there will be no error message and it "fails silently" 
  
   
Solution:
Double check the spelling of the prop and make sure it's in the correct Dash container prop.

` `  
` `  


### 4. Debugging custom functions with `log()` 

Please see the  <dccLink href='/getting-started/beyond-the-basics' children='Beyond the Basics' /> section for information
on debugging functions with `log()`


"""

layout = html.Div(
    [
        make_md(text1),
    ],
)


