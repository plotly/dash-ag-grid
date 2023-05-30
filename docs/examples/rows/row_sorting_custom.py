"""
Custom Comparator
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

# basic columns definition with column defaults
columnDefs = [
    {"field": "athlete", "sort": "desc"},
    {"field": "age", "width": 90},
    {"field": "country"},
    {"field": "year", "width": 90, "unSortIcon": True},
    {"field": "date", "comparator": {"function": "dateComparator"}},
    {"field": "sport"},
    {"field": "gold"},
    {"field": "silver"},
    {"field": "bronze"},
    {"field": "total"},
]
defaultColDef = {
    "width": 150,
    "sortable": True,
}

app.layout = html.Div(
    [
        dcc.Markdown("Date Sort Comparator Example"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)


"""
Add this to the dashAgGridFunctions.js file in the assets folder:

----------------


var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.dateComparator = function (date1, date2) {
  const date1Number = monthToComparableNumber(date1);
  const date2Number = monthToComparableNumber(date2);
  if (date1Number === null && date2Number === null) {
    return 0;
  }
  if (date1Number === null) {
    return -1;
  }
  if (date2Number === null) {
    return 1;
  }
  return date1Number - date2Number;
}

// eg 29/08/2004 gets converted to 20040829
function monthToComparableNumber(date) {
  if (date === undefined || date === null) {
    return null;
  }
  const yearNumber = parseInt(date.split('/')[2]);
  const monthNumber = parseInt(date.split('/')[1]);
  const dayNumber = parseInt(date.split('/')[0]);
  return (yearNumber * 10000) + (monthNumber * 100) + dayNumber;
}


"""
