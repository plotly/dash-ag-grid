import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import pandas as pd
import dash_bootstrap_components as dbc
import json

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

# basic columns definition for all the columns plus an id column
columnDefs = [{"field": c} for c in df.columns]

# add a custom value for the row id
rowData = df.to_dict("records")


app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Row"),
                        dcc.Dropdown(
                            options=[json.dumps(r) for r in rowData],
                            id="row-data",
                        ),
                        dbc.Label("Position"),
                        dcc.Dropdown(
                            options=["top", "bottom", "middle"],
                            id="row-position-3",
                        ),
                    ]
                ),
                dbc.Col(dbc.Button("Scroll to", id="btn-3"), align="center"),
            ],
            align="center",
            style={"margin-bottom": 20},
        ),
        dag.AgGrid(
            id="grid-3",
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="autoSize",
            defaultColDef={"resizable": True, "sortable": True},
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("grid-3", "scrollTo"),
    Input("btn-3", "n_clicks"),
    State("row-data", "value"),
    State("row-position-3", "value"),
)
def scroll_to_row_data(clicks, row_data, row_position):
    if clicks:
        scroll_to = {}
        if row_data:
            scroll_to["rowData"] = json.loads(row_data)
        if row_position:
            scroll_to["rowPosition"] = row_position
        return scroll_to


if __name__ == "__main__":
    app.run_server(debug=False)
