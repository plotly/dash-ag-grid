from dash import  html, register_page

from utils.utils import app_description
from utils.other_components import up_next, make_md, make_feature_card

register_page(
    __name__, order=9, description=app_description, title="Dash AG Grid - Range Selection"
)

text1 = """
# Range Selection

This is an AG Grid Enterprise feature.  Please see [AG Grid Docs Range Selection](https://www.ag-grid.com/react-data-grid/range-selection/)
"""
img= "https://user-images.githubusercontent.com/72614349/229211229-25e9d62e-f645-4291-93db-6bf99df3e99b.png"


layout = html.Div(
    [
        make_md(text1),
        make_feature_card(img, ""),

    ],
)
