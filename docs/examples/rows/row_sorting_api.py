"""
Example using Sorting API through columnState
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
    {"field": "athlete"},
    {"field": "age", "width": 90},
    {"field": "country"},
    {"field": "year", "width": 90},
    {"field": "date"},
    {"field": "sport"},
    {"field": "gold"},
    {"field": "silver"},
    {"field": "bronze"},
    {"field": "total"},
]

defaultColDef = {"sortable": True}

app.layout = html.Div(
    [
        dcc.Markdown("Example: Sorting API"),
        dbc.Button("Athlete Asc", id="athlete-asc"),
        dbc.Button("Athlete Desc", id="athlete-desc"),
        dbc.Button("Country, then Sport", id="country>sport"),
        dbc.Button("Sport, then Country", id="sport>country"),
        dbc.Button("Clear Sort", id="clear-sort"),
        dbc.Button("Save Sort", id="save-sort"),
        dbc.Button("Restore Sort", id="restore-sort"),
        dag.AgGrid(
            id="grid-row-sorting-api",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
        ),
        dcc.Store(id='store-state')
    ]
)


@app.callback(
    Output("grid-row-sorting-api", "columnState"),
    State("grid-row-sorting-api", "columnState"),
    Input("athlete-asc", "n_clicks"),
    Input("athlete-desc", "n_clicks"),
    Input("country>sport", "n_clicks"),
    Input("sport>country", "n_clicks"),
    Input("clear-sort", "n_clicks"),
    prevent_initial_call=True,
)
def update_sort_state(col_state, *_):
    if ctx.triggered_id == "athlete-asc":
        return [
            {
                'colId': col['colId'],
                'sort': 'asc' if col['colId'] == 'athlete' else None
            } for col in col_state
        ]
    elif ctx.triggered_id == "athlete-desc":
        return [
            {
                'colId': col['colId'],
                'sort': 'desc' if col['colId'] == 'athlete' else None
            } for col in col_state
        ]
    elif ctx.triggered_id == "country>sport":
        return [
            {
                'colId': col['colId'],
                'sort': 'asc' if col['colId'] in ['country', 'sport'] else None,
                'sortIndex': 0 if col['colId'] == 'country' else 1 if col['colId'] == 'sport' else None,
            } for col in col_state
        ]
    elif ctx.triggered_id == "sport>country":
        return [
            {
                'colId': col['colId'],
                'sort': 'asc' if col['colId'] in ['country', 'sport'] else None,
                'sortIndex': 1 if col['colId'] == 'country' else 0 if col['colId'] == 'sport' else None,
            } for col in col_state
        ]
    elif ctx.triggered_id == "clear-sort":
        return [
            {
                'colId': col['colId'],
                'sort': None,
            } for col in col_state
        ]


@app.callback(
    Output("store-state", "data"),
    Input("save-sort", "n_clicks"),
    State("grid-row-sorting-api", "columnState"),
    prevent_initial_call=True,
)
def save_column_state(_, col_state):
    sort_state = [
        {
            'colId': col['colId'],
            'sort': col['sort'],
            'sortIndex': col['sortIndex'],
        } for col in col_state if col['sort']
    ]
    return json.dumps(sort_state)


@app.callback(
    Output("grid-row-sorting-api", "columnState", allow_duplicate=True),
    Input("restore-sort", "n_clicks"),
    State("store-state", "data"),
    State("grid-row-sorting-api", "columnState"),
    prevent_initial_call=True,
)
def restore_column_state(_, saved_sort_state, col_state):
    # No restore if no save
    if not saved_sort_state:
        return dash.no_update

    saved_sort_state = json.loads(saved_sort_state)

    # Restore only the saved 'sort' and 'sortIndex' in columnState
    for saved_col in saved_sort_state:
        for col in col_state:
            if saved_col['colId'] == col['colId']:
                col['sort'] = saved_col['sort']
                col['sortIndex'] = saved_col['sortIndex']
    return col_state


if __name__ == "__main__":
    app.run_server(debug=True)
