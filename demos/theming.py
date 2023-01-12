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
            "Grids can be styled using one of four provided themes from ag-grid. Changing colors, e.g. setting a dark mode, can be done using the DDK theme editor."
        ),
        html.Div(
            [
                html.H3("Alpine (default)"),
                dag.AgGrid(
                    id="alpine",
                    columnDefs=columnDefs,
                    rowData=rowData,
                    theme="alpine",
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
                    theme="material",
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
                    theme="bootstrap",
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
                    theme="balham",
                    columnSize="sizeToFit",
                ),
                html.Hr(),
            ]
        ),
    ],
)


if __name__ == "__main__":
    app.run_server(debug=True)
