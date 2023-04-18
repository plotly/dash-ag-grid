from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=4,
    description=app_description,
    title="Dash AG Grid Components",
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

This component is included in dash-ag-grid

"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.components.row_menu", make_layout=make_tabs),
        #  up_next("text"),
    ],
)
