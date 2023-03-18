from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description

register_page(
    __name__,
    order=7,
    description=app_description,
    title="Dash AG Grid Layout and Style",
)

text1 = """
# Customising Borders
Control the borders around rows, cells and UI elements.

The grid exposes many variables for customising borders. For each kind of border, the style and colour are controlled by two different variables. For a given kind of border, --ag-borders-{kind} should be set to a CSS border style and width (e.g. solid 1px) or none to disable; and --ag-{kind}-border-color can be set to a CSS border color e.g. red.

These variables use Variable Cascading to allow you to enable/disable all borders quickly or fine tune the borders shown. In the list below, setting a parent item in the list will set the default value for all children:

- `--ag-borders` and `--ag-border-color` - the master control for all borders in the grid
    - `--ag-borders-critical` and `--ag-critical-border-color` - borders that are important for UX even on grids without many borders - for example to differentiate pinned from regular columns. Themes that disable borders generally may want to enable these borders
    - `--ag-borders-secondary` and `--ag-secondary-border-color` - borders separating UI elements within components.
        - `--ag-borders-input` and `--ag-secondary-border-row` - borders around text inputs
- `--ag-row-border-style`, `--ag-row-border-color` and `--ag-row-border-width` - borders separating the grid rows. Row borders are configured independently of other border properties.


### Example
```
.ag-theme-alpine {
    /* disable all borders */
    --ag-borders: none;
    /* then add back a border between rows */
    --ag-row-border-style: dashed;
    --ag-row-border-width: 5px;
    --ag-row-border-color: rgb(150, 150, 200);
}
```

"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.layout.borders", make_layout=make_tabs),
        # up_next("text"),
    ],
)
