from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid Editing with callbacks",
    name="Editing & Dash callbacks"
)


text1 = """
# Editing & Dash Callbacks

Use the following Dash props to access edited data in a callback:
 - `cellValueChanged`
 - `RowData`
 - `virtualRowData`
 - `cellRendererData` (see the components section)

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






text2="""
### Using `rowData` or `virtualRowData` in a Callback 

When the grid is editable, the _state_ of the `rowData` and `virtualRowData` is updated with user edits. Note that these props cannot
 be used to trigger a callback. To access the updated row data in a callback, use the `rowData` or `virtualRowData` prop in `State()` and
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
        example_app("examples.editing.editing_callbacks", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.editing.editing_callbacks2", make_layout=make_tabs),
        # up_next("text"),
    ],
)
