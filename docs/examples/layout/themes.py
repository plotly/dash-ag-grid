import dash_ag_grid as dag
import dash
from dash import html, dcc

app = dash.Dash(__name__)

columnDefs = [
    {
        "headerName": "Make",
        "field": "make",
        "sortable": True,
        "filter": True,
        "checkboxSelection": True,
        "headerCheckboxSelection": True,
    },
    {
        "headerName": "Model",
        "field": "model",
        "filter": True,
        "sortable": True,
    },
    {
        "headerName": "Price",
        "field": "price",
        "filter": True,
        "sortable": True,
    },
]

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxter", "price": 72000},
]


app.layout = html.Div(
    [
        dcc.Markdown(
            "Grids can be styled using one of six provided themes from ag-grid."
        ),
        html.Div(
            [
                html.H3("Alpine (default)"),
                dag.AgGrid(
                    id="alpine",
                    columnDefs=columnDefs,
                    rowData=rowData,
                    className="ag-theme-alpine",
                    columnSize="sizeToFit",
                ),
                html.Hr(),
            ]
        ),
        html.Div(
            [
                html.H3("Alpine dark"),
                dag.AgGrid(
                    id="alpine-dark",
                    columnDefs=columnDefs,
                    rowData=rowData,
                    className="ag-theme-alpine-dark",
                    columnSize="sizeToFit",
                ),
                html.Hr(),
            ]
        ),
        html.Div(
            [
                html.H3("Balham"),
                dag.AgGrid(
                    id="balham",
                    columnDefs=columnDefs,
                    rowData=rowData,
                    className="ag-theme-balham",
                    columnSize="sizeToFit",
                ),
                html.Hr(),
            ]
        ),
        html.Div(
            [
                html.H3("Balham Dark"),
                dag.AgGrid(
                    id="balham-dark",
                    columnDefs=columnDefs,
                    rowData=rowData,
                    className="ag-theme-balham-dark",
                    columnSize="sizeToFit",
                ),
                html.Hr(),
            ]
        ),
        html.Div(
            [
                html.H3("Material"),
                dag.AgGrid(
                    id="material",
                    columnDefs=columnDefs,
                    rowData=rowData,
                    className="ag-theme-material",
                    columnSize="sizeToFit",
                ),
                html.Hr(),
            ]
        ),
        html.Div(
            [
                html.H3("Bootstrap"),
                dag.AgGrid(
                    id="bootstrap",
                    columnDefs=columnDefs,
                    rowData=rowData,
                    className="ag-theme-bootstrap",
                    columnSize="sizeToFit",
                ),
                html.Hr(),
            ]
        ),
        html.Div(
            [
                html.H3("Alpine with custom css"),
                dag.AgGrid(
                    id="alpine-custom",
                    columnDefs=columnDefs,
                    rowData=rowData,
                    className="ag-theme-alpine ag-theme-busybee",
                    columnSize="sizeToFit",
                ),
                html.Hr(),
            ]
        ),
        dcc.Markdown(
            """
        The above example uses custom css in /assets
        ```
        
        .ag-theme-alpine.ag-theme-busybee {
            --ag-odd-row-background-color: #F7CE87;
            --ag-header-background-color: silver;
            --ag-header-cell-hover-background-color: #c7c4bf;
        }
        
        
        .ag-theme-alpine.ag-theme-busybee .ag-pinned-left-cols-container, .ag-theme-busybee .ag-pinned-right-cols-container {
            --ag-odd-row-background-color: rgb(215,215,215);
            --ag-background-color: rgb(230,230,230);
        }

        
        ```
        
        
        """
        ),
    ],
)


if __name__ == "__main__":
    app.run_server(debug=True)
