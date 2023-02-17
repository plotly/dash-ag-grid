"""
Grid example of textwrap and row height
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc
from random import randint


app = Dash(__name__)

columnDefs = [
    {"field": "latin_text", "width": 350, "wrapText": True, "autoHeight":True},
    {"field": "make"},
    {"field": "model"},
    {"field": "price"},
]

latinText =  'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
words = latinText.split()

def random_sentence():
    length = randint(1, len(words))
    return " ".join([words[i] for i in range(length)])


data = [
    {"latin_text": random_sentence(), "make": "Toyota", "model": "Celica", "price": 35000},
    {"latin_text": random_sentence(), "make": "Ford", "model": "Mondeo", "price": 32000},
    {"latin_text": random_sentence(), "make": "Porsche", "model": "Boxster", "price": 72000},
    {"latin_text": random_sentence(), "make": "BMW", "model": "M50", "price": 60000},
    {"latin_text": random_sentence(), "make": "Aston Martin", "model": "DBX", "price": 190000},
]

app.layout = html.Div(
    [
        dcc.Markdown("This grid shows textwrap and auto row height"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=data,
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)
