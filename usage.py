from importlib import import_module
from inspect import getsource
from copy import deepcopy
import json
import os

import dash
from dash import dcc, html, Input, Output, State
import dash_design_kit as ddk
import dash_daq as daq
import dash_ag_grid as dag

import demos
from theme import theme_d_w


def prepend_recursive(component, prefix: str) -> None:
    """in-place modifications"""
    if hasattr(component, "id"):
        if type(component.id) == str:
            component.id = prefix + component.id
        elif type(component.id) == dict:
            key = "type"
            if key in component.id:
                component.id[key] = prefix + component.id[key]

    if hasattr(component, "children") and component.children is not None:
        for child in component.children:
            prepend_recursive(child, prefix)


def prepend_list_of_dict(ls: list, prefix: str) -> list:
    new_ls = []

    for di in ls:
        di = deepcopy(di)
        try:  # is a dictionary
            di_id = json.loads(di["id"])
            key = "type"
            if key in di_id:
                di_id[key] = prefix + di_id[key]

            di["id"] = json.dumps(di_id).replace(" ", "")

        except ValueError:  # is a string
            di["id"] = prefix + di["id"]

        new_ls.append(di)
    return new_ls


def prepend_callback_map(di: dict, prefix: str) -> dict:
    new_di = {}
    for k, v in di.items():
        v = deepcopy(v)
        v["inputs"] = prepend_list_of_dict(v["inputs"], prefix)
        v["state"] = prepend_list_of_dict(v["state"], prefix)
        new_di[prefix + k] = v

    return new_di


def prepend_callback_list(ls: list, prefix: str) -> list:
    new_ls = []
    for di in ls:
        di = deepcopy(di)
        di["output"] = prefix + di["output"]
        di["inputs"] = prepend_list_of_dict(di["inputs"], prefix)
        di["state"] = prepend_list_of_dict(di["state"], prefix)

        new_ls.append(di)

    return new_ls


def Header(name, app):
    plotly_logo = html.Img(
        src=app.get_asset_url("assets/dash-logo.png"),
        style={"height": 50},
        id="logo-img",
    )
    plotly_link = html.A(plotly_logo, href="https://plotly.com/dash/", target="_blank")
    theme_toggle = html.Div(
        [
            html.Img(
                src=app.get_asset_url("images/sun.svg"),
                id="sun-icon",
                className="sun-icon",
                style={"filter": "grayscale(1)", "opacity": "0.5"},
            ),
            daq.BooleanSwitch(
                id="dark-mode-switch",
                className="darkmode-switch",
                on=False,  # default:dark mode
                persistence=True,
                persistence_type="local",
            ),
            html.Img(
                src=app.get_asset_url("images/moon.svg"),
                id="moon-icon",
                className="moon-icon",
            ),
        ],
        className="icon-div-outer",
        style={"margin-right": "20px"},
    )
    return ddk.Header(
        [
            ddk.Title(
                html.A(
                    name,
                    href=app.get_relative_path("/"),
                    style={
                        "textDecoration": "none",
                        "color": "var(--header_text)",
                    },
                ),
            ),
            ddk.Menu([theme_toggle, plotly_link]),
        ]
    )


def display_demo(name, layout, code):
    download_btn = html.A(
        html.Button("Download"),
        href=app.get_asset_url(name + ".py"),
        download="app.py",
        style={"position": "absolute", "top": "0.3em", "right": "0.3em"},
    )
    return ddk.Card(
        ddk.Row(
            [
                html.Div(
                    [
                        download_btn,
                        dcc.Markdown(
                            f"```python\n{code}\n```", style={"margin-top": "15px"}
                        ),
                    ],
                    style={
                        "float": "left",
                        "overflowY": "scroll",
                        "position": "relative",
                        "backgroundColor": "var(--background_content)",
                        "width": "50%",
                        "border-right": "1px solid grey",
                        "height": "calc(100vh - 125px)",
                    },
                ),
                html.Div(
                    layout,
                    style={
                        "float": "left",
                        "padding": "5px 1% 5px 1%",
                        "overflowY": "scroll",
                        "width": "50%",
                        "height": "calc(100vh - 125px)",
                    },
                ),
            ]
        )
    )


def grid_demo():
    with open(("demos/olympic-winners.json")) as json_file:
        data = json.load(json_file)

    columnDefs = [
        {
            "field": "athlete",
            "sortable": True,
            "filter": True,
            "checkboxSelection": True,
            "headerCheckboxSelection": True,
            "pinned": "left",
        },
        {"field": "age", "sortable": True, "filter": True, "pinned": "left"},
        {"field": "country", "sortable": True, "filter": True},
        {"field": "year", "sortable": True, "filter": True},
        {
            "field": "date",
            "sortable": True,
            "filter": True,
            "checkboxSelection": True,
        },
        {"field": "sport", "sortable": True, "filter": True},
        {"field": "gold", "sortable": True, "filter": True},
        {"field": "silver", "sortable": True, "filter": True},
        {"field": "bronze", "sortable": True, "filter": True},
        {"field": "total", "sortable": True, "filter": True, "pinned": "right"},
    ]
    return html.Div(
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=data,
            style={"width": "100%", "height": "400px"},
            rowSelection="multiple",
            columnSize="sizeToFit",
            defaultColDef=dict(
                resizable=True,
            ),
        )
    )


