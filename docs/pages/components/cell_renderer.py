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
"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.components.cell_renderer", make_layout=make_tabs),

        #  up_next("text"),
    ],
)
