from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid Editing",
)



text1 = """
# Enter Key Navigation

By default pressing Enter will start editing on a cell, or stop editing on an editing cell. It will not navigate to the cell below.

To allow consistency with Excel the grid has the following properties:

- `enterMovesDown`: Set to `True` to have Enter key move focus to the cell below if not editing. The default is Enter key starts editing the currently focused cell.
- `enterMovesDownAfterEdit`: Set to `True` to have Enter key move focus to the cell below after Enter is pressed while editing. The default is editing will stop and focus will remain on the editing cell.
The example below demonstrates the focus moving down when Enter is pressed.

"""


text2 = """
### Single-Click Editing
The default is for the grid to enter editing when you Double-Click on a cell. To change the default so that a single-click starts editing, set the property gridOptions.singleClickEdit = true. This is useful when you want a cell to enter edit mode as soon as you click on it, similar to the experience you get when inside Excel.

It is also possible to define single-click editing on a per-column basis using colDef.singleClickEdit = true.

The grid below has singleClickEdit = true so that editing will start on a cell when you single-click on it.

"""

text3 = """
>
> Cell Editing can also be performed via Cell Editor Components; please see Cell Editor Components for more information.
>

"""


layout = html.Div(
    [

        make_md(text1),
        example_app("examples.editing.start_stop_editing", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.editing.start_stop_editing2", make_layout=make_tabs),
        make_md(text3)

        # up_next("text"),
    ],
)
