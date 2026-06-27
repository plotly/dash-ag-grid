"""
Nested tables.
"""

import dash_ag_grid as dag
import dash
from dash import html, dcc
from . import utils
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)
data=df.to_dict("records")

def test_ca001_custom_aggFunc_functions(dash_duo):
    app = dash.Dash(__name__)

    columnDefs = [
        # Row group by country and by year is enabled.
        {
            "field": "country",
            "rowGroup": True,
            "hide": True,
            "suppressColumnsToolPanel": True,
        },
        {
            "field": "sport",
            "rowGroup": True,
            "hide": True,
            "suppressColumnsToolPanel": True,
        },
        {
            "field": "year",
            "pivot": True,
            "hide": True,
            "suppressColumnsToolPanel": True,
        },
        {"field": "gold", "sortable": True, "filter": True, "aggFunc": "sum"},
        {"field": "silver", "sortable": True, "filter": True, "aggFunc": "sum"},
        {
            "headerName": "ratio",
            "colId": "goldSilverRatio",
            "aggFunc": {"function": "ratioAggFunc(params)"},
            "valueGetter": {"function": "ratioValueGetter(params)"},
            "valueFormatter": {"function": "ratioFormatter(params)"},
        },
    ]

    app.layout = html.Div(
        [
            dcc.Markdown("Demonstration of row groupings in a Dash AG Grid."),
            dcc.Markdown("This grid groups first by country and then by year."),
            dag.AgGrid(
                columnDefs=columnDefs,
                rowData=data,
                defaultColDef=dict(
                    resizable=True,
                    rowSelection="multiple",
                    suppressAggFuncInHeader=True,
                ),
                id="grid",
                enableEnterpriseModules=True,
            ),
        ]
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "United States\n(1109)")
    grid.wait_for_cell_text(0, 4, "552")
    grid.wait_for_cell_text(0, 5, "440")
    grid.wait_for_cell_text(0, 6, "1.25")

    grid.get_cell_expandable(0, 0).click()
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-row-level-1 [aria-colindex="1"]', "Swimming\n(145)"
    )
    dash_duo.wait_for_text_to_equal('#grid .ag-row-level-1 [aria-colindex="5"]', "139")
    dash_duo.wait_for_text_to_equal('#grid .ag-row-level-1 [aria-colindex="6"]', "77")
    dash_duo.wait_for_text_to_equal('#grid .ag-row-level-1 [aria-colindex="7"]', "1.81")

def test_ca002_custom_aggFunc_functions(dash_duo):
    app = dash.Dash(__name__)

    columnDefs = [
        # Row group by country and by year is enabled.
        {
            "field": "country",
            "rowGroup": True,
            "hide": True,
            "suppressColumnsToolPanel": True,
        },
        {
            "field": "sport",
            "rowGroup": True,
            "hide": True,
            "suppressColumnsToolPanel": True,
        },
        {
            "field": "year",
            "pivot": True,
            "hide": True,
            "suppressColumnsToolPanel": True,
        },
        {"field": "gold", "sortable": True, "filter": True, "aggFunc": "sum"},
        {"field": "silver", "sortable": True, "filter": True, "aggFunc": "sum"},
        {
            "headerName": "ratio",
            "colId": "goldSilverRatio",
            "aggFunc": "ratioAggFunc",
            "valueGetter": {"function": "ratioValueGetter(params)"},
            "valueFormatter": {"function": "ratioFormatter(params)"},
        },
    ]

    app.layout = html.Div(
        [
            dcc.Markdown("Demonstration of row groupings in a Dash AG Grid."),
            dcc.Markdown("This grid groups first by country and then by year."),
            dag.AgGrid(
                columnDefs=columnDefs,
                rowData=data,
                defaultColDef=dict(
                    resizable=True,
                    rowSelection="multiple",
                    suppressAggFuncInHeader=True,
                ),
                id="grid",
                enableEnterpriseModules=True,
                dashGridOptions={
                    "rowSelection": "multiple",
                    "suppressAggFuncInHeader": True,
                    "animateRows": False,
                    'aggFuncs': {'ratioAggFunc': {"function": "ratioAggFunc"}},
                }
            ),
        ]
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "United States\n(1109)")
    grid.wait_for_cell_text(0, 4, "552")
    grid.wait_for_cell_text(0, 5, "440")
    grid.wait_for_cell_text(0, 6, "1.25")

    grid.get_cell_expandable(0, 0).click()
    dash_duo.wait_for_text_to_equal(
        '#grid .ag-row-level-1 [aria-colindex="1"]', "Swimming\n(145)"
    )
    dash_duo.wait_for_text_to_equal('#grid .ag-row-level-1 [aria-colindex="5"]', "139")
    dash_duo.wait_for_text_to_equal('#grid .ag-row-level-1 [aria-colindex="6"]', "77")
    dash_duo.wait_for_text_to_equal('#grid .ag-row-level-1 [aria-colindex="7"]', "1.81")