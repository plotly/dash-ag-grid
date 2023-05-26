from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=6,
    description=app_description,
    title="Scroll to row",
)

text1 = """

# Scroll to row

You can use the prop `scrollToRow` to scroll to a specific row given its index. 
"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.scrolling.scroll_to_row", make_layout=make_tabs),
        # up_next("text"),
    ],
)
