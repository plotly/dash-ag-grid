from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=4,
    description=app_description,
    title="Dash AG Grid Components - Custom Tooltip",

)

text1 = """
# Tooltip Component

Tooltip components allow you to add your own tooltips to the grid's column headers and cells. Use these when the provided tooltip component or the default browser tooltip do not meet your requirements.

See an example of a simple text tooltip for column headers in the columns section.

### Custom Tooltip

The example below demonstrates how to provide custom tooltips to the grid. Notice the following:

- The Custom Tooltip Component is defined in the `dashAgGridComponentFunctions.js` file in the `assets` folder.
- The Custom Tooltip Component is supplied by name via `tooltipComponent`.  
- The Custom Tooltip Parameters (for tooltip background color) are supplied using `tooltipComponentParams`.
- Tooltips are displayed instantly by setting `tooltipShowDelay` to 0.
- Tooltips hide in 2000ms by setting `tooltipHideDelay` to 2000.
- Tooltip is shown for the ticker column

"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.components.tooltip", make_layout=make_tabs),

    ],
)
