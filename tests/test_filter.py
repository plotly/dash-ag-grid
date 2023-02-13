from dash import Dash, html
from dash_ag_grid import AgGrid
import plotly.express as px

from . import utils


df = px.data.election()
default_display_cols = ["district_id", "district", "winner"]


def test_fi001_floating_filter(dash_duo):
    app = Dash()
    app.layout = html.Div([
        AgGrid(
            id="grid",
            rowData=df.to_dict("records"),
            columnDefs=[
                {"headerName": col.capitalize(), "field": col}
                for col in default_display_cols
            ],
            defaultColDef={"filter": True, "floatingFilter": True}
        )
    ])

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 1, "101-Bois-de-Liesse")

    grid.set_filter(0, "12")

    grid.wait_for_cell_text(0, 1, "112-DeLorimier")
    grid.wait_for_rendered_rows(5)
