import dash
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from utils.nav import navbar, make_side_nav
from utils.utils import example_apps


# syntax highlighting light or dark
light_hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/stackoverflow-light.min.css"
dark_hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/stackoverflow-dark.min.css"


# stylesheet with the .dbc class
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[
        dbc.themes.SPACELAB,
        dbc.icons.BOOTSTRAP,
        dbc.icons.FONT_AWESOME,
        dbc_css,
        dark_hljs,
    ],
    suppress_callback_exceptions=True,
)


for k in example_apps:
    new_callback_map = example_apps[k].callback_map
    new_callback_list = example_apps[k]._callback_list

    app.callback_map.update(new_callback_map)
    app._callback_list.extend(new_callback_list)


app.layout = dbc.Container(
    [
        navbar,
        dbc.Row(
            [
                dcc.Location(id="url"),
                dbc.Col(make_side_nav(), xs=5, md=3, xl=2),
                dbc.Col(
                    html.Div(
                        dash.page_container,
                        className="p-2",
                        style={"minWidth": 600},
                    ),
                    xs=7,
                    md=9,
                    xl=10,
                    id="content",
                ),
            ],
        ),
    ],
    className="mb-4",
    fluid=True,
)

#
# @app.callback(Output("sidebar", "active_item"), Input("url", "pathname"))
# def open_sidebar_category(path):
#     """
#     This opens the accordion sidebar category when navigating to it from the feature preview section.
#     """
#     if path == "/":
#         return "/getting-started"
#     # get the sidebar category (first segment of the path)
#     segments = path.split("/")
#     category = "/" + segments[1]
#     return category


if __name__ == "__main__":
    app.run_server(debug=True)
