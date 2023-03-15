"""
Enable column editing on all columns
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

df = px.data.medals_wide()


app.layout = html.Div(
    [
        dcc.Markdown("This grid has editing enabled on all columns"),
        dag.AgGrid(
            columnDefs=[{"field": i, "id": i} for i in df.columns],
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef={"editable": True},
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=False)
