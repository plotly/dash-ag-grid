"""
Converting date strings to date objects with d3
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)


columnDefs = [
    {"field": "athlete"},
    {"field": "country"},
    {
        "field": "date",
        "filter": "agDateColumnFilter",
        "valueGetter": {"function": "d3.timeParse('%d/%m/%Y')(params.data.date)"},
        "valueFormatter": {"function": "params.data.date"},
    },
]

defaultColDef = {
    "flex": 1,
    "minWidth": 150,
    "filter": True,
    "sortable": True,
}

app.layout = html.Div(
    [
        dcc.Markdown("Example: Sort and filter by date"),
        dag.AgGrid(columnDefs=columnDefs, rowData=df.to_dict("records"), defaultColDef=defaultColDef),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)