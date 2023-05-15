import dash_ag_grid as dag
import pandas as pd
from dash import Dash, html, dcc

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    {"field": "athlete", "pinned": "left"},
    {"field": "age", "pinned": "left"},
    {"field": "country", "colSpan": {"function": "simpleSpanning(params)"}},
    {"field": "year"},
    {"field": "date"},
    {"field": "sport"},
    {"field": "gold"},
    {"field": "silver"},
    {"field": "bronze"},
    {"field": "total"},
]

defaultColDef = {"width": 150, "resizable": True}

app.layout = html.Div(
    [
        dcc.Markdown("Example: Column Spanning Simple"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
        ),
    ],
    className='colSpanning'
)

if __name__ == "__main__":
    app.run_server(debug=True)

"""
--------------------

Add the following to the .css file in the assets folder:

--------------------

.colSpanning .ag-body-viewport [col-id='country'] {
  background-color: #a6e1ec;
}

----------------

Add the following to the dashAgGridFunctions.js file in the assets folder

----------------
var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.simpleSpanning = function (params) {
    const country = params.data.country;
    if (country === 'Russia') {
        // have all Russia age columns width 2
        return 2;
    } else if (country === 'United States') {
        // have all United States column width 4
        return 4;
    } else {
        // all other rows should be just normal
        return 1;
    }

"""
