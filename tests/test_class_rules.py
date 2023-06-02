import dash_ag_grid as dag
from dash import Dash, html, dcc
from . import utils
from dash.testing.wait import until


def test_cr001_class_rules(dash_duo):
    app = Dash(
        __name__,
        meta_tags=[
            {
                "http-equiv": "content-security-policy",
                "content": "default-src 'self'; script-src 'self' 'unsafe-inline';"
                " style-src https://* 'self' 'unsafe-inline'; "
                "font-src data: https://* 'self' 'unsafe-inline';"
                "img-src data: https://* 'self'",
            }
        ],
    )

    rowData = [
        {"make": "Toyota", "model": "Celica", "price": 35000},
        {"make": "Ford", "model": "Mondeo", "price": 32000},
        {"make": "Porsche", "model": "Boxster", "price": 72000},
    ]

    columnDefs = [
        {
            "headerName": "Make",
            "field": "make",
            "cellClassRules": {
                "orange": "params.value == 'Ford'",
                "red": "params.value == 'Porsche'",
                "blue": "params.value == 'Toyota'",
            },
        },
        {"headerName": "Model", "field": "model"},
        {"headerName": "Price", "field": "price"},
    ]

    app.layout = html.Div(
        [
            dcc.Markdown(
                "Try filtering the data in the grid using the inline filters (click the hamburger menu in each column). Though the data is still in `rowData`, you can view the virtual row data in callbacks by watching the `virtualRowData` property."
            ),
            dag.AgGrid(
                id="grid",
                columnDefs=columnDefs,
                rowData=rowData,
                defaultColDef={
                    "editable": True,
                },
                rowClassRules={
                    "row-orange": "params.data.model == 'Mondeo'",
                    "row-red": "params.data.model == 'Boxster'",
                    "row-blue": "params.data.model == 'Celica'",
                },
                dashGridOptions={"getRowClass": {"function": "rowTest(params)"}},
            ),
        ]
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Toyota")

    ### testing class rules
    grid.get_cell(0, 0).click()
    until(lambda: "row-blue" in grid.get_row(0).get_attribute("class"), timeout=3)
    until(lambda: "testing" in grid.get_row(0).get_attribute("class"), timeout=3)
    until(lambda: "blue" in grid.get_cell(0, 0).get_attribute("class"), timeout=3)
    grid.get_cell(0, 0).send_keys("t")
    grid.get_cell(0, 1).send_keys("t")
    grid.get_cell(1, 0).click()
    until(lambda: "row-blue" not in grid.get_row(0).get_attribute("class"), timeout=3)
    until(lambda: "blue" not in grid.get_cell(0, 0).get_attribute("class"), timeout=3)

    until(lambda: "row-orange" in grid.get_row(1).get_attribute("class"), timeout=3)
    until(lambda: "orange" in grid.get_cell(1, 0).get_attribute("class"), timeout=3)
    grid.get_cell(1, 0).send_keys("t")
    grid.get_cell(1, 1).send_keys("t")
    grid.get_cell(2, 0).click()
    until(lambda: "row-orange" not in grid.get_row(1).get_attribute("class"), timeout=3)
    until(lambda: "orange" not in grid.get_cell(1, 0).get_attribute("class"), timeout=3)

    until(lambda: "row-red" in grid.get_row(2).get_attribute("class"), timeout=3)
    until(lambda: "red" in grid.get_cell(2, 0).get_attribute("class"), timeout=3)
    grid.get_cell(2, 0).send_keys("t")
    grid.get_cell(2, 1).send_keys("t")
    grid.get_cell(1, 0).click()
    until(lambda: "red" not in grid.get_row(2).get_attribute("class"), timeout=3)
    until(lambda: "red" not in grid.get_cell(2, 0).get_attribute("class"), timeout=3)
