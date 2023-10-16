"""
Nested tables.
"""

import dash_ag_grid as dag
import dash
from dash import Input, Output, html, dcc, Dash
from . import utils
from dash.testing.wait import until
import time


def test_rf001_recursive_functions(dash_duo):
    app = Dash(__name__)
    masterColumnDefs = [
        {
            "headerName": "Country",
            "field": "country",
            "cellRenderer": "agGroupCellRenderer",
        },
        {"headerName": "Region", "field": "region"},
        {"headerName": "Population", "field": "population"},
    ]

    detailColumnDefs = [
        {
            "headerName": "City",
            "field": "city",
            "valueGetter": {"function": "`**${1+2}**`"},
            "cellStyle": {"color": "red"},
            "cellRendererParams": {
                "innerRenderer": "markdown"
            }
        },
        {"headerName": "Pop. (City proper)", "field": "population_city"},
        {"headerName": "Pop. (Metro area)", "field": "population_metro"},
        {
            "headerName": "testFun",
            "children": [
                {
                    "headerName": "Pop. (Metro area)",
                    "field": "population_metro",
                    "valueGetter": {"function": "`**${1+2}**`"},
                    "cellRenderer": "markdown"
                },
                {
                    "headerName": "testing",
                    "children": [
                        {
                            "headerName": "So Much Fun",
                            "field": "population_metro",
                            "valueFormatter": {"function": "3+5"},
                        },
                    ],
                },
            ],
        },
    ]

    nextLevel = detailColumnDefs.copy()
    nextLevel[0]["cellRenderer"] = "agGroupCellRenderer"

    rowData = [
        {
            "country": "China",
            "region": "Asia",
            "population": 1411778724,
            "cities": [
                {
                    "city": "Shanghai",
                    "population_city": 24870895,
                    "population_metro": "NA",
                },
                {
                    "city": "Beijing",
                    "population_city": 21893095,
                    "population_metro": "NA",
                },
                {
                    "city": "Chongqing",
                    "population_city": 32054159,
                    "population_metro": "NA",
                },
            ],
        },
        {
            "country": "India",
            "region": "Asia",
            "population": 1383524897,
            "cities": [
                {
                    "city": "Delhi",
                    "population_city": 16753235,
                    "population_metro": 29000000,
                    "cities": [
                        {
                            "city": "Delhi",
                            "population_city": 16753235,
                            "population_metro": 29000000,
                        },
                        {
                            "city": "Mumbai",
                            "population_city": 12478447,
                            "population_metro": 24400000,
                        },
                        {
                            "city": "Kolkata",
                            "population_city": 4496694,
                            "population_metro": 14035959,
                        },
                    ],
                },
                {
                    "city": "Mumbai",
                    "population_city": 12478447,
                    "population_metro": 24400000,
                },
                {
                    "city": "Kolkata",
                    "population_city": 4496694,
                    "population_metro": 14035959,
                },
            ],
        },
        {
            "country": "United States",
            "region": "Americas",
            "population": 332593407,
            "cities": [
                {
                    "city": "New York",
                    "population_city": 8398748,
                    "population_metro": 19303808,
                },
                {
                    "city": "Los Angeles",
                    "population_city": 3990456,
                    "population_metro": 13291486,
                },
                {
                    "city": "Chicago",
                    "population_city": 2746388,
                    "population_metro": 9618502,
                },
            ],
        },
        {
            "country": "Indonesia",
            "region": "Asia",
            "population": 271350000,
            "cities": [
                {
                    "city": "Jakarta",
                    "population_city": 10154134,
                    "population_metro": 33430285,
                },
            ],
        },
    ]

    cellStyle = {
        "styleConditions": [
            {"condition": 'params.data.city=="Delhi"', "style": {"color": "orange"}}
        ]
    }

    app.layout = html.Div(
        [
            dag.AgGrid(
                id="grid",
                columnDefs=masterColumnDefs,
                defaultColDef={"cellStyle": cellStyle},
                rowData=rowData,
                columnSize="sizeToFit",
                enableEnterpriseModules=True,
                masterDetail=True,
                detailCellRendererParams={
                    "detailGridOptions": {
                        "columnDefs": nextLevel,
                        "defaultColDef": {"cellStyle": cellStyle},
                        "detailCellRendererParams": {
                            "detailGridOptions": {
                                "columnDefs": detailColumnDefs,
                                "defaultColDef": {"cellStyle": cellStyle},
                            },
                            "detailColName": "cities",
                            "suppressCallback": True,
                        },
                        "masterDetail": True,
                    },
                    "detailColName": "cities",
                    "suppressCallback": True,
                },
                dashGridOptions={"detailRowAutoHeight": True},
            )
        ]
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")
    grid.wait_for_cell_text(0, 0, "China")

    grid.get_cell_expandable(1, 0).click()

    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="1"]', "3"
    )
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="1"] strong', "3"
    )
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="4"]', "3"
    )
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="4"] strong', "3"
    )
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="5"]', "8"
    )
    assert "color: red" in dash_duo.find_element(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="1"]'
    ).get_attribute("style")
    assert "color: orange" in dash_duo.find_element(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="2"]'
    ).get_attribute("style")
    assert "color: orange" in dash_duo.find_element(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="4"]'
    ).get_attribute("style")
    assert "color: orange" in dash_duo.find_element(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="5"]'
    ).get_attribute("style")

    dash_duo.find_element(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="1"] .ag-group-contracted'
    ).click()
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid .ag-details-grid [row-index="0"] [aria-colindex="1"]',
        "3",
    )
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid .ag-details-grid [row-index="0"] [aria-colindex="1"] strong',
        "3",
    )
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid .ag-details-grid [row-index="0"] [aria-colindex="4"]',
        "3",
    )
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid .ag-details-grid [row-index="0"] [aria-colindex="4"] strong',
        "3",
    )
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid .ag-details-grid [row-index="0"] [aria-colindex="5"]',
        "8",
    )
    assert "color: red" in dash_duo.find_element(
        '#grid .ag-details-grid .ag-details-grid [row-index="0"] [aria-colindex="1"]'
    ).get_attribute("style")
    assert "color: orange" in dash_duo.find_element(
        '#grid .ag-details-grid .ag-details-grid [row-index="0"] [aria-colindex="2"]'
    ).get_attribute("style")
    assert "color: orange" in dash_duo.find_element(
        '#grid .ag-details-grid .ag-details-grid [row-index="0"] [aria-colindex="4"]'
    ).get_attribute("style")
    assert "color: orange" in dash_duo.find_element(
        '#grid .ag-details-grid .ag-details-grid [row-index="0"] [aria-colindex="5"]'
    ).get_attribute("style")


