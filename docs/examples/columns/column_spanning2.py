import dash_ag_grid as dag
from dash import Dash, html, dcc

app = Dash(__name__)

rowData = [
    {"section": "big-title", "jan": "Warehouse 1"},
    {"section": "quarters", "jan": "Q1", "apr": "Q2"},
    {"jan": 534, "feb": 612, "mar": 243, "apr": 231, "may": 428, "jun": 231},
    {"jan": 765, "feb": 146, "mar": 243, "apr": 231, "may": 428, "jun": 231},
    {"jan": 335, "feb": 122, "mar": 243, "apr": 231, "may": 428, "jun": 231},
    {"jan": 35, "feb": 342, "mar": 243, "apr": 231, "may": 428, "jun": 231},
    {"jan": 568, "feb": 531, "mar": 243, "apr": 231, "may": 428, "jun": 231},
    {"jan": 365, "feb": 361, "mar": 243, "apr": 231, "may": 428, "jun": 231},
    {"section": "big-title", "jan": "Warehouse 2"},
    {"section": "quarters", "jan": "Q1", "apr": "Q2"},
    {"jan": 21, "feb": 12, "mar": 24, "apr": 31, "may": 28, "jun": 31},
    {"jan": 21, "feb": 12, "mar": 24, "apr": 31, "may": 28, "jun": 31},
    {"jan": 21, "feb": 12, "mar": 24, "apr": 31, "may": 28, "jun": 31},
    {"jan": 21, "feb": 12, "mar": 24, "apr": 31, "may": 28, "jun": 31},
    {"jan": 2, "feb": 32, "mar": 24, "apr": 31, "may": 48, "jun": 21},
    {"jan": 21, "feb": 12, "mar": 24, "apr": 31, "may": 28, "jun": 31},
]

cellClassRules = {
    "header-cell": 'params.data.section === "big-title"',
    "quarters-cell": 'params.data.section === "quarters"',
}

columnDefs = [
    {
        "headerName": "Jan",
        "field": "jan",
        "colSpan": {"function": "janColSpan(params)"},
        "cellClassRules": cellClassRules,
    },
    {"headerName": "Feb", "field": "feb"},
    {"headerName": "Mar", "field": "mar"},
    {
        "headerName": "Apr",
        "field": "apr",
        "colSpan": {"function": "aprColSpan(params)"},
        "cellClassRules": cellClassRules,
    },
    {"headerName": "May", "field": "may"},
    {"headerName": "Jun", "field": "jun"},
]


app.layout = html.Div(
    [
        dcc.Markdown("Example: Column Spanning Complex"),
        dag.AgGrid(
            style={"height": 600},
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            defaultColDef={"minWidth": 100},
            dashGridOptions={
                "getRowHeight": {
                    "function": "if (params.data.section === 'big-title') {return 60}"
                }
            },
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=False)


"""
--------------------

Add the following to the .css file in the assets folder:

--------------------

.header-cell {
  background-color: #a6e1ec;
  font-size: 25px;
  font-weight: bold;
  text-align: center;
}
.quarters-cell {
  background-color: #5bc0de;
  font-weight: bold;
}

----------------

Add the following to the dashAgGridFunctions.js file in the assets folder

----------------
var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

function isHeaderRow(params) {
  return params.data.section === 'big-title';
}
function isQuarterRow(params) {
  return params.data.section === 'quarters';
}

dagfuncs.janColSpan = function(params) {
    if (isHeaderRow(params)) {
      return 6;
    } else if (isQuarterRow(params)) {
      return 3;
    } else {
      return 1;
    }
}

dagfuncs.aprColSpan = function(params) {
    if (isQuarterRow(params)) {
      return 3;
    } else {
      return 1;
    }
}

"""