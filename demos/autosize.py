"""
Example of how to make columns adjust to fit either the screen or their contents.
"""

import dash_ag_grid as dag
import dash
from dash import Input, Output, State, html, dcc, dash_table

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
            id="columnSizing",
            options=[
                {"label": i, "value": j}
                for i, j in [
                    ("Auto size", "autoSizeAll"),
                    ("Size to fit", "sizeToFit"),
                ]
            ],
            value="autoSizeAll",
        ),
        dag.AgGrid(
            id="input",
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="autoSizeAll",
            defaultColDef=dict(
                resizable=True,
            ),
        ),
    ]
)


@app.callback(Output("input", "columnSize"), [Input("columnSizing", "value")])
def column_sizing(size_type):
    return size_type


if __name__ == "__main__":
    app.run_server(debug=True)
