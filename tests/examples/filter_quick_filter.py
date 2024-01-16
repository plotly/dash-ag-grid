"""
Example to test dashGridOptions.quickFilterParser and filterParams.textMatcher functions
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc, callback, Input, Output, Patch
import pandas as pd

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    {"field": "athlete"},
    {"field": "age"},
]

app.layout = html.Div(
    [
        dcc.Input(id="quick-filter-input", placeholder="filter..."),
        dag.AgGrid(
            id="quick-filter",
            rowData=df.to_dict("records"),
            columnDefs=columnDefs,
            dashGridOptions={
                # allows to split by space (default) and ',' for the words to search
                # 'michael phelps' works by default, now 'michael, phelps' or 'michael,phelps' also
                "quickFilterParser": {"function": r"params.split(/[\s,]+/)"},
                # allows to use regex in quick search, like 2[012] matching Age 20, 21 and 22
                # defining in dashAgGridFunctions.js:
                # dagfuncs.quickFilterMatcher = (quickFilterParts, rowQuickFilterAggregateText) = > {
                #   return quickFilterParts.every(part= > rowQuickFilterAggregateText.match(part));
                # }
                "quickFilterMatcher": {"function": "quickFilterMatcher"}
            }
        ),
    ]
)


@callback(
    Output("quick-filter", "dashGridOptions"),
    Input("quick-filter-input", "value"),
    prevent_initial_call=True,
)
def update_filter(filter_value):
    new_grid_option = Patch()
    new_grid_option['quickFilterText'] = filter_value
    return new_grid_option


if __name__ == "__main__":
    app.run(debug=True)
