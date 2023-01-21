from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=1,
    description=app_description,
    title="Dash AG Grid Components",
    # name="Bootstrap Utility Classes",
    # hashtags=["intro","background", "border", "color", "spacing", "text", "position"],
)

text1 = """
# Components

In Dash AG Grid community there are a limited number of in cell components and editors.  

Cell Editing components:
 - See the <dccLink href='/editing/cell-editors' children='Cell editors' />  section for regular and popup cell editors.
 - See the <dccLink href='/editing/provided-cell-editors' children='Provided cell editors' />  section for select (dropdown) editors, and large text (textarea) editors

Other components:
 - <dccLink href='/components/markdown' children='Markdown' /> .  Renders markdown syntax or html when `dangerously_allow_html=True`
 - <dccLink href='/components/row-menu' children='Row Menu' />  To access menu options in a callback
 - <dccLink href='/rendering/animation-renderer' children='Cell change animation renderer' />

### Markdown

"""

text2 = """
### Markdown with HTML

By default the grid does not allow raw html to reduce the risk of [XSS attacks.](https://owasp.org/www-community/attacks/xss/). For more
 information, see this community forum post on [writing secure dash apps ](https://community.plotly.com/t/writing-secure-dash-apps-community-thread/54619)  

The first example does not have `dangerously_allow_html` enabled, so the links which are raw html do not render.  The second
example has `dangerously_allow_html=True`.
"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.components.markdown", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.components.markdown_html", make_layout=make_tabs),
        #  up_next("text"),
    ],
)
