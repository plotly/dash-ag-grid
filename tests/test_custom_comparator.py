from dash import Dash, html, dcc, Output, Input
import dash_ag_grid as dag

from . import utils


def test_cc001_custom_comparator(dash_duo):
    import dash_ag_grid as dag
    from dash import Dash, html, dcc
    import pandas as pd

    app = Dash(__name__)

    df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
    )

    # basic columns definition with column defaults
    columnDefs = [
        {"field": "athlete", "sort": "desc"},
        {"field": "age", "width": 90},
        {"field": "country"},
        {"field": "year", "width": 90, "unSortIcon": True},
        {"field": "date", "comparator": {"function": "dateComparator"}},
        {"field": "sport"},
        {"field": "gold"},
        {"field": "silver"},
        {"field": "bronze"},
        {"field": "total"},
    ]
    defaultColDef = {
        "width": 170,
        "sortable": True,
    }

    app.layout = html.Div(
        [
            dcc.Markdown("Date Sort Comparator Example"),
            dag.AgGrid(
                columnDefs=columnDefs,
                rowData=df.to_dict("records")[:100],
                defaultColDef=defaultColDef,
                id="grid",
            ),
        ],
        style={"margin": 20},
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")
    grid.wait_for_cell_text(0, 0, "Yannick Agnel")

    grid.get_header_cell(4).click()
    grid.wait_for_cell_text(0, 0, "Aleksey Nemov")
    grid.wait_for_cell_text(0, 4, "1/10/2000")

    grid.get_header_cell(4).click()
    grid.wait_for_cell_text(0, 0, "Michael Phelps")
    grid.wait_for_cell_text(0, 4, "12/8/2012")
