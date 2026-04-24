import dash_ag_grid as dag
from dash import Dash
from . import utils


def test_gri001_get_row_id_none_renders(dash_duo):
    app = Dash(__name__)
    app.layout = [
        dag.AgGrid(
            id="grid",
            rowData=[{"test": 1}],
            columnDefs=[{"field": "test"}],
            getRowId=None,
        )
    ]

    dash_duo.start_server(app)
    grid = utils.Grid(dash_duo, "grid")
    grid.wait_for_cell_text(0, 0, "1")
