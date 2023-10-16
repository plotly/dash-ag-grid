from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=1,
    description=app_description,
    title="Dash AG Grid Row - Selection",
    name="Row selection single"
)

text1 = """

# Row Selection

Select a row by clicking on it. Selecting a row will remove any previous selection unless you hold down Ctrl while clicking. Selecting a row and holding down Shift while clicking a second row will select the range.


Configure row selection with the following properties:

- `rowSelection`: Type of row selection, set to either 'single' or 'multiple' to enable selection. 'single' will use single row selection, such that when you select a row, any previously selected row gets unselected. 'multiple' allows multiple rows to be selected.
- `rowMultiSelectWithClick`: Set to true to allow multiple rows to be selected with clicks. For example, if you click to select one row and then click to select another row, the first row will stay selected as well. Clicking a selected row in this mode will deselect the row. This is useful for touch devices where Ctrl and Shift clicking is not an option.
- `suppressRowDeselection`: Set to true to prevent rows from being deselected if you hold down Ctrl and click the row (i.e. once a row is selected, it remains selected until another row is selected in its place). By default the grid allows deselection of rows.
- `suppressRowClickSelection`: If true, rows won't be selected when clicked. Use, for example, when you want checkbox selection, and don't want to also select the row when the row is clicked.

##  Single Row Selection

The example below shows single row selection.

Property `rowSelection='single'` is set to enable single row selection. It is not possible to select multiple rows.
"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.selection.selection_single", make_layout=make_tabs),
        # up_next("text"),
    ],
)
