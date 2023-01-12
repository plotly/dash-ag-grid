import dash
from dash import dcc, html, Input, Output, State
import dash_design_kit as ddk
import dash_ag_grid as dag

app = dash.Dash()


rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxter", "price": 72000},
]


columnDefs = [
    {"headerName": "Make", "field": "make", "sortable": True},
    {"headerName": "Model", "field": "model"},
    {"headerName": "Price", "field": "price"},
]


app.layout = html.Div(
    [
        dcc.Markdown(
            "Try filtering the data in the grid using the inline filters (click the hamburger menu in each column). Though the data is still in `rowData`, you can view the virtual row data in callbacks by watching the `virtualRowData` property."
        ),
        dag.AgGrid(
            id="virtual-row-data-example",
            columnDefs=columnDefs,
            rowData=rowData,
            defaultColDef={
                "sortable": True,
                "filter": True,
            },
        ),
        html.Div(id="data-after-filter"),
    ]
)


@app.callback(
    Output("data-after-filter", "children"),
    Input("virtual-row-data-example", "virtualRowData"),
)
def get_virtual_data(virtual):
    return str(virtual)


if __name__ == "__main__":
    app.run_server(debug=True)
