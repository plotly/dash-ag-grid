from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=6,
    description=app_description,
    title="Dash AG Grid Editing",
)

text1="""
#  Full Row Editing
Full row editing is for when you want all cells in the row to become editable at the same time. This gives the impression to the user that the record the row represents is being edited.

To enable full row editing, set the grid option `editType = 'fullRow'`.
"""

layout = html.Div(
    [

        make_md(text1),
        example_app("examples.editing.full_row", make_layout=make_tabs),

        # up_next("text"),
    ],
)
