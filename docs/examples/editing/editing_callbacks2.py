"""
Accessing Row Data in an editable grid
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px
import pandas as pd


app = Dash(__name__)

df = px.data.medals_long()


app.layout = html.Div(
    [
        dcc.Markdown("Example of using `rowData` in a callback with an editable grid"),
        dag.AgGrid(
            id="editing-grid2",
            columnDefs=[{"field": i} for i in df.columns],
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef={"editable": True},
        ),
        html.Div(id="editing-grid-output2"),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("editing-grid-output2", "children"),
    Input("editing-grid2", "cellValueChanged"),
    State("editing-grid2", "rowData"),
)
def update(_, rows):
    dff = pd.DataFrame(rows)
    fig = px.bar(dff, x="nation", y="count", color="medal")
    return dcc.Graph(figure=fig)


if __name__ == "__main__":
    app.run_server(debug=False)
