import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    {"field": "athlete", "filter": False},
    {"field": "country", "filter": False},
    {
        "headerName": "Date",
        "filter": "agDateColumnFilter",
        "valueGetter": {"function": "d3.timeParse('%d/%m/%Y')(params.data.date)"},
        "valueFormatter": {"function": "params.data.date"},
        "filterParams": {
            "browserDatePicker": True,
            "minValidYear": 2000,
            "maxValidYear": 2021,
        },
        "cellStyle": {
            "styleConditions": [
                {
                    "condition": f"params.value < d3.timeParse('%d/%m/%Y')('24/08/2008')",
                    "style": {"color": "red"},
                },
            ],
        },
    },
]

defaultColDef = {
    "flex": 1,
    "minWidth": 150,
    "filter": True,
    "floatingFilter": True,
}

app.layout = html.Div(
    [
        dcc.Markdown("Grid with Conditional Cell Styles for Dates"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)
