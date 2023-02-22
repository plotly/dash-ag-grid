import dash
import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State, ctx

app = Dash(__name__)


rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxter", "price": 72000},
]

columnDefs = [
    {
        "headerName": "id",
        "valueGetter": {"function": "params.node.id"},
        "checkboxSelection": True,
    },
    {"field": "make"},
    {"field": "model"},
    {
        "field": "price",
        "cellRenderer": "agAnimateShowChangeCellRenderer",
    },
]

app.layout = html.Div(
    [
        html.Button("Update selected", id="transactions-update"),
        html.Button("Remove Selected", id="transactions-remove"),
        html.Button("Add Rows", id="transactions-add"),
        html.Button("Clear", id="transactions-clear"),
        html.Button("Start Over", id="transactions-start"),
        dag.AgGrid(
            id="transactions-grid",
            rowData=rowData,
            columnDefs=columnDefs,
            defaultColDef={"flex": 1},
            dashGridOptions={"rowSelection": "multiple"},
            getRowId="params.data.make",
        ),
    ],
)


@app.callback(
    Output("transactions-grid", "rowData"),
    Input("transactions-clear", "n_clicks"),
    Input("transactions-start", "n_clicks"),
)
def update_rowdata(*_):
    if ctx.triggered_id == "transactions-clear":
        return []
    return rowData


@app.callback(
    Output("transactions-grid", "rowTransaction"),
    Input("transactions-remove", "n_clicks"),
    Input("transactions-update", "n_clicks"),
    Input("transactions-add", "n_clicks"),
    State("transactions-grid", "selectionChanged"),
)
def update_rowdata(n1, n2, n3, selection):

    if ctx.triggered_id == "transactions-remove":
        if selection is None:
            return dash.no_update
        return {"remove": selection}

    if ctx.triggered_id == "transactions-update":
        if selection is None:
            return dash.no_update
        for row in selection:
            row["price"] = row["price"] + n2
        return {"update": selection}

    if ctx.triggered_id == "transactions-add":
        newRows = [row.copy() for row in rowData]
        for row in newRows:
            row["make"] = row["make"] + str(n3)
        return {"add": newRows}


if __name__ == "__main__":
    app.run(debug=True)
