import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import pandas as pd



def test_pi001_pivot_column_order(dash_duo):
    app = Dash(__name__)

    df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
    )

    columnDefs = [
        {"field": "country", "rowGroup": True},
        {"field": "sport", "pivot": True, "pivotComparator": {"function": "sortColumns"}},
        {"field": "year"},
        {"field": "date"},
        {"field": "gold", "aggFunc": "sum"},
    ]

    app.layout = html.Div(
        [
            dag.AgGrid(
                id="grid",
                columnDefs=columnDefs,
                rowData=df.to_dict("records"),
                dashGridOptions={
                    "autoGroupColumnDef": {"minWidth": 250},
                    "pivotMode": True,
                },
                enableEnterpriseModules=True,
            ),
            html.Div(id="col-order"),
        ],
    )

    @app.callback(
        Output("col-order", "children"),
        Input("grid", "columnState"),
        prevent_initial_call=True,
    )
    def display_state(col_state):

        # Pivot columns are identified in `columnState` by `colId`.
        # If not specified by the user, the `colId` is auto-generated with a `pivot_{field name}` prefix.

        pivot_columns = [
            c["colId"] for c in col_state if c["colId"].startswith("pivot_sport")
        ]

        # By default, the columns are sorted in ascending order.
        # This app uses a custom `pivotComparator` function to sort the columns in descending order.
        # The following check verifies if the columns are correctly sorted in descending order.
        descending = pivot_columns == sorted(pivot_columns, reverse=True)
        return f"pivot columns sorted in reverse order? {descending}"

    dash_duo.start_server(app)

    dash_duo.wait_for_text_to_equal(
        "#col-order", "pivot columns sorted in reverse order? True"
    )


