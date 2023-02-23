import dash_ag_grid as dag
from dash import Dash, html, dcc
from . import utils
import time
from dash.testing.wait import until

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
        {"field":"changes"}
    ]

    rowData = [
        {"make": "Toyota", "model": "Celica", "price": 35000},
        {"make": "Ford", "model": "Mondeo", "price": 32000},
        {"make": "Porsche", "model": "Boxter", "price": 72000},
    ]

    defaultColDef = {"valueSetter":{"function":"addEdits(params)"}, "editable": True}

    cellStyle = {"styleConditions": [
            {"condition": "highlightEdits(params)", "style": {"color": "orange"}},
        ]}

    getRowStyle= {
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
                cellStyle=cellStyle,
                getRowStyle=getRowStyle,
                id="grid",
            ),
            html.Button(id='focus')
        ],
        style={"margin": 20},
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Toyota")

    ### testing styles
    grid.get_cell(0,0).click()
    until(lambda: 'color: blue' in grid.get_row(0).get_attribute('style'), timeout=3)
    grid.get_cell(0, 0).send_keys('t')
    grid.get_cell(0, 1).click()
    until(lambda: 'color: orange' in grid.get_cell(0, 0).get_attribute('style'), timeout=3)
    until(lambda: 'color: blue' not in grid.get_row(0).get_attribute('style'), timeout=3)
    until(lambda: 'color: orange' not in grid.get_cell(0, 1).get_attribute('style'), timeout=3)
    grid.get_cell(0, 1).send_keys('t')
    grid.get_cell(0,2).click()
    until(lambda: 'color: orange' not in grid.get_cell(0, 2).get_attribute('style'), timeout=3)
    until(lambda: 'color: orange' in grid.get_cell(0, 1).get_attribute('style'), timeout=3)
    grid.get_cell(0, 2).send_keys('t')
    grid.get_cell(0,0).click()
    until(lambda: 'color: orange' in grid.get_cell(0, 2).get_attribute('style'), timeout=3)
    assert 'color: orange' in grid.get_cell(0, 0).get_attribute('style')
