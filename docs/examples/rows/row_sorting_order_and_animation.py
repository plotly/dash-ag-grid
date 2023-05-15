"""
Modify the default sorting order and override the sorting order on some columns
Enable row sorting animation
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    {"field": "athlete", "sortingOrder": ['asc', 'desc']},
    {"field": "age", "width": 90, "sortingOrder": ['desc', 'asc']},
    {"field": "country", "sortingOrder": ['desc', None]},
    {"field": "year", "width": 90, "sortingOrder": ['asc']},
    {"field": "date"},
    {"field": "sport"},
    {"field": "gold"},
    {"field": "silver"},
    {"field": "bronze"},
    {"field": "total"},
]
defaultColDef = {
    "width": 170,
    "sortable": True,
}

app.layout = html.Div(
    [
        dcc.Markdown("Example: Sorting Order and Animation"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            dashGridOptions={
                'sortingOrder': ['desc', 'asc', None],
                'animateRows': True
            }
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)
