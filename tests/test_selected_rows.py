import dash_ag_grid as dag
from dash import Dash, html, dcc, Output, Input, no_update
import requests
from . import utils
import pandas as pd
import time


def test_sr001_selected_rows(dash_duo):
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
                dashGridOptions={"rowSelection": "single"},
                persistence=True,
                persistence_type="session",
            ),
            html.Button(id="setSelection"),
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
        prevent_initial_call=True,
    )
    def selected(n):
        if n > 0:
            return [
                {
                    "athlete": "Natalie Coughlin",
                    "age": 25,
                    "country": "United States",
                    "year": 2008,
                    "date": "24/08/2008",
                    "sport": "Swimming",
                    "gold": 1,
                    "silver": 2,
                    "bronze": 3,
                    "total": 6,
                }
            ]
        return no_update

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Michael Phelps")

    grid.get_cell(0, 0).click()
    dash_duo.wait_for_text_to_equal(
        "#selections-single-output", "You selected athlete: Michael Phelps"
    )
    dash_duo.driver.refresh()

    grid.wait_for_cell_text(0, 0, "Michael Phelps")
    dash_duo.wait_for_text_to_equal(
        "#selections-single-output", "You selected athlete: Michael Phelps"
    )
    dash_duo.find_element("#setSelection").click()
    dash_duo.wait_for_text_to_equal(
        "#selections-single-output", "You selected athlete: Natalie Coughlin"
    )

def test_sr2_selected_rows_rowdata(dash_duo):
    app = Dash(__name__)

    # Placeholder DataFrame
    df = pd.DataFrame()

    app.layout = html.Div([
        html.Button('Update Table', id='update-button', n_clicks=0),
        html.Button('Select Two', id='select-two', n_clicks=0),
        dag.AgGrid(
            id='grid',
            columnSize="sizeToFit",
            columnDefs=[{'field': 'A'}],
            dashGridOptions={
                "rowHeight": None,
                "domLayout": "normal",
                "rowSelection": "multiple",
                "filter": True,
            },
            style={"maxHeight": "200px", "overflow": "auto"},
        ),
        html.Div(id='selected-row-info')  # Div to display selected row information
    ])

    @app.callback(
        Output('grid', 'columnDefs'),
        Output('grid', 'rowData'),
        Output('grid', 'selectedRows'),
        Input('update-button', 'n_clicks'),
        prevent_initial_call=True
    )
    def update_data(n_clicks):
        df = pd.DataFrame({
            "A": [1, 2, 3],
            "B": [4, 5, 6]
        })
        column_defs = [{"headerName": col, "field": col, "filter": "agTextColumnFilter"} for col in df.columns]
        row_data = df.to_dict("records")
        selected_rows = df.head(1).to_dict("records")
        return column_defs, row_data, selected_rows

    @app.callback(
        Output('selected-row-info', 'children'),
        Input('grid', 'selectedRows')
    )
    def update_selected_row_info(selected_rows):
        if isinstance(selected_rows, list):
            selected_row_info = f"Selected Row: {selected_rows[-1]}" if selected_rows else "No row selected"
            return selected_row_info
        return no_update

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_header_text(0, 'A')

    dash_duo.find_element('#update-button').click()

    grid.wait_for_cell_text(0, 0, "1")

    grid.get_cell(1, 0).click()
    dash_duo.wait_for_text_to_equal(
        "#selected-row-info", "Selected Row: {'A': 2, 'B': 5}"
    )

    dash_duo.find_element('#update-button').click()

    time.sleep(1) ## delay to make sure the selection sticks

    dash_duo.wait_for_text_to_equal(
        "#selected-row-info", "Selected Row: {'A': 1, 'B': 4}"
    )

    time.sleep(1)  ## delay to make sure the selection sticks

    assert 'ag-row-selected' in grid.get_row(0).get_attribute('class')

