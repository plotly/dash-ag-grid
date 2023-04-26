"""
Column Size
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
        dcc.Markdown("This grid demonstrates setting the column size"),
        dcc.RadioItems(
            id="column-size-radio",
            options=[
                {"label": "Auto size", "value": "autoSize"},
                {"label": "Auto size skip header", "value": "autoSizeSkipHeader"},
                {"label": "Size to fit", "value": "sizeToFit"},
                {"label": "Responsive Size to fit", "value": "responsiveSizeToFit"}
            ],
            value="autoSize",
        ),

        dag.AgGrid(
            id="column-size-grid",
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="autoSize",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
        ),
    ],
    style={"margin": 20},
)

@app.callback(
    Output("column-size-grid","columnSize"),
    Output("column-size-grid", "columnSizeOptions"),
    Input("column-size-radio", "value"),
)
def update_columnSize(v):
    if v == "autoSizeSkipHeader":
        return "autoSize", {"skipHeader": True}
    return v, {"skipHeader": False}


if __name__ == "__main__":
    app.run_server(debug=True)
