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


@pytest.mark.parametrize(
    "scroll_to_input,row,column",
    [
        ({"rowIndex": 100, "rowPosition": "bottom"}, 100, 0),
        ({"column": "age", "columnPosition": "start"}, 0, 1),
        ({"rowId": 200, "rowPosition": "bottom"}, 200, 0),
        ({"rowIndex": 300, "rowId": 500}, 300, 0),
        (
            {
                "rowIndex": 400,
                "rowId": 500,
                "column": "age",
                "rowPosition": "bottom",
                "columnPosition": "start",
            },
            400,
            1,
        ),
        (
            {
                "rowIndex": 100,
                "rowId": 200,
                "column": "age",
                "columnPosition": "start",
            },
            100,
            1,
        ),
        (
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
                "column": "age",
                "columnPosition": "start",
            },
            100,
            1,
        ),
        (
            {
                "rowIndex": 100,
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
            100,
            1,
        ),
    ],
)
def test_st001_scroll_to(scroll_to_input, row, column, dash_duo, df):
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

    @app.callback(
        Output("scrollTo-output", "children"),
        Input("grid", "scrollTo"),
    )
    def display_scrollTo(scroll_to):
        return json.dumps(scroll_to)

    @app.callback(
        Output("grid", "scrollTo"),
        Input("btn", "n_clicks"),
        prevent_initial_call=True,
    )
    def update_scrollTo(n_clicks):
        return scroll_to_input

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")
    until(lambda: "Michael Phelps" == grid.get_cell(0, 0).text, timeout=3)
    dash_duo.find_element("#btn").click()
    dash_duo.wait_for_text_to_equal(
        "#scrollTo-output", json.dumps(scroll_to_input), timeout=5
    )

    until(
        lambda: grid.get_cell(row, column).is_displayed(),
        timeout=3,
    )
