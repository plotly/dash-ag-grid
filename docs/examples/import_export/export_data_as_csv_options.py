"""
Download the virtual row data.
"""

import dash_ag_grid as dag
import dash
from dash import Input, Output, html, dcc, ctx

app = dash.Dash(__name__)

columnDefs = [
    {"headerName": "Make", "field": "make"},
    {"headerName": "Model", "field": "model"},
    {"headerName": "Price", "field": "price"},
    {"headerName": "Sale Price", "field": "sale", "hide": True},
]

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000, "sale": 33000},
    {"make": "Ford", "model": "Mondeo", "price": 32000, "sale": 29000},
    {"make": "Porsche", "model": "Boxter", "price": 72000, "sale": 69000},
]

app.layout = html.Div(
    [
        dcc.Markdown(
            "Click on the download button below to enable the export data to CSV feature of AG Grid."
        ),
        html.Button("Download CSV - no headings", id="no-headings", n_clicks=0),
        html.Button("Download CSV - include hidden", id="all-cols", n_clicks=0),
        dag.AgGrid(
            id="export-grid-options",
            columnSize="sizeToFit",
            columnDefs=columnDefs,
            rowData=rowData,
        ),
    ]
)


@app.callback(
    Output("export-grid-options", "exportDataAsCsv"),
    Output("export-grid-options", "csvExportParams"),
    Input("no-headings", "n_clicks"),
    Input("all-cols", "n_clicks"),
    prevent_initial_call=True,
)
def export_data_as_csv(*_):
    if ctx.triggered_id == "no-headings":
        return True, {
            "fileName": "ag_grid_no_headings_test.csv",
            "skipColumnHeaders": True,
        }
    return True, {"fileName": "ag_grid_all_cols_test.csv", "allColumns": True}


if __name__ == "__main__":
    app.run_server(debug=True)
