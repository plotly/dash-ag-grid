"""
Column Groups
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
        "children": [
            {
                "field": "athlete",
                "width": 180,
                "filter": "agTextColumnFilter",
            },
            {
                "field": "age",
                "width": 90,
                "filter": "agNumberColumnFilter",
            },
            {"headerName": "Country", "field": "country", "width": 140},
        ],
    },
    {
        "headerName": "Sports Results",
        "children": [
            {"field": "sport", "width": 140},
            {
                "columnGroupShow": "closed",
                "field": "total",
                "width": 100,
                "filter": "agNumberColumnFilter",
            },
            {
                "columnGroupShow": "open",
                "field": "gold",
                "width": 100,
                "filter": "agNumberColumnFilter",
            },
            {
                "columnGroupShow": "open",
                "field": "silver",
                "width": 100,
                "filter": "agNumberColumnFilter",
            },
            {
                "columnGroupShow": "open",
                "field": "bronze",
                "width": 100,
                "filter": "agNumberColumnFilter",
            },
        ],
    },
]

defaultColDef = {"resizable": True, "initialWidth": 200, "filter": True}

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration column groups."),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=data,
            defaultColDef=defaultColDef,
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
