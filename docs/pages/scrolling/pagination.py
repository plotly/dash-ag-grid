from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=1,
    description=app_description,
    title="Dash AG Grid Pagination",
)

text1 = """

# Row Pagination
 Pagination allows the grid to paginate rows, removing the need for a vertical scroll to view more data.
 
 To enable pagination set the grid property `pagination=True`.


### Example: Enable Pagination
The first example shows the default settings for pagination.
"""

text2 = """
### Example: Auto Page Size

The example above shows Auto Page size.  When you set `paginationAutoPageSize`=True the grid will automatically show as
 many rows in each page as it can fit. If you resize the display area of the grid, the page size automatically changes. 
 Note that there are no vertical scroll bars in this example.
 

### Example: Setting Page Size

The example below sets the number of rows to display in each page with `paginationPageSize`
"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.scrolling.row_pagination", make_layout=make_tabs),
        make_md(text2),
        example_app(
            "examples.scrolling.row_pagination_page_size", make_layout=make_tabs
        ),
        # up_next("text"),
    ],
)
