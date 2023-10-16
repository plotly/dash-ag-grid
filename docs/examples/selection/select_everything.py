import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

columnDefs = [
    {
        "headerName": "Athlete",
        "field": "athlete",
        "minWidth": 180,
    },
    {"field": "age"},
    {"field": "country", "minWidth": 150},
    {"field": "year"},
    {"field": "date", "minWidth": 150},
    {"field": "sport", "minWidth": 150},
    {"field": "gold"},
    {"field": "silver"},
    {"field": "bronze"},
    {"field": "total"},
]
defaultColDef = {
    "flex": 1,
    "minWidth": 100,
    "resizable": True,
    "headerCheckboxSelection": {"function": "isFirstColumn(params)"},
    "checkboxSelection": {"function": "isFirstColumn(params)"},
}


app.layout = html.Div(
    [
        dcc.Markdown(
            "This grid demonstrates selecting everything and not just filter."
        ),
        dcc.Input(id="select-everything-input", placeholder="filter..."),
        dag.AgGrid(
            id="select-everything-grid",
            columnDefs=columnDefs,
            defaultColDef=defaultColDef,
            rowData=df.to_dict("records"),
            dashGridOptions={"rowSelection": "multiple"},
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("select-everything-grid", "dashGridOptions"),
    Input("select-everything-input", "value"),
    State("select-everything-grid", "dashGridOptions"),
)
def update_filter(filter_value, gridOptions):
    gridOptions["quickFilterText"] = filter_value
    return gridOptions


if __name__ == "__main__":
    app.run_server(debug=True)

"""
Place the following in the dashAgGridFunctions.js file in the /assets folder:

----------

var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.isFirstColumn = function(params) {
  var displayedColumns = params.columnApi.getAllDisplayedColumns();
  var thisIsFirstColumn = displayedColumns[0] === params.column;
  return thisIsFirstColumn;
}

"""
