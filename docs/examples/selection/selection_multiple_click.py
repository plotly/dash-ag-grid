"""
Multiple Row Selection - without check boxes.  Use shift click or ctr click to select
"""
import dash

import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import requests

app = Dash(__name__)


data = requests.get(
    r"https://www.ag-grid.com/example-assets/olympic-winners.json"
).json()


columnDefs = [
    {"field": "athlete"},
    {"field": "age"},
    {"field": "country"},
    {"field": "year"},
    {"field": "date"},
    {"field": "sport"},
    {"field": "gold"},
    {"field": "silver"},
    {"field": "bronze"},
    {"field": "total"},
]

app.layout = html.Div(
    [
        dcc.Markdown("This grid has multi-select rows.  Click to select rows"),
        html.Div(id="selections-multiple-click-output"),
        dag.AgGrid(
            id="selection-multiple-click-grid",
            columnDefs=columnDefs,
            rowData=data,
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
            dashGridOptions={"rowSelection":"multiple", "rowMultiSelectWithClick": True},
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("selections-multiple-click-output", "children"),
    Input("selection-multiple-click-grid", "selectedRows"),
)
def selected(selected):
    if selected:
        selected_athlete = [s["athlete"] for s in selected]
        return f"You selected athletes: {selected_athlete}"
    return "No selections"


if __name__ == "__main__":
    app.run_server(debug=True)
