from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid Infinite Scroll",
)

text1 = """
# Infinite Row Model

> If you are an Enterprise user you should consider using the [Server-Side Row Model](https://www.ag-grid.com/react-data-grid/server-side-model/) instead of the Infinite Row Model. It offers the same functionality with many more features.


Infinite scrolling allows the grid to lazy-load rows from the server depending on what the scroll position is of the grid. In its simplest form, the more the user scrolls down, the more rows get loaded.

The grid will have an 'auto extending' vertical scroll. That means as the scroll reaches the bottom position, the grid will extend the height to allow scrolling even further down, almost making it impossible for the user to reach the bottom. This will stop happening once the grid has extended the scroll to reach the last record in the table.

### Turning on Infinite Scrolling

```
dag.AgGrid(
    rowModelType="infinite",
    # other props
)
```

### Datasource Interface

In a nutshell, every time the grid wants more rows, it will call `getRows()` on the datasource. Use the
 `getRowsRequest` prop as the `Input` of the Dash callback. The callback responds with the rows requested.  Use
  `getRowsResponse` as the `Output` of the callback to provide data to the grid.


- `getRowsRequest` (dict; optional): Infinite Scroll, Datasource interface. `getRowsRequest` is a dict with keys:

  - `context` (boolean | number | string | dict | list; optional): The grid context object.

  - `endRow` (number; optional): The first row index to NOT get.

  - `failCallback` (*optional): Callback to call when the request fails.

  - `filterModel` (dict*; optional): If filtering, what the filter model is.

  - `sortModel` (list of dicts; optional): If sorting, what the sort model is.

  - `startRow` (number; optional): The first row index to get.

  - `successCallback` (*optional): Callback to call when the request is successful.


- `getRowsResponse` (dict*; optional): Serverside model data response object. `getRowsResponse` is a dict with keys:

  - `rowCount` (number; optional): Current row count, if known.

  - `rowData` (list of dicts; optional): Data retreived from the server.

  - `storeInfo` (boolean | number | string | dict | list; optional): Any extra info for the grid to associate with this load.

### Example 1:  Infinite Scroll Simple Example

Tip - You can also use the keyboard to navigate. Click on a row to focus the grid.  Then use `page up` and `page down` keys to scroll by page.  Use the `home` and
 `end` keys to quickly go to the first and last row of the data.
"""

text2 = """

### Aggregation and Grouping
Aggregation and grouping are not available in infinite scrolling. This is because to do so would require the grid knowing the entire dataset, which is not possible when using the Infinite Row Model. If you need aggregation and / or grouping for large datasets, check the Server-Side Row Model for doing aggregations on the server-side.

### Sorting & Filtering
The grid cannot do sorting or filtering for you, as it does not have all of the data. Sorting or filtering must be done on the server-side. For this reason, if the sort or filter changes, the grid will use the datasource to get the data again and provide the sort and filter state to you.

### Example 2: Infinite Scroll with Sort and Filter
"""

text3 = """

### Example 3 Infinite Scroll with Pagination

Pagination in AG Grid is supported in all the different row models.  Here is an example with the Infinite Row Model.

"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.scrolling.infinite_scroll", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.scrolling.infinite_scroll_sort_filter", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.scrolling.infinite_scroll_pagination", make_layout=make_tabs),
        # up_next("text"),
    ],
)
