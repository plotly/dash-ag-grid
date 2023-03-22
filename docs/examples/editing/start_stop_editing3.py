"""
The example below demonstrates the focus moving down when Enter is pressed.
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)


columnDefs = [
    {"field": "country"},
    {"field": "year"},
    {"field": "athlete"},
    {"field": "age"},
    {"field": "date"},
    {"field": "sport"},
    {"field": "total"},
]

app.layout = html.Div(
    [
        dcc.Markdown(
            "This grid demonstrates that clicking outside the grid will stop the editing and keep the edits."
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef={"editable": True},
            dashGridOptions={"stopEditingWhenCellsLoseFocus": True},
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=False)
