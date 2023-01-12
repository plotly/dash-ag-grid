"""
Download the row data in an AG-grid with a callback.
"""

import dash_ag_grid as dag

import dash
from dash import Input, Output, State, html, dcc, dash_table
import pandas as pd
import json
import urllib

app = dash.Dash(__name__)

with open(("demos/olympic-winners.json")) as json_file:
    data = json.load(json_file)

columnDefs = [
    {"field": "athlete", "sortable": True, "filter": True},
    {"field": "age", "sortable": True, "filter": True},
    {"field": "country", "sortable": True, "filter": True},
    {"field": "year", "sortable": True, "filter": True},
    {"field": "date", "sortable": True, "filter": True},
    {"field": "sport", "sortable": True, "filter": True},
    {"field": "total", "sortable": True, "filter": True},
]

app.layout = html.Div(
    [
        dcc.Markdown("Click the 'Download' button to download the data in the table."),
        html.Div(
            html.Button(
                [
                    html.A(
                        "Download CSV",
                        id="download-link",
                        download="datatable.csv",
                        href="",
                        target="_blank",
                        style={
                            "text-decoration": "none",
                            "color": "white",
                        },
                    )
                ],
                id="csv-button",
            ),
            style={"margin": "20px"},
        ),
        html.Div(
            dag.AgGrid(
                columnDefs=columnDefs,
                rowData=data,
                style={"width": "100%", "height": "400px"},
                rowSelection="multiple",
                columnSize="sizeToFit",
                defaultColDef=dict(
                    resizable=True,
                ),
                id="downloadable-grid",
            )
        ),
    ]
)


@app.callback(
    Output("download-link", "href"),
    Input("downloadable-grid", "rowData"),
)
def dl_csv(rowData):
    if rowData is None:
        return dash.no_update
    else:
        df = pd.DataFrame(rowData)

        csv_string = df.to_csv(index=False, encoding="utf-8")
        csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_string)
        return csv_string


if __name__ == "__main__":
    app.run_server(debug=True)
