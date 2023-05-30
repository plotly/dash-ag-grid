import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

# basic columns definition with column defaults
columnDefs = [{"field": c} for c in df.columns]

app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Row index"),
                        dbc.Input(
                            id="row-index",
                            type="number",
                            min=0,
                            max=df.shape[0] - 1,
                            step=1,
                        ),
                        dbc.Label("Position"),
                        dcc.Dropdown(
                            options=["top", "bottom", "middle"],
                            id="row-index-position",
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Label("Column"),
                        dcc.Dropdown(
                            options=[c["field"] for c in columnDefs], id="column"
                        ),
                        dbc.Label("Position"),
                        dcc.Dropdown(
                            options=["auto", "start", "middle", "end"],
                            id="column-position",
                        ),
                    ]
                ),
                dbc.Col(dbc.Button("Scroll to", id="btn"), align="center"),
            ],
            align="center",
            style={"margin-bottom": 20},
        ),
        dag.AgGrid(
            id="grid",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="autoSize",
            defaultColDef={"resizable": True, "sortable": True},
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("grid", "scrollTo"),
    Input("btn", "n_clicks"),
    State("row-index", "value"),
    State("column", "value"),
    State("row-index-position", "value"),
    State("column-position", "value"),
)
def scroll_to_row_and_col(
    clicks, row_index, column, row_index_position, column_position
):
    if clicks:
        scroll_to = {}
        if row_index or row_index == 0:
            scroll_to["rowIndex"] = row_index
        if column:
            scroll_to["column"] = column
        if row_index_position:
            scroll_to["rowIndexPosition"] = row_index_position
        if column_position:
            scroll_to["columnPosition"] = column_position
        scroll_to["columnPosition"] = None
        return scroll_to


if __name__ == "__main__":
    app.run_server(debug=False)
