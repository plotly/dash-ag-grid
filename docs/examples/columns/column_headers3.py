"""
Header Tooltips
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
    {"field": "athlete", "headerTooltip": "The full Name of the athlete"},
    {
        "field": "age",
        "headerTooltip": "The number of Years since the athlete was born",
        "initialWidth": 120,
    },
    {"field": "country", "headerTooltip": "The Country the athlete was born in"},
    {"field": "sport", "headerTooltip": "The Sport the athlete participated in"},
    {
        "field": "total",
        "headerTooltip": "The Total number of medals won by the athlete",
    },
]

defaultColDef = {
    "resizable": True,
    "initialWidth": 200,
}

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration auto header height."),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=data,
            defaultColDef=defaultColDef,
            dashGridOptions={"tooltipShowDelay":500,}
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
