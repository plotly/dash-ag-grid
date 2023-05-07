from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid Filtering with Dash Callbacks",
)

text1 = """
# Filter Model & Dash Callbacks

The filter model represents the state of filters for all columns and has the following structure:
```
# Sample filterModel
{
    'athlete': {
        'filterType': 'text',
        'type': 'startsWith',
        'filter': 'mich'
    },
    'age': {
        'filterType': 'number',
        'type': 'lessThan',
        'filter': 30
    }
}
```

This is useful if you want to set the filter initially, or save the filter state and apply it at a later stage.
 It is also useful when you want to pass the filter state to the server for filtering in a Dash callback,.

### Example 1:  Setting the Filter Model in a callback

This example demonstrates
 - Setting the `filterModel` in a callback with the "Update Filter" button
 - Using persistence to maintain user selections when the page is refreshed
"""

text2 = """

### Example 2:  Setting the Filter Model when the app starts

This example demonstrates 
 - Settings the filter when the app starts
 - Accessing  the `filterModel` in a callback

"""


text3 = """
### Example 3:  Filtered and sorted data

This example demonstrates using the `virtualRowData` in a callback to access filtered and sorted data in a callback..
Note - Use `rowData` to get the original data.

"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.filtering.filter_model1", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.filtering.filter_model2", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.filtering.virtualrowdata", make_layout=make_tabs),
    ],
)
