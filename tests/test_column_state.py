from dash import Dash, html, Output, Input, no_update, State, ctx, Patch, dcc
import dash_ag_grid as dag
import plotly.express as px
import json
import time
import pandas as pd

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
        "width": 200,
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
    testState[1]["width"] = 200
    until(
        lambda: json.dumps(testState)
        in dash_duo.find_element("#reset-column-state-grid-pre").text,
        timeout=3,
    )

    dash_duo.find_element("#load-column-defs").click()

    time.sleep(0.5)  # pausing to emulate separation because user inputs

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

def test_cs003_column_state(dash_duo):
    data = [
        {
            "localTime": "5:00am",
            "a": 0.231,
            "b": 0.523,
            "c": 0.423,
            "d": 0.527,
        },
        {
            "localTime": "5:15am",
            "a": 0.423,
            "b": 0.452,
            "c": 0.523,
            "d": 0.543,
        },
        {
            "localTime": "5:30am",
            "a": 0.537,
            "b": 0.246,
            "c": 0.426,
            "d": 0.421,
        },
        {
            "localTime": "5:45am",
            "a": 0.893,
            "b": 0.083,
            "c": 0.532,
            "d": 0.983,
        },
        {
            "localTime": "6:00am",
            "a": 0.231,
            "b": 0.523,
            "c": 0.423,
            "d": 0.527,
        },
        {
            "localTime": "6:15am",
            "a": 0.423,
            "b": 0.452,
            "c": 0.523,
            "d": 0.543,
        },
        {
            "localTime": "6:30am",
            "a": 0.537,
            "b": 0.246,
            "c": 0.426,
            "d": 0.421,
        },
        {
            "localTime": "6:45am",
            "a": 0.893,
            "b": 0.083,
            "c": 0.532,
            "d": 0.983,
        },
        {
            "localTime": "7:00am",
            "a": 0.231,
            "b": 0.523,
            "c": 0.423,
            "d": 0.527,
        },
        {
            "localTime": "7:15am",
            "a": 0.423,
            "b": 0.452,
            "c": 0.523,
            "d": 0.543,
        },
        {
            "localTime": "7:30am",
            "a": 0.537,
            "b": 0.246,
            "c": 0.426,
            "d": 0.421,
        },
        {
            "localTime": "7:45am",
            "a": 0.893,
            "b": 0.083,
            "c": 0.532,
            "d": 0.983,
        },
        {
            "localTime": "8:00am",
            "a": 0.231,
            "b": 0.523,
            "c": 0.423,
            "d": 0.527,
        },
        {
            "localTime": "8:15am",
            "a": 0.423,
            "b": 0.452,
            "c": 0.523,
            "d": 0.543,
        },
        {
            "localTime": "8:30am",
            "a": 0.537,
            "b": 0.246,
            "c": 0.426,
            "d": 0.421,
        },
        {
            "localTime": "8:45am",
            "a": 0.893,
            "b": 0.083,
            "c": 0.532,
            "d": 0.983,
        },
        {
            "localTime": "8:00am",
            "a": 0.231,
            "b": 0.523,
            "c": 0.423,
            "d": 0.527,
        },
        {
            "localTime": "8:15am",
            "a": 0.423,
            "b": 0.452,
            "c": 0.523,
            "d": 0.543,
        },
        {
            "localTime": "8:30am",
            "a": 0.537,
            "b": 0.246,
            "c": 0.426,
            "d": 0.421,
        },
        {
            "localTime": "8:45am",
            "a": 0.893,
            "b": 0.083,
            "c": 0.532,
            "d": 0.983,
        },
    ]

    columnDefs = [
        {"field": "localTime"},
        {"field": "a"},
        {"field": "b"},
        {"field": "c"},
        {"field": "d"},
    ]

    app = Dash(__name__)

    app.layout = html.Div(
        [
            html.Div(
                [
                    html.Button("Remove Column", id="remove-column", n_clicks=0),
                    html.Div(
                        id="grid-holder",
                        children=[
                            dag.AgGrid(
                                id=f"grid",
                                columnDefs=columnDefs,
                                rowData=data,
                                columnSize="autoSize",
                            )
                        ],
                    ),
                ],
            ),
        ]
    )

    @app.callback(
        Output("grid", "columnDefs"),
        Input("remove-column", "n_clicks"),
    )
    def remove_column(n):
        if n:
            cols = Patch()
            if n < 3:
                del cols[0]
                return cols
        return no_update

    dash_duo.start_server(
        app,
        debug=True,
        use_reloader=False,
        use_debugger=True,
        dev_tools_hot_reload=False,
        dev_tools_props_check=True,
        dev_tools_disable_version_check=True,
    )

    for x in range(3):
        dash_duo.find_element("#remove-column").click()
        time.sleep(2)  # pausing to emulate separation because user inputs
    assert list(filter(lambda i: i.get("level") != "ERROR", dash_duo.get_logs())) == []

def test_toggle_column_visibility(dash_duo):
    data = pd.DataFrame([
        {"a": 1, "b": 2},
        {"a": 3, "b": 4},
    ])

    app = Dash(__name__)

    app.layout = html.Div([
        dcc.Dropdown(
            id="select-columns",
            value=list(data.columns),
            options=[{"label": col, "value": col} for col in data.columns],
            multi=True,
        ),
        dag.AgGrid(
            id="ag-grid",
            style={"height": "75vh", "width": "100%"},
            rowData=data.to_dict(orient="records"),
        ),
    ])

    @app.callback(
        Output("ag-grid", "columnDefs"),
        Input("select-columns", "value"),
    )
    def toggle_column_visibility(selected_columns):
        if not selected_columns:
            return no_update
        return [
            {
                "headerName": col_name,
                "field": col_name,
                "hide": col_name not in selected_columns,
            }
            for col_name in data.columns
        ]

    dash_duo.start_server(app)

    # Wait for grid to render
    grid = utils.Grid(dash_duo, "ag-grid")

    grid.wait_for_cell_text(0, 0, "1")

    # Hide column 'b'
    dropdown = dash_duo.find_element("#select-columns")
    option_b = dash_duo.find_element('span.Select-value-icon:nth-child(1)')
    option_b.click()
    time.sleep(1)

    # Only column 'a' should be visible
    grid_headers = dash_duo.find_elements("div.ag-header-cell-label")
    header_texts = [h.text for h in grid_headers]
    assert "a" not in header_texts
    assert "b" in header_texts

    # Show both columns again
    dropdown.click()
    option_b = dash_duo.find_element('.Select-menu')
    option_b.click()
    time.sleep(1)
    grid_headers = dash_duo.find_elements("div.ag-header-cell-label")
    header_texts = [h.text for h in grid_headers]
    assert "a" in header_texts
    assert "b" in header_texts
