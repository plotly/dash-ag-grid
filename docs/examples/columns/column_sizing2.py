"""
Resizing Groups

"""

import dash_ag_grid as dag
from dash import Dash, dcc, html
import pandas as pd

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    {
        "headerName": "Everything Resizes",
        "children": [
            {"field": "athlete", "headerClass": "resizable-header"},
            {"field": "age", "headerClass": "resizable-header"},
            {"field": "country", "headerClass": "resizable-header"},
        ],
    },
    {
        "headerName": "Only Year Resizes",
        "children": [
            {"field": "year", "headerClass": "resizable-header"},
            {"field": "date", "resizable": False, "headerClass": "fixed-size-header"},
            {"field": "sport", "resizable": False, "headerClass": "fixed-size-header"},
        ],
    },
    {
        "headerName": "Nothing Resizes",
        "children": [
            {"field": "gold", "resizable": False, "headerClass": "fixed-size-header"},
            {"field": "silver", "resizable": False, "headerClass": "fixed-size-header"},
            {"field": "bronze", "resizable": False, "headerClass": "fixed-size-header"},
            {"field": "total", "resizable": False, "headerClass": "fixed-size-header"},
        ],
    },
]

defaultColDef = {
    "width": 150,
    "resizable": True,
}

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration resizing groups."),
        dag.AgGrid(
            id="group-changes",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
