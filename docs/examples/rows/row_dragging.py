"""
Row Managed Dragging with options
"""

import dash_ag_grid as dag
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    {'field': 'athlete', 'rowDrag': True},
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
        dcc.Markdown("This grid shows the row managed dragging with options"),
        dbc.Switch(id="switch-animateRows", label="Animate rows"),
        dbc.Switch(id="switch-suppressMove", label="Suppress move when dragging"),
        dbc.Switch(id="switch-multiRow", label="Multi-row dragging"),
        dag.AgGrid(
            id='grid-row-dragging',
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            dashGridOptions={"rowDragManaged": True}
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("grid-row-dragging", "dashGridOptions"),
    Input("switch-animateRows", "value"),
    Input("switch-suppressMove", "value"),
    Input("switch-multiRow", "value"),
    prevent_initial_call=True,
)
def update_dragging_options(animate_on, suppress_move_on, multi_on):
    return {
        "animateRows": animate_on,
        "suppressMoveWhenRowDragging": suppress_move_on,
        "rowDragMultiRow": multi_on,
        "rowSelection": "multiple" if multi_on else "single",
    }


if __name__ == "__main__":
    app.run_server(debug=True)
