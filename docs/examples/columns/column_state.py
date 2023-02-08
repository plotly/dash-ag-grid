"""
Column State - Resetting columns with a callback.
"""

import json
import dash_ag_grid as dag
import dash
from dash import Input, Output, State, html, dcc, ctx
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

columnDefs = [
    {"headerName": "Make", "field": "make"},
    {"headerName": "Model", "field": "model"},
    {"headerName": "Price", "field": "price"},
]


defaultColDef = {
    "initialWidth": 150,
    "sortable": True,
    "resizable": True,
    "filter": True,
}

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxter", "price": 72000},
]

app.layout = html.Div(
    [
        dcc.Markdown(
            "Click on the reset button below to reset the column state using the internal API of AG Grid."
        ),
        html.Div(
            [
                dbc.Button(
                    "Reset Column State", id="reset-column-state-button", n_clicks=0
                ),
                dbc.Button(
                    "Get Column State", id="get-column-state-button", n_clicks=0
                ),
            ],
        ),
        dag.AgGrid(
            id="reset-column-state-grid",
            columnSize="sizeToFit",
            columnDefs=columnDefs,
            defaultColDef=defaultColDef,
            rowData=rowData,
        ),
        html.Pre(id="reset-column-state-grid-pre"),
    ]
)


@app.callback(
    Output("reset-column-state-grid", "enableResetColumnState"),
    Output("reset-column-state-grid", "updateColumnState"),
    Input("reset-column-state-button", "n_clicks"),
    Input("get-column-state-button", "n_clicks"),
)
def reset_column_state(n_reset, n_state):
    if ctx.triggered_id == "reset-column-state-button":
        return True, False
    elif ctx.triggered_id == "get-column-state-button":
        return False, True
    return dash.no_update

@app.callback(
    Output("reset-column-state-grid-pre", "children"),
    Input("reset-column-state-grid", "columnState"),
)
def display_column_state(col_state):
    return json.dumps(col_state, indent=2),


if __name__ == "__main__":
    app.run_server(debug=True)
