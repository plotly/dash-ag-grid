"""
Column Moving

"""

import dash_ag_grid as dag
from dash import Dash, dcc, html
import pandas as pd

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)
columnDefs = [
    {"field": "athlete", "suppressMovable": True, "cellClass": "suppress-movable-col"},
    {"field": "country"},
    {"field": "year"},
    {"field": "total", "lockPosition": "right", "cellClass": "locked-col"},
    {"field": "age", "lockPosition": "left", "cellClass": "locked-col"},
]

defaultColDef = {
    "lockPinned": True,  # Don't allow pinning for this example
}

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration of suppress movable, lock position and not allowing lock Pin"),
        dag.AgGrid(
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            columnDefs=columnDefs,
            dashGridOptions={"suppressDragLeaveHidesColumns": True}
        ),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
