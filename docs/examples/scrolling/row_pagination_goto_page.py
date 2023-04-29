"""
AG Grid pagination
"""
import dash
import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import pandas as pd

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)


columnDefs = [
    {"field": "country"},
    {"field": "year"},
    {"field": "athlete"},
    {"field": "age"},
    {"field": "date"},
    {"field": "sport"},
    {"field": "total"},
]

app.layout = html.Div(
    [
        html.Div("Go to page:"),
        dcc.Input(id="goto-page-input", type="number", min=1, value=5),
        dag.AgGrid(
            id="goto-page-grid",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
            dashGridOptions={"pagination": True},
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("goto-page-grid", "paginationGoTo"),
    Input("goto-page-input", "value"),

)
def update_page_size(goto):
    if goto is None:
        return dash.no_update
    # grid page numbers start at zero
    return goto - 1


if __name__ == "__main__":
    app.run_server(debug=True)
