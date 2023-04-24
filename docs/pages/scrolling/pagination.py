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

The example above shows Auto Page size.  When you set `paginationAutoPageSize=True` the grid will automatically show as
 many rows in each page as it can fit. If you resize the display area of the grid, the page size automatically changes. 
 Note that there are no vertical scroll bars in this example.
 

### Example: Setting Page Size

The example below sets the number of rows to display in each page with `paginationPageSize`.
"""

text3 = """
### Example: Custom Pagination Controls

If you would like to provide your own pagination controls, do the following:
 - Set `pagination=True` to enable pagination.
 - Set `suppressPaginationPanel=True` so the grid will not show the standard navigation controls for pagination.
 - Provide your own  pagination component.

```
dag.AgGrid(
    dashGridOptions={"pagination": True, "suppressPaginationPanel": True}
    # other props
)

```


Use the following Dash props to control the pagination.

- `paginationGoTo` (a value equal to: 'first', 'last', 'next', 'previous', null | number; optional): When pagination is enabled, this will navigate to the specified page.

- `paginationInfo` (dict; optional): When pagination is enabled, this will be populated with info from the pagination API. `paginationInfo` is a dict with keys:

    - `currentPage` (number; optional)

    - `isLastPageFound` (boolean; optional)

    - `pageSize` (number; optional)

    - `rowCount` (number; optional)

    - `totalPages` (number; optional)

In the example below you can see how this works. 

- The pagination component is `dbc.Pagination` from the dash-bootstrap-components library
- We use `paginationGoTo` as the output of the callback to go to the page selected.
- We use  `totalPages ` in the `paginationInfo` dict to update the dbc.Pagination buttons when the number of pages changes, such as when filtering data.

The example also sets property `suppressScrollOnNewData=True`, which tells the grid to NOT scroll to the top when the page changes.


"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.scrolling.row_pagination", make_layout=make_tabs),
        make_md(text2),
        example_app(
            "examples.scrolling.row_pagination_page_size", make_layout=make_tabs
        ),
        # make_md(text3),
        # example_app("examples.scrolling.row_pagination_custom", make_layout=make_tabs),
        # up_next("text"),
    ],
)