def generate_TOC(pages):
    TOC = [
        {
            "name": page.replace("_", " ").title(),
            "description": (getattr(demos, page)).__doc__,
            "link": app.get_relative_path(f"/{page}"),
        }
        for page in pages
    ]
    return TOC


def display_TOC(table_of_contents):
    components = dcc.Markdown(
        [
            f"""- [{page['name'].strip()}]({page["link"]}): {page['description'].strip() if page['description'] else 'No description provided.'}"""
            for page in table_of_contents
        ]
    )
    return ddk.Card(components)


def display_sidebar(table_of_contents):
    components = [
        dcc.Link(
            [ddk.Icon(icon_name="home"), "Home"],
            href=app.get_relative_path("/"),
        ),
    ]
    for page in table_of_contents:
        components.append(
            dcc.Link(
                children=[
                    page["name"],
                ],
                href=page["link"],
            )
        )
    return ddk.Menu(children=components)


app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    assets_folder="demos",
    external_stylesheets=["demos/images/overrides.css"],
)

server = app.server
app.title = "Dash AG-Grid Documentation"

pages = [p.replace(".py", "") for p in sorted(os.listdir("./demos")) if ".py" in p]
modules = {p: import_module(f"demos.{p}") for p in pages}
apps = {p: m.app for p, m in modules.items()}
table_of_contents = generate_TOC(pages)
source_codes = {p: getsource(m) for p, m in modules.items()}
notfound_404 = html.Div(
    [
        html.H1("404"),
        "Webpage not found. Please contact us if a page is supposed to be here.",
    ]
)

app.layout = ddk.App(
    [
        Header("Dash AG-Grid Documentation", app),
        ddk.Sidebar(foldable=True, children=display_sidebar(table_of_contents)),
        ddk.SidebarCompanion(
            [
                html.Div(id="display"),
                dcc.Location(id="url", refresh=True),
            ]
        ),
    ],
    theme=theme_d_w["light"],
    id="app",
)

for k in apps:
    # Prepend to layout IDs recursively in-place
    new_callback_map = apps[k].callback_map
    new_callback_list = apps[k]._callback_list

    app.callback_map.update(new_callback_map)
    app._callback_list.extend(new_callback_list)


@app.callback(Output("url", "pathname"), Input("app-choice", "value"))
def update_url(name):
    if name:
        return app.get_relative_path(f"/{name}")
    return dash.no_update


@app.callback(Output("display", "children"), [Input("url", "pathname")])
def display_content(pathname):
    name = app.strip_relative_path(pathname)

    with open("package.json") as json_file:
        data = json.load(json_file)
    version = data["version"]

    readme = (
        open("INSTRUCTIONS.md", "r")
        .read()
        .format(
            version,
            app.get_asset_url("theme.js"),
        )
        .split("DOWNLOAD_LINK")
    )

    if not name:
        return [
            ddk.Card(
                [
                    dcc.Markdown(readme[0]),
                    html.A(
                        id="download-link",
                        children="dash_ag_grid-{}.tar.gz".format(version),
                        style={
                            "margin-left": "40px",
                            "color": "#317ECC",
                            "text-decoration": "underline",
                        },
                    ),
                    html.P(),
                    dcc.Download(id="package", type="application/x-tar"),
                    dcc.Markdown(readme[1]),
                ]
            ),
            ddk.Card(
                grid_demo(),
            ),
            display_TOC(table_of_contents),
        ]

    elif name in pages:
        return display_demo(
            name=name, layout=apps[name].layout, code=source_codes[name]
        )
    return notfound_404


@app.callback(
    Output("package", "data"),
    Input("download-link", "n_clicks"),
    State("download-link", "children"),
    prevent_initial_call=True,
)
def func(n_clicks, f):
    return dcc.send_file("./packages/{}".format(f))


@app.callback(
    [
        Output("app", "theme"),
        Output("sun-icon", "style"),
        Output("moon-icon", "style"),
        Output("logo-img", "src"),
    ],
    [Input("dark-mode-switch", "on")],
)
def update_theme(switch_theme):
    dim = {"filter": "grayscale(1)", "opacity": "0.5"}
    light_logo = app.get_asset_url("images/light_plotly_dash_logo.png")
    dark_logo = app.get_asset_url("images/dark_plotly_dash_logo.png")

    if switch_theme:
        return theme_d_w["dark"], dim, {}, light_logo
    return theme_d_w["light"], {}, dim, dark_logo


if __name__ == "__main__":
    app.run_server(debug=True)
