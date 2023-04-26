"""
AG Grid custom pagination example

"""
import dash

import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


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
        dcc.Markdown(
            "Example of custom pagination controls with Dash Bootstrap Components `dbc.Pagination`"
        ),
        dbc.Pagination(
            id="custom-pagination",
            max_value=87,
            first_last=True,
            previous_next=True,
            size="sm",
            fully_expanded=False,
        ),
        dag.AgGrid(
            id="custom-pagination-grid",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
            dashGridOptions={
                "pagination": True,
                "suppressPaginationPanel": True,
                "suppressScrollOnNewData": True,
            },
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("custom-pagination", "max_value"),
    Input("custom-pagination-grid", "paginationInfo"),
)
def update_pagination_control(pagination_info):
    if pagination_info is None:
        return dash.no_update
    return pagination_info["totalPages"]


@app.callback(
    Output("custom-pagination-grid", "paginationGoTo"),
    Input("custom-pagination", "active_page"),
    prevent_initial_call=True
)
def goto_page(n):
    if n is None or n == 1:
        return "first"
    # grid pagination starts at zero
    return n - 1


if __name__ == "__main__":
    app.run_server(debug=True)
