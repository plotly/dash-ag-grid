import dash
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from utils.nav import navbar, make_side_nav
from utils.utils import example_apps

# need these two imports for the custom comonents
import dash_mantine_components
import dash_iconify


# syntax highlighting light or dark
light_hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/stackoverflow-light.min.css"
dark_hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/stackoverflow-dark.min.css"


# stylesheet with the .dbc class
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

# for the custom datepicker example
jquery_external_scripts=[
        "https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.1/jquery.min.js",
        "https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js",
    ]
jquery_external_stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.css"
    ]


app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[
        dbc.themes.SPACELAB,
        dbc.icons.BOOTSTRAP,
        dbc.icons.FONT_AWESOME,
        dbc_css,
        dark_hljs,
    ] + jquery_external_stylesheets,
    suppress_callback_exceptions=True,
    external_scripts=jquery_external_scripts
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
                dcc.Store(id="enterprise-store", data=""),
                dbc.Col(make_side_nav(), xs=5, md=4, xl=3, style={"maxWidth": 300},),
                dbc.Col(
                    html.Div(
                        dash.page_container,
                        className="p-2",
                        style={"minWidth": 600},
                    ),
                    xs=7,
                    md=8,
                    xl=9,
                    id="content",
                ),
            ],
        ),
    ],
    className="mb-4",
    fluid=True,
)


@app.callback(Output("sidebar", "active_item"), Input("url", "pathname"))
def open_sidebar_category(path):
    """
    This opens the accordion sidebar category when navigating to it from the feature preview section.
    """
    if path is None:
        return dash.no_update
    if path == "/":
        return "/getting-started"
    # get the sidebar category (first segment of the path)
    segments = path.split("/")
    category = "/" + segments[1]
    return category


# refreshes the page after visiting AG Grid Enterprise examples to reset to AG Grid Community
app.clientside_callback(
    """
    function(url, enterpriseStore) {
        const newStore = url.startsWith("/enterprise") ? "enterprise" : "";
        if (!url.startsWith("/enterprise")  && enterpriseStore === "enterprise") {
            window.location.reload()    
        }
        return newStore
    }
    """,
    Output('enterprise-store', 'data'),
    Input('url', 'pathname'),
    State('enterprise-store', 'data'),
)


if __name__ == "__main__":
    app.run_server(debug=True)
