"""
Updating rowData in a callback
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import pandas as pd

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)


columnDefs = [
    {"field": "sport", "filter": False},
    {"field": "athlete"},
    {"field": "age"},
    {"field": "country"},
    {"field": "year"},
    {"field": "total"},
]

app.layout = html.Div(
    [
        html.Label("Select Sport:"),
        dcc.Dropdown(
            df["sport"].unique(), "Equestrian", id="update-rowdata-dd", clearable=False
        ),
        dag.AgGrid(
            id="update-rowdata-grid",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="responsiveSizeToFit",
            defaultColDef={
                "resizable": True,
                "sortable": True,
                "filter": True,
                "minWidth": 125,
            },
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("update-rowdata-grid", "rowData"),
    Input("update-rowdata-dd", "value"),
)
def selected(value):
    dff = df[df["sport"] == value]
    return dff.to_dict("records")


if __name__ == "__main__":
    app.run_server(debug=True)
