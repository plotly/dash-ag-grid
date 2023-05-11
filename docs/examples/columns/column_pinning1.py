"""
Example Column Pinning
"""
import json

import dash
import dash_ag_grid as dag
from dash import dcc, html, Input, Output, ctx, State
import dash_bootstrap_components as dbc
import pandas as pd

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
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

defaultColDef = {"sortable": True, "resizable": True}

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration of Pinning"),
        dbc.Button("clear pinned", id="clear-pinned"),
        dbc.Button(
            " Left=[Athlete, Age] Right=Total",
            id="reset-pinned",
            className="mx-1",
        ),
        dbc.Button("Left = Country", id="pin-country"),
        dag.AgGrid(
            id="column-pinning",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
        ),

    ]
)


@app.callback(
    Output("column-pinning", "columnState"),
    Input("clear-pinned", "n_clicks"),
    Input("reset-pinned", "n_clicks"),
    Input("pin-country", "n_clicks"),
    State("column-pinning", "columnState"),
    prevent_initial_call=True,
)
def update_col_def(n1, n2, n3, column_state):
    left = []
    right = []

    if ctx.triggered_id == "reset-pinned":
        left = ['athlete', 'age']
        right = ['total']
    elif ctx.triggered_id == "pin-country":
        left = ['country']

    return [
        {
            'colId': col['colId'],
            'pinned': 'left' if col['colId'] in left else 'right' if col['colId'] in right else None
        }
        for col in column_state
    ]


if __name__ == "__main__":
    app.run_server(debug=True)
