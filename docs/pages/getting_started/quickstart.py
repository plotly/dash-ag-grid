from dash import Dash, html, dcc, register_page
from utils.code_and_show import example_app, make_app_first
from utils.utils import app_description
from utils.other_components import up_next, make_md, make_feature_card

register_page(
    __name__, order=1, description=app_description, title="Dash AG Grid")

text1 = """
# Quickstart


Be sure to check out the Introductory video, sample app and feature preview in the <dccLink href='/getting-started/intro' children='Intro Section' /> 

Here's a quick preview of some basic AG Grid features:

- Sort by clicking on the heading
- Re-order the columns by dragging them to a different position
- Resized the columns by dragging the top right portion of the column
- Pin columns by dragging them to the edge until the pin icon appears
- Click on a cell to demo triggering a Dash callback

"""

text2 = """
👈 Check out each section to see more examples and learn how to customize the grid.

"""
quickstart_img = "https://user-images.githubusercontent.com/72614349/224881288-8dc17683-a209-4b6a-aa26-772250bed7dc.gif"

layout = html.Div(
    [
        make_md(text1),
        make_feature_card(img=quickstart_img, txt=""),
        example_app("examples.getting_started.quickstart", run=False, make_layout=make_app_first),
        make_md(text2)
    ],
)


