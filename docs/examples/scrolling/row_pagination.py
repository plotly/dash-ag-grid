"""
AG Grid pagination
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import requests

app = Dash(__name__)


data = requests.get(
    r"https://www.ag-grid.com/example-assets/olympic-winners.json"
).json()

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
        dcc.Markdown("To enable pagination set the grid property `pagination=True`"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=data,
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
            dashGridOptions={"pagination": True},
        ),
        dcc.Markdown(
            "Auto Page Size example.  Enter grid height in px", style={"marginTop": 100}
        ),
        dcc.Input(id="input-height", type="number", min=150, max=1000, value=400),
        dag.AgGrid(
            id="grid-height",
            columnDefs=columnDefs,
            rowData=data,
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
            dashGridOptions={"pagination": True, "paginationAutoPageSize": True},
        ),
    ],
    style={"margin": 20},
)


@app.callback(Output("grid-height", "style"), Input("input-height", "value"))
def update_height(h):
    h = "400px" if h is None else h
    return {"height": h, "width": "100%"}


if __name__ == "__main__":
    app.run_server(debug=False)
