import dash_ag_grid as dag
from dash import Dash, html
from . import utils


def test_cr001_custom_row_selectable(dash_duo):
    app = Dash(__name__)

    columnDefs = [
        {
            "field": "ticker",
            "headerCheckboxSelection": True,
            "checkboxSelection": True,
            "showDisabledCheckboxes": True,
        }
    ]
    grid = dag.AgGrid(
        id="grid",
        columnDefs=columnDefs,
        rowData=[{"ticker": "AAPL"}, {"ticker": "MSFT"}],
        dashGridOptions={
            "isRowSelectable": {
                "function": 'params.data.ticker == "AAPL" ? true: false'
            },
            "rowSelection": "multiple",
        },
    )

    app = Dash(__name__)

    app.layout = html.Div(grid)

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "AAPL")

    assert (
        dash_duo.find_element(
            '#grid [row-index="0"] [aria-colindex="1"] ' ".ag-selection-checkbox input"
        ).get_attribute("disabled")
        == None
    )
    assert dash_duo.find_element(
        '#grid [row-index="1"] [aria-colindex="1"] ' ".ag-selection-checkbox input"
    ).get_attribute("disabled")
