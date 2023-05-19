"""
Adding & Removing Columns
"""


import dash_ag_grid as dag
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

medals_included = [
    "athlete",
    "gold",
    "silver",
    "bronze",
    "total",
    "age",
    "country",
    "sport",
    "year",
    "date",
]
medals_excluded = ["athlete", "age", "country", "sport", "year", "date"]

columns_medals_included = [{"field": i} for i in medals_included]
columns_medals_excluded = [{"field": i} for i in medals_excluded]

defaultColDef = {
    "initialWidth": 150,
    "sortable": True,
    "resizable": True,
    "editable": True,
}


app.layout = html.Div(
    [
        dcc.Markdown("Demonstration of updating column definitions in a callback"),
        dbc.Button("Exclude Medals", id="medal-toggle", n_clicks=1),
        dag.AgGrid(
            id="toggle-metals-columns",
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            columnDefs=columns_medals_included,
        ),
    ]
)


@app.callback(
    Output("toggle-metals-columns", "columnDefs"),
    Output("medal-toggle", "children"),
    Input("medal-toggle", "n_clicks"),
    prevent_initial_call=True,
)
def toggle_cols(n):
    if n % 2 == 0:
        return columns_medals_excluded, "Include Medals"
    return columns_medals_included, "Exclude Medals"


if __name__ == "__main__":
    app.run_server(debug=False)
