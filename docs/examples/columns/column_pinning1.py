"""
Example Column Pinning
"""
import requests
import dash
import dash_ag_grid as dag
from dash import dcc, html, Input, Output, ctx
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

data = requests.get(
    r"https://www.ag-grid.com/example-assets/olympic-winners.json"
).json()

columnDefs1 = [
    {
        "headerName": "#",
        "colId": "rowNum",
        "valueGetter": "node.id",
        "width": 80,
        "pinned": "",
    },
    {"field": "athlete", "width": 240, "pinned": ""},
    {"field": "age", "width": 90, "pinned": ""},
    {"field": "country", "width": 150, "pinned": ""},
    {"field": "year", "width": 90},
    {"field": "date", "width": 110},
    {"field": "sport", "width": 150},
    {"field": "gold", "width": 100},
    {"field": "silver", "width": 100},
    {"field": "bronze", "width": 100},
    {"field": "total", "width": 100, "pinned": ""},
]


columnDefs2 = [
    {
        "headerName": "#",
        "colId": "rowNum",
        "valueGetter": "node.id",
        "width": 80,
        "pinned": "left",
    },
    {"field": "athlete", "width": 240, "pinned": "left"},
    {"field": "age", "width": 90, "pinned": "left"},
    {"field": "country", "width": 150},
    {"field": "year", "width": 90},
    {"field": "date", "width": 110},
    {"field": "sport", "width": 150},
    {"field": "gold", "width": 100},
    {"field": "silver", "width": 100},
    {"field": "bronze", "width": 100},
    {"field": "total", "width": 100, "pinned": "right"},
]


columnDefs3 = [
    {
        "headerName": "#",
        "colId": "rowNum",
        "valueGetter": "node.id",
        "width": 80,
    },
    {"field": "athlete", "width": 240},
    {"field": "age", "width": 90},
    {"field": "country", "width": 150, "pinned": "left"},
    {"field": "year", "width": 90},
    {"field": "date", "width": 110},
    {"field": "sport", "width": 150},
    {"field": "gold", "width": 100},
    {"field": "silver", "width": 100},
    {"field": "bronze", "width": 100},
    {"field": "total", "width": 100},
]


defaultColDef = {"resizable": True}

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration of Pinning via Column Dragging and lock pin"),
        dbc.Button("clear pinned", id="clear-pinned"),
        dbc.Button(
            " Left = #, Athlete, Age; Right = Total",
            id="reset-pinned",
            className="mx-1",
        ),
        dbc.Button("Left = Country", id="pin-country"),
        dag.AgGrid(
            id="column-pinning",
            columnDefs=columnDefs1,
            rowData=data,
            defaultColDef=defaultColDef,
        ),
    ]
)


@app.callback(
    Output("column-pinning", "columnDefs"),
    Input("clear-pinned", "n_clicks"),
    Input("reset-pinned", "n_clicks"),
    Input("pin-country", "n_clicks"),
    prevent_initial_call=True,
)
def update_col_def(*_):
    if ctx.triggered_id == "clear-pinned":
        return columnDefs1
    if ctx.triggered_id == "reset-pinned":
        return columnDefs2
    if ctx.triggered_id == "pin-country":
        return columnDefs3


if __name__ == "__main__":
    app.run_server(debug=True)

