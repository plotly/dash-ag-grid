import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

columnDefs = [
    {
        "headerName": "Athlete",
        "field": "athlete",
        "minWidth": 180,
        "headerCheckboxSelection": True,
        "headerCheckboxSelectionFilteredOnly": True,
        "checkboxSelection": True,
    },
    {"field": "age"},
    {"field": "country", "minWidth": 150},
    {"field": "year"},
    {"field": "date", "minWidth": 150},
    {"field": "sport", "minWidth": 150},
    {"field": "gold"},
    {"field": "silver"},
    {"field": "bronze"},
    {"field": "total"},
]
defaultColDef = {
    "flex": 1,
    "minWidth": 100,
    "resizable": True,
}


app.layout = html.Div(
    [
        dcc.Markdown(
            "This grid demonstrates the checkbox working on the filtered items only."
        ),
        dcc.Input(id="just-filtered-input", placeholder="filter..."),
        dag.AgGrid(
            id="just-filtered-grid",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            dashGridOptions={"rowSelection": "multiple"},
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("just-filtered-grid", "dashGridOptions"),
    Input("just-filtered-input", "value"),
    State("just-filtered-grid", "dashGridOptions"),
)
def update_filter(filter_value, gridOptions):
    gridOptions["quickFilterText"] = filter_value
    return gridOptions


if __name__ == "__main__":
    app.run_server(debug=True)
