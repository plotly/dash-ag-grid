from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=0,
    description=app_description,
    title="Dash AG Grid - Cell Selection",
)

text1 = """

# Cell Selection

You can trigger a Dash callback by clicking on a cell.  In the dash callback, use the `cellClicked` prop

`cellClicked` is a dict with keys:

- `colId` (boolean | number | string | dict | list; optional): column where the cell was clicked.

- `rowId` (boolean | number | string | dict | list; optional): Row Id from the grid, this could be a number automatically, or set via getRowId.

- `rowIndex` (number; optional): rowIndex, typically a row number.

- `timestamp` (boolean | number | string | dict | list; optional): timestamp of last action.

- `value` (boolean | number | string | dict | list; optional): value of the clicked cell.

"""

text2 = """
### Cell selection with Custom Components

You can also trigger Dash callback with custom components.  For more information, please see:

- <dccLink href='' children='Cell Renderers' /> for creating custom buttons and other custom components

- <dccLink href='' children='Row Menu Component' /> for a custom component that allow the user to select several options when clicking on a cell.


"""


text3 = """
### Cell selection with Double click

In the same way you can use the prop `cellDoubleClicked` to select cells double clicking

"""
layout = html.Div(
    [
        make_md(text1),
        example_app("examples.getting_started.quickstart", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.selection.double_clicked_cell", make_layout=make_tabs),
        # up_next("text"),
    ],
)
