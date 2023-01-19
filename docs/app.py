import dash
from dash import Dash, html, dcc
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
                dbc.Col(make_side_nav(), xs=5, md=3, xl=2, id="sidebar"),
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


if __name__ == "__main__":
    app.run_server(debug=True)
