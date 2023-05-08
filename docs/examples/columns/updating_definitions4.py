"""
Updating Column Groups

"""

import dash_ag_grid as dag
from dash import Dash, dcc, html, Input, Output, ctx
import dash_bootstrap_components as dbc
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs1 = [
    {
        "headerName": "Group A",
        "groupId": "groupA",
        "children": [
            {"field": "athlete"},
            {"field": "age"},
            {"field": "country", "columnGroupShow": "open"},
        ],
    },
    {
        "headerName": "Group B",
        "children": [
            {"field": "sport"},
            {"field": "year"},
            {"field": "date", "columnGroupShow": "open"},
        ],
    },
    {
        "headerName": "Group C",
        "groupId": "groupC",
        "children": [
            {"field": "total"},
            {"field": "gold", "columnGroupShow": "open"},
            {"field": "silver", "columnGroupShow": "open"},
            {"field": "bronze", "columnGroupShow": "open"},
        ],
    },
]

columnDefs2 = [
    {
        "headerName": "GROUP A",
        "groupId": "groupA",
        "children": [
            {"field": "athlete"},
            {"field": "age"},
            {"field": "country", "columnGroupShow": "open"},
        ],
    },
    {
        "headerName": "Group B",
        "children": [
            {"field": "sport"},
            {"field": "year"},
            {"field": "date", "columnGroupShow": "open"},
        ],
    },
    {
        "headerName": "Group C",
        "groupId": "groupC",
        "children": [
            {"field": "total"},
            {"field": "gold", "columnGroupShow": "open"},
            {"field": "silver", "columnGroupShow": "open"},
            {"field": "bronze", "columnGroupShow": "open"},
            {"field": "extraA"},
            {"field": "extraB", "columnGroupShow": "open"},
        ],
    },
]

defaultColDef = {
    "initialWidth": 150,
    "sortable": True,
    "resizable": True,
    "filter": True,
}

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration of updating column groups"),
        dbc.Button("First Column Set", id="column-group1-set-btn", n_clicks=0),
        dbc.Button("Second Column Set", id="column-group2-set-btn", n_clicks=0),
        dag.AgGrid(
            id="column-group-set",
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            columnDefs=columnDefs1,
        ),
    ]
)


@app.callback(
    Output("column-group-set", "columnDefs"),
    Input("column-group1-set-btn", "n_clicks"),
    Input("column-group2-set-btn", "n_clicks"),
    prevent_initial_call=True,
)
def toggle_cols(*_):
    return columnDefs2 if ctx.triggered_id == "column-group2-set-btn" else columnDefs1


if __name__ == "__main__":
    app.run_server(debug=False)
