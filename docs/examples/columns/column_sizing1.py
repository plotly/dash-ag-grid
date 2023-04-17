"""
Column Sizing
"""

import dash_ag_grid as dag
import dash
from dash import Input, Output, html, dcc

app = dash.Dash(__name__)

columnDefs = [
    {"headerName": "Make", "field": "make"},
    {"headerName": "Model", "field": "model"},
    {"headerName": "Price", "field": "price"},
]

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxter", "price": 72000},
]


app.layout = html.Div(
    [
        dcc.Markdown(
            "Switch between autosize and size to fit to see the columns respond. Columns can also be resized by dragging at their edge."
        ),
        dcc.RadioItems(
            id="column-size-radio",
            options=[
                {"label": "Auto size", "value": "autoSize"},
                {"label": "Size to fit", "value": "sizeToFit"}
            ],
            value="autoSize",
        ),
        dag.AgGrid(
            id="column-size-grid",
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="autoSize",
            defaultColDef={"resizable":True}
        ),
    ]
)


@app.callback(Output("column-size-grid", "columnSize"), Input("column-size-radio", "value"))
def column_sizing(size_type):
    return size_type


if __name__ == "__main__":
    app.run_server(debug=True)
