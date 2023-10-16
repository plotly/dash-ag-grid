from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=5,
    description=app_description,
    title="Dash AG Grid - Quick Filter",
)

text1 = """
# Quick Filter

In addition to the column specific filtering, a 'quick filter' can also be applied. 

The quick filter text will check all words provided against the full row. For example if the text provided is "Tony Ireland", the quick filter will only include rows with both "Tony" AND "Ireland" in them.

Use the `quickFilterText prop on the grid level.  Update this prop in a callback to filter the table

 - `quickFilterText` (string) - Rows are filtered using this text as a quick filter.
 
 
"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.filtering.quick_filter", make_layout=make_tabs),
    ],
)
