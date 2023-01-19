"""
Column Definitions vs Column Group Definitions

"""


import requests
import dash
import dash_ag_grid as dag
from dash import dcc, html

app = dash.Dash(__name__)

data = requests.get(
    r"https://www.ag-grid.com/example-assets/olympic-winners.json"
).json()

columnDefs = [
    {
        "headerName": "Athlete Details",
        "marryChildren": True,
        "children": [
            {"field": "athlete", "colId": "athlete"},
            {"field": "country", "colId": "country"},
        ],
    },
    {"field": "age", "colId": "age"},
    {
        "headerName": "Sports Results",
        "marryChildren": True,
        "children": [
            {"field": "sport", "colId": "sport"},
            {"field": "total", "colId": "total"},
            {"field": "gold", "colId": "gold"},
            {"field": "silver", "colId": "silver"},
            {"field": "bronze", "colId": "bronze"},
        ],
    },
]

defaultColDef = {
    "resizable": True,
    "initialWidth": 160,
}

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration column groups."),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=data,
            defaultColDef=defaultColDef,
        ),
    ],
    className="header3",
)


if __name__ == "__main__":
    app.run_server(debug=True)
