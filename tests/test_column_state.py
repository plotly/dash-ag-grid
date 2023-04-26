from dash import Dash, html, Output, Input, no_update, State, ctx
import dash_ag_grid as dag
import plotly.express as px
import json

from . import utils
from dash.testing.wait import until


df = px.data.election()
default_display_cols = ["district_id", "district", "winner"]


def test_cs001_column_state(dash_duo):
    app = Dash(__name__)
    columnDefs = [
        {"headerName": "Make", "field": "make"},
        {"headerName": "Model", "field": "model"},
        {"headerName": "Price", "field": "price"},
    ]

    defaultColDef = {
        "initialWidth": 150,
        "sortable": True,
        "resizable": True,
        "filter": True,
    }

    rowData = [
        {"make": "Toyota", "model": "Celica", "price": 35000},
        {"make": "Ford", "model": "Mondeo", "price": 32000},
        {"make": "Porsche", "model": "Boxster", "price": 72000},
    ]

    colState = [
        {
            "colId": "make",
            "width": 150,
            "hide": False,
            "pinned": "left",
            "sort": None,
            "sortIndex": None,
            "aggFunc": None,
            "rowGroup": False,
            "rowGroupIndex": None,
            "pivot": False,
            "pivotIndex": None,
            "flex": None
        },
        {
            "colId": "price",
            "width": 150,
            "hide": False,
            "pinned": "left",
            "sort": None,
            "sortIndex": None,
            "aggFunc": None,
            "rowGroup": False,
            "rowGroupIndex": None,
            "pivot": False,
            "pivotIndex": None,
            "flex": None
        },
        {
            "colId": "model",
            "width": 150,
            "hide": False,
            "pinned": None,
            "sort": None,
            "sortIndex": None,
            "aggFunc": None,
            "rowGroup": False,
            "rowGroupIndex": None,
            "pivot": False,
            "pivotIndex": None,
            "flex": None
        }
    ]

    app.layout = html.Div(
        [
            html.Div(
                [
                    html.Button(
                        "Reset Column State", id="reset-column-state-button", n_clicks=0
                    ),
                    html.Button(
                        "Get Column State", id="get-column-state-button", n_clicks=0
                    ),
                    html.Button(
                        "Load State", id="load-column-state-button", n_clicks=0
                    ),
                ],
            ),
            dag.AgGrid(
                id="grid",
                columnSize="autoSize",
                columnDefs=columnDefs,
                defaultColDef=defaultColDef,
                rowData=rowData,
                columnState=colState,
            ),
            html.Div(id="reset-column-state-grid-pre"),
        ]
    )

    @app.callback(
        Output("grid", "resetColumnState"),
        Output("grid", "updateColumnState"),
        Input("reset-column-state-button", "n_clicks"),
        Input("get-column-state-button", "n_clicks"),
    )
    def reset_column_state(n_reset, n_state):
        if ctx.triggered_id == "reset-column-state-button":
            return True, False
        elif ctx.triggered_id == "get-column-state-button":
            return False, True
        return no_update

    @app.callback(
        Output('grid', 'columnState'),
        Input('load-column-state-button', 'n_clicks'),
        prevent_initial_call=True
    )
    def loadState(n):
        if n:
            return colState
        return no_update

    @app.callback(
        Output("reset-column-state-grid-pre", "children"),
        Input("grid", "columnState"),
    )
    def display_column_state(col_state):
        return json.dumps(col_state)

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Toyota")

    grid.wait_for_pinned_cols(2)
    grid.wait_for_viewport_cols(1)

    until(lambda: json.dumps(colState) in dash_duo.find_element('#reset-column-state-grid-pre').text, timeout=3)

    grid.resize_col(1, 50)
    dash_duo.find_element('#get-column-state-button').click()
    testState = colState.copy()
    testState[1]['width'] = 198
    until(lambda: json.dumps(testState) in dash_duo.find_element('#reset-column-state-grid-pre').text, timeout=3)

    dash_duo.find_element('#load-column-state-button').click()
    until(lambda: json.dumps(colState) in dash_duo.find_element('#reset-column-state-grid-pre').text, timeout=3)