"""
AG Grid pagination
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import pandas as pd

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
        dcc.Markdown("Setting Page Size.  Enter number of rows"),
        dcc.Input(id="input-page-size", type="number", min=1, max=len(df), value=10),
        dag.AgGrid(
            id="grid-page-size",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
            dashGridOptions={"pagination": True},
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("grid-page-size", "dashGridOptions"),
    Input("input-page-size", "value"),
    State("grid-page-size", "dashGridOptions"),
)
def update_page_size(page_size, grid_options):
    page_size = 1 if page_size is None else page_size
    grid_options["paginationPageSize"] = page_size
    return grid_options


if __name__ == "__main__":
    app.run_server(debug=False)
