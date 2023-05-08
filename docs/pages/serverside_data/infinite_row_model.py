from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description
from pages.scrolling.infinite_scroll import text1, text2, text3


register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid Infinite Row Model",
)

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.scrolling.infinite_scroll", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.scrolling.infinite_scroll_sort_filter", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.scrolling.infinite_scroll_pagination", make_layout=make_tabs),
        # up_next("text"),
    ],
)
