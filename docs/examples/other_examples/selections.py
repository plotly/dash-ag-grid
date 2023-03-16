"""
Demonstration of working with AG-Grid in a variety of use-cases involving selections.
"""
import dash_ag_grid as dag
from dash import Dash, Input, Output, html, dcc, ctx, no_update

app = Dash(__name__)

columnDefs = [
    {
        "headerName": "Make",
        "field": "make",
        "checkboxSelection": True,
        "headerCheckboxSelection": True,
    },
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
        dcc.Markdown("Select rows and the data will be displayed below the table."),
        dag.AgGrid(
            id="selectable-grid",
            rowData=rowData,
            columnDefs=columnDefs,
            columnSize="sizeToFit",
            dashGridOptions={"rowSelection": "multiple"},
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
            dashGridOptions={"rowSelection": "multiple"},
            persistence=True,
            columnDefs=columnDefs,
        ),
        html.Hr(),
        dcc.Markdown(
            "Selections can also be set using a callbacks, as `selectedRows` supports read and write:"
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
            dashGridOptions={"rowSelection": "multiple"},
            columnDefs=[
                {"headerName": "Make", "field": "make"},
                {"headerName": "Model", "field": "model"},
                {"headerName": "Price", "field": "price"},
            ],
        ),
        html.Hr(),
    ]
)


@app.callback(
    Output("currentSelections", "children"),
    Input("selectable-grid", "selectedRows"),
)
def display_selected_car2(selectedRows):
    if selectedRows:
        return "You selected " + ", ".join(
            [
                "{} (model {} and price {})".format(
                    s["make"],
                    s["model"],
                    s["price"],
                )
                for s in selectedRows
            ]
        )


@app.callback(
    Output("selection-checklist", "value"),
    Output("selectable-grid-callbacks", "selectedRows"),
    Input("selection-checklist", "value"),
    Input("selectable-grid-callbacks", "selectedRows"),
)
def select_rows(values, selectedRows):
    if ctx.triggered_id == "selection-checklist":
        return no_update, [i for i in rowData if i["make"] in values]
    if ctx.triggered_id == "selectable-grid-callbacks":
        return [i["make"] for i in selectedRows], no_update

    return no_update, no_update


if __name__ == "__main__":
    app.run_server(debug=True)
