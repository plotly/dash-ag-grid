"""

Aggrigation with custom functions.  For more information, see:
https://www.ag-grid.com/react-data-grid/aggregation-custom-functions/#example-multi-column-aggregation
"""


import dash
from dash import html, dcc
import requests
import dash_ag_grid as dag

app = dash.Dash(__name__)

data = requests.get(
    r"https://www.ag-grid.com/example-assets/olympic-winners.json"
).json()

columnDefs = [
    # Row group by country and by year is enabled.
    {
        "field": "country",
        "rowGroup": True,
        "hide": True,
        "suppressColumnsToolPanel": True,
    },
    {
        "field": "sport",
        "rowGroup": True,
        "hide": True,
        "suppressColumnsToolPanel": True,
    },
    {
        "field": "year",
        "pivot": True,
        "hide": True,
        "suppressColumnsToolPanel": True,
    },
    {"field": "gold", "sortable": True, "filter": True, "aggFunc": "sum"},
    {"field": "silver", "sortable": True, "filter": True, "aggFunc": "sum"},
    {
        "headerName": "ratio",
        "colId": "goldSilverRatio",
        "aggFunc": {"function": "ratioAggFunc(params)"},
        "valueGetter": {"function": "ratioValueGetter(params)"},
        "valueFormatter": {"function": "ratioFormatter(params)"},
    },
]

app.layout = html.Div(
    [
        dcc.Markdown(
            "This is an example of how to calculate a ratio using values from multiple columns."
        ),
        dag.AgGrid(
            enableEnterpriseModules=True,
            columnDefs=columnDefs,
            rowData=data,
            defaultColDef={"resizable":True},
            dashGridOptions={
                "rowSelection": "multiple",
                "suppressAggFuncInHeader": True,
            }
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=False)


"""
Place the following into the `dashAgGridFunctions.js file in the assets folder
----------

var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.ratioValueGetter = function (params) {
  if (!(params.node && params.node.group)) {
    // no need to handle group levels - calculated in the 'ratioAggFunc'
    return createValueObject(params.data.gold, params.data.silver);
  }
}
dagfuncs.ratioAggFunc = function (params) {
  let goldSum = 0;
  let silverSum = 0;
  params.values.forEach((value) => {
    if (value && value.gold) {
      goldSum += value.gold;
    }
    if (value && value.silver) {
      silverSum += value.silver;
    }
  });
  return createValueObject(goldSum, silverSum);
}

function createValueObject(gold, silver) {
  return {
    gold: gold,
    silver: silver,
    toString: () => `${gold && silver ? gold / silver : 0}`,
  };
}

dagfuncs.ratioFormatter = function (params) {
  if (!params.value || params.value === 0) return '';
  return '' + Math.round(params.value * 100) / 100;
}

"""
