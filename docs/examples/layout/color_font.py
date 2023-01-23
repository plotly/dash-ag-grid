"""
Colors and fonts
"""
import dash

import dash_ag_grid as dag
from dash import Dash, html, dcc


app = Dash(__name__)

columnDefs = [
    {"field": "make"},
    {"field": "model"},
    {"field": "price"},
]


rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxster", "price": 72000},
    {"make": "BMW", "model": "M50", "price": 60000},
    {"make": "Aston Martin", "model": "DBX", "price": 190000},
]


app.layout = html.Div(
    [
        dcc.Markdown("Styling fonts and colors"),
        dag.AgGrid(
            className="ag-theme-alpine color-fonts ",
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            rowSelection="single",
            defaultColDef={"sortable": True},
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)

"""
Add the following to a .css file in /assets


.ag-theme-alpine.color-fonts {
    --ag-foreground-color: rgb(126, 46, 132);
    --ag-background-color: rgb(249, 245, 227);
    --ag-header-foreground-color: rgb(204, 245, 172);
    --ag-header-background-color: rgb(209, 64, 129);
    --ag-odd-row-background-color: rgb(0, 0, 0, 0.03);
    --ag-header-column-resize-handle-color: rgb(126, 46, 132);

    --ag-font-size: 17px;
    --ag-font-family: monospace;
}


"""
