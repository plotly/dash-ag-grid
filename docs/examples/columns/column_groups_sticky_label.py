"""
Example of sticky headings
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
        "headerName": "Athlete Details",
        "stickyLabel": True,
        "children": [
            {"field": "athlete", "pinned": True, "colId": "athlete"},
            {"field": "country", "colId": "country"},
            {"field": "age", "colId": "age"},
        ],
    },
    {
        "headerName": "Sports Results",
        "stickyLabel": True,
        "openByDefault": True,
        "children": [
            {"field": "sport", "colId": "sport"},
            {"field": "gold", "colId": "gold", "columnGroupShow": "open"},
            {"field": "silver", "colId": "silver", "columnGroupShow": "open"},
            {"field": "bronze", "colId": "bronze", "columnGroupShow": "open"},
            {"field": "total", "colId": "total", "columnGroupShow": "closed"},
        ],
    },
]

defaultColDef = {
    "resizable": True,
    "width": 200,
}

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration sticky label."),
        dag.AgGrid(
            id="my-grid",
            rowData=df.to_dict("records"),
            columnDefs=columnDefs,
            defaultColDef=defaultColDef,
        )
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)
