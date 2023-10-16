"""
Updating rowData in a callback
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)


df1 = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)
df2 = px.data.gapminder()
df3 = px.data.iris()


app.layout = html.Div(
    [
        html.Label("Select Dataset"),
        dcc.Dropdown(
            ["Olympic Winners", "Gap Minder", "Iris"],
            "Iris",
            id="update-rowdata-dd2",
            clearable=False,
            style={"marginBottom": 10},
        ),
        dag.AgGrid(
            id="update-rowdata-grid2",
            columnSize="autoSize",
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
    Output("update-rowdata-grid2", "rowData"),
    Output("update-rowdata-grid2", "columnDefs"),
    Input("update-rowdata-dd2", "value"),
)
def selected(value):
    if value == "Olympic Winners":
        return df1.to_dict("records"), [{"field": i} for i in df1.columns]
    if value == "Gap Minder":
        return df2.to_dict("records"), [{"field": i} for i in df2.columns]
    return df3.to_dict("records"), [{"field": i} for i in df3.columns]


if __name__ == "__main__":
    app.run_server(debug=True)
