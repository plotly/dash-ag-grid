from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description
from utils.other_components import enterprise_blurb


register_page(
    __name__,
    order=1,
    description=app_description,
    title="Dash AG Grid Enterprise Features",
)

text1 = """
# Enabling Enterprise

"""


layout = html.Div(
    [
        make_md(text1),
        make_md(enterprise_blurb),
        example_app("examples.enterprise.enabling_enterprise", make_layout=make_tabs),
        # up_next("text"),
    ],
)
