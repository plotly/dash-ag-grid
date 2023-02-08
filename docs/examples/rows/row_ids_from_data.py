"""
Data assigned ids
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc


app = Dash(__name__)

columnDefs = [
    {"headerName": "Row ID", "valueGetter": "node.id"},
    {"field": "make"},
    {"field": "model"},
    {"field": "price"},
]

data = [
    {"id": "c1", "make": "Toyota", "model": "Celica", "price": 35000},
    {"id": "c2", "make": "Ford", "model": "Mondeo", "price": 32000},
    {"id": "c8", "make": "Porsche", "model": "Boxster", "price": 72000},
    {"id": "c4", "make": "BMW", "model": "M50", "price": 60000},
    {"id": "c14", "make": "Aston Martin", "model": "DBX", "price": 190000},
]

app.layout = html.Div(
    [
        dcc.Markdown(
            "This grid shows setting the ID for a particular row node based on the data."
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=data,
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
            getRowId="id",
            dangerously_allow_code=True,
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)
