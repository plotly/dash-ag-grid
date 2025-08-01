import dash_ag_grid as dag
from dash import Dash, html, dcc
from . import utils


def test_cd001_cell_renderer_function(dash_duo):
    app = Dash(__name__)

    rowData = [
        {"size": 0, "is_available": True},
        {"size": 1, "is_available": False},
        {"size": 2, "is_available": True},
    ]

    columnDefs = [
        {
            "field": "size",
            "cellRenderer": {"function": "params.value < 1 ? 'small' : params.value < 2 ? 'medium' : 'large'"},
        },
        {
            "field": "is_available",
            "cellRenderer": {"function": "params.value ? 'yes' : 'no'"},
        },
    ]

    app.layout = html.Div(
        [
            dcc.Markdown(
                "This grid uses a javascript function to display computed values for each cell, rather than the raw numbers."
            ),
            dag.AgGrid(
                columnDefs=columnDefs,
                rowData=rowData,
                id="grid",
            ),
        ],
        style={"margin": 20},
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "small")
    grid.wait_for_cell_text(0, 1, "yes")
    grid.wait_for_cell_text(1, 0, "medium")
    grid.wait_for_cell_text(1, 1, "no")
    grid.wait_for_cell_text(2, 0, "large")
    grid.wait_for_cell_text(2, 1, "yes")
