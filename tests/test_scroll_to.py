from dash import Dash, html, Input, Output
from dash_ag_grid import AgGrid
import plotly.express as px
import json
from dash.testing.wait import until
import pandas as pd

from . import utils


def test_st001_(dash_duo):
    app = Dash()

    df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
    )

    # basic columns definition with column defaults
    columnDefs = [
        {"field": "country"},
        {"field": "year"},
        {"field": "athlete"},
        {"field": "age"},
        {"field": "date"},
        {"field": "sport"},
        {"field": "total"},
    ]

    app.layout = html.Div(
        [
            AgGrid(
                id="grid",
                columnDefs=columnDefs,
                rowData=df.to_dict("records"),
                columnSize="sizeToFit",
                defaultColDef={"resizable": True, "sortable": True, "filter": True},
            ),
            html.Button(id="btn"),
            html.Div(id="scrollTo-output"),
            html.Div(id="scrollTo-input"),
        ]
    )
    scroll_to_inputs = [
        {"rowIndex": 1234, "rowPosition": "bottom"},
        {"column": "age", "columnPosition": "start"},
        {"rowId": 1234, "rowPosition": "bottom"},
        {"rowIndex": 1234, "rowId": 1235},
        {
            "rowIndex": 1234,
            "rowId": 1235,
            "column": "age",
            "rowPosition": "bottom",
            "columnPosition": "start",
        },
        {"rowIndex": 1234, "rowId": 1235, "column": "age"},
    ]

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
        return scroll_to_inputs[n_clicks - 1]

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")
    until(lambda: "United States" == grid.get_cell(0, 0).text, timeout=3)
    for scroll_to_input in scroll_to_inputs:
        dash_duo.find_element("#btn").click()
        dash_duo.wait_for_text_to_equal(
            "#scrollTo-output", json.dumps(scroll_to_input), timeout=3
        )
