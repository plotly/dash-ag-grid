"""
Resetting columnSize sizeToFit in a callback
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)


columnDefs = [
    {"headerName": "Make of the Car", "field": "make"},
    {"headerName": "Model", "field": "model"},
    {"headerName": "Price", "field": "price"},
]

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxster", "price": 72000},
]


app.layout = html.Div(
    [
        dcc.Markdown("This grid demonstrates resetting `sizeToFit` with a callback"),
        html.Button("resize", id="resize"),
        dag.AgGrid(
            id="column-size-grid2",
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
        ),
    ],
    style={"margin": 20},
)

@app.callback(
    Output("column-size-grid2","columnSize"),
    Input("resize", "n_clicks"),
)
def update_columnSize(_):
    return "sizeToFit"


if __name__ == "__main__":
    app.run_server(debug=True)
