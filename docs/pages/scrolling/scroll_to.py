from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=6,
    description=app_description,
    title="Scroll to",
)

text1 = """

# Scroll to 

You can use the prop `scrollTo` to scroll to a specific position. 

`scrollTo` is a dict with keys:

- `rowIndex` (number; optional): rowIndex, typically a row number, to scroll to.

- `rowIndexPosition` ("top" | "bottom" | "middle"; optional):  Default "top".

- `column` (number; optional): column to scroll to, must be equal to one `field` in `columnDefs`.

- `columnPosition` ("auto" | "start" | "middle" | "end"; optional): position of the column in the grid after scrolling.  Default "auto".
"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.scrolling.scroll_to", make_layout=make_tabs),
        # up_next("text"),
    ],
)
