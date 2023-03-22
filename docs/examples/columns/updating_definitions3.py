"""
Column Definition State Retrieval
"""


import json

import dash_ag_grid as dag
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs1 = [
    {"field": "country"},
    {"field": "year"},
    {"field": "athlete"},
    {"field": "age"},
    {"field": "sport"},
    {"field": "total"},
]


columnDefs2 = [
    {"field": "country", "headerName": "C1"},
    {"field": "year", "headerName": "C2"},
    {"field": "athlete", "headerName": "C3"},
    {"field": "age", "headerName": "C4"},
    {"field": "sport", "headerName": "C5"},
    {"field": "total", "headerName": "C6"},
]


defaultColDef = {
    "initialWidth": 150,
    "sortable": True,
    "resizable": True,
    "filter": True,
}

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration of column state information"),
        dbc.Button("Set Header Names", id="header-names-toggle-btn", n_clicks=0),
        dag.AgGrid(
            id="toggle-header-names",
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            columnDefs=columnDefs1,
        ),
        html.Pre(id="col-state"),
    ]
)


@app.callback(
    Output("toggle-header-names", "columnDefs"),
    Output("header-names-toggle-btn", "children"),
    Output("col-state", "children"),
    Input("header-names-toggle-btn", "n_clicks"),
    Input("toggle-header-names", "columnState"),
    prevent_initial_call=True,
)
def toggle_cols(n, col_state):
    if n % 2 == 0:
        return columnDefs1, "Set Header Names", json.dumps(col_state, indent=2)
    return columnDefs2, "Remove Header Names", json.dumps(col_state, indent=2)


if __name__ == "__main__":
    app.run_server(debug=False)
