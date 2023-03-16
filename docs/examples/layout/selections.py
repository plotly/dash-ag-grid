"""
styling selected rows
"""


import dash_ag_grid as dag
from dash import Dash, html, dcc


app = Dash(__name__)

columnDefs = [
    {"field": "make", "checkboxSelection": True, "headerCheckboxSelection": True},
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
        dcc.Markdown("Styling selected rows"),
        dag.AgGrid(
            className="ag-theme-alpine selection",
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            dashGridOptions={"rowSelection": "single"},
            defaultColDef={"sortable": True},
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)

"""
Add the following to a .css file in /assets
.ag-theme-alpine.selection {
    /* bright green, 10% opacity */
    --ag-selected-row-background-color: rgb(0, 255, 0, 0.1);
}

"""
