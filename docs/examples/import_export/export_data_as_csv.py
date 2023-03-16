"""
Download the virtual row data.
"""

import dash_ag_grid as dag
import dash
from dash import Input, Output, html, dcc

app = dash.Dash(__name__)

columnDefs = [
    {"headerName": "Make", "field": "make"},
    {"headerName": "Model", "field": "model"},
    {"headerName": "Price", "field": "price"},
]

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxter", "price": 72000},
]

app.layout = html.Div(
    [
        dcc.Markdown(
            "Click on the download button below to enable the export data to CSV feature of AG Grid."
        ),
        html.Div(
            html.Button("Download CSV", id="csv-button", n_clicks=0),
        ),
        dag.AgGrid(
            id="export-data-grid",
            columnSize="sizeToFit",
            columnDefs=columnDefs,
            rowData=rowData,
            csvExportParams={
                "fileName": "ag_grid_test.csv",
            },
        ),
    ]
)


@app.callback(
    Output("export-data-grid", "exportDataAsCsv"),
    Input("csv-button", "n_clicks"),
)
def export_data_as_csv(n_clicks):
    if n_clicks:
        return True

    return False


if __name__ == "__main__":
    app.run_server(debug=True)
