import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px
from . import utils
import json

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
    cellClicked = dash_duo.find_element('#log').text
    assert json.loads(cellClicked).get('value') == 15

    # Test right click
    action = utils.ActionChains(dash_duo.driver)
    action.context_click(grid.get_cell(0, 2)).perform()
    cellClicked = dash_duo.find_element('#log').text
    assert json.loads(cellClicked).get('value') == 13
    assert json.loads(cellClicked).get('contextMenu')

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
    assert dash_duo.find_element('#log').text == "rawr"
