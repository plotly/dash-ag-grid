"""
How to group columns in AG-grid.
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc
import requests

app = Dash(__name__)


data = requests.get(
    r"https://www.ag-grid.com/example-assets/olympic-winners.json"
).json()

# grouped column example
# If you want the columns to be grouped, you can include them as children like so:
columnDefs = [
    {
        "headerName": "Group A",
        "children": [{"field": "athlete"}, {"field": "sport"}, {"field": "age"}],
    }
]


app.layout = html.Div(
    [
        dcc.Markdown("This grid has a grouped column"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=data,
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=False)
