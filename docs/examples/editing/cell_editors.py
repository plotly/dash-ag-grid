import dash_ag_grid as dag
from dash import Dash, html, dcc

app = Dash(__name__)

columnDefs = [
    {
        "headerName": "Make",
        "field": "make",
        "cellEditorPopup": True,
        "cellEditorPopupPosition": "under",
    },
    {
        "headerName": "Model",
        "field": "model",
        "cellEditorPopup": True,
        "cellEditorPopupPosition": "over",
    },
    {"headerName": "Price", "field": "price"},
]

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxster", "price": 72000},
]


app.layout = html.Div(
    [
        dcc.Markdown(
            "In this grid, the __Make__ column has a popup below the cell,  the __Model__ has a popup above the cell, and the __Price__ has the default (in cell) editor."
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            defaultColDef={"editable": True},
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=False)
