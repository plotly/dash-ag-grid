import pytest
import dash_ag_grid as dag
from dash import Dash, html, dcc, Output, Input, no_update, ctx, State
import requests
from . import utils
import json
from dash.testing.wait import until
import time


def test_sb001_sizing_buttons(dash_duo):
    app = Dash(__name__)

    data = requests.get(
        r"https://www.ag-grid.com/example-assets/olympic-winners.json"
    ).json()

    columnDefs = [
        {"field": "athlete"},
        {"field": "age"},
        {"field": "country"},
        {"field": "year"},
        {"field": "date"},
        {"field": "sport"},
        {"field": "gold"},
        {"field": "silver"},
        {"field": "bronze"},
        {"field": "total"},
    ]

    app.layout = html.Div(
        [
            dcc.Markdown("This grid has single-select rows."),
            dag.AgGrid(
                id="grid",
                columnDefs=columnDefs,
                rowData=data[:100],
                columnSize="sizeToFit",
                defaultColDef={
                    "resizable": True,
                    "sortable": True,
                    "filter": True,
                    "floatingFilter": True,
                },
                dashGridOptions={"rowSelection": "multiple"},
                persistence=True,
                persistence_type="session",
            ),
            html.Button(id="autoSizeAllColumns", children="Auto Size All"),
            html.Button(
                id="autoSizeAllColumnsSkipHeaders", children="Auto Size All SkipHeaders"
            ),
            html.Div(id="columnState"),
        ],
        style={"margin": 20},
    )

    @app.callback(
        Output("grid", "columnSize", allow_duplicate=True),
        Output("grid", "columnSizeOptions", allow_duplicate=True),
        Input("autoSizeAllColumns", "n_clicks"),
        prevent_initial_call=True,
    )
    def setSelection(n):
        if n:
            return "autoSize", {"skipHeader": False}
        return no_update, no_update

    @app.callback(
        Output("grid", "columnSize", allow_duplicate=True),
        Output("grid", "columnSizeOptions", allow_duplicate=True),
        Input("autoSizeAllColumnsSkipHeaders", "n_clicks"),
        prevent_initial_call=True,
    )
    def setSelection(n):
        if n:
            return "autoSize", {"skipHeader": True}
        return no_update, no_update

    @app.callback(
        Output("columnState", "children"),
        Input("grid", "columnState"),
        State("columnState", "children"),
        State("grid", "columnSizeOptions"),
    )
    def selected(state, oldState, opts):
        if state:
            test = True
            if oldState and opts == {"skipHeader": True}:
                oldState = json.loads(oldState)
                for i in range(len(state)):
                    if i in [1, 6, 7, 8, 9]:
                        if state[i]["width"] > oldState[i]["width"]:
                            test = False
                            break
            assert test
            return json.dumps(state)
        return ""

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Michael Phelps")

    oldValue = ""
    until(lambda: oldValue != dash_duo.find_element("#columnState").text, timeout=3)
    oldValue = dash_duo.find_element("#columnState").text
    for x in columnDefs:
        assert x["field"] in oldValue

    for x in ["autoSizeAllColumns", "autoSizeAllColumnsSkipHeaders"]:
        dash_duo.find_element(f"#{x}").click()
        until(
            lambda: oldValue
            != dash_duo.find_element("#columnState").get_attribute("innerText"),
            timeout=3,
        )
        oldValue = dash_duo.find_element("#columnState").text


