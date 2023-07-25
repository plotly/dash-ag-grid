from dash import Dash, html, Input, Output
from dash_ag_grid import AgGrid
import plotly.express as px
import json

from . import utils


df = px.data.election()
default_display_cols = ["district_id", "district", "winner"]


def test_fi001_floating_filter(dash_duo):
    app = Dash()
    app.layout = html.Div(
        [
            AgGrid(
                id="grid",
                rowData=df.to_dict("records"),
                columnDefs=[
                    {"headerName": col.capitalize(), "field": col}
                    for col in default_display_cols
                ],
                defaultColDef={"filter": True, "floatingFilter": True},
                filterModel={
                    "district": {
                        "filterType": "text",
                        "type": "contains",
                        "filter": "12",
                    }
                },
            ),
            html.Div(id="filterModel"),
            html.Button(id="resetFilters", n_clicks=0),
        ]
    )

    @app.callback(
        Output("filterModel", "children"),
        Input("grid", "filterModel"),
    )
    def updateFilterModel(fM):
        return json.dumps(fM)

    @app.callback(
        Output("grid", "filterModel"),
        Input("resetFilters", "n_clicks"),
        prevent_initial_call=True,
    )
    def updateFilterModel(n):
        return {}

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")
    grid.wait_for_cell_text(0, 1, "112-DeLorimier")
    dash_duo.find_element("#resetFilters").click()

    grid.wait_for_cell_text(0, 1, "101-Bois-de-Liesse")
    dash_duo.wait_for_text_to_equal("#filterModel", "{}")

    grid.set_filter(0, "12")
    dash_duo.wait_for_text_to_equal(
        "#filterModel",
        '{"district_id": {"filterType": "number",'
        ' "type": "equals", "filter": 12}}',
    )

    grid.wait_for_cell_text(0, 1, "12-Saint-Sulpice")
    grid.wait_for_rendered_rows(1)

    dash_duo.find_element("#resetFilters").click()
    grid.wait_for_cell_text(0, 1, "101-Bois-de-Liesse")
