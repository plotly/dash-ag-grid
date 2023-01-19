from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=4,
    description=app_description,
    title="Dash AG Grid Selection",
)

text1 = """

# Checkbox Row Selection

To include checkbox selection for a column, set the attribute 'checkboxSelection' to true on the column definition. You can set this attribute on as many columns as you like, however it doesn't make sense to have it in more than one column in a table.

"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.selection.selection_checkbox", make_layout=make_tabs),
        # up_next("text"),
    ],
)