@pytest.mark.flaky(max_runs=5, min_passes=1)
def test_sb002_sizing_buttons(dash_duo):
    app = Dash(__name__)

    data = requests.get(
        r"https://www.ag-grid.com/example-assets/olympic-winners.json"
    ).json()

    columnDefs = [
        {"field": "athlete"},
        {"field": "age"},
        {"field": "country"},
        {"field": "year"},
        {"field": "date"},
        {"field": "sport"},
        {"field": "gold"},
        {"field": "silver"},
        {"field": "bronze"},
        {"field": "total"},
    ]

    app.layout = html.Div(
        [
            dcc.Markdown("This grid has single-select rows."),
            dag.AgGrid(
                id="grid",
                columnDefs=columnDefs,
                rowData=data[:100],
                columnSize="autoSize",
                defaultColDef={
                    "resizable": True,
                    "sortable": True,
                    "filter": True,
                    "floatingFilter": True,
                },
                dashGridOptions={"rowSelection": "multiple"},
                persistence=True,
                persistence_type="session",
            ),
            html.Button(id="sizeToFit", children="sizeToFit"),
            html.Button(id="responsiveSizeToFit", children="responsiveSizeToFit"),
            html.Div(id="columnState"),
        ],
        style={"margin": 20},
    )

    @app.callback(
        Output("grid", "columnSize", allow_duplicate=True),
        Input("sizeToFit", "n_clicks"),
        prevent_initial_call=True,
    )
    def setSelection(n):
        if n:
            return "sizeToFit"
        return no_update

    @app.callback(
        Output("grid", "columnSize", allow_duplicate=True),
        Input("responsiveSizeToFit", "n_clicks"),
        prevent_initial_call=True,
    )
    def setSelection(n):
        if n:
            return "responsiveSizeToFit"
        return no_update

    @app.callback(
        Output("columnState", "children"),
        Input("grid", "columnState"),
    )
    def selected(state):
        if state:
            return json.dumps(state)
        return ""

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Michael Phelps")
    dash_duo.driver.set_window_size(1000, 1000)
    oldValue = ""
    until(lambda: oldValue != dash_duo.find_element("#columnState").text, timeout=3)
    oldValue = dash_duo.find_element("#columnState").text
    for x in columnDefs:
        assert x["field"] in oldValue

    time.sleep(.5) # allow window size to change
    for x in ["sizeToFit", "responsiveSizeToFit"]:
        dash_duo.find_element(f"#{x}").click()
        if x != "responsiveSizeToFit":
            until(
                lambda: oldValue
                != dash_duo.find_element("#columnState").get_attribute("innerText"),
                timeout=3,
            )
        oldValue = dash_duo.find_element("#columnState").text
        dash_duo.driver.set_window_size(500, 500)
        if x == "responsiveSizeToFit":
            until(
                lambda: oldValue
                != dash_duo.find_element("#columnState").get_attribute("innerText"),
                timeout=3,
            )
        else:
            assert oldValue == dash_duo.find_element("#columnState").get_attribute(
                "innerText"
            )

        oldValue = dash_duo.find_element("#columnState").text
        dash_duo.driver.set_window_size(1000, 1000)


def test_sb003_sizing_buttons(dash_duo):
    app = Dash(__name__)

    data = requests.get(
        r"https://www.ag-grid.com/example-assets/olympic-winners.json"
    ).json()

    columnDefs = [
        {"field": "athlete"},
        {"field": "age"},
        {"field": "country"},
        {"field": "year"},
        {"field": "date"},
        {"field": "sport"},
        {"field": "gold"},
        {"field": "silver"},
        {"field": "bronze"},
        {"field": "total"},
    ]

    app.layout = html.Div(
        [
            dcc.Markdown("This grid has single-select rows."),
            dag.AgGrid(
                id="grid",
                columnDefs=columnDefs,
                rowData=data[:100],
                columnSize="sizeToFit",
                defaultColDef={
                    "resizable": True,
                    "sortable": True,
                    "filter": True,
                    "floatingFilter": True,
                },
                dashGridOptions={"rowSelection": "multiple"},
                persistence=True,
                persistence_type="session",
            ),
            html.Button(id="autoSizeOneColumn", children="Auto Size One"),
            html.Button(
                id="autoSizeOneColumnSkipHeaders", children="Auto Size One SkipHeaders"
            ),
            html.Div(id="columnState"),
        ],
        style={"margin": 20},
    )

    @app.callback(
        Output("grid", "columnSize", allow_duplicate=True),
        Output("grid", "columnSizeOptions", allow_duplicate=True),
        Input("autoSizeOneColumn", "n_clicks"),
        prevent_initial_call=True,
    )
    def setSelection(n):
        if n:
            return "autoSize", {"keys": ["gold"]}
        return no_update, no_update

    @app.callback(
        Output("grid", "columnSize", allow_duplicate=True),
        Output("grid", "columnSizeOptions", allow_duplicate=True),
        Input("autoSizeOneColumnSkipHeaders", "n_clicks"),
        prevent_initial_call=True,
    )
    def setSelection(n):
        if n:
            return "autoSize", {"skipHeader": True, "keys": ["gold"]}
        return no_update, no_update

    @app.callback(
        Output("columnState", "children"),
        Input("grid", "columnState"),
        State("columnState", "children"),
        State("grid", "columnSizeOptions"),
    )
    def selected(state, oldState, opts):
        if state:
            test = True
            if oldState and opts == {"skipHeader": True, "keys": ["gold"]}:
                oldState = json.loads(oldState)
                for i in range(len(state)):
                    if i in [6]:
                        if state[i]["width"] > oldState[i]["width"]:
                            test = False
                            break
            assert test
            return json.dumps(state)
        return ""

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Michael Phelps")

    oldValue = ""
    until(lambda: oldValue != dash_duo.find_element("#columnState").text, timeout=3)
    oldValue = dash_duo.find_element("#columnState").text
    for x in columnDefs:
        assert x["field"] in oldValue

    for x in ["autoSizeOneColumn", "autoSizeOneColumnSkipHeaders"]:
        dash_duo.find_element(f"#{x}").click()
        until(
            lambda: oldValue
            != dash_duo.find_element("#columnState").get_attribute("innerText"),
            timeout=3,
        )
        oldValue = dash_duo.find_element("#columnState").text

