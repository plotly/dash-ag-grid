"""
full row editing
"""


import dash_ag_grid as dag
from dash import Dash, html, dcc

app = Dash(__name__)

columnDefs = [
    {"headerName": "Make", "field": "make"},
    {"headerName": "Model", "field": "model"},
    {"headerName": "Price", "field": "price"},
]

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxster", "price": 72000},
]


app.layout = html.Div(
    [
        dcc.Markdown("This grid has Full Row Editing enabled."),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            defaultColDef={"editable": True},
            dashGridOptions={
                "undoRedoCellEditing": True,
                "undoRedoCellEditingLimit": 20,
                "editType": "fullRow",
            },
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=False)
