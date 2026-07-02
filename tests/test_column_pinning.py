import dash_ag_grid as dag
from dash import Dash, html, dcc
from . import utils
import uuid


def test_cd001_process_unpinned_columns(dash_duo):
    """ Test that the processUnpinnedColumns function is called when the available viewport space is exceeded and the right most columns are unpinned."""
    
    # Make sure that the pinned columns will not fit in the available viewport space and
    # the processUnpinnedColumns function will be called.
    window_width = 1280
    dash_duo.driver.set_window_size(window_width, 720)

    column_width = 300
    column_count = int(window_width / column_width) + 1
    row_count = 10
    row_data = [
        {f"COL_{col_idx}": uuid.uuid4().hex for col_idx in range(column_count)} for _ in range(row_count)
    ]

    app = Dash(__name__)
    column_defs = [
        {
            "field": col,
            "pinned": "left",
            "width": column_width,
        }
        for col in row_data[0].keys()
    ]

    app.layout = html.Div(
        [
            dcc.Markdown(
                "This grid uses a javascript function to make sure,"
                " that the right most columns are unpinned when the available viewport space is exceeded."
            ),
            dag.AgGrid(
                columnDefs=column_defs,
                rowData=row_data,
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
    for col_idx in range(1, column_count):
        grid.wait_for_pinned_column(col_id=f"COL_{col_idx}", pin_state="scrolling")
        
