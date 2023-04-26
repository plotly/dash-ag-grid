import dash_ag_grid as dag
import dash
from dash import html, dcc
import pandas as pd


app = dash.Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)


columnDefs = [
    {"field": "country", "rowGroup": True, "enableRowGroup": True},
    {"field": "sport", "pivot": True},
    {"field": "year"},
    {"field": "date"},
    {"field": "gold", "aggFunc": "sum"},
    {"field": "silver", "aggFunc": "sum"},
    {"field": "bronze", "aggFunc": "sum"},
]

defaultColDef = {
    "flex": 1,
    "minWidth": 150,
    "sortable": True,
    "resizable": True,
}


app.layout = html.Div(
    [
        dcc.Markdown("Demonstration of pivot in a Dash AG Grid."),
        dcc.Markdown(
            "The example below shows a simple pivot on the Sport column using the Gold, Silver and Bronze columns for values."
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            dashGridOptions={
                "autoGroupColumnDef": {"minWidth": 250},
                "pivotMode": True,
            },
            defaultColDef=defaultColDef,
            # Pivot groupings is an ag-grid Enterprise feature.
            # A license key should be provided if it is used.
            # License keys can be passed to the `licenseKey` argument of dag.AgGrid
            enableEnterpriseModules=True,
            licenseKey="LICENSE_KEY_HERE",
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
