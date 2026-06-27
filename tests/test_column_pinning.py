import dash_ag_grid as dag
from dash import Dash, html, dcc
from . import utils
import uuid


def test_cd001_process_unpinned_columns(dash_duo):
    """ Test that the processUnpinnedColumns function is called when the available viewport space is exceeded and the right most columns are unpinned."""
    
    column_count = 10
    row_count = 10
    rowData = [
        {f"COL_{col_idx}": uuid.uuid4().hex for col_idx in range(column_count)} for _ in range(row_count)
    ]

    app = Dash(__name__)
    columnDefs = [
        {
            "field": col,
            "pinned": "left"
        }
        for col in rowData[0].keys()
    ]

    app.layout = html.Div(
        [
            dcc.Markdown(
                "This grid uses a javascript function to make sure,"
                " that the right most columns are unpinned when the available viewport space is exceeded."
            ),
            dag.AgGrid(
                columnDefs=columnDefs,
                rowData=rowData,
                id="grid",
                dashGridOptions={
                    "processUnpinnedColumns": {"function": "unpinAllButFirstColumn(params)"},
                }
            ),
        ],
        style={"margin": 20},
    )
    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_pinned_column(col_id="COL_0", pin_state="left")
    grid.wait_for_pinned_column(col_id="COL_1", pin_state="scrolling")
    grid.wait_for_pinned_column(col_id="COL_4", pin_state="scrolling")
        
