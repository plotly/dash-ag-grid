"""
Example to test filterParams.textFormatter and filterParams.textMatcher functions
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
        "filterParams": {"textFormatter": {"function": "myTextFormatter(params)"}},
    },
    {
        "field": "country",
        "filterParams": {"textMatcher": {"function": "myTextMatcher(params)"}},
    },
]

app.layout = html.Div(
    [
        dag.AgGrid(
            id="text-filter-custom",
            rowData=df.to_dict("records"),
            columnDefs=columnDefs,
            columnSize="sizeToFit",
            defaultColDef={"filter": True, "floatingFilter": True}
        ),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
