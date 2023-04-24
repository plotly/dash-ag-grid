from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=8,
    description=app_description,
    title="Dash AG Grid -  Row Dragging",
)

text1 = """

# Row Dragging
Row dragging is used to rearrange rows by dragging the row with the mouse. To enable row dragging, set the column property rowDrag on one (typically the first) column.

## Enabling Row Dragging

`rowDrag` boolean Set to true to allow row dragging. Default: false

To enable row dragging on all columns, set the column property `rowDrag = True` on one (typically the first) column.

```
const columnDefs = [
    # make all rows draggable
    { 'field': 'athlete', 'rowDrag': True },
]
```
There are two ways in which row dragging works in the grid, managed and unmanaged:

- Managed Dragging: This is the simplest, where the grid will rearrange rows as you drag them.
- Unmanaged Dragging: This is more complex and more powerful. The grid will not rearrange rows as you drag. Instead the application is responsible for responding to events fired by the grid and rows are rearranged by the application.

## Managed Dragging
In managed dragging, the grid is responsible for rearranging the rows as the rows are dragged. Managed dragging is enabled with the property rowDragManaged=true.

The example below shows simple managed dragging. The following can be noted:

The first column has `rowDrag=True` which results in a draggable area being included in the cell.
The property rowDragManaged is set, to tell the grid to move the row as the row is dragged.
If a sort (click on the header) or filter (open up the column menu) is applied to the column, the draggable icon for row dragging is hidden. This is consistent with the constraints explained after the example.
"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.rows.row_dragging", make_layout=make_tabs),
        # up_next("text"),
    ],
)
