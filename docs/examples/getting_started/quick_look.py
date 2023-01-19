"""
This is the first example in the "Getting Started" section of ag-grid https://www.ag-grid.com/react-data-grid/getting-started/
"""

import dash_ag_grid as dag
import dash
from dash import html, dcc

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
            "A grid can be defined in one of two ways: Either by passing in column definitions to the `columnDefs` prop, or by passing in column defintions as children to a `dag.AgGrid` component using the `dag.AgGridColumn` components. This demo has two grids, one defined with each method. Both methods have the same features and parameters."
        ),
        html.Div(
            [
                dag.AgGrid(
                    id="input",
                    columnSize="sizeToFit",
                    columnDefs=columnDefs,
                    rowData=rowData,
                ),
            ]
        ),
        html.Div(
            [
                dag.AgGrid(
                    id="input2",
                    columnSize="sizeToFit",
                    rowData=rowData,
                    children=[
                        dag.AgGridColumn(
                            id="column1",
                            field="make",
                        ),
                        dag.AgGridColumn(id="column2", field="model"),
                        dag.AgGridColumn(
                            id="column3",
                            field="price",
                        ),
                    ],
                ),
            ],
            style={"marginTop": "10px"},
        ),
    ],
    style={"flexWrap": "wrap"},
)


if __name__ == "__main__":
    app.run_server(debug=True)
