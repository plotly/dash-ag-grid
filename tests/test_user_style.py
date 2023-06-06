from dash import Dash, html, Output, Input, no_update, State, ctx
import dash_ag_grid as dag
import plotly.express as px
import json

from . import utils
from dash.testing.wait import until


df = px.data.election()
default_display_cols = ["district_id", "district", "winner"]


def test_us001_user_style(dash_duo):
    app = Dash(__name__)
    columnDefs = [
        {"headerName": "Make", "field": "make"},
        {"headerName": "Model", "field": "model"},
        {"headerName": "Price", "field": "price"},
    ]

    defaultColDef = {
        "initialWidth": 150,
        "sortable": True,
        "resizable": True,
        "filter": True,
    }

    rowData = [
        {"make": "Toyota", "model": "Celica", "price": 35000},
        {"make": "Ford", "model": "Mondeo", "price": 32000},
        {"make": "Porsche", "model": "Boxster", "price": 72000},
    ]

    app.layout = html.Div(
        [
            dag.AgGrid(
                id="grid",
                columnSize="autoSize",
                columnDefs=columnDefs,
                defaultColDef=defaultColDef,
                rowData=rowData,
                style={"height": "500px", "width": "500px"},
            ),
        ]
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Toyota")
    until(
        lambda: "height: 500px"
        in dash_duo.find_element("div.ag-theme-alpine").get_attribute("style"),
        timeout=3,
    )
    until(
        lambda: "width: 500px"
        in dash_duo.find_element("div.ag-theme-alpine").get_attribute("style"),
        timeout=3,
    )
