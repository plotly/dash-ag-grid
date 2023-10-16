import dash_ag_grid as dag
from dash import Dash, html, dcc
from . import utils
from dash.testing.wait import until
import pandas as pd
import time


def test_ca001_cell_change_anitmation(dash_duo):
    app = Dash(__name__)

    df = pd.DataFrame(data=[[1, 2, 3], [2, 3, 4], [9, 8, 6]], columns=list("abc"))
    df.reset_index(inplace=True)

    columnDefs = [
        {
            "headerName": "Editable A",
            "field": "a",
            "editable": True,
            "resizable": True,
        },
        {
            "headerName": "Editable B",
            "field": "b",
            "editable": True,
        },
        {
            "headerName": "API C",
            "field": "c",
            "cellRenderer": "agAnimateShowChangeCellRenderer",
        },
        {
            "headerName": "Total",
            "valueGetter": {
                "function": "Number(params.data.a) + Number(params.data.b) + Number(params.data.c)"
            },
            "cellRenderer": "agAnimateShowChangeCellRenderer",
        },
        {
            "headerName": "Average",
            "valueGetter": {
                "function": "Math.round((Number(params.data.a) + Number(params.data.b) + Number(params.data.c)) * 10 / 3) /10"
            },
            "cellRenderer": "agAnimateShowChangeCellRenderer",
        },
    ]

    defaultColDef = {
        "type": ["numberColumn", "rightAligned"],
        "filter": "agNumberColumnFilter",
        "resizable": True,
        "sortable": True,
    }

    app.layout = html.Div(
        [
            dcc.Markdown(
                "This grid demonstrates the renderer for animating changes.  Try entering new values into the editable columns and press the button to update column c in a callback"
            ),
            html.Button("Update column C", id="live-data-grid-btn"),
            dag.AgGrid(
                id="grid",
                columnDefs=columnDefs,
                rowData=df.to_dict("records"),
                columnSize="sizeToFit",
                defaultColDef=defaultColDef,
                # setting a row ID is required when updating data in a callback
                getRowId="params.data.index",
            ),
        ],
        style={"margin": 20},
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "1")

    ### testing animations
    grid.get_cell(1, 1).send_keys("50")
    grid.get_cell(1, 2).click()
    start = time.time()
    until(
        lambda: "47" in grid.get_cell_animation(1, 3).get_attribute("innerText"),
        timeout=3,
    )
    until(
        lambda: "47" not in grid.get_cell_animation(1, 3).get_attribute("innerText"),
        timeout=3,
    )
    end = time.time()
    assert (end - start) > 1.8

    grid.get_cell(2, 1).send_keys("50")
    grid.get_cell(2, 2).click()
    start = time.time()
    until(
        lambda: "42" in grid.get_cell_animation(2, 3).get_attribute("innerText"),
        timeout=3,
    )
    until(
        lambda: "42" not in grid.get_cell_animation(2, 3).get_attribute("innerText"),
        timeout=3,
    )
    end = time.time()
    assert (end - start) > 1.8
