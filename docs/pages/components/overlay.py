from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=4,
    description=app_description,
    title="Dash AG Grid Components - Custom Overlay",

)

text1 = """
# Overlay Component

Overlay components allow you to add your own overlays to AG Grid. Use these when the provided overlays do not meet your requirements.


### Custom Loading Overlay

The example below demonstrates how to provide custom loading message to the grid. Notice the following:

- The Custom Loading Component is defined in the `dashAgGridComponentFunctions.js` file in the `assets` folder.
- The Custom Loading Component is supplied by name via `loadingOverlayComponent`.  
- The Custom Tooltip Parameters (for text color and the message) are supplied using `loadingOverlayComponentParams`.

"""

text2 = """
### Custom No Rows Overlay


The example below demonstrates how to provide custom no rows message to the grid. Notice the following:

- The Custom No Rows Component is defined in the `dashAgGridComponentFunctions.js` file in the `assets` folder.
- The Custom No Rows Component is supplied by name via `noRowsOverlayComponent`.  
- The Custom Tooltip Parameters (for text color and the message) are supplied using `noRowsOverlayComponentParams`.




"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.components.overlay_loading", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.components.overlay_norows", make_layout=make_tabs),

    ],
)
