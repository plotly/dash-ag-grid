"""
AG Grid Text Filters
"""
import requests
import dash_ag_grid as dag
from dash import Dash, html

app = Dash(__name__)

data = requests.get(
    r"https://www.ag-grid.com/example-assets/olympic-winners.json"
).json()


athleteFilterParams = {
    "filterOptions": ["contains", "notContains"],
    "debounceMs": 200,
    "suppressAndOrCondition": True,
}

countryFilterParams = {
    "filterOptions": ["contains"],
    "trimInput": True,
    "debounceMs": 1000,
}

columnDefs = [
    {
        "field": "athlete",
        "filterParams": athleteFilterParams,
    },
    {
        "field": "country",
        "filter": "agTextColumnFilter",
        "filterParams": countryFilterParams,
    },
    {
        "field": "sport",
        "filter": "agTextColumnFilter",
        "filterParams": {
            "caseSensitive": True,
            "defaultOption": "startsWith",
        },
    },
]
defaultColDef = {
    "flex": 1,
    "sortable": True,
    "filter": True,
}


app.layout = html.Div(
    [
        dag.AgGrid(
            rowData=data,
            columnDefs=columnDefs,
            columnSize="sizeToFit",
            defaultColDef=defaultColDef,
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
