"""
Row Drag Simple Managed
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc
import requests

app = Dash(__name__)


data = requests.get(
    r"https://www.ag-grid.com/example-assets/olympic-winners.json"
).json()


columnDefs = [
    {"field": "athlete", "rowDrag": True},
    {"field": "country"},
    {"field": "age"},
    {"field": "sport"},
    {"field": "total", "sortable": False},
]

app.layout = html.Div(
    [
        dcc.Markdown("This grid  demonstrates simple managed row drag"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=data,
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
            dashGridOptions={"rowDragManaged": True}
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)
