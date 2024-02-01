import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import json
from . import utils
from dash.testing.wait import until


def test_ga001_grid_apis(dash_duo):
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
            dag.AgGrid(
                id="grid",
                columnDefs=columnDefs,
                rowData=[rowData[0]],
                defaultColDef={
                    "editable": True,
                },
                rowClassRules={
                    "row-orange": "params.data.model == 'Mondeo'",
                    "row-red": "params.data.model == 'Boxster'",
                    "row-blue": "params.data.model == 'Celica'",
                },
                dashGridOptions={"getRowClass": {"function": "rowTest(params)"},
                                 "preventDefaultOnContextMenu": True},
            ),
            html.Button(id='addRow', children='add_row', n_clicks=0),
            html.Button(id='hidePrice', n_clicks=0),
            html.Div(id='virtualRowData'),
            html.Div(id='columnState'),
            html.Div(id='cellContext')
        ]
    )

    app.clientside_callback("function (n) { if (n) {" \
                            "grid = dash_ag_grid.getApi('grid'); " \
                            "if (n == 1) {" \
                            "grid.applyTransactionAsync({'add': [" + json.dumps(rowData[1]) + "]});" \
                                                                                              "} else {" \
                                                                                              "grid.applyTransactionAsync({'add': [" + json.dumps(
        rowData[2]) + "]});" \
                      "}} return dash_clientside.no_update}", Output('addRow', 'id'), Input('addRow', 'n_clicks'),
                            prevent_intial_Call=True)

    app.clientside_callback(
        """function (d) {
            return JSON.stringify(d)
        }""", Output('virtualRowData', 'children'), Input('grid', 'virtualRowData')
    )

    app.clientside_callback(
        """function (d) {
            return JSON.stringify(d)
        }""", Output('columnState', 'children'), Input('grid', 'columnState')
    )

    app.clientside_callback(
        """async function (id) {
            grid = await dash_ag_grid.getApiAsync(id)
            grid.addEventListener('cellContextMenu', (params) => {
                    document.getElementById('cellContext').innerText = params.value;
                })
            return window.dash_clientside.no_update
        }""",
        Output('grid', 'id'), Input('grid', 'id')
    )

    app.clientside_callback(
        """function (n) {
            if (n) {
                dash_ag_grid.getApi('grid').setColumnVisible("price", false)
            }
            return dash_clientside.no_update
        }""",
        Output('hidePrice', 'id'), Input('hidePrice', 'n_clicks')
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Toyota")

    # testing adding data
    dash_duo.find_element("#addRow").click()
    grid.wait_for_cell_text(1, 0, "Ford")

    dash_duo.find_element("#addRow").click()
    grid.wait_for_cell_text(2, 0, "Porsche")

    until(lambda: json.loads(dash_duo.find_element('#virtualRowData').text) == rowData, timeout=3)

    dash_duo.find_element("#hidePrice").click()
    until(lambda: dash_duo.find_element('#columnState').text != '', timeout=3)
    until(lambda: json.loads(dash_duo.find_element('#columnState').text)[2]['hide'], timeout=3)

    action = utils.ActionChains(dash_duo.driver)
    action.context_click(grid.get_cell(0,0)).perform()
    until(lambda: dash_duo.find_element('#cellContext').text == 'Toyota', timeout=3)
