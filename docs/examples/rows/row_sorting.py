"""
Grid with sorting enabled on certain columns
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
    {"field": "country"},
    {"field": "athlete"},
    {"field": "age"},
    {"field": "sport"},
    {"field": "total", "sortable": False},
]

app.layout = html.Div(
    [
        dcc.Markdown("This grid can be sorted by all rows except the Total column"),
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
    app.run_server(debug=True)