@pytest.mark.flaky(max_runs=5, min_passes=1)
def test_sb004_sizing_buttons(dash_duo):
    app = Dash(__name__)

    data = requests.get(
        r"https://www.ag-grid.com/example-assets/olympic-winners.json"
    ).json()

    columnDefs = [
        {"field": "athlete"},
        {"field": "age"},
        {"field": "country"},
        {"field": "year"},
        {"field": "date"},
        {"field": "sport"},
        {"field": "gold"},
        {"field": "silver"},
        {"field": "bronze"},
        {"field": "total"},
    ]

    app.layout = html.Div(
        [
            dcc.Markdown("This grid has single-select rows."),
            dag.AgGrid(
                id="grid",
                columnDefs=columnDefs,
                rowData=data[:100],
                columnSize="autoSize",
                defaultColDef={
                    "resizable": True,
                    "sortable": True,
                    "filter": True,
                    "floatingFilter": True,
                },
                dashGridOptions={"rowSelection": "multiple"},
                persistence=True,
                persistence_type="session",
            ),
            html.Button(id="sizeToFit", children="sizeToFit"),
            html.Button(id="responsiveSizeToFit", children="responsiveSizeToFit"),
            html.Div(id="columnState"),
        ],
        style={"margin": 20},
    )

    @app.callback(
        Output("grid", "columnSize", allow_duplicate=True),
        Output("grid", "columnSizeOptions", allow_duplicate=True),
        Input("sizeToFit", "n_clicks"),
        prevent_initial_call=True,
    )
    def setSelection(n):
        if n:
            return "sizeToFit", {"defaultMaxWidth": 50}
        return no_update, no_update

    @app.callback(
        Output("grid", "columnSize", allow_duplicate=True),
        Output("grid", "columnSizeOptions", allow_duplicate=True),
        Input("responsiveSizeToFit", "n_clicks"),
        prevent_initial_call=True,
    )
    def setSelection(n):
        if n:
            return "responsiveSizeToFit", {"defaultMinWidth": 50}
        return no_update, no_update

    @app.callback(
        Output("columnState", "children"),
        Input("grid", "columnState"),
    )
    def selected(state):
        if state:
            return json.dumps(state)
        return ""

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Michael Phelps")
    dash_duo.driver.set_window_size(1000, 1000)
    oldValue = ""
    until(lambda: oldValue != dash_duo.find_element("#columnState").text, timeout=3)
    oldValue = dash_duo.find_element("#columnState").text
    for x in columnDefs:
        assert x["field"] in oldValue
    time.sleep(.5)

    for x in ["sizeToFit", "responsiveSizeToFit"]:
        dash_duo.find_element(f"#{x}").click()
        if x != "responsiveSizeToFit":
            until(
                lambda: oldValue
                != dash_duo.find_element("#columnState").get_attribute("innerText"),
                timeout=3,
            )
        oldValue = dash_duo.find_element("#columnState").text
        dash_duo.driver.set_window_size(400, 400)
        if x == "responsiveSizeToFit":
            until(
                lambda: oldValue
                != dash_duo.find_element("#columnState").get_attribute("innerText"),
                timeout=3,
            )
        else:
            assert oldValue == dash_duo.find_element("#columnState").get_attribute(
                "innerText"
            )
            time.sleep(.5) # allow window size to change
            dash_duo.find_element(f"#{x}").click()
            until(
                lambda: oldValue
                != dash_duo.find_element("#columnState").get_attribute("innerText"),
                timeout=3,
            )

        oldValue = dash_duo.find_element("#columnState").text
        dash_duo.driver.set_window_size(1000, 1000)
        time.sleep(.2) # allow oldValue to change to the bigger size
