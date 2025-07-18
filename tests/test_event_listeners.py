import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State, Patch
import plotly.express as px
from . import utils
import json
from selenium.webdriver.common.by import By
from dash.testing.wait import until
import time


df = px.data.medals_wide()

columnDefs = []
for i in df.columns:
    if i == "nation":
        columnDefs.append({"field": i, "editable": False})
    else:
        columnDefs.append({"field": i})


def test_el001_event_listener(dash_duo):
    app = Dash(__name__, suppress_callback_exceptions=True)
    app.layout = html.Div(
        [
            dag.AgGrid(
                columnDefs=columnDefs,
                rowData=df.to_dict("records"),
                columnSize="sizeToFit",
                defaultColDef={"editable": True},
                id="grid",
                getRowId="params.data.nation",
                eventListeners={'cellContextMenu': ['showOutput(params, setGridProps)']},
                dashGridOptions={'suppressContextMenu': True, "preventDefaultOnContextMenu": True}
            ),
            html.Div(id="log")
        ]
    )

    app.clientside_callback(
        """function countEvents(cellClicked) {
            return JSON.stringify(cellClicked)
        }""",
        Output("log", "children"),
        Input("grid", "cellClicked"),
        prevent_initial_call=True,
        suppress_callback_exception=True
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")
    grid.wait_for_cell_text(0, 0, "South Korea")

    # Test left click.
    grid.get_cell(1, 2).click()
    until(lambda: json.loads(dash_duo.find_element('#log').text or "{}").get('value') == 15, timeout=3)

    # Test right click
    action = utils.ActionChains(dash_duo.driver)
    action.context_click(grid.get_cell(0, 2)).perform()
    until(lambda: json.loads(dash_duo.find_element('#log').text).get('value') == 13, timeout=3)
    until(lambda: json.loads(dash_duo.find_element('#log').text).get('contextMenu'), timeout=3)

def test_el002_event_listener(dash_duo):
    app = Dash(__name__, suppress_callback_exceptions=True)
    app.layout = html.Div(
        [
            dag.AgGrid(
                columnDefs=columnDefs,
                rowData=df.to_dict("records"),
                columnSize="sizeToFit",
                defaultColDef={"editable": True},
                id="grid",
                getRowId="params.data.nation",
                eventListeners={'cellClicked': ['dash_clientside.set_props("log", {children: "rawr"})']},
            ),
            html.Div(id="log")
        ]
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")
    grid.wait_for_cell_text(0, 0, "South Korea")

    # Test left click.
    grid.get_cell(1, 2).click()
    until(lambda: dash_duo.find_element('#log').text == "rawr", timeout=3)

def test_el003_event_listener(dash_duo):
    app = Dash(__name__, suppress_callback_exceptions=True)
    app.layout = html.Div([
        dag.AgGrid(id='grid',
                   columnDefs=[{'field': 'test'}],
                   rowData=[{'test': '1'}],
                   eventListeners={'cellClicked': ['TestEvent(params, setEventData)']}
                   ),
        html.Div(id='output', children=[])
    ]
    )

    @app.callback(
        Output('output', 'children'),
        Input('grid', 'eventData')
    )
    def show_event_data(v):
        children = Patch()
        if v:
            children.append(html.Div(json.dumps(v)))
        return children

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")
    grid.wait_for_cell_text(0, 0, "1")

    for i in range(5):
        grid.get_cell(0, 0).click()

        # Assert that the output element has children
        until(lambda: len(dash_duo.find_element("#output").find_elements(By.XPATH, "*")) == (i + 1), timeout=3)


