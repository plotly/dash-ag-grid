"""
Infintie scroll with pagination
"""


import dash_ag_grid as dag
import dash
from dash import Input, Output, html, dcc, no_update


import pandas as pd

app = dash.Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/liquor_iowa_2021.csv"
)


app.layout = html.Div(
    [
        dag.AgGrid(
            id="infinite-scroll-pagination-grid",
            columnDefs=[{"field": i} for i in df.columns],
            rowModelType="infinite",
            columnSize="autoSize",
            defaultColDef=dict(
                resizable=True, sortable=True, filter=True, minWidth=100
            ),
            dashGridOptions={"pagination": True},
        ),
    ]
)


@app.callback(
    Output("infinite-scroll-pagination-grid", "getRowsResponse"),
    Input("infinite-scroll-pagination-grid", "getRowsRequest"),
)
def infinite_scroll(request):
    if request is None:
        return no_update
    partial = df.iloc[request["startRow"] : request["endRow"]]
    return {"rowData": partial.to_dict("records"), "rowCount": len(df.index)}


if __name__ == "__main__":
    app.run_server(debug=True)
