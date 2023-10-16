import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, no_update
from . import utils
import time
from dash.testing.wait import until
import json


def test_td001_tree_data(dash_duo):
    app = Dash(__name__)

    rowData = [
        {
            "orgHierarchy": ["Erica Rogers"],
            "jobTitle": "CEO",
            "employmentType": "Permanent",
        },
        {
            "orgHierarchy": ["Erica Rogers", "Malcolm Barrett"],
            "jobTitle": "Exec. Vice President",
            "employmentType": "Permanent",
        },
        {
            "orgHierarchy": ["Erica Rogers", "Malcolm Barrett", "Esther Baker"],
            "jobTitle": "Director of Operations",
            "employmentType": "Permanent",
        },
        {
            "orgHierarchy": [
                "Erica Rogers",
                "Malcolm Barrett",
                "Esther Baker",
                "Brittany Hanson",
            ],
            "jobTitle": "Fleet Coordinator",
            "employmentType": "Permanent",
        },
        {
            "orgHierarchy": [
                "Erica Rogers",
                "Malcolm Barrett",
                "Esther Baker",
                "Brittany Hanson",
                "Leah Flowers",
            ],
            "jobTitle": "Parts Technician",
            "employmentType": "Contract",
        },
        {
            "orgHierarchy": [
                "Erica Rogers",
                "Malcolm Barrett",
                "Esther Baker",
                "Brittany Hanson",
                "Tammy Sutton",
            ],
            "jobTitle": "Service Technician",
            "employmentType": "Contract",
        },
        {
            "orgHierarchy": [
                "Erica Rogers",
                "Malcolm Barrett",
                "Esther Baker",
                "Derek Paul",
            ],
            "jobTitle": "Inventory Control",
            "employmentType": "Permanent",
        },
        {
            "orgHierarchy": ["Erica Rogers", "Malcolm Barrett", "Francis Strickland"],
            "jobTitle": "VP Sales",
            "employmentType": "Permanent",
        },
        {
            "orgHierarchy": [
                "Erica Rogers",
                "Malcolm Barrett",
                "Francis Strickland",
                "Morris Hanson",
            ],
            "jobTitle": "Sales Manager",
            "employmentType": "Permanent",
        },
        {
            "orgHierarchy": [
                "Erica Rogers",
                "Malcolm Barrett",
                "Francis Strickland",
                "Todd Tyler",
            ],
            "jobTitle": "Sales Executive",
            "employmentType": "Contract",
        },
        {
            "orgHierarchy": [
                "Erica Rogers",
                "Malcolm Barrett",
                "Francis Strickland",
                "Bennie Wise",
            ],
            "jobTitle": "Sales Executive",
            "employmentType": "Contract",
        },
        {
            "orgHierarchy": [
                "Erica Rogers",
                "Malcolm Barrett",
                "Francis Strickland",
                "Joel Cooper",
            ],
            "jobTitle": "Sales Executive",
            "employmentType": "Permanent",
        },
    ]

    grid = html.Div(
        [
            dag.AgGrid(
                columnDefs=[
                    # we're using the auto group column by default!
                    {"field": "jobTitle"},
                    {"field": "employmentType"},
                ],
                defaultColDef={
                    "flex": 1,
                },
                dashGridOptions={
                    "autoGroupColumnDef": {
                        "headerName": "Organisation Hierarchy",
                        "minWidth": 300,
                        "cellRendererParams": {
                            "suppressCount": True,
                        },
                    },
                    "groupDefaultExpanded": -1,
                    "getDataPath": {"function": "getDataPath(params)"},
                    "treeData": True,
                },
                rowData=rowData,
                enableEnterpriseModules=True,
                id="grid",
            ),
            html.Hr(),
        ]
    )

    app.layout = html.Div(
        [
            grid,
        ]
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Erica Rogers")

    ### testing tree functions
    grid.wait_for_cell_text(1, 0, "Malcolm Barrett")
    grid.wait_for_cell_text(3, 0, "Brittany Hanson")
    grid.get_cell_collapsable(2, 0).click()
    grid.wait_for_cell_text(3, 0, "Francis Strickland")
    grid.get_cell_expandable(2, 0).click()
    grid.wait_for_cell_text(3, 0, "Brittany Hanson")


def test_td002_tree_data(dash_duo):
    app = Dash(__name__)

    rowData = [
        {
            "orgHierarchy": ["Erica Rogers"],
            "jobTitle": "CEO",
            "employmentType": "Permanent",
        },
        {
            "orgHierarchy": ["Erica Rogers", "Malcolm Barrett"],
            "jobTitle": "Exec. Vice President",
            "employmentType": "Permanent",
        },
        {
            "orgHierarchy": ["Erica Rogers", "Malcolm Barrett", "Esther Baker"],
            "jobTitle": "Director of Operations",
            "employmentType": "Permanent",
        },
        {
            "orgHierarchy": [
                "Erica Rogers",
                "Malcolm Barrett",
                "Esther Baker",
                "Brittany Hanson",
            ],
            "jobTitle": "Fleet Coordinator",
            "employmentType": "Permanent",
        },
        {
            "orgHierarchy": [
                "Erica Rogers",
                "Malcolm Barrett",
                "Esther Baker",
                "Brittany Hanson",
                "Leah Flowers",
            ],
            "jobTitle": "Parts Technician",
            "employmentType": "Contract",
        },
        {
            "orgHierarchy": [
                "Erica Rogers",
                "Malcolm Barrett",
                "Esther Baker",
                "Brittany Hanson",
                "Tammy Sutton",
            ],
            "jobTitle": "Service Technician",
            "employmentType": "Contract",
        },
        {
            "orgHierarchy": [
                "Erica Rogers",
                "Malcolm Barrett",
                "Esther Baker",
                "Derek Paul",
            ],
            "jobTitle": "Inventory Control",
            "employmentType": "Permanent",
        },
        {
            "orgHierarchy": ["Erica Rogers", "Malcolm Barrett", "Francis Strickland"],
            "jobTitle": "VP Sales",
            "employmentType": "Permanent",
        },
        {
            "orgHierarchy": [
                "Erica Rogers",
                "Malcolm Barrett",
                "Francis Strickland",
                "Morris Hanson",
            ],
            "jobTitle": "Sales Manager",
            "employmentType": "Permanent",
        },
        {
            "orgHierarchy": [
                "Erica Rogers",
                "Malcolm Barrett",
                "Francis Strickland",
                "Todd Tyler",
            ],
            "jobTitle": "Sales Executive",
            "employmentType": "Contract",
        },
        {
            "orgHierarchy": [
                "Erica Rogers",
                "Malcolm Barrett",
                "Francis Strickland",
                "Bennie Wise",
            ],
            "jobTitle": "Sales Executive",
            "employmentType": "Contract",
        },
        {
            "orgHierarchy": [
                "Erica Rogers",
                "Malcolm Barrett",
                "Francis Strickland",
                "Joel Cooper",
            ],
            "jobTitle": "Sales Executive",
            "employmentType": "Permanent",
        },
    ]

    grid = html.Div(
        [
            dag.AgGrid(
                columnDefs=[
                    # we're using the auto group column by default!
                    {"field": "jobTitle"},
                    {"field": "employmentType"},
                ],
                defaultColDef={
                    "flex": 1,
                },
                dashGridOptions={
                    "autoGroupColumnDef": {
                        "headerName": "Organisation Hierarchy",
                        "minWidth": 300,
                        "cellRendererParams": {
                            "suppressCount": True,
                        },
                    },
                    "getDataPath": {"function": "getDataPath(params)"},
                    "treeData": True,
                },
                rowData=rowData,
                enableEnterpriseModules=True,
                id="grid",
            ),
            html.Hr(),
            html.Button(id="reset"),
        ]
    )

    @app.callback(Output("grid", "rowData"), Input("reset", "n_clicks"))
    def resetRowData(n):
        if n:
            return rowData
        return no_update

    app.layout = html.Div(
        [
            grid,
        ]
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Erica Rogers")

    ### testing tree functions
    grid.get_cell_expandable(0, 0).click()
    grid.wait_for_cell_text(1, 0, "Malcolm Barrett")
    grid.get_cell_expandable(1, 0).click()
    grid.wait_for_cell_text(2, 0, "Esther Baker")
    grid.get_cell_expandable(2, 0).click()
    grid.wait_for_cell_text(3, 0, "Brittany Hanson")
    dash_duo.find_element("#reset").click()

    grid.wait_for_cell_text(3, 0, "Brittany Hanson")
