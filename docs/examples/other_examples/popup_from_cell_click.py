"""
Triggering a popup when a cell is clicked with a callback.
"""
import dash_ag_grid as dag
import dash
from dash import Input, Output, html, dcc
import dash_bootstrap_components as dbc

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
            "Select rows to trigger a popup with more information about that row."
        ),
        dag.AgGrid(
            id="selectable-grid-popup",
            rowData=rowData,
            columnSize="sizeToFit",
            rowSelection="single",
            children=[
                dag.AgGridColumn(
                    field="make",
                    checkboxSelection=True,
                ),
                dag.AgGridColumn(
                    field="model",
                ),
                dag.AgGridColumn(
                    field="price",
                ),
            ],
        ),
        dbc.Modal(
            [
                dbc.ModalHeader("More information about selected row"),
                dbc.ModalBody(id="modal-content"),
                dbc.ModalFooter(dbc.Button("Close", id="close", className="ml-auto")),
            ],
            id="modal",
        ),
    ]
)


@app.callback(
    Output("modal", "is_open"),
    Output("modal-content", "children"),
    Input("selectable-grid-popup", "selectionChanged"),
    Input("close", "n_clicks"),
)
def open_modal(selection, close_clicks):
    ctx = dash.callback_context
    if "close" in ctx.triggered[0]["prop_id"]:
        return False, dash.no_update
    if selection:
        return True, "You selected " + ", ".join(
            [
                "{} (model {} and price {})".format(
                    s["make"],
                    s["model"],
                    s["price"],
                )
                for s in selection
            ]
        )

    return dash.no_update


if __name__ == "__main__":
    app.run_server(debug=True)
