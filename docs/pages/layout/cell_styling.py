from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description

register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid - Styling Cells",
)

text1 = """
# Styling Cells
Cell customisation is done a the column level via the column definition. You can mix and match the following mechanisms:

- Cell Style: Providing a CSS style for the cells.
- Cell Class: Providing a CSS class for the cells.
- Cell Class Rules: Providing rules for applying CSS classes.

Some cell styles may also be overridden with CSS variables. See the full [CSS variables reference](https://www.ag-grid.com/react-data-grid/global-style-customisation-variables/).

### Cell Style
- `cellStyle` Used to provide CSS styles directly (not using a class) to the cell. Can be either a dict of CSS styles, or 
a dict with keys `styleConditions` and `defaultStyle`.
    
- `styleConditions` (list of dicts). Each dict has keys of "condition" and "style". The value of the "condition" 
    key is a  condition that when `True` the value of the "style" key will be applied.  Note:  `styleConditions` is
     a Dash prop only and you will not find this in the official AG Grid docs.     
 - `defaultStyle` (dict).  The default style for all cells in the table. Note:  `defaultStyle` is a Dash prop only and you will not find this in the official AG Grid docs.
 
 
Example Snippets:

Using CSS styles directly:
```
columnDefs = [
    # these column will have the same style for each row
    {    
        'field': 'col1',
        'cellStyle': {'color': 'red', 'background-color': 'green'}
    },
]
```

Using default style- when set on the grid level, the text color of all the cells in the grid will be "blue":
```
 cellStyle={"defaultStyle": {"color": "blue"}},
```

Conditional Formatting - In this snippet, cell values of 72000 will have orange text color:

```
cellStyle={
    "styleConditions": [
        {"condition": "params.value == 72000", "style": {"color": "orange"}},       
    ]
}
```

The params available for use in "condition":
- `column` The columns
- `colDef` Te colDef associated with the column for this cell
- `value`  The value to be rendered    
- `data` The data associated with this row from rowData. Data is undefined for row groups.
- `node` The RowNode associated with this row
- `rowIndex` The index of the row
- `api` The grid api.
- `columnApi` The column api.
- `context` Application context as set on gridOptions.context.


### Cell Class
 - `cellClass` Provides a class for the cells in this column. 

```
columnDefs = [
    # This column uses Bootstrap class names
    {    
        'field': 'col2',
        'cellClass': "bg-primary text-white"
    },
]
```

### Cell Class Rules

- `cellClassRules` Rules which can be applied to include certain CSS classes.  

The following snippet is `cellClassRules` applied to a year column:
```
columnDefs = [
    {
        'field': 'year',
        'cellClassRules': {
            # apply background color primary to 2008
            'bg-primary': 'params.value === 2008',
            # apply background color secondary to  2004
            'bg-secondary': 'params.value === 2004',
            # apply background color success  to 2000
            'bg-success': 'params.value === 2000',
        }
    }
]
```


"""

text2 = """
### Refresh of Styles
If you refresh a cell, or a cell is updated due to editing, the `cellStyle`, `cellClass`are applied again. This has the following effect:

- `cellStyle`: All new styles are applied. If a new style is the same as an old style, the new style overwrites the old style. If a new style is not present, the old style is left (the grid will NOT remove styles).
- `cellClass`: All new classes are applied. Old classes are not removed so be aware that classes will accumulate. If you want to remove old classes, then use `cellClassRules`.
- `cellClassRules`:  Rules that return true will have the class applied the second time. Rules that return false will have the class removed second time.

If you are using cellStyle to highlight changing data, then please take note that grid will not remove styles. For example if you are setting text color to 'red' for a condition, then you should explicitly set it back to default eg 'black' when the condition is not met. Otherwise the highlight will remain once it's first applied.

```
# unsafe, the red will stay after initially applied
cellStyle={
    "styleConditions": [
        {"condition": "params.value > 80", "style": {"color": "red"}},       
    ]
}

# safe, to black will override the red when the condition is not true
cellStyle={
    "styleConditions": [
        {"condition": "params.value > 80", "style": {"color": "red"}},   
        {"condition": "params.value <= 80", "style": {"color": "black"}},       
    ]
}
```

"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.layout.cell_styling", make_layout=make_tabs),
        make_md(text2)
        # up_next("text"),
    ],
)
