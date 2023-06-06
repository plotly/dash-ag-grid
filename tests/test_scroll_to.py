from dash import Dash, html, Input, Output
from dash_ag_grid import AgGrid
import plotly.express as px
import json
from dash.testing.wait import until
import pandas as pd
import pytest

from . import utils


@pytest.fixture
def df():
    return pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
    )


@pytest.fixture
def scroll_to_inputs():
    return [
        {"rowIndex": 100, "rowPosition": "bottom"},
        {"column": "bronze", "columnPosition": "end"},
        {"rowId": 200, "rowPosition": "top"},
        {"rowIndex": 300, "rowId": 500},
        {
            "rowIndex": 400,
            "rowId": 500,
            "column": "age",
            "rowPosition": "bottom",
            "columnPosition": "start",
        },
        {
            "data": {
                "athlete": "Sabine Völker",
                "age": 28,
                "country": "Germany",
                "year": 2002,
                "date": "24/02/2002",
                "sport": "Speed Skating",
                "gold": 0,
                "silver": 2,
                "bronze": 1,
                "total": 3,
            },
            "column": "bronze",
            "columnPosition": "end",
        },
        {
            "rowIndex": 2000,
            "rowId": 200,
            "data": {
                "athlete": "Elizabeth Beisel",
                "age": 19,
                "country": "United States",
                "year": 2012,
                "date": "12/8/2012",
                "sport": "Swimming",
                "gold": 0,
                "silver": 1,
                "bronze": 1,
                "total": 2,
            },
            "column": "age",
            "columnPosition": "start",
        },
    ]


