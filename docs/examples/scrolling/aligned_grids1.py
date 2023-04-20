# Aligned grids - simple example

import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

app = Dash(__name__)

defaultColDef = {
    "editable": True,
    "sortable": True,
    "resizable": True,
    "filter": True,
    "flex": 1,
    "minWidth": 100,
}

columnDefs = [
    {"field": "athlete"},
    {"field": "age"},
    {"field": "country"},
    {"field": "year"},
    {"field": "date"},
    {"field": "sport"},
    {
        "headerName": "Medals",
        "children": [
            {
                "columnGroupShow": "closed",
                "field": "total",
                "valueGetter": "data.gold + data.silver + data.bronze",
                "width": 200,
            },
            {"columnGroupShow": "open", "field": "gold", "width": 100},
            {"columnGroupShow": "open", "field": "silver", "width": 100},
            {"columnGroupShow": "open", "field": "bronze", "width": 100},
        ],
    },
]


top_grid = dag.AgGrid(
    id="top-grid",
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    defaultColDef=defaultColDef,
    dashGridOptions={"alignedGrids": ["bottom-grid"]},
    suppressDragLeaveHidesColumns=False,
)
bottom_grid = dag.AgGrid(
    id="bottom-grid",
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    defaultColDef=defaultColDef,
    suppressDragLeaveHidesColumns=False,
)

app.layout = html.Div(
    [
        dcc.Markdown(
            "Simple Example of aligned grids.  To hide a column, drag it off the grid"
        ),
        top_grid,
        bottom_grid,
    ],
    style={"margin": 20},
)


if __name__ == "__main__":
    app.run_server(debug=True)
