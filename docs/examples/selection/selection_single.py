"""
Single Row Selection - without check boxes.
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import pandas as pd

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)


columnDefs = [
    {"field": "athlete"},
    {"field": "age"},
    {"field": "country"},
    {"field": "year"},
    {"field": "date"},
    {"field": "sport"},
    {"field": "gold"},
    {"field": "silver"},
    {"field": "bronze"},
    {"field": "total"},
]

app.layout = html.Div(
    [
        dcc.Markdown("This grid has single-select rows."),
        html.Div(id="selections-single-output"),
        dag.AgGrid(
            id="selection-single-grid",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef={
                "resizable": True,
                "sortable": True,
                "filter": True,
                "minWidth": 125,
            },
            dashGridOptions={"rowSelection": "single"},
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("selections-single-output", "children"),
    Input("selection-single-grid", "selectedRows"),
)
def selected(selected):
    if selected:
        return f"You selected athlete: {selected[0]['athlete']}"
    return "No selections"


if __name__ == "__main__":
    app.run_server(debug=True)
