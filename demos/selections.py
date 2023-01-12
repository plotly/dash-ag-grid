"""
Demonstration of working with AG-Grid in a variety of use-cases involving selections.
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
            "Select rows and the data will be used to populate a second component."
        ),
        dag.AgGrid(
            id="selectable-grid",
            rowData=rowData,
            columnSize="sizeToFit",
            rowSelection="multiple",
            children=[
                dag.AgGridColumn(
                    field="make",
                    checkboxSelection=True,
                    headerCheckboxSelection=True,
                ),
                dag.AgGridColumn(
                    field="model",
                ),
                dag.AgGridColumn(
                    field="price",
                ),
            ],
        ),
        dcc.Markdown(id="currentSelections"),
        html.Hr(),
        dcc.Markdown(
            "Selections support persistence. Note `persistence=True` in this example. Try selecting rows here and then refresh the page:"
        ),
        dag.AgGrid(
            id="selectable-grid-persistence",
            rowData=rowData,
            columnSize="sizeToFit",
            rowSelection="multiple",
            persistence=True,
            children=[
                dag.AgGridColumn(
                    field="make",
                    checkboxSelection=True,
                    headerCheckboxSelection=True,
                ),
                dag.AgGridColumn(
                    field="model",
                ),
                dag.AgGridColumn(
                    field="price",
                ),
            ],
        ),
        html.Hr(),
        dcc.Markdown(
            "Selections can also be set using a callbacks, as `selectionChanged` supports read and write:"
        ),
        dcc.Checklist(
            options=[
                {"label": name, "value": name} for name in ["Toyota", "Ford", "Porsche"]
            ],
            id="selection-checklist",
        ),
        html.Br(),
        dag.AgGrid(
            id="selectable-grid-callbacks",
            rowData=rowData,
            columnSize="sizeToFit",
            rowSelection="multiple",
            children=[
                dag.AgGridColumn(
                    field="make",
                ),
                dag.AgGridColumn(
                    field="model",
                ),
                dag.AgGridColumn(
                    field="price",
                ),
            ],
        ),
        html.Hr(),
    ]
)


@app.callback(
    Output("currentSelections", "children"),
    Input("selectable-grid", "selectionChanged"),
)
def display_selected_car2(selectionChanged):
    if selectionChanged:
        return "You selected " + ", ".join(
            [
                "{} (model {} and price {})".format(
                    s["make"],
                    s["model"],
                    s["price"],
                )
                for s in selectionChanged
            ]
        )


@app.callback(
    Output("selection-checklist", "value"),
    Output("selectable-grid-callbacks", "selectionChanged"),
    Input("selection-checklist", "value"),
    Input("selectable-grid-callbacks", "selectionChanged"),
)
def select_rows(values, selectionChanged):
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if trigger_id == "selection-checklist":
        return dash.no_update, [i for i in rowData if i["make"] in values]
    elif trigger_id == "selectable-grid-callbacks":
        return [i["make"] for i in selectionChanged], dash.no_update

    return dash.no_update, dash.no_update


if __name__ == "__main__":
    app.run_server(debug=True)
