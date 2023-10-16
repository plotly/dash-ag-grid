import dash
import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State, ctx
import json

from . import utils


def test_sp001_selection_persistence(dash_duo):
    app = Dash(__name__)

    rowData = [
        {"make": "Toyota", "model": "Celica", "price": 35000},
        {"make": "Ford", "model": "Mondeo", "price": 32000},
        {"make": "Porsche", "model": "Boxster", "price": 72000},
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
            html.Button(id="ids"),
            html.Button(id="function"),
            html.Button(id="rowInfo"),
            dag.AgGrid(
                id="grid",
                rowData=rowData,
                columnDefs=columnDefs,
                defaultColDef={"flex": 1},
                dashGridOptions={"rowSelection": "multiple"},
                getRowId="params.data.make",
            ),
            html.Div(id="selectedRows"),
        ],
    )

    @app.callback(
        Output("grid", "rowData"),
        Input("transactions-clear", "n_clicks"),
        Input("transactions-start", "n_clicks"),
    )
    def update_rowdata(*_):
        if ctx.triggered_id == "transactions-clear":
            return []
        return rowData

    @app.callback(
        Output("grid", "rowTransaction"),
        Input("transactions-remove", "n_clicks"),
        Input("transactions-update", "n_clicks"),
        Input("transactions-add", "n_clicks"),
        State("grid", "selectedRows"),
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

    @app.callback(Output("selectedRows", "children"), Input("grid", "selectedRows"))
    def selectedRows(s):
        return json.dumps(s)

    @app.callback(
        Output("grid", "selectedRows"),
        Input("ids", "n_clicks"),
        Input("function", "n_clicks"),
        Input("rowInfo", "n_clicks"),
    )
    def setSelections(n, n1, n2):
        if n or n1 or n2:
            if ctx.triggered_id == "ids":
                return {"ids": ["Toyota"]}
            if ctx.triggered_id == "function":
                return {"function": "params.data.make === 'Porsche'"}
            return [{"make": "Ford", "model": "Mondeo", "price": 32000}]
        return []

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")
    grid.wait_for_cell_text(0, 0, "Toyota")
    grid.get_cell(1, 0).click()
    dash_duo.wait_for_text_to_equal(
        "#selectedRows", '[{"make": "Ford", "model": "Mondeo", "price": 32000}]'
    )

    dash_duo.find_element("#transactions-update").click()
    dash_duo.wait_for_text_to_equal(
        "#selectedRows", '[{"make": "Ford", "model": "Mondeo", "price": 32001}]'
    )

    dash_duo.find_element("#transactions-start").click()
    dash_duo.wait_for_text_to_equal(
        "#selectedRows", '[{"make": "Ford", "model": "Mondeo", "price": 32000}]'
    )

    dash_duo.find_element("#ids").click()
    dash_duo.wait_for_text_to_equal(
        "#selectedRows", '[{"make": "Toyota", "model": "Celica", "price": 35000}]'
    )

    dash_duo.find_element("#function").click()
    dash_duo.wait_for_text_to_equal(
        "#selectedRows", '[{"make": "Porsche", "model": "Boxster", "price": 72000}]'
    )

    dash_duo.find_element("#rowInfo").click()
    dash_duo.wait_for_text_to_equal(
        "#selectedRows", '[{"make": "Ford", "model": "Mondeo", "price": 32000}]'
    )
