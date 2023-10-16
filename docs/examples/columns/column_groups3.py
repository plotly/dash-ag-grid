"""
Group Changes
"""

import dash_ag_grid as dag
from dash import Dash, dcc, html, Input, Output, ctx
import dash_bootstrap_components as dbc
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

noGroups = [
    {"field": "athlete", "colId": "athlete"},
    {"field": "age", "colId": "age"},
    {"field": "country", "colId": "country"},
    {"field": "year", "colId": "year"},
    {"field": "date", "colId": "date"},
    {"field": "total", "colId": "total"},
    {"field": "gold", "colId": "gold"},
    {"field": "silver", "colId": "silver"},
    {"field": "bronze", "colId": "bronze"},
]

medalsInGroupOnly = [
    {"field": "athlete", "colId": "athlete"},
    {"field": "age", "colId": "age"},
    {"field": "country", "colId": "country"},
    {"field": "year", "colId": "year"},
    {"field": "date", "colId": "date"},
    {
        "headerName": "Medals",
        "headerClass": "medals-group",
        "children": [
            {"field": "total", "colId": "total"},
            {"field": "gold", "colId": "gold"},
            {"field": "silver", "colId": "silver"},
            {"field": "bronze", "colId": "bronze"},
        ],
    },
]

participantInGroupOnly = [
    {
        "headerName": "Participant",
        "headerClass": "participant-group",
        "children": [
            {"field": "athlete", "colId": "athlete"},
            {"field": "age", "colId": "age"},
            {"field": "country", "colId": "country"},
            {"field": "year", "colId": "year"},
            {"field": "date", "colId": "date"},
        ],
    },
    {"field": "total", "colId": "total"},
    {"field": "gold", "colId": "gold"},
    {"field": "silver", "colId": "silver"},
    {"field": "bronze", "colId": "bronze"},
]

participantAndMedalsInGroups = [
    {
        "headerName": "Participant",
        "headerClass": "participant-group",
        "children": [
            {"field": "athlete", "colId": "athlete"},
            {"field": "age", "colId": "age"},
            {"field": "country", "colId": "country"},
            {"field": "year", "colId": "year"},
            {"field": "date", "colId": "date"},
        ],
    },
    {
        "headerName": "Medals",
        "headerClass": "medals-group",
        "children": [
            {"field": "total", "colId": "total"},
            {"field": "gold", "colId": "gold"},
            {"field": "silver", "colId": "silver"},
            {"field": "bronze", "colId": "bronze"},
        ],
    },
]

defaultColDef = {
    "resizable": True,
    "initialWidth": 160,
    "sortable": True,
    "filter": True,
}

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration group changes."),
        dbc.Button("No Groups", id="no-groups"),
        dbc.Button("Participants in Group", id="participants-in-group"),
        dbc.Button("Medals in Group", id="medals-in-group"),
        dbc.Button(
            "Participants and Medals in Group", id="participants-and-medals-in-group"
        ),
        dag.AgGrid(
            id="group-changes",
            columnDefs=noGroups,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
        ),
    ],
)


@app.callback(
    Output("group-changes", "columnDefs"),
    Input("no-groups", "n_clicks"),
    Input("participants-in-group", "n_clicks"),
    Input("medals-in-group", "n_clicks"),
    Input("participants-and-medals-in-group", "n_clicks"),
)
def update(*_):
    if ctx.triggered_id == "participants-and-medals-in-group":
        return participantAndMedalsInGroups
    if ctx.triggered_id == "participants-in-group":
        return participantInGroupOnly
    if ctx.triggered_id == "medals-in-group":
        return medalsInGroupOnly
    return noGroups


if __name__ == "__main__":
    app.run_server(debug=True)
