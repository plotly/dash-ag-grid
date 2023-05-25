"""
Accessing the hidden/displayed state of the columns with Enterprise AG-grid modules.
"""

import dash_ag_grid as dag
import dash
from dash import html, dcc, Input, Output, State


app = dash.Dash(__name__)

columnDefs = [
    {"headerName": "Make", "field": "make", "hide": True},
    {"headerName": "Model", "field": "model", "hide": False},
    {"headerName": "Price", "field": "price", "hide": False},
]

columnDefs_grouped = [
    {
        "headerName": "Group 1",
        "children": [{"headerName": "Make", "field": "make", "hide": True}],
    },
    {
        "headerName": "Group 2",
        "children": [
            {"headerName": "Model", "field": "model"},
            {"headerName": "Price", "field": "price"},
        ],
    },
]

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxster", "price": 72000},
]

app.layout = html.Div(
    [
        dcc.Markdown(
            "Using the enterprise menu you can select to display or hide columns and column groups. This state can be accessed in a callback using the property columnVisible"
        ),
        html.Button("SHOW ALL", id="show"),
        dag.AgGrid(
            id="grid-1",
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            defaultColDef=dict(
                resizable=True,
            ),
            enableEnterpriseModules=True,
            licenseKey="LICENSE_KEY_HERE",
        ),
        html.Div(id="output-1"),
        dag.AgGrid(
            id="grid-2",
            columnDefs=columnDefs_grouped,
            rowData=rowData,
            columnSize="sizeToFit",
            defaultColDef=dict(
                resizable=True,
            ),
            enableEnterpriseModules=True,
            licenseKey="LICENSE_KEY_HERE",
        ),
        html.Div(id="output-2"),
    ],
)


@app.callback(
    Output("grid-1", "columnState"),
    Input("show", "n_clicks"),
    State("grid-1", "columnState"),
)
def show_column_visible_grid1(click, columns):
    if click:
        for c in columns:
            c["hide"] = False
        return columns


@app.callback(
    Output("output-1", "children"),
    Input("grid-1", "columnState"),
)
def show_column_visible_grid1(col_visible):
    return str(col_visible)


@app.callback(
    Output("output-2", "children"),
    Input("grid-2", "columnVisible"),
)
def show_column_visible_grid2(col_visible):
    return str(col_visible)


if __name__ == "__main__":
    app.run_server(debug=True)
