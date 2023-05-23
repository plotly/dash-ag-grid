"""
Entire Row Dragging
"""

import dash_ag_grid as dag
from dash import Dash, dcc, html
import pandas as pd

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    {'field': 'athlete'},
    {'field': 'country'},
    {'field': 'year', 'width': 100},
    {'field': 'date'},
    {'field': 'sport'},
    {'field': 'gold'},
    {'field': 'silver'},
    {'field': 'bronze'},
]

defaultColDef = {'width': 170, "sortable": True, "filter": True}

app.layout = html.Div(
    [
        dcc.Markdown("This grid shows the row dragging on entire row"),
        dag.AgGrid(
            id='grid-row-dragging-entire-row',
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            dashGridOptions={
                "rowDragManaged": True,
                "animateRows": True,
                "rowDragMultiRow": True,
                "rowSelection": "multiple" ,
                "rowDragEntireRow": True,
            }
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)
