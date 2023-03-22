
"""
Pinning via Column Dragging
"""

import dash
import dash_ag_grid as dag
from dash import dcc, html
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

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
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
