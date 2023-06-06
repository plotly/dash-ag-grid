import dash_ag_grid as dag
from dash import Dash, html
from . import utils
from dash.testing.wait import until


def test_ds001_default_styles(dash_duo):
    app = Dash(__name__)

    columnDefs = [
        {"headerName": "Make", "field": "make"},
        {"headerName": "Model", "field": "model"},
        {
            "headerName": "Price",
            "field": "price",
            "cellStyle": {"defaultStyle": {"color": "green"}},
        },
    ]

    rowData = [
        {"make": "Toyota", "model": "Celica", "price": 35000},
        {"make": "Ford", "model": "Mondeo", "price": 32000},
        {"make": "Porsche", "model": "Boxster", "price": 72000},
    ]

    grid_with_default_cell_styles = html.Div(
        [
            html.H3(children="Grid with Default Cell Styles"),
            dag.AgGrid(
                columnDefs=columnDefs,
                rowData=rowData,
                columnSize="sizeToFit",
                defaultColDef=dict(
                    resizable=True,
                    cellStyle={"defaultStyle": {"color": "blue"}},
                ),
                id="grid",
            ),
            html.Hr(),
        ]
    )

    app.layout = grid_with_default_cell_styles

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Toyota")

    ### testing styles
    until(
        lambda: "color: blue" in grid.get_cell(0, 0).get_attribute("style"), timeout=3
    )
    until(
        lambda: "color: green" in grid.get_cell(0, 2).get_attribute("style"), timeout=3
    )
