"""
AG Grid Filter Buttons
"""
import requests
import dash_ag_grid as dag
from dash import Dash, html

app = Dash(__name__)

data = requests.get(
    r"https://www.ag-grid.com/example-assets/olympic-winners.json"
).json()

columnDefs = [
    {
        "field": "athlete",
        "filter": "agTextColumnFilter",
        "filterParams": {
            "buttons": ["reset", "apply"],
        },
    },
    {
        "field": "age",
        "maxWidth": 100,
        "filter": "agNumberColumnFilter",
        "filterParams": {
            "buttons": ["apply", "reset"],
            "closeOnApply": True,
        },
    },
    {
        "field": "country",
        "filter": "agTextColumnFilter",
        "filterParams": {
            "buttons": ["clear", "apply"],
        },
    },
    {
        "field": "year",
        "filter": "agNumberColumnFilter",
        "filterParams": {
            "buttons": ["apply", "cancel"],
            "closeOnApply": True,
        },
        "maxWidth": 100,
    },
    {"field": "sport"},
    {"field": "gold", "filter": "agNumberColumnFilter"},
    {"field": "silver", "filter": "agNumberColumnFilter"},
    {"field": "bronze", "filter": "agNumberColumnFilter"},
    {"field": "total", "filter": "agNumberColumnFilter"},
]

defaultColDef = {
    "flex": 1,
    "minWidth": 150,
    "filter": True,
}

app.layout = html.Div(
    [
        dag.AgGrid(rowData=data, columnDefs=columnDefs, columnSize="sizeToFit"),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
