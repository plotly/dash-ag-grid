"""
Grid example of textwrap and row height
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc


app = Dash(__name__)

columnDefs = [
    {"field": "latin_text", "headerName": "Latin Text", "width": 350, "wrapText": True},
    {"field": "make"},
    {"field": "model"},
    {"field": "price"},
]

latinText =  'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'


data = [
    {"latin_text": latinText, "make": "Toyota", "model": "Celica", "price": 35000},
    {"latin_text": latinText, "make": "Ford", "model": "Mondeo", "price": 32000},
    {"latin_text": latinText, "make": "Porsche", "model": "Boxster", "price": 72000},
    {"latin_text": latinText, "make": "BMW", "model": "M50", "price": 60000},
    {"latin_text": latinText, "make": "Aston Martin", "model": "DBX", "price": 190000},
]

app.layout = html.Div(
    [
        dcc.Markdown("This grid shows textwrap and rows with a fixed row height"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=data,
            dashGridOptions={"rowHeight": 120},
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)
