import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    {
        "field": "athlete",
        "rowSpan": {"function": "rowSpan(params)"},
        "cellClassRules": {
            "cell-span": "params.value==='Aleksey Nemov' || params.value==='Ryan Lochte'",
        },
        "width": 200,
    },
    {"field": "age", "width": 100},
    {"field": "country"},
    {"field": "year", "width": 100},
    {"field": "date"},
    {"field": "sport"},
    {"field": "gold"},
    {"field": "silver"},
    {"field": "bronze"},
    {"field": "total"},
]
defaultColDef = {
    "width": 170,
    "resizable": True,
}


app.layout = html.Div(
    [
        dcc.Markdown("Example: Row Spanning Simple"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            dashGridOptions={"suppressRowTransform": True},
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)


"""

--------------------

Add the following to the .css file in the assets folder:

--------------------

.cell-span {
  background-color: #00e5ff;
}

----------------

Add the following to the dashAgGridFunctions.js file in the assets folder

----------------

var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.rowSpan = function(params) {
  var athlete = params.data ? params.data.athlete : undefined;
  if (athlete === 'Aleksey Nemov') {
    // have all Aleksey Nemov cells in column athlete of height of 2 rows
    return 2;
  } else if (athlete === 'Ryan Lochte') {
    // have all Ryan Lochte cells in column athlete of height of 4 rows
    return 4;
  } else {
    // all other rows should be just normal
    return 1;
  }
}
"""