def test_st001_scroll_to(dash_duo, df, scroll_to_inputs):
    app = Dash()

    # basic columns definition with column defaults
    columnDefs = [{"field": c} for c in df.columns]

    app.layout = html.Div(
        [
            AgGrid(
                id="grid",
                columnDefs=columnDefs,
                rowData=df.to_dict("records"),
                defaultColDef={"resizable": True, "sortable": True, "filter": True},
            ),
            html.Button(id="btn"),
            html.Div(id="scrollTo-output"),
            html.Div(id="scrollTo-input"),
        ]
    )

    # Displays the prop scrollTo when it changes in the grid
    @app.callback(
        Output("scrollTo-output", "children"),
        Input("grid", "scrollTo"),
    )
    def display_scrollTo(scroll_to):
        return json.dumps(scroll_to)

    # On click sets up a new value for scrollTo from the fixture scroll_to_inputs
    @app.callback(
        Output("grid", "scrollTo"),
        Input("btn", "n_clicks"),
        prevent_initial_call=True,
    )
    def update_scrollTo(n_clicks):
        return scroll_to_inputs[n_clicks - 1]

    dash_duo.start_server(app)
    grid = utils.Grid(dash_duo, "grid")

    # Check that the grid has been loaded successfully
    until(lambda: "Michael Phelps" == grid.get_cell(0, 0).text, timeout=3)

    # Get the location and size of the grid to later check which cells are visible
    grid_location = dash_duo.find_element("#grid").location
    grid_size = dash_duo.find_element("#grid").size

    dash_duo.find_element("#btn").click()  # Sets scrollTo as scroll_to_inputs[0]
    dash_duo.wait_for_text_to_equal(
        "#scrollTo-output", json.dumps(scroll_to_inputs[0]), timeout=5
    )

    # As rowPosition is set to 'bottom' the next cell should be out of the grid
    next_cell_y = grid.get_cell(101, 0).location["y"]
    until(
        lambda: grid.get_cell(100, 0).is_displayed()
        and next_cell_y >= grid_location["y"] + grid_size["height"] - 1,
        timeout=3,
    )

    dash_duo.find_element("#btn").click()  # Sets scrollTo as scroll_to_inputs[1]
    dash_duo.wait_for_text_to_equal(
        "#scrollTo-output", json.dumps(scroll_to_inputs[1]), timeout=5
    )
    # The vertical scroll should't changed so cell 101 should remain out of the grid.
    # As columnPosition is set to 'end' the next column should be out of the grid
    next_cell_location = grid.get_cell(101, 9).location
    until(
        lambda: grid.get_cell(100, 8).is_displayed()
        and next_cell_location["x"] >= grid_location["x"] + grid_size["width"] - 1
        and next_cell_location["y"] >= grid_location["y"] + grid_size["height"] - 1,
        timeout=3,
    )

    dash_duo.find_element("#btn").click()  # Sets scrollTo as scroll_to_inputs[2]
    dash_duo.wait_for_text_to_equal(
        "#scrollTo-output", json.dumps(scroll_to_inputs[2]), timeout=5
    )
    # The horizontal scroll hasn't changed so the column number 9 should remain out of the grid
    # As the rowPosition is set to 'top' the previous row should be out of the grid
    prev_cell_location = grid.get_cell(199, 8).location
    until(
        lambda: grid.get_cell(200, 8).is_displayed()
        and grid.get_cell(200, 9).location["x"]
        >= grid_location["x"] + grid_size["width"] - 1
        and grid.get_cell(199, 8).location["y"]
        <= grid_location["y"] + grid.get_cell(199, 8).size["height"] + 1,
        timeout=3,
    )

    dash_duo.find_element("#btn").click()  # Sets scrollTo as scroll_to_inputs[3]
    dash_duo.wait_for_text_to_equal(
        "#scrollTo-output", json.dumps(scroll_to_inputs[3]), timeout=5
    )
    # The horizontal scroll hasn't changed so the column number 9 should remain out of the grid
    # rowIndex has priority over rowId so the grid should scroll to the row 300 on top
    until(
        lambda: grid.get_cell(300, 8).is_displayed()
        and grid.get_cell(300, 9).location["x"]
        >= grid_location["x"] + grid_size["width"] - 1
        and grid.get_cell(299, 8).location["y"]
        <= grid_location["y"] + grid.get_cell(299, 8).size["height"] + 1,
        timeout=3,
    )

    dash_duo.find_element("#btn").click()  # Sets scrollTo as scroll_to_inputs[4]
    dash_duo.wait_for_text_to_equal(
        "#scrollTo-output", json.dumps(scroll_to_inputs[4]), timeout=5
    )
    # columnPosition is set to "start" so the position of the first column should be on the left of the grid
    # rowIndex has priority over rowId so the grid should scroll to the row 400 at the bottom
    next_cell_location = grid.get_cell(401, 0).location
    until(
        lambda: grid.get_cell(400, 1).is_displayed()
        and next_cell_location["x"] <= grid_location["x"]
        and next_cell_location["y"] >= grid_location["y"] + grid_size["height"] - 1,
        timeout=3,
    )

    dash_duo.find_element("#btn").click()  # Sets scrollTo as scroll_to_inputs[5]
    dash_duo.wait_for_text_to_equal(
        "#scrollTo-output", json.dumps(scroll_to_inputs[5]), timeout=5
    )

    # data will search for the row number 100 an scroll to there
    # the column 9 should be out of the grid
    prev_cell_location = grid.get_cell(99, 8).location
    until(
        lambda: grid.get_cell(100, 8).is_displayed()
        and grid.get_cell(100, 9).location["x"]
        >= grid_location["x"] + grid_size["width"] - 1
        and prev_cell_location["y"]
        <= grid_location["y"] + grid.get_cell(99, 8).size["height"] + 1,
        timeout=3,
    )

    dash_duo.find_element("#btn").click()  # Sets scrollTo as scroll_to_inputs[6]
    dash_duo.wait_for_text_to_equal(
        "#scrollTo-output", json.dumps(scroll_to_inputs[6]), timeout=5
    )
    # rowIndex has priority over rowId and data so it should scroll to the row number 2000
    prev_cell_location = grid.get_cell(1999, 1).location
    until(
        lambda: grid.get_cell(2000, 1).is_displayed()
        and grid.get_cell(2000, 0).location["x"] <= grid_location["x"]
        and prev_cell_location["y"]
        <= grid_location["y"] + grid.get_cell(1999, 1).size["height"] + 1,
        timeout=3,
    )


def test_st002_initial_scroll_to(dash_duo, df):
    app = Dash()

    # basic columns definition with column defaults
    columnDefs = [{"field": c} for c in df.columns]

    app.layout = html.Div(
        [
            AgGrid(
                id="grid",
                columnDefs=columnDefs,
                rowData=df.to_dict("records"),
                defaultColDef={"resizable": True, "sortable": True, "filter": True},
                scrollTo={
                    "rowIndex": 2000,
                    "rowPosition": "top",
                    "column": "bronze",
                    "columnPosition": "end",
                },
            ),
        ]
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")
    until(lambda: "1" == grid.get_cell(2000, 9).text, timeout=3)
    # Get the location and size of the grid to later check which cells are visible
    grid_location = dash_duo.find_element("#grid").location
    grid_size = dash_duo.find_element("#grid").size

    until(
        lambda: grid.get_cell(2000, 8).is_displayed()
        and grid.get_cell(2000, 9).location["x"]
        >= grid_location["x"] + grid_size["width"] - 1
        and grid.get_cell(1999, 8).location["y"]
        <= grid_location["y"] + grid.get_cell(1999, 8).size["height"] + 1,
        timeout=3,
    )
