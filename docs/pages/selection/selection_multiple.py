from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid - Row Selection",
    name="Row selection multiple"
)

text1 = """

# Multiple Row Selection
The example below shows multi-row selection.

Property `rowSelection='multiple'` is set to enable multiple row selection. Selecting multiple rows can be achieved by holding down Ctrl and mouse clicking the rows. A range of rows can be selected by using Shift.
"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.selection.selection_multiple", make_layout=make_tabs),
        # up_next("text"),
    ],
)
