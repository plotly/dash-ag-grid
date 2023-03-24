from dash import Dash, html
import dash_ag_grid as dag
import plotly.express as px
import pandas as pd

from . import utils


df = px.data.election()
default_display_cols = ["district_id", "district", "winner"]

df = pd.concat([df, pd.DataFrame({'district': ['test']})])



def test_fi002_custom_filter(dash_duo):
    app = Dash(__name__)

    app.layout = html.Div([
        dag.AgGrid(
            id="grid",
            rowData=df.to_dict("records"),
            columnDefs=[
                {"headerName": col.capitalize(), "field": col,
                 'filterParams': {'function': 'filterParams()'},
                 'filter': 'agNumberColumnFilter'}
                for col in default_display_cols
            ],
            defaultColDef={"floatingFilter": True}
        )
    ])

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 1, "101-Bois-de-Liesse")

    grid.set_filter(0, "12")

    grid.wait_for_cell_text(0, 1, "11-Sault-au-Récollet")
    grid.wait_for_rendered_rows(2)
