"""
Header Tooltips
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
    {'field': 'athlete', 'headerTooltip': "The athlete's name"},
    {'field': 'age', 'headerTooltip': "The athlete's age"},
    {'field': 'country'},
    {'field': 'year'},
    {'field': 'date', 'headerTooltip': 'The date of the Olympics'},
    {'field': 'sport', 'headerTooltip': 'The sport the medal was for'},
    {'field': 'gold', 'headerTooltip': 'How many gold medals'},
    {'field': 'silver', 'headerTooltip': 'How many silver medals'},
    {'field': 'bronze', 'headerTooltip': 'How many bronze medals'},
    {'field': 'total', 'headerTooltip': 'The total number of medals'},
]

defaultColDef = {'width': 150}

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration header tooltips."),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            dashGridOptions={"tooltipShowDelay": 500}
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
