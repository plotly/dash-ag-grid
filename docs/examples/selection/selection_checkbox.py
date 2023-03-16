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
    {"field": "athlete", "checkboxSelection": True, "headerCheckboxSelection": True},
    {"field": "age", "maxWidth": 100},
    {"field": "country"},
    {"field": "year", "maxWidth": 120},
    {"field": "date", "minWidth": 150},
    {"field": "sport"},
    {"field": "gold"},
    {"field": "silver"},
    {"field": "bronze"},
    {"field": "total"},
]


defaultColDef = {
    "flex": 1,
    "minWidth": 150,
    "sortable": True,
    "resizable": True,
    "filter": True,
}


app.layout = html.Div(
    [
        dcc.Markdown("This grid has multi-select rows with checkboxes."),
        dag.AgGrid(
            id="selection-checkbox-grid",
            columnDefs=columnDefs,
            rowData=data,
            defaultColDef=defaultColDef,
            dashGridOptions={"rowSelection":"multiple"},
        ),
        html.Div(id="selections-checkbox-output"),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("selections-checkbox-output", "children"),
    Input("selection-checkbox-grid", "selectedRows"),
)
def selected(selected):
    if selected:
        selected_athlete = [s["athlete"] for s in selected]
        return f"You selected athletes: {selected_athlete}"
    return "No selections"


if __name__ == "__main__":
    app.run_server(debug=True)
