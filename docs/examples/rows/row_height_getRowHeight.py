"""
Grid example of getRowHeight Callback
"""
import dash_ag_grid as dag
import pandas as pd
from dash import Dash, html, dcc

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)
df['rowHeight'] = pd.Series([40, 80, 120, 200]*(len(df)//4 + 1))

columnDefs = [
    {'field': 'rowHeight'},
    {"field": "athlete"},
    {"field": "age", 'width': 80},
    {"field": "country"},
    {"field": "year", 'width': 90},
    {"field": "date"},
    {"field": "sport"},
    {"field": "gold"},
    {"field": "silver"},
    {"field": "bronze"},
    {"field": "total"},
]

defaultColDef = {"width": 150, 'sortable': True, 'resizable': True, 'filter': True}

app.layout = html.Div(
    [
        dcc.Markdown("This grid shows row's height set with getRowHeight callback"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            dashGridOptions={"getRowHeight": {"function": "params.data.rowHeight"}}
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)