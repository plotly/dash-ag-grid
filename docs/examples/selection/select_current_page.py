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
        "headerCheckboxSelectionCurrentPageOnly": True,
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
dashGridOptions = {"rowSelection": "multiple"}

app.layout = html.Div(
    [
        dcc.Markdown(
            "This grid demonstrates selecting items only on the current page."
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            dashGridOptions={"pagination": True, "paginationAutoPageSize": True},
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)
