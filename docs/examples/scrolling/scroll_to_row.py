import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

# basic columns definition with column defaults
columnDefs = [
    {"field": "country"},
    {"field": "year"},
    {"field": "athlete"},
    {"field": "age"},
    {"field": "date"},
    {"field": "sport"},
    {"field": "total"},
]

app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Input(
                        id="row-index",
                        type="number",
                        min=0,
                        max=df.shape[0] - 1,
                        step=1,
                    )
                ),
                dbc.Col(dbc.Button("Go to row", id="btn")),
            ],
            style={"margin-bottom": 20},
        ),
        dag.AgGrid(
            id="grid",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("grid", "scrollToRow"), Input("btn", "n_clicks"), State("row-index", "value")
)
def scroll_to_row(clicks, row):
    if clicks:
        return row


if __name__ == "__main__":
    app.run_server(debug=False)
