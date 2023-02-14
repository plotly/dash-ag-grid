"""
Grid assigned ids
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc


app = Dash(__name__)

columnDefs = [
    {"headerName": "Row ID", "valueGetter": {"function": "params.node.id"}},
    {"field": "make"},
    {"field": "model"},
    {"field": "price"},
]

data = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxster", "price": 72000},
    {"make": "BMW", "model": "M50", "price": 60000},
    {"make": "Aston Martin", "model": "DBX", "price": 190000},
]

app.layout = html.Div(
    [
        dcc.Markdown("This grid shows the grid assigned ids"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=data,
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
            dangerously_allow_code=True,
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)
