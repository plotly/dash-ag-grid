"""
Accessing the hidden/displayed state of the columns with Enterprise AG-grid modules.
"""

import dash_ag_grid as dag
import dash
from dash import html, dcc, Input, Output


app = dash.Dash(__name__)

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
        dcc.Markdown(
            "Using the enterprise menu you can select to display or hide columns and column groups. This state can be accessed in a callback using the property columnVisible"
        ),
        dag.AgGrid(
            id="input",
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            defaultColDef=dict(
                resizable=True,
            ),
            enableEnterpriseModules=True,
            licenseKey="LICENSE_KEY_HERE",
            dashGridOptions={"enableRangeSelection": True},
        ),
        html.Div(id="output"),
    ],
)


@app.callback(
    Output("output", "children"),
    Input("input", "columnDefs"),
)
def show_col_definitions(col_defs):
    return str(col_defs)


if __name__ == "__main__":
    app.run_server(debug=True)
