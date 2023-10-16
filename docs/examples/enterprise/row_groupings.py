"""
How to group rows in AG-grid.
"""

import dash_ag_grid as dag
import dash
from dash import html, dcc
import pandas as pd


app = dash.Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    # Row group by country and by year is enabled.
    {"field": "country", "sortable": True, "filter": True, "rowGroup": True},
    {"field": "year", "sortable": True, "filter": True, "rowGroup": True},
    {"field": "athlete", "sortable": True, "filter": True},
    {"field": "age", "sortable": True, "filter": True},
    {"field": "date", "sortable": True, "filter": True},
    {"field": "sport", "sortable": True, "filter": True},
    {"field": "total", "sortable": True, "filter": True},
]

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration of row groupings in a Dash AG Grid."),
        dcc.Markdown("This grid groups first by country and then by year."),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            dashGridOptions={"rowSelection": "multiple"},
            defaultColDef=dict(
                resizable=True,
            ),
            id="grouped-grid",
            # Row groupings is an ag-grid Enterprise feature.
            # A license key should be provided if it is used.
            # License keys can be passed to the `licenseKey` argument of dag.AgGrid
            enableEnterpriseModules=True,
            licenseKey="LICENSE_KEY_HERE",
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
