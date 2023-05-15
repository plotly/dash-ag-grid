"""
Example post-sort
"""

import dash
import dash_ag_grid as dag
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    {"field": "athlete"},
    {"field": "age", "width": 100},
    {"field": "country", "sort": 'asc'},
    {"field": "year"},
    {"field": "date"},
    {"field": "sport"},
    {"field": "gold"},
    {"field": "silver"},
    {"field": "bronze"},
    {"field": "total"},
]

defaultColDef = {"width": 170, "sortable": True}

app.layout = html.Div(
    [
        dcc.Markdown("Example: Post Sort"),
        dag.AgGrid(
            id="grid-row-post-sort",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            dashGridOptions={
                "postSortRows": {"function": "postSort(params)"}
            }
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)

"""
----------------

Add the following to the dashAgGridFunctions.js file in theA assets folder

----------------
var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.postSort = function (params) {
    const rowNodes = params.nodes;
    // here we put Michael Phelps rows on top while preserving the sort order
    let nextInsertPos = 0;
    for (let i = 0; i < rowNodes.length; i++) {
        const athlete = rowNodes[i].data ? rowNodes[i].data.athlete : undefined;
        if (athlete === 'Michael Phelps') {
            rowNodes.splice(nextInsertPos, 0, rowNodes.splice(i, 1)[0]);
            nextInsertPos++;
        }
    }
}
"""
