"""
Copy text to clipboard like a regular table
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")

app = Dash(__name__)

grid = dag.AgGrid(
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i, "id": i} for i in df.columns],
    columnSize="sizeToFit",
    defaultColDef={"minWidth":125},
    dashGridOptions={"enableCellTextSelection": True, "ensureDomOrder": True},
)

textarea = dcc.Textarea(
    placeholder="paste area",
    style={"width": "100%", "height": 200},
)

markdown = dcc.Markdown(
    "Example of using a regular text selection as if the grid were a regular table"
)

app.layout = html.Div(
    [markdown, grid, textarea],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)
