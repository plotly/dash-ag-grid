"""
Column Headers formatting

"""


import requests
import dash_ag_grid as dag
from dash import Dash, dcc, html

app = Dash(__name__)

data = requests.get(
    r"https://www.ag-grid.com/example-assets/olympic-winners.json"
).json()

column_names = [
    "athlete",
    "gold",
    "silver",
    "bronze",
    "total",
    "age",
    "country",
    "sport",
    "year",
    "date",
]

columnDefs = [
    {"headerName": "Athlete Details", "children": [{"field": i} for i in column_names]}
]
defaultColDef = {
    "initialWidth": 100,
    "sortable": True,
    "resizable": True,
    "editable": True,
}


app.layout = html.Div(
    [
        dcc.Markdown("Demonstration of formatting column headers"),
        dag.AgGrid(
            id="toggle-metals-columns",
            rowData=data,
            defaultColDef=defaultColDef,
            columnDefs=columnDefs,
            columnSize="sizeToFit",
            groupHeaderHeight=75,
            headerHeight=150,
        ),
    ],
    className="header1",
)

if __name__ == "__main__":
    app.run_server(debug=True)


"""
Addd the following to a .css file in the assets folder

```
.header1 .ag-header-cell-label {
  /*Necessary to allow for text to grow vertically*/
  height: 100%;
  padding: 0 !important;
}

.header1 .ag-header-group-cell {
  font-size: 50px;
}

.header1 .ag-header-cell-label .ag-header-cell-text {
  /*Force the width corresponding at how much width
    we need once the text is laid out vertically*/
  width: 55px;
  writing-mode: vertical-lr;
  -ms-writing-mode: tb-lr;
  line-height: 2em;
  margin-top: 60px;
}
```

"""
