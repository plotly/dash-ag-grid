"""
Example of using `cellValueChanged` in a callback
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px


app = Dash(__name__)

df = px.data.gapminder()


app.layout = html.Div(
    [
        dcc.Markdown("Example of using `cellValueChanged` in a callback"),
        dag.AgGrid(
            id="editing-grid",
            columnDefs=[{"field": i, "id": i} for i in df.columns],
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef={"editable": True},
        ),
        html.Div(id="editing-grid-output"),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("editing-grid-output", "children"), Input("editing-grid", "cellValueChanged")
)
def update(cell_changed):
    return f"{cell_changed}"


if __name__ == "__main__":
    app.run_server(debug=False)
