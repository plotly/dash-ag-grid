import dash_ag_grid as dag
from dash import Dash, html, dcc, Output, Input, no_update, ctx
import requests
from . import utils


def test_sb001_selection_buttons(dash_duo):
    app = Dash(__name__)

    data = requests.get(
        r"https://www.ag-grid.com/example-assets/olympic-winners.json"
    ).json()

    columnDefs = [
        {"field": "athlete"},
        {"field": "age"},
        {"field": "country"},
        {"field": "year"},
        {"field": "date"},
        {"field": "sport"},
        {"field": "gold"},
        {"field": "silver"},
        {"field": "bronze"},
        {"field": "total"},
    ]

    app.layout = html.Div(
        [
            dcc.Markdown("This grid has single-select rows."),
            dag.AgGrid(
                id="grid",
                columnDefs=columnDefs,
                rowData=data,
                columnSize="sizeToFit",
                defaultColDef={
                    "resizable": True,
                    "sortable": True,
                    "filter": True,
                    "floatingFilter": True,
                },
                dashGridOptions={"rowSelection": "multiple"},
                persistence=True,
                persistence_type="session",
            ),
            html.Button(id="selectAll", children="Select All"),
            html.Button(id="selectAllFiltered", children="Select All Filtered"),
            html.Button(id="deselectAll", children="Deselect All"),
            html.Div(id="selections"),
        ],
        style={"margin": 20},
    )

    @app.callback(
        Output("grid", "selectAll"),
        Input("selectAll", "n_clicks"),
        Input("selectAllFiltered", "n_clicks"),
    )
    def setSelection(n, n2):
        if n:
            if ctx.triggered_id == "selectAll":
                return True
            else:
                return {"filtered": True}
        return no_update

    @app.callback(Output("grid", "deselectAll"), Input("deselectAll", "n_clicks"))
    def setSelection(n):
        if n:
            return True
        return no_update

    @app.callback(
        Output("selections", "children"),
        Input("grid", "selectedRows"),
    )
    def selected(selected):
        if selected:
            return len(selected)
        return "No selections"

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Michael Phelps")
    grid.set_filter(0, "f")

    grid.wait_for_cell_text(0, 0, "Missy Franklin")

    dash_duo.find_element("#selectAll").click()
    dash_duo.wait_for_text_to_equal("#selections", "8618")
    dash_duo.find_element("#deselectAll").click()
    dash_duo.wait_for_text_to_equal("#selections", "No selections")
    dash_duo.find_element("#selectAllFiltered").click()
    dash_duo.wait_for_text_to_equal("#selections", "816")
    dash_duo.find_element("#deselectAll").click()
    dash_duo.wait_for_text_to_equal("#selections", "No selections")
