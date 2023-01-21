from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=3,
    description=app_description,
    title="Dash AG Grid Selection",
)

text1 = """

#  Multi Select Rows With Click
The example below shows multi-select with click. Clicking multiple rows will select a range of rows without the need for Ctrl or Shift keys. Clicking a selected row will deselect it. This is useful for touch devices where Ctrl and Shift clicks are not available.

Property `rowMultiSelectWithClick=True` is set to enable multiple row selection with clicks.
Clicking multiple rows will select multiple rows without needing to press Ctrl or Shift keys.
Clicking a selected row will deselect that row.
"""


layout = html.Div(
    [
        make_md(text1),
        example_app(
            "examples.selection.selection_multiple_click", make_layout=make_tabs
        ),
        # up_next("text"),
    ],
)
