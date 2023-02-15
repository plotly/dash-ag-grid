"""
Single Row Selection - without check boxes.
"""
import dash

import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import requests

app = Dash(__name__)


data = requests.get(
    r"https://www.ag-grid.com/example-assets/olympic-winners.json"
).json()


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
            rowData=data,
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
            rowSelection="single",
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
