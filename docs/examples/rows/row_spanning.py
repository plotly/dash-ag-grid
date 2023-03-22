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

Put the following in the .css file in the assets folder.  This is important because if 
a background was not set, the cell background would be transparent and the underlying 
cell would still be visible.

.cell-span {
  background-color: #00e5ff;
}

---------------------------

Put the following in the dashAgGridComponentFunctions.js file in the assets folder
This will register the functions used to format the currencies.

---------------

var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.rowSpan = function(params) {
  var athlete = params.data ? params.data.athlete : undefined;
  if (athlete === 'Aleksey Nemov') {
    // have all Russia age columns width 2
    return 2;
  } else if (athlete === 'Ryan Lochte') {
    // have all United States column width 4
    return 4;
  } else {
    // all other rows should be just normal
    return 1;
  }
}
"""
