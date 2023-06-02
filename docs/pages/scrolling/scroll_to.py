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

- `rowId` (string; optional): Id of the row to scroll to.

- `data` (dict; optional): Data of the row to scroll to.

- `rowPosition` ("top" | "bottom" | "middle"; optional):  Default "top".

- `column` (number; optional): column to scroll to, must be equal to one `field` in `columnDefs`.

- `columnPosition` ("auto" | "start" | "middle" | "end"; optional): position of the column in the grid after scrolling.  Default "auto".

NOTE: If any of `rowIndex`, `rowId`, and `data` are passed to `scrollTo` simultaneously only one of them will be used as all of them set the vertical scroll position.
The order of priority will be `rowIndex`, then `rowId`, and finally `data`.
           
"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.scrolling.scroll_to", make_layout=make_tabs),
        example_app("examples.scrolling.scroll_to_row_id", make_layout=make_tabs),
        example_app("examples.scrolling.scroll_to_row_data", make_layout=make_tabs),
        # up_next("text"),
    ],
)