def test_sr3_selected_rows_modes(dash_duo):
    app = Dash(__name__)

    # Placeholder DataFrame
    df = pd.DataFrame()

    app.layout = html.Div([
        html.Button('Update Table', id='update-button', n_clicks=0),
        html.Button('Select Ids', id='select-ids', n_clicks=0),
        html.Button('Select Function', id='select-function', n_clicks=0),
        dag.AgGrid(
            id='grid',
            columnSize="sizeToFit",
            columnDefs=[{'field': 'A'}],
            dashGridOptions={
                "rowHeight": None,
                "domLayout": "normal",
                "rowSelection": "multiple",
                "filter": True,
            },
            style={"maxHeight": "200px", "overflow": "auto"},
            getRowId='params.data.A'
        ),
        html.Div(id='selected-row-info')  # Div to display selected row information
    ])

    @app.callback(
        Output('grid', 'columnDefs'),
        Output('grid', 'rowData'),
        Output('grid', 'selectedRows'),
        Input('update-button', 'n_clicks'),
        prevent_initial_call=True
    )
    def update_data(n_clicks):
        df = pd.DataFrame({
            "A": [1, 2, 3],
            "B": [4, 5, 6]
        })
        column_defs = [{"headerName": col, "field": col, "filter": "agTextColumnFilter"} for col in df.columns]
        row_data = df.to_dict("records")
        selected_rows = df.head(1).to_dict("records")
        return column_defs, row_data, selected_rows

    @app.callback(
        Output('grid', 'selectedRows', allow_duplicate=True),
        Input('select-ids', 'n_clicks'),
        prevent_initial_call=True
    )
    def select_ids(n_clicks):
        return {'ids': ['1', '2']}

    @app.callback(
        Output('grid', 'selectedRows', allow_duplicate=True),
        Input('select-function', 'n_clicks'),
        prevent_initial_call=True
    )
    def select_ids(n_clicks):
        return {'function': 'params.data.A > 2'}

    @app.callback(
        Output('selected-row-info', 'children'),
        Input('grid', 'selectedRows')
    )
    def update_selected_row_info(selected_rows):
        if isinstance(selected_rows, list):
            selected_row_info = f"Selected Row: {selected_rows[-1]}" if selected_rows else "No row selected"
            return selected_row_info
        return no_update

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_header_text(0, 'A')

    dash_duo.find_element('#update-button').click()

    grid.wait_for_cell_text(0, 0, "1")

    dash_duo.wait_for_text_to_equal(
        "#selected-row-info", "Selected Row: {'A': 1, 'B': 4}"
    )

    assert 'ag-row-selected' in grid.get_row(0).get_attribute('class')
    assert 'ag-row-selected' not in grid.get_row(1).get_attribute('class')
    assert 'ag-row-selected' not in grid.get_row(2).get_attribute('class')

    dash_duo.find_element('#select-ids').click()

    time.sleep(1)  ## delay to make sure the selection sticks

    dash_duo.wait_for_text_to_equal(
        "#selected-row-info", "Selected Row: {'A': 2, 'B': 5}"
    )

    time.sleep(1)  ## delay to make sure the selection sticks

    assert 'ag-row-selected' in grid.get_row(0).get_attribute('class')
    assert 'ag-row-selected' in grid.get_row(1).get_attribute('class')
    assert 'ag-row-selected' not in grid.get_row(2).get_attribute('class')

    dash_duo.find_element('#select-function').click()

    time.sleep(1)  ## delay to make sure the selection sticks

    dash_duo.wait_for_text_to_equal(
        "#selected-row-info", "Selected Row: {'A': 3, 'B': 6}"
    )

    time.sleep(1)  ## delay to make sure the selection sticks

    assert 'ag-row-selected' not in grid.get_row(0).get_attribute('class')
    assert 'ag-row-selected' not in grid.get_row(1).get_attribute('class')
    assert 'ag-row-selected' in grid.get_row(2).get_attribute('class')