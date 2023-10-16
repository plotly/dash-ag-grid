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

columnDefs = [
    {"field": "country"},
    {"field": "year"},
    {"field": "athlete"},
    {"field": "age"},
    {"field": "sport"},
    {"field": "total"},
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
        dag.AgGrid(
            id="col-state-AG-Grid",
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            columnDefs=columnDefs,
        ),
        html.Pre(id="col-state-pre"),
    ]
)


@app.callback(
    Output("col-state-pre", "children"),
    Input("col-state-AG-Grid", "columnState"),
    prevent_initial_call=True,
)
def toggle_cols(col_state):
    return json.dumps(col_state, indent=2)


if __name__ == "__main__":
    app.run_server(debug=False)
