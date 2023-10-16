from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid Persistence",
)

text1 = """
# Persistence

Persistence works with AG Grid the same way as in other Dash components. See more information on persistence in the
 [Dash Documentation](https://dash.plotly.com/persistence).  Note that the grid must have an `id` to enable persistence.

This is from the <dccLink href="/getting-started/reference" children="Reference section"/>:

**`persisted_props`** (*list of strings*; default `['selectedRows']`): Properties whose user interactions will persist after refreshing the component or the page.

**`persistence`** (*boolean | string | number*; optional): Used to allow user interactions in this component to be persisted when the component - or the page - is refreshed. If `persisted` is truthy and hasn't changed from its previous value, a `value` that the user has changed while using the app will keep that change, as long as the new `value` also matches what was given originally. Used in conjunction with `persistence_type`.

**`persistence_type`** (*a value equal to: 'local', 'session', 'memory'*; default `'local'`): Where persisted user changes will be stored: memory: only kept in memory, reset on page refresh. local: window.localStorage, data is kept after the browser quit. session: window.sessionStorage, data is cleared once the browser quit.

### Example 1:

Here is an example with `selectedRows` persisted.  Note that selections persist after the page is refreshed.

"""

text2 = """

### Example 2:

In this example, we set the `filterModel` prop for persistence.  This maintains the user filter selections when the page is refreshed.
```
        dag.AgGrid(         
            persistence=True,
            persisted_props=["filterModel"]
            # other props
        ),
```
For more info on `filterModel` please see the 
 <dccLink href="filtering/filter-callbacks" children="Filter Callbacks" /> section of the docs


"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.persistence.persistence_selected_rows", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.filtering.filter_model1", make_layout=make_tabs),

    ],
)
