"""
styling headers
"""


import requests
import dash
import dash_ag_grid as dag
from dash import dcc, html

app = dash.Dash(__name__)

data = requests.get(
    r"https://www.ag-grid.com/example-assets/olympic-winners.json"
).json()


columnDefs = [
    {
        "headerName": "Group 1",
        "children": [
            {"field": "athlete", "minWidth": 170, "resizable": True},
            {"field": "age", "resizable": True},
        ],
    },
    {
        "headerName": "Group 2",
        "children": [
            {"field": "country"},
            {"field": "year"},
            {"field": "date"},
            {"field": "sport"},
            {"field": "gold"},
            {"field": "silver"},
            {"field": "bronze"},
            {"field": "total"},
        ],
    },
]

defaultColDef = {"sortable": True, "filter": True, "editable": True}

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration of header styling."),
        dag.AgGrid(
            className="ag-theme-alpine headers1",
            columnDefs=columnDefs,
            rowData=data,
            defaultColDef=defaultColDef,
        ),
        html.Hr(),
        dcc.Markdown("Demonstration of header column separators and resize handles."),
        dag.AgGrid(
            className="ag-theme-alpine headers2",
            columnDefs=columnDefs,
            rowData=data,
            defaultColDef=defaultColDef,
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)

"""
Add the following to a .css file in /assets

```
/* example 1 */

.ag-theme-alpine.headers1 {
    --ag-header-height: 30px;
    --ag-header-foreground-color: white;
    --ag-header-background-color: black;
    --ag-header-cell-hover-background-color: rgb(80, 40, 140);
    --ag-header-cell-moving-background-color: rgb(80, 40, 140);
}
.ag-theme-alpine.headers1 .ag-header.headers1 {
    font-family: cursive;
}
.ag-theme-alpine.headers1 .ag-header-group-cell.headers1 {
    font-weight: normal;
    font-size: 22px;
}
.ag-theme-alpine.headers1 .ag-header-cell.headers1 {
    font-size: 18px;
}




/* example 2  */

.ag-theme-alpine.headers2 {
    --ag-header-column-separator-display: block;
    --ag-header-column-separator-height: 100%;
    --ag-header-column-separator-width: 2px;
    --ag-header-column-separator-color: purple;

    --ag-header-column-resize-handle-display: block;
    --ag-header-column-resize-handle-height: 25%;
    --ag-header-column-resize-handle-width: 5px;
    --ag-header-column-resize-handle-color: orange;
}

```

"""
