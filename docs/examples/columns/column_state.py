"""
Column State - Resetting and saving/restoring column state with a callback.
"""

import json
import dash_ag_grid as dag
import dash
from dash import Input, Output, html, dcc, State
import dash_bootstrap_components as dbc
import pandas as pd

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

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
        dcc.Markdown(
            "Click on the reset button below to reset the column state using the internal API of AG Grid."
        ),
        html.Div(
            [
                dbc.Button("Save Column State", id="save-column-state-button"),
                dbc.Button("Restore Column State", id="restore-column-state-button"),
                dbc.Button("Reset Column State", id="reset-column-state-button"),
            ],
        ),
        dag.AgGrid(
            id="reset-column-state-grid",
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            columnDefs=columnDefs,
        ),
        dcc.Markdown("Saved columns state:"),
        html.Pre(id="reset-column-state-grid-pre"),
    ]
)


@app.callback(
    Output("reset-column-state-grid-pre", "children"),
    Input("save-column-state-button", "n_clicks"),
    State("reset-column-state-grid", "columnState"),
    prevent_initial_call=True,
)
def save_column_state(_, col_state):
    return json.dumps(col_state, indent=2)


@app.callback(
    Output("reset-column-state-grid", "columnState"),
    Input("restore-column-state-button", "n_clicks"),
    State("reset-column-state-grid-pre", "children"),
    prevent_initial_call=True,
)
def restore_column_state(_, saved_col_state):
    return json.loads(saved_col_state) if saved_col_state else dash.no_update


@app.callback(
    Output("reset-column-state-grid", "resetColumnState"),
    Input("reset-column-state-button", "n_clicks"),
)
def reset_column_state(_):
    # Triggers the AG Grid internal method resetColumnState() by setting dag.AgGrid.resetColumnState = True
    return True


if __name__ == "__main__":
    app.run_server(debug=True)
