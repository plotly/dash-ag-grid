"""
AG Grid Text Filters
"""

import dash_ag_grid as dag
from dash import Dash, html
import pandas as pd

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)


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
            rowData=df.to_dict("records"),
            columnDefs=columnDefs,
            columnSize="sizeToFit",
            defaultColDef=defaultColDef,
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
