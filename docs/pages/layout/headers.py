from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description

register_page(
    __name__,
    order=5,
    description=app_description,
    title="Dash AG Grid Layout and Style",
)

text1 = """
# Customising the Header
Style grid header cells and column groups.

The grid exposes many CSS variables starting `--ag-header-*` for customising header appearance, and when these are not enough you can use CSS classes, in particular `ag-header`, `ag-header-cell`, `and ag-header-group-cell`:

``````
.ag-theme-alpine {
    --ag-header-height: 30px;
    --ag-header-foreground-color: white;
    --ag-header-background-color: black;
    --ag-header-cell-hover-background-color: rgb(80, 40, 140);
    --ag-header-cell-moving-background-color: rgb(80, 40, 140);
}
.ag-theme-alpine .ag-header {
    font-family: cursive;
}
.ag-theme-alpine .ag-header-group-cell {
    font-weight: normal;
    font-size: 22px;
}
.ag-theme-alpine .ag-header-cell {
    font-size: 18px;
}
```
"""

text2 = """
# Header Column Separators and Resize Handles

Header Column Separators appear between every column, whereas Resize Handles only appear on resizeable columns (Group 1 in the example above).

```
ag-theme-alpine {
    --ag-header-column-separator-display: block;
    --ag-header-column-separator-height: 100%;
    --ag-header-column-separator-width: 2px;
    --ag-header-column-separator-color: purple;

    --ag-header-column-resize-handle-display: block;
    --ag-header-column-resize-handle-height: 25%;
    --ag-header-column-resize-handle-width: 5px;
    --ag-header-column-resize-handle-color: orange;
}
```
"""

text3 = """

### Full List of Header Variables
- `--ag-header-foreground-color` CSS color (e.g. `red` or `#fff`) Colour of text and icons in the header
- `--ag-header-background-color` CSS color (e.g. `red` or `#fff`) Background colour for all headers, including the grid header, panels etc- 
- `--ag-header-cell-hover-background-color` CSS color (e.g. `red` or `#fff`) Rollover colour for header cells. If you set this variable and have enabled column reordering by dragging, you may want to set --ag-header-cell-moving-background-color to ensure that the rollover colour remains in place during dragging.
- `--ag-header-cell-moving-background-color` CSS color (e.g. `red` or `#fff`) Colour applied to header cells when the column is being dragged to a new position
- `--ag-header-height CSS length` (e.g. `0`, `4px` or `50%`) Height of header rows
- `--ag-header-column-separator-display` CSS display value - `block` to show or `none` to hide Whether to display the header column separator - a vertical line that displays between every header cell
- `--ag-header-column-separator-height` CSS length (e.g. `0`, `4px` or `50%`) Height of the header column separator. Percentage values are relative to the header height.
- `--ag-header-column-separator-width` CSS length (e.g. `0`, `4px` or `50%`) Width of the header column separator
- `--ag-header-column-separator-color` CSS color (e.g. `red` or `#fff`) Colour of the header column separator
- `--ag-header-column-resize-handle-display` CSS display value - `block` to show or `none` to hide Whether to show the header column resize handle - a vertical line that displays only between resizeable header columns, indicating where to drag in order to resize the column.
- `--ag-header-column-resize-handle-height` CSS length (e.g. `0`, `4px` or `50%`) Height of the header resize handle. Percentage values are relative to the header height.
- `--ag-header-column-resize-handle-width` CSS length (e.g. `0`, `4px` or `50%`) Width of the header resize handle.
- `--ag-header-column-resize-handle-color` CSS color (e.g. `red` or `#fff`) Colour of the header resize handle

"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.layout.headers", make_layout=make_tabs),
        make_md(text2),
        make_md(text3),
        # up_next("text"),
    ],
)
