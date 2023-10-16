from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=4,
    description=app_description,
    title="Dash AG Grid Components - Row Menu",
)

text1 = """
# Components 

In Dash AG Grid community there are a limited number of in cell components and editors.

Cell Editing components:
 - See the <dccLink href='/editing/cell-editors' children='Cell editors' />  section for regular and popup cell editors.
 - See the <dccLink href='/editing/provided-cell-editors' children='Provided cell editors' />  section for select (dropdown) editors, and large text (textarea) editors

Other components:
 - <dccLink href='/components/markdown' children='Markdown' /> .  Renders markdown syntax or html when `dangerously_allow_code=True`
 - <dccLink href='/components/row-menu' children='Row Menu' />  To access menu options in a callback
 - <dccLink href='/rendering/animation-renderer' children='Cell change animation renderer' />

Custom components:

You can also create custom components and cell renderers.  For examples see:  

 - <dccLink href='/components/cell-renderer' children='Cell Renderers' />  for examples of several custom components`
 - <dccLink href='/components/overlay' children='Overlay' />  for custom loading and no rows overlay components
 - <dccLink href='/components/tooltip' children='Tooltip' /> for a custom Tooltip component.

### Row Menu

The `rowMenu` is a Cell Renderer component that is automatically included with  dash-ag-grid. This means that it's
 not not necessary to include it in the `dashAgGridComponentFunctions.js` file in the `assets` folder. 

When the user selects an option from the rowMenu, the `cellRendererData` is updated.


`cellRendererData` (dict; optional): Special prop to allow feedback from cell renderer to the grid. `cellRendererData` is a dict with keys:

- `colId` (string; optional): Column ID from where the event was fired.

- `rowId` (boolean | number | string | dict | list; optional): Row Id from the grid, this could be a number automatically, or set via getRowId.

- `rowIndex` (number; optional): Row Index from the grid, this is associated with the row count.

- `timestamp` (boolean | number | string | dict | list; optional): Timestamp of when the event was fired.

- `value` (boolean | number | string | dict | list; optional): value of the menu item selected..

"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.components.row_menu", make_layout=make_tabs),
        #  up_next("text"),
    ],
)
