import dash_ag_grid as dag
from dash import Dash, html, dcc, Output, Input, no_update, ctx, State
import requests
from . import utils
import json
from dash.testing.wait import until


def test_sb001_sizing_buttons(dash_duo):
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
                rowData=data[:100],
                columnSize="sizeToFit",
                defaultColDef={"resizable": True, "sortable": True, "filter": True, "floatingFilter": True},
                dashGridOptions={'rowSelection': "multiple"},
                persistence=True,
                persistence_type='session',
                autoSizeAllColumns={'skipHeaders': True}
            ),
            html.Button(id='autoSizeAllColumns', children='Auto Size All'),
            html.Button(id='autoSizeAllColumnsSkipHeaders', children='Auto Size All SkipHeaders'),
            html.Button(id='updateColumnState', children='Update Column State'),
            html.Div(id="columnState"),
        ],
        style={"margin": 20},
    )

    @app.callback(Output('grid', 'autoSizeAllColumns'),
                  Input('autoSizeAllColumns', 'n_clicks'), Input('autoSizeAllColumnsSkipHeaders', 'n_clicks'),
                  prevent_initial_call=True)
    def setSelection(n, n2):
        if n:
            if ctx.triggered_id == 'autoSizeAllColumns':
                return True
            else:
                return {'skipHeaders': True}
        return no_update

    @app.callback(Output('grid', 'updateColumnState'),
                  Input('updateColumnState', 'n_clicks'))
    def setSelection(n):
        if n:
            return True
        return no_update

    @app.callback(
        Output("columnState", "children"),
        Input("grid", "columnState"),
        State("columnState", "children"),
        State('updateColumnState', 'n_clicks'),

    )
    def selected(state, oldState, n):
        if state:
            test = True
            if oldState and n > 1:
                oldState = json.loads(oldState)
                for i in range(len(state)):
                    if i in [1, 6, 7, 8, 9]:
                        if state[i]['width'] > oldState[i]['width']:
                            test = False
                            break
            assert test
            return json.dumps(state)
        return ""

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Michael Phelps")

    oldValue = ''
    until(lambda: oldValue != dash_duo.find_element('#columnState').text, timeout=3)
    oldValue = dash_duo.find_element('#columnState').text
    for x in columnDefs:
        assert x['field'] in oldValue

    for x in ['autoSizeAllColumns', 'autoSizeAllColumnsSkipHeaders']:
        dash_duo.find_element(f'#{x}').click()
        dash_duo.find_element('#updateColumnState').click()
        until(lambda: oldValue != dash_duo.find_element('#columnState').get_attribute('innerText'), timeout=3)
        oldValue = dash_duo.find_element('#columnState').get_attribute('innerText')


def test_sb002_sizeColumnsToFit_button(dash_duo):
    app = Dash(__name__)

    app.layout = html.Div([
        html.Button("size-to-fit", id="btn"),
        dag.AgGrid(
            id="grid",
            rowData=[{"A": "xxx"}],
            columnSize="sizeToFit",
            columnDefs=[{"field": "A"}],
        )
    ])

    @app.callback(
        Output("grid", "sizeColumnsToFit"),
        Input("btn", "n_clicks"),
    )
    def update_grid(_):
        return True

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")
    grid.wait_for_cell_text(0, 0, "xxx")
    width1 = grid.get_cell(0, 0).get_attribute('style')

    dash_duo.driver.set_window_size(400, 800)
    dash_duo.find_element('#btn').click()
    width2 = grid.get_cell(0, 0).get_attribute('style')

    until(lambda: width1 != width2, timeout=3)

