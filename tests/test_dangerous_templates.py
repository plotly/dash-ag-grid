from dash import Dash, html, dcc, Output, Input
import dash_ag_grid as dag

from . import utils


def test_dt001_dangerous_templates(dash_duo):
    columnDefs = [
        {
            "headerName": "Stock Ticker",
            "field": "ticker",
        },
        {
            "headerName": "Company",
            "field": "company",
        },
        {
            "headerComponentParams": {"template": "<div>Testing</div>"},
            "field": "price",
            "valueFormatter": {"function": """d3.format("($,.2f")(params.value)"""},
        },
    ]

    grid = dag.AgGrid(
        id="grid",
        columnDefs=columnDefs,
        columnSize="sizeToFit",
        dashGridOptions={
            "overlayLoadingTemplate": "<div>CustomLoadingOverlay</div>",
            "overlayNoRowsTemplate": "<div>whoops no info</div>",
        },
    )

    app = Dash(__name__)

    app.layout = html.Div(
        [
            dcc.Markdown("Example of custom loading overlay"),
            grid,
            html.Button("load", id="loadBlank", n_clicks=0),
        ],
        style={"margin": 20},
    )

    @app.callback(
        Output("grid", "rowData"),
        Input("loadBlank", "n_clicks"),
        prevent_initial_call=True,
    )
    def loadBlank(n):
        if n:
            return []

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    assert grid.get_header_cell(0).text == "Stock Ticker"

    dash_duo.wait_for_text_to_equal(".ag-overlay-loading-center", "Loading...")
    dash_duo.find_element("#loadBlank").click()
    dash_duo.wait_for_text_to_equal(".ag-overlay-no-rows-wrapper", "No Rows To Show")
    assert grid.get_header_cell(2).text == "Price"


def test_dt002_dangerous_templates(dash_duo):
    columnDefs = [
        {
            "headerName": "Stock Ticker",
            "field": "ticker",
        },
        {
            "headerName": "Company",
            "field": "company",
        },
        {
            "headerComponentParams": {"template": "<div>Testing</div>"},
            "field": "price",
            "valueFormatter": {"function": """d3.format("($,.2f")(params.value)"""},
        },
    ]

    grid = dag.AgGrid(
        id="grid",
        columnDefs=columnDefs,
        columnSize="sizeToFit",
        dashGridOptions={
            "overlayLoadingTemplate": "<div>CustomLoadingOverlay</div>",
            "overlayNoRowsTemplate": "<div>whoops no info</div>",
        },
        dangerously_allow_code=True,
    )

    app = Dash(__name__)

    app.layout = html.Div(
        [
            dcc.Markdown("Example of custom loading overlay"),
            grid,
            html.Button("load", id="loadBlank", n_clicks=0),
        ],
        style={"margin": 20},
    )

    @app.callback(
        Output("grid", "rowData"),
        Input("loadBlank", "n_clicks"),
        prevent_initial_call=True,
    )
    def loadBlank(n):
        if n:
            return []

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    assert grid.get_header_cell(0).text == "Stock Ticker"

    dash_duo.wait_for_text_to_equal(
        ".ag-overlay-loading-wrapper", "CustomLoadingOverlay"
    )
    dash_duo.find_element("#loadBlank").click()
    dash_duo.wait_for_text_to_equal(".ag-overlay-no-rows-wrapper", "whoops no info")
    assert grid.get_header_cell(2).text == "Testing"
