
"""
Column Moving

"""


import requests

import dash_ag_grid as dag
from dash import Dash, dcc, html

app = Dash(__name__)

data = requests.get(
    r"https://www.ag-grid.com/example-assets/olympic-winners.json"
).json()

columnDefs = [
    {
        "field": "athlete",
        "suppressMovable": True,
        "cellClass": "suppress-movable-col",
    },
    {"field": "country"},
    {"field": "year"},
    {"field": "age"},
    {"field": "total", "lockPosition": "right", "cellClass": "locked-col"},
    {"field": "age", "lockPosition": "left", "cellClass": "locked-col"},
]


defaultColDef = {
    "lockPinned": True,  # Dont allow pinning for this example
}


app.layout = html.Div(
    [
        dcc.Markdown("Demonstration of suppress movable and not allowing lock Pin"),
        dag.AgGrid(
            rowData=data,
            defaultColDef=defaultColDef,
            columnDefs=columnDefs,
            dashGridOptions={"suppressDragLeaveHidesColumns": True}
        ),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
