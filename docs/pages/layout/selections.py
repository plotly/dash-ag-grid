from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description

register_page(
    __name__,
    order=5,
    description=app_description,
    title="Dash AG Grid Layout and Style - Customising Selections",
)

text1 = """

# Customising Selections
Control how selected rows and cells appear.

### Row Selections
When row selection is enabled, you can set the color of selected rows using --ag-selected-row-background-color. If your grid uses alternating row colours we recommend setting this to a semi-transparent colour so that the alternating row colours are visible below it.

```
.ag-theme-alpine {
    /* bright green, 10% opacity */
    --ag-selected-row-background-color: rgb(0, 255, 0, 0.1);
}
```
"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.layout.selections", make_layout=make_tabs),
        # up_next("text"),
    ],
)
