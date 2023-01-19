# TODO  add css


"""
Pinning via Column Dragging
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
        "headerName": "Athlete (locked as pinned)",
        "field": "athlete",
        "width": 240,
        "pinned": "left",
        "lockPinned": True,
        "cellClass": "lock-pinned",
    },
    {
        "headerName": "Age (locked as not pinnable)",
        "field": "age",
        "width": 260,
        "lockPinned": True,
        "cellClass": "lock-pinned",
    },
    {"field": "country", "width": 150},
    {"field": "year", "width": 90},
    {"field": "date", "width": 150},
    {"field": "sport", "width": 150},
    {"field": "gold"},
    {"field": "silver"},
    {"field": "bronze"},
    {"field": "total"},
]

defaultColDef = {"resizable": True}

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration of Pinning via Column Dragging and lock pin"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=data,
            defaultColDef=defaultColDef,
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
