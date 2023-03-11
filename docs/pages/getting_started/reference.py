from dash import Dash, html, dcc, register_page
from utils.utils import app_description
from utils.other_components import up_next, make_md

register_page(
    __name__, order=1, description=app_description, title="Dash AG Grid")

text1 = """
# Dash AG Grid Reference


Please see the AG Grid docs for the [API reference](https://www.ag-grid.com/react-data-grid/grid-api/).  

__Content (coming soon)__

1. Props unique to Dash and not included in the AG Grid API reference

2. Props that can trigger a Dash Callback

3. Props that take JavaScript functions as inputs

4. D3 format libraries bundled with  dash-ag-grid

5. Applying conditional formatting with a dash helper function.

6. Creating custom components with Cell Renderer

7. Writing Secure Dash Apps

"""

layout = html.Div(
    [
        make_md(text1)
    ],
)


