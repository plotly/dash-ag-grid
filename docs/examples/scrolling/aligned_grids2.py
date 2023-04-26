# Aligned grids - grid as a footer

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
    {"field": "athlete", "width": 200},
    {"field": "age", "width": 150},
    {"field": "country", "width": 150},
    {"field": "year", "width": 120},
    {"field": "date", "width": 150},
    {"field": "sport", "width": 150},
    # in the total col, we have a value getter, which usually means we don't need to provide a field
    # however the master/slave depends on the column id (which is derived from the field if provided) in
    #  order ot match up the columns
    {
        "headerName": "Total",
        "field": "total",
        "valueGetter": {
            "function": "params.data.gold + params.data.silver + params.data.bronze"
        },
        "width": 200,
    },
    {"field": "gold", "width": 100},
    {"field": "silver", "width": 100},
    {"field": "bronze", "width": 100},
]

bottomData = [
    {
        "athlete": "Total",
        "age": "15 - 61",
        "country": "Ireland",
        "year": "2020",
        "date": "26/11/1970",
        "sport": "Synchronised Riding",
        "gold": 55,
        "silver": 65,
        "bronze": 12,
    },
]


top_grid = dag.AgGrid(
    id="top-grid-footer",
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    defaultColDef=defaultColDef,
    dashGridOptions={
        "alignedGrids": ["bottom-grid-footer"],
        "suppressHorizontalScroll": True,
    },
    suppressDragLeaveHidesColumns=False,
)
bottom_grid = dag.AgGrid(
    id="bottom-grid-footer",
    columnDefs=columnDefs,
    rowData=bottomData,
    defaultColDef=defaultColDef,
    suppressDragLeaveHidesColumns=False,
    dashGridOptions={"headerHeight": 0, "rowStyle": {"fontWeight": "bold"}},
    style={"height": 50},
)

app.layout = html.Div(
    [
        dcc.Markdown(
            "Example of an aligned grid as a footer.  To hide a column, drag it off the grid"
        ),
        top_grid,
        bottom_grid,
    ],
    style={"margin": 20},
)


if __name__ == "__main__":
    app.run_server(debug=True)

#
