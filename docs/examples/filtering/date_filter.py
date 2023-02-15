"""
Simple column filters - number filter and text filter
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc
import requests

app = Dash(__name__)


data = requests.get(
    r"https://www.ag-grid.com/example-assets/olympic-winners.json"
).json()

# basic columns definition with column defaults
columnDefs = [
    {"field": "athlete", "filter": False},
    {"field": "country", "filter": False},
    {
        "headerName": "Date",
        "filter": "agDateColumnFilter",
        "valueGetter": {"function": "d3.timeParse('%d/%m/%Y')(params.data.date)"},
        "valueFormatter": {"function": "params.data.date"},
        "filterParams": {
            "browserDatePicker": True,
            "minValidYear": 2000,
            "maxValidYear": 2021,
        },
    },
]

defaultColDef = {
    "flex": 1,
    "minWidth": 150,
    "filter": True,
    "floatingFilter": True,
}

app.layout = html.Div(
    [
        dcc.Markdown("Date Filter Example"),
        dag.AgGrid(columnDefs=columnDefs, rowData=data, defaultColDef=defaultColDef),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)
