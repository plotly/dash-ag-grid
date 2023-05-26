from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=4,
    description=app_description,
    title="Dash AG Grid Rows - Pinning",
)

text1 = """
# Row Pinning

Pinned rows appear either above or below the normal rows of a table. This feature in other grids is also known as Frozen Rows or Floating Rows.

To put pinned rows into your grid, set `pinnedTopRowData` or `pinnedBottomRowData` in the same way as you would set normal data into rowData. 
 - `pinnedTopRowData` (any[]) Data to be displayed as pinned top rows in the grid.
 - `pinnedBottomRowData` (any[]) Data to be displayed as pinned bottom rows in the grid.

 
## Cell Editing
Cell editing can take place as normal on pinned rows.

## Cell Rendering
Cell rendering can take place as normal on pinned rows. If you want to use a different Cell Renderer for pinned rows vs normal rows, use `cellRendererSelector` to specify different Cell Renderers for different rows.

## Example 1  Pinned Top Rows

This example pins the selected row to the top row of the grid.

"""


text2="""
## Example 2 Pinned Bottom Rows

This example pins a summary row to the bottom of the grid.  The **Average**s are calculated in a Dash callback based on the filtered rows.
"""

text3 = """
## Non Supported Items
Pinned rows are not part of the main row model. For this reason, the following is not possible:

- Sorting: Pinned rows cannot be sorted.
- Filtering: Pinned rows are not filtered.
- Row Grouping: Pinned rows cannot be grouped.
- Row Selection: Pinned rows cannot be selected.
"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.rows.row_pinning", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.rows.row_pinning_bottom", make_layout=make_tabs),
        make_md(text3),
        # up_next("text"),
    ],
)
