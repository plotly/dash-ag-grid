"""
AG Grid Floating Filters
"""

import dash_ag_grid as dag
from dash import Dash, html
import pandas as pd

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    {"field": "athlete", "filter": "agTextFilter", "suppressMenu": True},
    {"field": "age", "filter": "agNumberColumnFilter", "suppressMenu": True},
    {"field": "country", "filter": "agSetColumnFilter", "suppressMenu": True},
    {
        "field": "year",
        "maxWidth": 120,
        "filter": "agNumberColumnFilter",
        "floatingFilter": False,
    },
    {"field": "sport", "suppressMenu": True, "filter": "agTextColumnFilter"},
    {
        "field": "gold",
        "filter": "agNumberColumnFilter",
        "filterParams": {
            "buttons": ["apply"],
        },
        "suppressMenu": True,
    },
    {
        "field": "silver",
        "filter": "agNumberColumnFilter",
        "floatingFilterComponentParams": {
            "suppressFilterButton": True,
        },
    },
    {
        "field": "bronze",
        "filter": "agNumberColumnFilter",
        "floatingFilterComponentParams": {
            "suppressFilterButton": True,
        },
    },
    {"field": "total", "filter": False},
]

defaultColDef = {
    "flex": 1,
    "minWidth": 150,
    "filter": True,
    "sortable": True,
    "floatingFilter": True,
}


app.layout = html.Div(
    [
        dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=columnDefs,
            columnSize="sizeToFit",
            defaultColDef=defaultColDef,
        )
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
