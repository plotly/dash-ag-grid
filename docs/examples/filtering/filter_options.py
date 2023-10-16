"""
AG Grid Filter Options
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)


columnDefs = [
    {"field": "athlete"},
    {
        "field": "country",
        "filterParams": {
            "filterOptions": ["contains", "startsWith", "endsWith"],
            "defaultOption": "startsWith",
        },
    },
    {
        "field": "age",
        "filter": "agNumberColumnFilter",
        "filterParams": {
            "filterPlaceholder": "Age...",
            "alwaysShowBothConditions": True,
            "defaultJoinOperator": "OR",
        },
        "maxWidth": 100,
    },
]
defaultColDef = {
    "flex": 1,
    "minWidth": 150,
    "filter": True,
}


app.layout = html.Div(
    [
        dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=columnDefs,
            columnSize="sizeToFit",
            defaultColDef=defaultColDef,
        ),
        dcc.Markdown("Grid with Header styled on filter", style={"marginTop": 30}),
        dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=columnDefs,
            columnSize="sizeToFit",
            defaultColDef=defaultColDef,
            className="header-style-on-filter ag-theme-alpine",
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
