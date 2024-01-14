"""
Example to test filterParams.filterOptions.predicate function
"""

import dash_ag_grid as dag
from dash import Dash, html
import pandas as pd

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    {
        "field": "athlete",
        "filterParams": {
            "filterOptions": [
                {
                    "displayKey": 'nameStartsWith',
                    "displayName": 'Name starts with',
                    "predicate": {"function": "startWith"},
                    "numberOfInputs": 1,
                },
            ],
        },
    },
]

app.layout = html.Div(
    [
        dag.AgGrid(
            id="filter-conditions-custom-options",
            rowData=df.to_dict("records"),
            columnDefs=columnDefs,
            defaultColDef={"flex": 1, "filter": True, "floatingFilter": True},
            dashGridOptions={"animateRows": False}
        ),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
