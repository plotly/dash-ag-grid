import dash_ag_grid as dag
from dash import Dash, html, dcc
from . import utils
import time
import dash_mantine_components

def test_cm001_context_menu(dash_duo):
    app = Dash(__name__)

    masterColumnDefs = [
        {
            "headerName": "Country",
            "field": "country",
        },
        {"headerName": "Region", "field": "region"},
        {"headerName": "Population", "field": "population"},
    ]
    rowData = [
        {
            "country": "China",
            "region": "Asia",
            "population": 1411778724,
        },
        {
            "country": "India",
            "region": "Asia",
            "population": 1383524897,
        },
        {
            "country": "United States",
            "region": "Americas",
            "population": 332593407,
        },
        {
            "country": "Indonesia",
            "region": "Asia",
            "population": 271350000,
        },
    ]

    app.layout = html.Div(
        [
            dag.AgGrid(
                id="grid",
                enableEnterpriseModules=True,
                columnDefs=masterColumnDefs,
                rowData=rowData,
                columnSize="sizeToFit",
                dashGridOptions={
                                 'getContextMenuItems': {'function': 'contextTest(params)'},
                                 'popupParent': {'function': 'setBody()'}
                                 },
            ),
        ]
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "China")

    ### testing animations
    action = utils.ActionChains(dash_duo.driver)
    action.context_click(grid.get_cell(0, 0)).perform()
    dash_duo.find_element('body > .ag-popup')

    assert dash_duo.find_element('.ag-popup .ag-menu-option-part.ag-menu-option-text').text == 'Alert China'