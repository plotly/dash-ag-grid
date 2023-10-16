"""
Basic column definitions and default column definitions
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs= [
    {'field': 'athlete', 'width': 150, 'suppressSizeToFit': True},
    {'field': 'age', 'width': 50, 'maxWidth': 50},
    {'colId': 'country', 'field': 'country', 'maxWidth': 300},
    {'field': 'year', 'width': 90},
    {'field': 'date', 'width': 110},
    {'field': 'sport', 'width': 110},
    {'field': 'gold', 'width': 100},
    {'field': 'silver', 'width': 100},
    {'field': 'bronze', 'width': 100},
    {'field': 'total', 'width': 100},
]

columnSizeOptions = {
    'defaultMinWidth': 100,
    'columnLimits': [{ 'key': 'country', 'minWidth': 900 }],
}


app.layout = html.Div(
    [
        dcc.Markdown("This grid demonstrates sizeToFit"),

        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            columnSizeOptions=columnSizeOptions,
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
        ),
    ],
    style={"margin": 20},
)


if __name__ == "__main__":
    app.run_server(debug=True)
