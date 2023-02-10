"""
Demo of using checkboxes to hide/show columns in AG Grid.
"""

import json
import time

import dash
from dash import dcc, html, Input, Output, State, ALL
import dash_ag_grid as dag
import dash_design_kit as ddk
import plotly.express as px

app = dash.Dash()
server = app.server

# Get sample data from plotly express
df = px.data.election()

# Set default columns to display
default_display_cols = ["district_id", "district", "winner"]

# Function for generating a row of checkboxes for filtering the given column of the dataframe
def checklist(colname):
    unique_values = list(df[colname].unique())
    return html.Details(
        [
            html.Summary(colname.capitalize()),
            dcc.Checklist(
                id="col-display-checklist",
                options=[{"label": x.capitalize(), "value": x} for x in df.columns],
                value=unique_values,
                labelStyle={"display": "inline-block"},
            ),
        ]
    )


app.layout = ddk.App(
    [
        ddk.Card(
            [
                ddk.CardHeader(title="Show/Hide columns in AG Grid"),
                html.P(
                    [
                        """
                        This test demonstrates adding and removing columns
                        from an AG Grid table using a callback.

                        The column widths should update correctly when
                        columns are added or removed.
                        """,
                    ],
                    style={"padding-left": "10px"},
                ),
            ],
        ),
        ddk.Card(
            [
                ddk.CardHeader(title="Election results"),
                ddk.ControlCard(
                    html.Details(
                        [
                            html.Summary("Column display settings"),
                            dcc.Checklist(
                                id="col-display-checklist",
                                options=[
                                    {"label": x.capitalize(), "value": x}
                                    for x in df.columns
                                ],
                                value=default_display_cols,
                                labelStyle={"display": "inline-block"},
                            ),
                        ],
                        open=False,
                        style={"background-color": "#F6F7F8", "font-size": "0.9rem"},
                    ),
                    style={
                        "background-color": "#F6F7F8",
                        "margin-left": "0px",
                        "width": "100%",
                    },
                ),
                dag.AgGrid(
                    id="col-display-data-table",
                    rowData=df.to_dict("records"),
                    columnDefs=[
                        {"headerName": col.capitalize(), "field": col}
                        for col in default_display_cols
                    ],
                    columnSize="sizeToFit",
                    defaultColDef=dict(
                        autoHeight=True,
                        resizable=True,
                        sortable=True,
                    ),
                    enableEnterpriseModules=True,
                ),
            ]
        ),
    ]
)

# Callback to hide/show selected columns
@app.callback(
    Output("col-display-data-table", "columnDefs"),
    Input("col-display-checklist", "value"),
)
def hide_show_cols(display_cols):

    column_defs = [
        {
            "headerName": col.capitalize(),
            "field": col,
        }
        for col in display_cols
    ]
    return column_defs


if __name__ == "__main__":
    app.run_server(debug=True)
