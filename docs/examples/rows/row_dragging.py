"""
Row Drag Simple Managed
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)


columnDefs = [
    {"field": "athlete", "rowDrag": True},
    {"field": "country"},
    {"field": "age"},
    {"field": "sport"},
    {"field": "total", "sortable": False},
]

app.layout = html.Div(
    [
        dcc.Markdown("This grid  demonstrates simple managed row drag"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
            dashGridOptions={"rowDragManaged": True}
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)
