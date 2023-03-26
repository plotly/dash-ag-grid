"""
Conditional editing example
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

cellStyle = {
    "styleConditions": [
        {
            "condition": "params.data.year == 2012",
            "style": {"backgroundColor": "lightBlue"},
        },
    ]
}

columnDefs = [
    {
        "field": "athlete",
        "editable": {"function": "params.data.year == 2012"},
        "cellStyle": cellStyle,
    },
    {"field": "age"},
    {"field": "country"},
    {"field": "year", "maxWidth": 120},
    {"field": "date"},
    {"field": "sport"},
    {"field": "gold"},
    {"field": "silver"},
    {"field": "bronze"},
    {"field": "total"},
]

defaultColDef = {
    "flex": 1,
    "minWidth": 150,
}


app.layout = html.Div(
    [
        dcc.Markdown("Example: Conditional Cell Editing  - Athlete cells are editable on rows where the Year is 2012. "),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)
