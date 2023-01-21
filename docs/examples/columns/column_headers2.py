# TODO need ag-grid >=28

"""
Auto Header Height
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
    {"field": "athlete", "headerName": "The full Name of the athlete"},
    {
        "field": "age",
        "headerName": "The number of Years since the athlete was born",
        "initialWidth": 120,
    },
    {"field": "country", "headerName": "The Country the athlete was born in"},
    {"field": "sport", "headerName": "The Sport the athlete participated in"},
    {
        "field": "total",
        "headerName": "The Total number of medals won by the athlete",
    },
]

defaultColDef = {
    "resizable": True,
    "initialWidth": 200,
    "wrapHeaderText": True,
    "autoHeaderHeight": True,
}

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration auto header height."),
        dag.AgGrid(
            # style={"width": "100%", "height": "100%"},
            columnDefs=columnDefs,
            rowData=data,
            defaultColDef=defaultColDef,
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