def test_rf002_recursive_functions_server(dash_duo):
    app = Dash(__name__)
    masterColumnDefs = [
        {
            "headerName": "Country",
            "field": "country",
            "cellRenderer": "agGroupCellRenderer",
        },
        {"headerName": "Region", "field": "region"},
        {"headerName": "Population", "field": "population"},
    ]

    detailColumnDefs = [
        {
            "headerName": "City",
            "field": "city",
            "valueGetter": {"function": "`**${1+2}**`"},
            "cellRendererParams": {"innerRenderer": "markdown"},
            "cellStyle": {"color": "red"},
        },
        {"headerName": "Pop. (City proper)", "field": "population_city"},
        {"headerName": "Pop. (Metro area)", "field": "population_metro"},
        {
            "headerName": "testFun",
            "children": [
                {
                    "headerName": "Pop. (Metro area)",
                    "field": "population_metro",
                    "valueGetter": {"function": "`**${1+2}**`"},
                    "cellRenderer": "markdown"
                },
                {
                    "headerName": "testing",
                    "children": [
                        {
                            "headerName": "So Much Fun",
                            "field": "population_metro",
                            "valueFormatter": {"function": "3+5"},
                        },
                    ],
                },
            ],
        },
    ]

    nextLevel = detailColumnDefs.copy()
    nextLevel[0]["cellRenderer"] = "agGroupCellRenderer"

    rowData = [
        {
            "country": "China",
            "region": "Asia",
            "population": 1411778724,
            "cities": [
                {
                    "city": "Shanghai",
                    "population_city": 24870895,
                    "population_metro": "NA",
                },
                {
                    "city": "Beijing",
                    "population_city": 21893095,
                    "population_metro": "NA",
                },
                {
                    "city": "Chongqing",
                    "population_city": 32054159,
                    "population_metro": "NA",
                },
            ],
        },
        {
            "country": "India",
            "region": "Asia",
            "population": 1383524897,
            "cities": [
                {
                    "city": "Delhi",
                    "population_city": 16753235,
                    "population_metro": 29000000,
                    "cities": [
                        {
                            "city": "Delhi",
                            "population_city": 16753235,
                            "population_metro": 29000000,
                        },
                        {
                            "city": "Mumbai",
                            "population_city": 12478447,
                            "population_metro": 24400000,
                        },
                        {
                            "city": "Kolkata",
                            "population_city": 4496694,
                            "population_metro": 14035959,
                        },
                    ],
                },
                {
                    "city": "Mumbai",
                    "population_city": 12478447,
                    "population_metro": 24400000,
                },
                {
                    "city": "Kolkata",
                    "population_city": 4496694,
                    "population_metro": 14035959,
                },
            ],
        },
        {
            "country": "United States",
            "region": "Americas",
            "population": 332593407,
            "cities": [
                {
                    "city": "New York",
                    "population_city": 8398748,
                    "population_metro": 19303808,
                },
                {
                    "city": "Los Angeles",
                    "population_city": 3990456,
                    "population_metro": 13291486,
                },
                {
                    "city": "Chicago",
                    "population_city": 2746388,
                    "population_metro": 9618502,
                },
            ],
        },
        {
            "country": "Indonesia",
            "region": "Asia",
            "population": 271350000,
            "cities": [
                {
                    "city": "Jakarta",
                    "population_city": 10154134,
                    "population_metro": 33430285,
                },
            ],
        },
    ]

    cellStyle = {
        "styleConditions": [
            {"condition": 'params.data.city=="Delhi"', "style": {"color": "orange"}}
        ]
    }

    app.layout = html.Div(
        [
            dag.AgGrid(
                id="grid",
                columnDefs=masterColumnDefs,
                defaultColDef={"cellStyle": cellStyle},
                rowData=rowData,
                columnSize="sizeToFit",
                enableEnterpriseModules=True,
                masterDetail=True,
                detailCellRendererParams={
                    "detailGridOptions": {
                        "columnDefs": nextLevel,
                        "defaultColDef": {"cellStyle": cellStyle},
                        "detailCellRendererParams": {
                            "detailGridOptions": {
                                "columnDefs": detailColumnDefs,
                                "defaultColDef": {"cellStyle": cellStyle},
                            },
                            "suppressCallback": False,
                        },
                        "masterDetail": True,
                    },
                    "suppressCallback": False,
                },
                dashGridOptions={"detailRowAutoHeight": True},
            )
        ]
    )

    @app.callback(
        Output("grid", "getDetailResponse"),
        Input("grid", "getDetailRequest"),
        prevent_initial_call=True,
    )
    def handle_request(request):
        return request["data"]["cities"]

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")
    grid.wait_for_cell_text(0, 0, "China")

    grid.get_cell_expandable(1, 0).click()

    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="1"]', "3"
    )
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="1"] strong', "3"
    )
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="4"]', "3"
    )
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="4"] strong', "3"
    )
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="5"]', "8"
    )
    assert "color: red" in dash_duo.find_element(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="1"]'
    ).get_attribute("style")
    assert "color: orange" in dash_duo.find_element(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="2"]'
    ).get_attribute("style")
    assert "color: orange" in dash_duo.find_element(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="4"]'
    ).get_attribute("style")
    assert "color: orange" in dash_duo.find_element(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="5"]'
    ).get_attribute("style")

    dash_duo.find_element(
        '#grid .ag-details-grid [row-index="0"] [aria-colindex="1"] .ag-group-contracted'
    ).click()
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid .ag-details-grid [row-index="0"] [aria-colindex="1"]',
        "3",
    )
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid .ag-details-grid [row-index="0"] [aria-colindex="1"] strong',
        "3",
    )
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid .ag-details-grid [row-index="0"] [aria-colindex="4"]',
        "3",
    )
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid .ag-details-grid [row-index="0"] [aria-colindex="4"] strong',
        "3",
    )
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-details-grid .ag-details-grid [row-index="0"] [aria-colindex="5"]',
        "8",
    )
    assert "color: red" in dash_duo.find_element(
        '#grid .ag-details-grid .ag-details-grid [row-index="0"] [aria-colindex="1"]'
    ).get_attribute("style")
    assert "color: orange" in dash_duo.find_element(
        '#grid .ag-details-grid .ag-details-grid [row-index="0"] [aria-colindex="2"]'
    ).get_attribute("style")
    assert "color: orange" in dash_duo.find_element(
        '#grid .ag-details-grid .ag-details-grid [row-index="0"] [aria-colindex="4"]'
    ).get_attribute("style")
    assert "color: orange" in dash_duo.find_element(
        '#grid .ag-details-grid .ag-details-grid [row-index="0"] [aria-colindex="5"]'
    ).get_attribute("style")
