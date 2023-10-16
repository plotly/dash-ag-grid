"""
Working with  row menus.
"""
import dash_ag_grid as dag
import dash
from dash import Input, Output, html, dcc

app = dash.Dash(__name__)

columnDefs = [
    {"headerName": "Make", "field": "make", "sortable": True},
    {"headerName": "Model", "field": "model"},
    {"headerName": "Price", "field": "price"},
    {"headerName": "Menu", "field": "menu", "cellRenderer": "rowMenu"},
]

rowData = [
    {
        "make": "Toyota",
        "model": "Celica",
        "price": 35000,
        "menu": [
            {"label": "Option 1", "value": 1},
            {"label": "Option 2", "value": 2},
            {"label": "Option 3", "value": 3},
        ],
    },
    {
        "make": "Ford",
        "model": "Mondeo",
        "price": 32000,
        "menu": [
            {"label": "Option 4", "value": 4},
            {"label": "Option 5", "value": 5},
            {"label": "Option 6", "value": 6},
        ],
    },
    {
        "make": "Porsche",
        "model": "Boxster",
        "price": 72000,
        "menu": [
            {"label": "Option 7", "value": 7},
            {"label": "Option 8", "value": 8},
            {"label": "Option 9", "value": 9},
        ],
    },
]


grid = dag.AgGrid(
    id="cellrenderer-grid",
    columnSize="sizeToFit",
    getRowId="params.data.make",
    columnDefs=columnDefs,
    rowData=rowData,
)

app.layout = html.Div(
    [
        dcc.Markdown("Example: Row Menu Component"),
        grid,
        html.P(id="cellrenderer-data"),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("cellrenderer-data", "children"),
    Input("cellrenderer-grid", "cellRendererData"),
)
def show_click_data(data):
    if data:
        return (
            "You selected option {} from the colId {}, rowIndex {}, rowId {}.".format(
                data["value"],
                data["colId"],
                data["rowIndex"],
                data["rowId"],
            )
        )
    return "No menu item selected."


if __name__ == "__main__":
    app.run_server(debug=True)
