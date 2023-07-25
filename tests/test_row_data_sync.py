import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, no_update, ctx
import json
from . import utils


def test_rs001_rowdata_sync(dash_duo):
    app = Dash(__name__)

    columnDefs = [
        {
            "headerName": "Make",
            "field": "make",
        },
        {
            "headerName": "Model",
            "field": "model",
        },
        {"headerName": "Price", "field": "price"},
    ]

    rowData = [
        {"make": "Toyota", "model": "Celica", "price": 35000},
        {"make": "Ford", "model": "Mondeo", "price": 32000},
        {"make": "Porsche", "model": "Boxster", "price": 72000},
    ]

    extraData = [
        {"make": "Subaru", "model": "Impreza", "price": 35000},
        {"make": "Mazda", "model": "CX-5", "price": 32000},
        {"make": "Honda", "model": "Pilot", "price": 72000},
    ]

    defaultColDef = {"editable": True}

    app.layout = html.Div(
        [
            dcc.Markdown(
                "In this grid, the __Make__ column has a popup below the cell,  the __Model__ has a popup above the cell, and the __Price__ has the default (in cell) editor."
            ),
            dag.AgGrid(
                columnDefs=columnDefs,
                rowData=rowData,
                defaultColDef=defaultColDef,
                columnSize="sizeToFit",
                id="grid",
                dashGridOptions={"editType": "fullRow"},
            ),
            html.Div(id="data"),
            html.Div(id="virtualData"),
            html.Button("edit mode", id="editMode", n_clicks=0),
            html.Button(id="reset", children="reset", n_clicks=0),
            html.Button("addRow", id="addRow", n_clicks=0),
            html.Button("addRow_notAsync", id="addRow_notAsync", n_clicks=0),
        ],
        style={"margin": 20},
    )

    @app.callback(Output("grid", "dashGridOptions"), Input("editMode", "n_clicks"))
    def toggleMode(n):
        if n:
            assert n > 0
            if n % 2 == 0:
                return {"editType": "fullRow"}
            else:
                return {"editType": None}

    @app.callback(
        Output("data", "children"),
        Input("grid", "cellValueChanged"),
        Input("grid", "rowData"),
    )
    def rowDataUpdate(c, d):
        if d:
            return json.dumps(d)

    @app.callback(
        Output("grid", "rowData"),
        Output("addRow", "n_clicks"),
        Output("addRow_notAsync", "n_clicks"),
        Input("reset", "n_clicks"),
    )
    def reset(n):
        if n > 0:
            return rowData, 0, 0
        return no_update, no_update, no_update

    @app.callback(
        Output("grid", "rowTransaction"),
        Input("addRow", "n_clicks"),
        Input("addRow_notAsync", "n_clicks"),
    )
    def addRows(n, n2):
        if n or n2:
            if ctx.triggered_id == "addRow":
                return {"add": [extraData[n - 1]]}
            if ctx.triggered_id == "addRow_notAsync":
                return {"add": [extraData[n2 - 1]], "async": False}

    @app.callback(
        Output("virtualData", "children"),
        Input("grid", "cellValueChanged"),
        Input("grid", "virtualRowData"),
    )
    def virtualDataUpdate(c, d):
        if d:
            return json.dumps(d)

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Toyota")

    base = (
        '[{"make": "Toyota", "model": "Celica", "price": 35000}, '
        '{"make": "Ford", "model": "Mondeo", "price": 32000}, '
        '{"make": "Porsche", "model": "Boxster", "price": 72000}'
    )

    ### testing editing sync
    for x in range(2):
        grid.get_cell(0, 0).click()
        grid.get_cell(0, 0).send_keys("t")
        grid.get_cell(1, 1).click()
        dash_duo.wait_for_text_to_equal(
            "#data",
            '[{"make": "t", "model": "Celica", "price": 35000}, '
            '{"make": "Ford", "model": "Mondeo", "price": 32000}, '
            '{"make": "Porsche", "model": "Boxster", "price": 72000}]',
        )
        dash_duo.wait_for_text_to_equal(
            "#virtualData",
            '[{"make": "t", "model": "Celica", "price": 35000}, '
            '{"make": "Ford", "model": "Mondeo", "price": 32000}, '
            '{"make": "Porsche", "model": "Boxster", "price": 72000}]',
        )
        grid.get_cell(1, 1).send_keys("t")
        grid.get_cell(2, 2).click()
        dash_duo.wait_for_text_to_equal(
            "#data",
            '[{"make": "t", "model": "Celica", "price": 35000}, '
            '{"make": "Ford", "model": "t", "price": 32000}, '
            '{"make": "Porsche", "model": "Boxster", "price": 72000}]',
        )
        dash_duo.wait_for_text_to_equal(
            "#virtualData",
            '[{"make": "t", "model": "Celica", "price": 35000}, '
            '{"make": "Ford", "model": "t", "price": 32000}, '
            '{"make": "Porsche", "model": "Boxster", "price": 72000}]',
        )
        grid.get_cell(2, 2).send_keys("t")
        grid.get_cell(0, 0).click()
        dash_duo.wait_for_text_to_equal(
            "#data",
            '[{"make": "t", "model": "Celica", "price": 35000}, '
            '{"make": "Ford", "model": "t", "price": 32000}, '
            '{"make": "Porsche", "model": "Boxster", "price": null}]',
        )
        dash_duo.wait_for_text_to_equal(
            "#virtualData",
            '[{"make": "t", "model": "Celica", "price": 35000}, '
            '{"make": "Ford", "model": "t", "price": 32000}, '
            '{"make": "Porsche", "model": "Boxster", "price": null}]',
        )
        dash_duo.find_element("#reset").click()
        dash_duo.wait_for_text_to_equal("#data", base + "]")
        dash_duo.find_element("#editMode").click()

    for x in ["addRow", "addRow_notAsync"]:
        dash_duo.find_element(f"#{x}").click()
        dash_duo.wait_for_text_to_equal(
            "#data", base + ', {"make": "Subaru", "model": "Impreza", "price": 35000}]'
        )
        dash_duo.wait_for_text_to_equal(
            "#virtualData",
            base + ', {"make": "Subaru", "model": "Impreza", "price": 35000}]',
        )
        dash_duo.find_element(f"#{x}").click()
        dash_duo.wait_for_text_to_equal(
            "#data",
            base + ', {"make": "Subaru", "model": "Impreza", "price": 35000},'
            ' {"make": "Mazda", "model": "CX-5", "price": 32000}]',
        )
        dash_duo.wait_for_text_to_equal(
            "#virtualData",
            base + ', {"make": "Subaru", "model": "Impreza", "price": 35000},'
            ' {"make": "Mazda", "model": "CX-5", "price": 32000}]',
        )
        dash_duo.find_element(f"#{x}").click()
        dash_duo.wait_for_text_to_equal(
            "#data",
            base + ', {"make": "Subaru", "model": "Impreza", "price": 35000},'
            ' {"make": "Mazda", "model": "CX-5", "price": 32000}, '
            '{"make": "Honda", "model": "Pilot", "price": 72000}]',
        )
        dash_duo.wait_for_text_to_equal(
            "#virtualData",
            base + ', {"make": "Subaru", "model": "Impreza", "price": 35000},'
            ' {"make": "Mazda", "model": "CX-5", "price": 32000}, '
            '{"make": "Honda", "model": "Pilot", "price": 72000}]',
        )

        dash_duo.find_element("#reset").click()
        dash_duo.wait_for_text_to_equal("#data", base + "]")
