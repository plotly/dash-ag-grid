import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

# basic columns definition for all the columns plus an id column
columnDefs = [
    {"headerName": "Row ID", "valueGetter": {"function": "params.node.id"}}
] + [{"field": c} for c in df.columns]

# add a custom value for the row id
rowData = df.to_dict("records")
for i, r in enumerate(rowData):
    r["id"] = f"row-id-{i}"

app.layout = html.Div(
    [
        dcc.Markdown(
            """
            This example uses the row id to set the vertical scroll. In this case the row id is assigned in the application as `"row-id-{index}"` but it can be customized as needed.
            """
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Row"),
                        dcc.Dropdown(
                            options=[r["id"] for r in rowData],
                            id="row-id",
                        ),
                        dbc.Label("Position"),
                        dcc.Dropdown(
                            options=["top", "bottom", "middle"],
                            id="row-position-2",
                        ),
                    ]
                ),
                dbc.Col(dbc.Button("Scroll to", id="btn-2"), align="center"),
            ],
            align="center",
            style={"margin-bottom": 20},
        ),
        dag.AgGrid(
            id="grid-2",
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="autoSize",
            defaultColDef={"resizable": True, "sortable": True},
            getRowId="params.data.id",
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("grid-2", "scrollTo"),
    Input("btn-2", "n_clicks"),
    State("row-id", "value"),
    State("row-position-2", "value"),
)
def scroll_to_row_id(clicks, row_id, row_position):
    if clicks:
        scroll_to = {}
        if row_id:
            scroll_to["rowId"] = row_id
        if row_position:
            scroll_to["rowPosition"] = row_position
        return scroll_to


if __name__ == "__main__":
    app.run_server(debug=False)
