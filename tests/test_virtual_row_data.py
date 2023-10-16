from dash import Dash, html, dcc, Output, Input
import dash_ag_grid as dag

from . import utils


def test_vr001_virtual_row_data(dash_duo):
    app = Dash(__name__)

    rowData = [
        {"make": "Toyota", "model": "Celica", "price": 35000},
        {"make": "Ford", "model": "Mondeo", "price": 32000},
        {"make": "Porsche", "model": "Boxster", "price": 72000},
    ]

    columnDefs = [
        {"headerName": "Make", "field": "make", "sortable": True},
        {"headerName": "Model", "field": "model"},
        {"headerName": "Price", "field": "price"},
    ]

    app.layout = html.Div(
        [
            dcc.Markdown(
                "Try filtering the data in the grid using the inline filters (click the hamburger menu in each column). Though the data is still in `rowData`, you can view the virtual row data in callbacks by watching the `virtualRowData` property."
            ),
            dag.AgGrid(
                id="grid",
                columnDefs=columnDefs,
                rowData=rowData,
                defaultColDef={
                    "sortable": True,
                    "filter": True,
                    "floatingFilter": True,
                },
            ),
            html.Div(id="data-after-filter"),
        ]
    )

    @app.callback(
        Output("data-after-filter", "children"),
        Input("grid", "virtualRowData"),
    )
    def get_virtual_data(virtual):
        return str(virtual)

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    dash_duo.wait_for_text_to_equal(
        "#data-after-filter",
        "[{'make': 'Toyota', 'model': 'Celica', 'price': 35000}, "
        "{'make': 'Ford', 'model': 'Mondeo', 'price': 32000}, "
        "{'make': 'Porsche', 'model': 'Boxster', 'price': 72000}]",
    )

    grid.set_filter(0, "F")

    dash_duo.wait_for_text_to_equal(
        "#data-after-filter", "[{'make': 'Ford', 'model': 'Mondeo', 'price': 32000}]"
    )

    grid.set_filter(0, "")

    dash_duo.wait_for_text_to_equal(
        "#data-after-filter",
        "[{'make': 'Toyota', 'model': 'Celica', 'price': 35000}, "
        "{'make': 'Ford', 'model': 'Mondeo', 'price': 32000}, "
        "{'make': 'Porsche', 'model': 'Boxster', 'price': 72000}]",
    )

    grid.get_header_cell(0).click()

    dash_duo.wait_for_text_to_equal(
        "#data-after-filter",
        "[{'make': 'Ford', 'model': 'Mondeo', 'price': 32000}, "
        "{'make': 'Porsche', 'model': 'Boxster', 'price': 72000},"
        " {'make': 'Toyota', 'model': 'Celica', 'price': 35000}]",
    )

    grid.get_header_cell(0).click()

    dash_duo.wait_for_text_to_equal(
        "#data-after-filter",
        "[{'make': 'Toyota', 'model': 'Celica', 'price': 35000}, "
        "{'make': 'Porsche', 'model': 'Boxster', 'price': 72000}, "
        "{'make': 'Ford', 'model': 'Mondeo', 'price': 32000}]",
    )

    grid.get_header_cell(0).click()

    dash_duo.wait_for_text_to_equal(
        "#data-after-filter",
        "[{'make': 'Toyota', 'model': 'Celica', 'price': 35000}, "
        "{'make': 'Ford', 'model': 'Mondeo', 'price': 32000}, "
        "{'make': 'Porsche', 'model': 'Boxster', 'price': 72000}]",
    )
