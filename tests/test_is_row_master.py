"""
Nested tables.
"""

import dash_ag_grid as dag
import dash
from dash import Input, Output, html, dcc, Dash
from . import utils
from dash.testing.wait import until
import time


def test_rm001_row_master(dash_duo):
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
        {"headerName": "City", "field": "city"},
        {"headerName": "Pop. (City proper)", "field": "population_city"},
        {"headerName": "Pop. (Metro area)", "field": "population_metro"},
    ]
    rowData = [
        {
            "country": "China",
            "region": "Asia",
            "population": 1411778724,
            "cities": [
                {"city": "Shanghai", "population_city": 24870895, "population_metro": "NA"},
                {"city": "Beijing", "population_city": 21893095, "population_metro": "NA"},
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

    app.layout = html.Div(
        [
            dag.AgGrid(
                id="grid",
                enableEnterpriseModules=True,
                columnDefs=masterColumnDefs,
                rowData=rowData,
                columnSize="sizeToFit",
                masterDetail=True,
                detailCellRendererParams={
                    "detailGridOptions": {
                        "columnDefs": detailColumnDefs,
                    },
                    "detailColName": "cities",
                    "suppressCallback": True,
                },
                dashGridOptions={"detailRowAutoHeight": True,
                                 'isRowMaster': {'function': 'params ? params.country == "China" : false'}},
            ),
        ]
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")
    grid.wait_for_cell_text(0, 0, "China")
    grid.get_cell_expandable(0, 0)

    try:
        grid.get_cell_expandable(1, 0)
        ### expandable row was found on India
        assert False
    except:
        ### expandable row was not found on India
        assert True

