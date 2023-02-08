"""
Simple column filters - number filter and text filter
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc
import requests

app = Dash(__name__)


data = requests.get(
    r"https://www.ag-grid.com/example-assets/olympic-winners.json"
).json()

# basic columns definition with column defaults
columnDefs = [
    {"field": "athlete"},
    {"field": "age", "filter": "agNumberColumnFilter", "maxWidth": 100},
    {"field": "country"},
    {"field": "year"},
    {"field": "sport"},
    {"field": "total"},
]

app.layout = html.Div(
    [
        dcc.Markdown(
            "This grid has a number filter on the 'Age' column and a text filter on the other columns"
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=data,
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=False)
