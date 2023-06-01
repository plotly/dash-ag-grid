import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
from . import utils
from dash.testing.wait import until
import json


def test_cc001_cell_clicked(dash_duo):
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

    defaultColDef = {"valueSetter": {"function": "addEdits(params)"}, "editable": True}

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
                getRowId="params.data.model",
                id="grid",
            ),
            html.Div(id="focus"),
        ],
        style={"margin": 20},
    )

    @app.callback(Output("focus", "children"), Input("grid", "cellClicked"))
    def clickData(d):
        return json.dumps(d)

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Toyota")

    ### testing styles
    grid.get_cell(0, 0).click()
    until(
        lambda: '{"value": "Toyota", "colId": "make", "rowIndex": 0, "rowId": "Celica"'
        in dash_duo.find_element("#focus").get_attribute("innerText"),
        timeout=3,
    )
    grid.get_cell(1, 1).click()
    until(
        lambda: '{"value": "Mondeo", "colId": "model", "rowIndex": 1, "rowId": "Mondeo"'
        in dash_duo.find_element("#focus").get_attribute("innerText"),
        timeout=3,
    )
    grid.get_cell(2, 2).click()
    until(
        lambda: '{"value": 72000, "colId": "price", "rowIndex": 2, "rowId": "Boxster"'
        in dash_duo.find_element("#focus").get_attribute("innerText"),
        timeout=3,
    )
