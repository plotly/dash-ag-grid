import dash_ag_grid as dag
from dash import Dash, html, dcc, Output, Input, no_update
import requests
from . import utils
import time

def test_fi001_selected_rows(dash_duo):

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
            html.Div(id="selections-single-output"),
            dag.AgGrid(
                id="grid",
                columnDefs=columnDefs,
                rowData=data,
                columnSize="sizeToFit",
                defaultColDef={"resizable": True, "sortable": True, "filter": True},
                rowSelection="single",
                persistence=True,
                persistence_type='session'
            ),
            html.Button(id='setSelection')
        ],
        style={"margin": 20},
    )


    @app.callback(
        Output("selections-single-output", "children"),
        Input("grid", "selectedRows"),
    )
    def selected(selected):
        if selected:
            return f"You selected athlete: {selected[0]['athlete']}"
        return "No selections"

    @app.callback(
        Output("grid", "selectedRows"),
        Input("setSelection", "n_clicks"),
        prevent_initial_call=True
    )
    def selected(n):
        if n > 0:
            return [{'athlete': 'Natalie Coughlin', 'age': 25, 'country': 'United States', 'year': 2008, 'date': '24/08/2008', 'sport': 'Swimming', 'gold': 1, 'silver': 2, 'bronze': 3, 'total': 6}]
        return no_update

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Michael Phelps")

    grid.get_cell(0,0).click()
    dash_duo.wait_for_text_to_equal('#selections-single-output', "You selected athlete: Michael Phelps")
    dash_duo.driver.refresh()

    grid.wait_for_cell_text(0, 0, "Michael Phelps")
    dash_duo.wait_for_text_to_equal('#selections-single-output', "You selected athlete: Michael Phelps")
    dash_duo.find_element('#setSelection').click()
    dash_duo.wait_for_text_to_equal('#selections-single-output', "You selected athlete: Natalie Coughlin")