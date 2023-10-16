"""
AG-grid styling Cells.
"""

import dash_ag_grid as dag
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

cellStyle = {
    "styleConditions": [
        {
            "condition": "params.data.color == 'yellow'",
            "style": {"backgroundColor": "#FFDC00"},
        },
        {
            "condition": "params.data.color == 'green'",
            "style": {"backgroundColor": "#2ECC40"},
        },
        {
            "condition": "params.data.color == 'black'",
            "style": {"backgroundColor": "#111111", "color": "white"},
        },
    ]
}

columnDefs = [
    {"field": "make"},
    {"field": "model"},
    {"field": "price", "cellStyle": cellStyle},
]

rowData = [
    {"color": "black", "make": "Toyota", "model": "Celica", "price": 35000},
    {"color": "green", "make": "Ford", "model": "Mondeo", "price": 32000},
    {"color": "yellow", "make": "Porsche", "model": "Boxster", "price": 72000},
]

grid = dag.AgGrid(
    columnDefs=columnDefs,
    rowData=rowData,
    columnSize="sizeToFit",
)


app.layout = html.Div(
    [html.H5("Styling cells based on value in a different column"), grid],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)
