"""
Column Hover Highlights
"""



import dash
import dash_ag_grid as dag
from dash import dcc, html
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)


columnDefs = [
    {
        "headerName": "Participant",
        "children": [{"field": "athlete"}, {"field": "age"}],
    },
    {
        "headerName": "Details",
        "children": [
            {"field": "country"},
            {"field": "year"},
            {"field": "date"},
            {"field": "sport"},
        ],
    },
]


defaultColDef = {"flex": 1, "resizeable": True}

app.layout = html.Div(
    [
        dcc.Markdown(
            "Demonstration of Rows and Column highlighting. Note if you hover over a header group, all columns in the group will be highlighted."
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            dashGridOptions={"columnHoverHighlight": True},
        ),
        dcc.Markdown(
            "Demonstration no highlighting on Rows or Columns.", style={"marginTop": 40}
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            dashGridOptions={"suppressRowHoverHighlight": True},
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
