import dash_ag_grid as dag
from dash import Dash, html, dcc
from . import utils
from dash.testing.wait import until
import pandas as pd


def test_cf001_conditional_formatting(dash_duo):
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
        {"field": "changes"},
    ]

    rowData = [
        {"make": "Toyota", "model": "Celica", "price": 35000},
        {"make": "Ford", "model": "Mondeo", "price": 32000},
        {"make": "Porsche", "model": "Boxster", "price": 72000},
    ]

    cellStyle = {
        "styleConditions": [
            {"condition": "highlightEdits(params)", "style": {"color": "orange"}},
        ]
    }

    defaultColDef = {
        "valueSetter": {"function": "addEdits(params)"},
        "editable": True,
        "cellStyle": cellStyle,
    }

    getRowStyle = {
        "styleConditions": [
            {"condition": "params.data.make == 'Toyota'", "style": {"color": "blue"}}
        ]
    }

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
                getRowStyle=getRowStyle,
                id="grid",
            ),
            html.Button(id="focus"),
        ],
        style={"margin": 20},
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Toyota")

    ### testing styles
    grid.get_cell(0, 0).click()
    until(lambda: "color: blue" in grid.get_row(0).get_attribute("style"), timeout=3)
    grid.get_cell(0, 0).send_keys("t")
    grid.get_cell(0, 1).click()
    until(
        lambda: "color: orange" in grid.get_cell(0, 0).get_attribute("style"), timeout=3
    )
    until(
        lambda: "color: blue" not in grid.get_row(0).get_attribute("style"), timeout=3
    )
    until(
        lambda: "color: orange" not in grid.get_cell(0, 1).get_attribute("style"),
        timeout=3,
    )
    grid.get_cell(0, 1).send_keys("t")
    grid.get_cell(0, 2).click()
    until(
        lambda: "color: orange" not in grid.get_cell(0, 2).get_attribute("style"),
        timeout=3,
    )
    until(
        lambda: "color: orange" in grid.get_cell(0, 1).get_attribute("style"), timeout=3
    )
    grid.get_cell(0, 2).send_keys("t")
    grid.get_cell(0, 0).click()
    until(
        lambda: "color: orange" in grid.get_cell(0, 2).get_attribute("style"), timeout=3
    )
    assert "color: orange" in grid.get_cell(0, 0).get_attribute("style")

def test_cf002_conditional_formatting_enterprise(dash_duo):
    app = Dash(__name__)

    df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
    )

    columnDefs = [
        # Row group by country and by year is enabled.
        {
            "field": "country",
            "rowGroup": True,
            "hide": True,
            "suppressColumnsToolPanel": True,
        },
        {
            "field": "gold",
            "filter": True,
            "aggFunc": "sum",
            "valueFormatter": {"function": "d3.format('(,.2f')(params.value)"},
            "cellStyle": {

                    "styleConditions": [

                        {
                            "condition": f"params.value < 100",
                            "style": {"backgroundColor": "lightgreen"},
                        },

                    ],
                    "defaultStyle": {"backgroundColor": "yellow"},
                },

            },
    ]

    app.layout = html.Div(
        [
            dag.AgGrid(
                id="grid",
                columnDefs=columnDefs,
                rowData=df.to_dict("records"),
                defaultColDef=dict(
                    suppressAggFuncInHeader=True
                ),
                dashGridOptions={"rowSelection":"multiple", "animateRows": False},
                enableEnterpriseModules=True,
                getRowStyle={
                    "styleConditions": [
                        {
                            "condition": "params.node.aggData ? params.node.aggData.gold < 3 : false",
                            "style": {"backgroundColor": "silver"},
                        }
                    ]
                },
            ),
        ]
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    until(
        lambda: "United States" in grid.get_cell(0, 0).text, timeout=3
    )

    ### testing styles
    until(
        lambda: "background-color: yellow" in grid.get_cell(0, 2).get_attribute("style"), timeout=3
    )
    until(
        lambda: "background-color: lightgreen" in grid.get_cell(4, 2).get_attribute("style"), timeout=3
    )
    until(
        lambda: "background-color: silver" in grid.get_row(6).get_attribute("style"),
        timeout=3,
    )

def test_cf003_conditional_formatting(dash_duo):
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
        {"field": "changes"},
    ]

    rowData = [
        {"make": "Toyota", "model": "Celica", "price": 35000},
        {"make": "Ford", "model": "Mondeo", "price": 32000},
        {"make": "Porsche", "model": "Boxster", "price": 72000},
    ]

    defaultColDef = {
        "valueSetter": {"function": "addEdits(params)"},
        "editable": True,
    }

    getRowStyle = {
        "function": 'testToyota(params)'
    }

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
                getRowStyle=getRowStyle,
                id="grid",
            ),
            html.Button(id="focus"),
        ],
        style={"margin": 20},
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Toyota")

    ### testing styles
    grid.get_cell(0, 0).click()
    until(lambda: "color: blue" in grid.get_row(0).get_attribute("style"), timeout=3)
    grid.get_cell(0, 0).send_keys("t")
    grid.get_cell(0, 1).click()
    until(
        lambda: "color: blue" not in grid.get_row(0).get_attribute("style"), timeout=3
    )