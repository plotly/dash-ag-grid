"""
Updating Column Groups

"""


import requests
import dash_ag_grid as dag
from dash import Dash, dcc, html, Input, Output, State, ctx
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

data = requests.get(
    r"https://www.ag-grid.com/example-assets/olympic-winners.json"
).json()

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
            rowData=data,
            defaultColDef=defaultColDef,
            columnDefs=columnDefs1,
        ),
    ]
)


@app.callback(
    Output("column-group-set", "columnDefs"),
    Input("column-group1-set-btn", "n_clicks"),
    Input("column-group2-set-btn", "n_clicks"),
    State("column-group-set", "columnState"),
    prevent_initial_call=True,
)
def toggle_cols(n1, n2, col_state):
    # print(col_state)
    if ctx.triggered_id == "column-group2-set-btn":
        print("2")
        return columnDefs2
    print("1")
    return columnDefs1


if __name__ == "__main__":
    app.run_server(debug=False)
