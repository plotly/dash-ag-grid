from dash import Dash, html
from dash_ag_grid import AgGrid
import plotly.express as px

from . import utils


df = px.data.election()
default_display_cols = ["district_id", "district", "winner"]


def test_cd001_drag_columns(dash_duo):
    app = Dash()
    app.layout = html.Div([
        AgGrid(
            id="grid",
            rowData=df.to_dict("records"),
            columnDefs=[
                {"headerName": col.capitalize(), "field": col}
                for col in default_display_cols
            ],
        )
    ])

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_all_header_texts(["District_id", "District", "Winner"])
    grid.wait_for_pinned_cols(0)
    grid.wait_for_viewport_cols(3)

    grid.drag_col(2, 0)  # last column first but not pinned

    grid.wait_for_all_header_texts(["Winner", "District_id", "District"])
    grid.wait_for_pinned_cols(0)
    grid.wait_for_viewport_cols(3)

    grid.pin_col(1)  # middle column pinned

    grid.wait_for_all_header_texts(["District_id", "Winner", "District"])
    grid.wait_for_pinned_cols(1)
    grid.wait_for_viewport_cols(2)

    # pin first non-pinned column by dragging it to its own left edge
    grid.pin_col(1, 1)

    grid.wait_for_all_header_texts(["District_id", "Winner", "District"])
    grid.wait_for_pinned_cols(2)
    grid.wait_for_viewport_cols(1)
