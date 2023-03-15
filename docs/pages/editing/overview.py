from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=1,
    description=app_description,
    title="Dash AG Grid Editing",
)

text1 = """
# Cell Editing

### Enable Editing
To enable Cell Editing for a Column use the editable property on the Column Definition.

 - `editable` (boolean) Set to `True` if this column is editable, otherwise `False`. Default: `False`

```
columnDefs = [
    {
        'field': 'athlete',
        # enables editing
        'editable': True
    }
]
```

To enable Cell Editing for all Columns, set `editable` to `True` in the default column definitions:

```
defaultColDef = {'editable': True}
```

"""

text2="""
### Triggering callback when cell values change

If the grid is editable, you can trigger a callback by using the `cellValueChanged` prop in a callback `Input()`.

- `cellValueChanged` (dict) with keys:
  - `rowIndex` (number) a row number
  - `rowId` - row id from the grid, this could be a number automatically, or set via getRowId
  - `data` (dict) - data object from the row
  - `oldValue`  - old value of the cell
  - `newValue` - new value of the cell
  - `colId` - the id of the column where the cell was changed

Try editing a cell of the grid to see the data included in the `cellValueChanged` prop
"""

text3="""
### Using `rowData` in a Callback 

When the grid is editable, the _state_ of the `rowData` is updated with user edits. Note that the  `rowData` prop cannot
 be used to trigger a callback. To access the updated row data in a callback, use the `rowData` prop in `State()` and
  use something else as the `Input()` to trigger the callback - such as a Button, or the grid's `cellValueChanged` prop.

```
# This won't work
@app.callback(
    Output("my-output", "children"),
    Input("grid", "rowData")
)
def update(row_data):
    # do something
```

Here we use the `n_clicks` prop of a button to trigger the callback:

```
# This will work
@app.callback(
    Output("my-output", "children"),
    Input("btn", "n_clicks"),
    State("grid", "rowData")
)
def update(n, row_data):
    # do something
```

The example below uses `cellValueChanged` prop to trigger the callback so that the figure is updated after each edit.

"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.editing.overview", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.editing.editing_callbacks", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.editing.editing_callbacks2", make_layout=make_tabs),
        # up_next("text"),
    ],
)
