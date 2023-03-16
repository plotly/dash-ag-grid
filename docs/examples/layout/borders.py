"""
styling borders
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
        dcc.Markdown("Styling borders"),
        dag.AgGrid(
            className="ag-theme-alpine borders",
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


.ag-theme-alpine.borders {
    /* disable all borders */
    --ag-borders: none;
    /* then add back a border between rows */
    --ag-row-border-style: dashed;
    --ag-row-border-width: 5px;
    --ag-row-border-color: rgb(150, 150, 200);
}


"""
