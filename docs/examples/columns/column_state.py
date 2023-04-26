"""
Column State - Resetting and loading column state with a callback.
"""

import json
import dash_ag_grid as dag
import dash
from dash import Input, Output, html, dcc, ctx
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

columnDefs = [
    {"field": "make"},
    {"field": "model"},
    {"field": "price"},
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
    {"make": "Porsche", "model": "Boxster", "price": 72000},
]

colState = [
    {
        "colId": "make",
        "width": 150,
        "hide": False,
        "pinned": "left",
        "sort": None,
        "sortIndex": None,
        "aggFunc": None,
        "rowGroup": False,
        "rowGroupIndex": None,
        "pivot": False,
        "pivotIndex": None,
        "flex": None,
    },
    {
        "colId": "price",
        "width": 150,
        "hide": False,
        "pinned": "left",
        "sort": None,
        "sortIndex": None,
        "aggFunc": None,
        "rowGroup": False,
        "rowGroupIndex": None,
        "pivot": False,
        "pivotIndex": None,
        "flex": None,
    },
    {
        "colId": "model",
        "width": 150,
        "hide": False,
        "pinned": None,
        "sort": None,
        "sortIndex": None,
        "aggFunc": None,
        "rowGroup": False,
        "rowGroupIndex": None,
        "pivot": False,
        "pivotIndex": None,
        "flex": None,
    },
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
                dbc.Button("Load State", id="load-column-state-button", n_clicks=0),
            ],
        ),
        dag.AgGrid(
            id="reset-column-state-grid",
            columnSize="autoSize",
            columnDefs=columnDefs,
            defaultColDef=defaultColDef,
            rowData=rowData,
            columnState=colState,
        ),
        html.Pre(id="reset-column-state-grid-pre"),
    ]
)


@app.callback(
    Output("reset-column-state-grid", "resetColumnState"),
    Input("reset-column-state-button", "n_clicks"),
)
def reset_column_state(n):
    if n:
        return True
    return dash.no_update


@app.callback(
    Output("reset-column-state-grid-pre", "children"),
    Input("reset-column-state-grid", "columnState"),
)
def display_column_state(col_state):
    return (json.dumps(col_state, indent=2),)


@app.callback(
    Output("reset-column-state-grid", "columnState"),
    Input("load-column-state-button", "n_clicks"),
)
def loadState(n):
    if n:
        return colState
    return dash.no_update


if __name__ == "__main__":
    app.run_server(debug=True)
