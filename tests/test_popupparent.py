import dash_ag_grid as dag
from dash import Dash, html, dcc
from . import utils
import time
import dash_mantine_components


def test_pp001_popupParent(dash_duo):
    app = Dash(__name__)

    app.layout = html.Div(
        [
            dag.AgGrid(
                rowData=[{'cities': ''}, {'cities': 'dallas'}, {'cities': 'houston'}],
                columnDefs=[{'field': 'cities', 'cellEditor': {'function': 'DMC_Select'},
                             'cellEditorParams': {'options': ['dallas', 'houston']},
                             'cellEditorPopup': True, 'editable': True}],
                style={'resize': 'both', 'overflow': 'auto'},
                dashGridOptions={'popupParent': {'function': 'setBody()'}},
                id='grid'
            )
        ],

    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "")

    ### testing animations
    action = utils.ActionChains(dash_duo.driver)
    action.double_click(grid.get_cell(0, 0)).perform()

    dash_duo.find_element('body > .ag-popup .mantine-Select-input')
