from dash import Dash, html, Output, Input, no_update, State, ctx
import dash_ag_grid as dag
import plotly.express as px
import json
import time

from . import utils
from dash.testing.wait import until


df = px.data.election()
default_display_cols = ["district_id", "district", "winner"]

columnDefs = [
        {"headerName": "Make", "field": "make"},
        {"headerName": "Model", "field": "model"},
        {"headerName": "Price", "field": "price"},
    ]

alt_columnDefs = [
    {"field": "price", "pinned": False, "sort": "asc"},
    {"field": "model", "pinned": False},
    {"field": "make", "pinned": False},
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
        "flex": None,
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
        "flex": None,
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
        "flex": None,
    },
]

alt_colState = [
    {
        "colId": "price",
        "width": 198,
        "hide": False,
        "pinned": None,
        "sort": "asc",
        "sortIndex": None,
        "aggFunc": None,
        "rowGroup": False,
        "rowGroupIndex": None,
        "pivot": False,
        "pivotIndex": None,
        "flex": None,
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
        "flex": None,
    },
    {
        "colId": "make",
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
        "flex": None,
    },
]


def test_cs001_column_state(dash_duo):
    app = Dash(__name__)


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
                    html.Button(
                        "Change Column Defs", id="load-column-defs", n_clicks=0
                    ),
                    html.Button(
                        "Load Both Column Defs and State",
                        id="load-column-state-defs-button",
                        n_clicks=0,
                    ),
                ],
            ),
            dag.AgGrid(
                id="grid",
                # columnSize="autoSize",
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
        Output("grid", "columnState"),
        Input("load-column-state-button", "n_clicks"),
        prevent_initial_call=True,
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

    @app.callback(
        Output("grid", "columnDefs"),
        Input("load-column-defs", "n_clicks"),
        prevent_initial_call=True,
    )
    def loadState(n):
        if n:
            return alt_columnDefs
        return no_update

    @app.callback(
        Output("grid", "columnState", allow_duplicate=True),
        Output("grid", "columnDefs", allow_duplicate=True),
        Input("load-column-state-defs-button", "n_clicks"),
        prevent_initial_call=True,
    )
    def loadState(n):
        if n:
            return colState, columnDefs
        return no_update, no_update

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Toyota")

    grid.wait_for_pinned_cols(2)
    grid.wait_for_viewport_cols(1)

    dash_duo.find_element("#get-column-state-button").click()
    time.sleep(0.5)  # pausing to emulate separation because user inputs

    until(
        lambda: json.dumps(colState)
        in dash_duo.find_element("#reset-column-state-grid-pre").text,
        timeout=3,
    )

    grid.resize_col(1, 50)

    dash_duo.find_element("#get-column-state-button").click()
    testState = colState.copy()
    testState[1]["width"] = 198
    until(
        lambda: json.dumps(testState)
        in dash_duo.find_element("#reset-column-state-grid-pre").text,
        timeout=3,
    )

    dash_duo.find_element("#load-column-defs").click()
    until(
        lambda: json.dumps(alt_colState)
        in dash_duo.find_element("#reset-column-state-grid-pre").text,
        timeout=3,
    )
    grid.wait_for_all_header_texts(["Price", "Model", "Make"])
    grid.wait_for_cell_text(0, 0, "32000")

    time.sleep(0.5)  # pausing to emulate separation because user inputs

    dash_duo.find_element("#load-column-state-defs-button").click()
    until(
        lambda: json.dumps(colState)
        in dash_duo.find_element("#reset-column-state-grid-pre").text,
        timeout=3,
    )
    grid.wait_for_all_header_texts(["Make", "Price", "Model"])

def test_cs002_column_state(dash_duo):
    app = Dash(__name__)

    app.layout = html.Div(
        [
            html.Div(
                [
                    html.Button(
                        "Add Grid", id="add-grid", n_clicks=0
                    ),
                    html.Div(
                        id='grid-holder'
                    )
                ],
            ),
        ]
    )

    app.clientside_callback(
        """async ()=> {
            await new Promise(resolve => setTimeout(resolve, 400));
            return []
        }""",
        Output('grid-holder', 'children', allow_duplicate=True),
        Input('grid-holder', 'children'),
        prevent_initial_call=True
    )

    @app.callback(
        Output('grid-holder', 'children'),
        Input('add-grid', 'n_clicks'),
        prevent_initial_call=True
    )
    def make_grid(n):
        return dag.AgGrid(
                id=f"grid_{n}",
                columnDefs=columnDefs,
                defaultColDef=defaultColDef,
                rowData=rowData,
                columnSize='Auto'
            )

    dash_duo.start_server(app)

    for x in range(10):
        dash_duo.find_element("#add-grid").click()
        time.sleep(2)  # pausing to emulate separation because user inputs
    assert list(filter(lambda i: i.get("level") != "WARNING", dash_duo.get_logs())) == []