"""

Centering Columns

"""

import dash
import dash_ag_grid as dag
from dash import dcc, html

app = dash.Dash(__name__)

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxster", "price": 72000},
]

columnDefs = [{"field": "make"},  {"field": "model"}, {"field": "price"}]
defaultColDef = {"headerClass": 'center-header', "cellStyle": {'textAlign': 'center'}}

app.layout = html.Div(
    [
        dcc.Markdown("Example of centering columns."),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="responsiveSizeToFit",
            defaultColDef=defaultColDef
        ),
    ],
    style={"margin": 20}
)


if __name__ == "__main__":
    app.run_server(debug=True)

"""
Add the following to the .css file in the assets folder:
-------------

.center-header .ag-header-cell-label {
   justify-content: center;
}
"""