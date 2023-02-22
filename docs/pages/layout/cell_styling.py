from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description

register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid Layout and Style",
)

text1 = """
# Cell Styles
Cell customisation is done a the column level via the column definition. You can mix and match the following mechanisms:

- Cell Style: Providing a CSS style for the cells.
- Cell Class: Providing a CSS class for the cells.

Some cell styles may also be overridden with CSS variables. See the full [CSS variables reference](https://www.ag-grid.com/react-data-grid/global-style-customisation-variables/).

### Cell Style
Used to provide CSS styles directly (not using a class) to the cell. Can be either an object of CSS styles, or conditional formatting using `styleConditions`

```
columnDefs = [
    # these column will have the same style for each row
    {    
        'field': 'col1',
        'cellStyle': {'color': 'red', 'background-color': 'green'}
    },
    # This column uses Bootstrap class names
    {    
        'field': 'col2',
        'cellClass': "bg-primary text-white"
    },
]
```


### Conditional cell style

 - `styleConditions` (list of dicts). Each dict has keys of "condition" and "style". The value of the "condition" key is a 
 JavaScript function that when True the value of the "style" key will be applied.
 
 In this example, cell values of 72000 will have orange text color.

```
cellStyle={
    "styleConditions": [
        {"condition": "params.value == 72000", "style": {"color": "orange"}},       
    ]
}

```

The properties available are:
- `column` The columns
-  `colDef` Te colDef associated with the column for this cell
- `value`  The value to be rendered    
- `data` The data associated with this row from rowData. Data is undefined for row groups.
- `node` The RowNode associated with this row
- `rowIndex` The index of the row
- `api` The grid api.
- `columnApi` The column api.
- `context` Application context as set on gridOptions.context.
"""

text2 = """
### Refresh of Styles
If you refresh a cell, or a cell is updated due to editing, the `cellStyle`, `cellClass`are applied again. This has the following effect:

- `cellStyle`: All new styles are applied. If a new style is the same as an old style, the new style overwrites the old style. If a new style is not present, the old style is left (the grid will NOT remove styles).
- `cellClass`: All new classes are applied. Old classes are not removed so be aware that classes will accumulate. If you want to remove old classes, then use `cellClassRules`.
- `cellClassRules`: Note!  `cellClassRules` is not yet available in dash-ag-grid.

If you are using cellStyle to highlight changing data, then please take note that grid will not remove styles. For example if you are setting text color to 'red' for a condition, then you should explicitly set it back to default eg 'black' when the condition is not met. Otherwise the highlight will remain once it's first applied.

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


"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.layout.cell_styling", make_layout=make_tabs),
        # up_next("text"),
    ],
)
