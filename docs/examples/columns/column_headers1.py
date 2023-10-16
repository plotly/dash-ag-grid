import dash_ag_grid as dag
from dash import Dash, dcc, html
import pandas as pd

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

column_names = ["athlete", "gold", "silver", "bronze", "total", "age", "country", "sport", "year", "date"]

columnDefs = [
    {"headerName": "Athlete Details", "children": [{"field": i} for i in column_names]}
]
defaultColDef = {
    "initialWidth": 100,
    "sortable": True,
    "resizable": True,
    "editable": True,
    "filter": True,
    "floatingFilter": True
}

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration of formatting column headers"),
        dag.AgGrid(
            id="toggle-metals-columns",
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            columnDefs=columnDefs,
            columnSize="sizeToFit",
            dashGridOptions={
                'groupHeaderHeight': 75,
                'headerHeight': 150,
                'floatingFiltersHeight': 50,
            }
        ),
    ],
    className="header1",
)

if __name__ == "__main__":
    app.run_server(debug=True)
