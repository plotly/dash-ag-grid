from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid Import Export - clipboard",
)

text1 = """
# Clipboard

The AG Grid clipboard is an Enterprise feature.  Learn more in the [AG Grid docs](https://www.ag-grid.com/react-data-grid/clipboard/)

If you are using AG Grid community, then you can get some limited clipboard functionality by using the `dcc.Clipboard` component.

### Example 1
This example demonstrates getting the rowData from the selected rows in a callback, and returning it to the `content`
 prop of the `dcc.Clipboard`.  We use the pandas `to_string` method to format the dataframe as a string.  You could also 
 format the data in different ways, for example `to_markdown`, `to_csv` or `to_excel`  See the
pandas docs for more information.  Note - do not use the pandas `to_clipboard` function because it copies to the server's 
clipboard and will fail in production.

"""

text2 = """
### Example 2

In this example we also use the column state when formatting the clipboard data.  Try changing the column order,
 (by clicking on the heading and dragging to a new position), then select some rows and click the copy to clipboard button.
   You will see that the pasted data will have the columns in the same order as displayed in the grid.
"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.import_export.clipboard", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.import_export.clipboard_colstate", make_layout=make_tabs),
        #  up_next("text"),
    ],
)
