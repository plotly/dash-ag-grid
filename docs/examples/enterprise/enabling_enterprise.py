"""
Working with Enterprise AG-grid modules.
"""

import dash_ag_grid as dag
import dash
from dash import html, dcc


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
            "To enable Enterprise modules from ag-grid, a grid component must have the `enableEnterpriseModules` parameter set to `True` and a valid key added in the `licenseKey` parameter. This example uses a dummy key. In general, it is recommended to save the key as an environment variable."
        ),
        dcc.Markdown(
            "More information on using ag-grid Enterprise with or without a license key, as well as a listing of which features are restricted only to Enterprise ag-grid, is available on [their website](https://www.ag-grid.com/react-grid/licensing/)."
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
            dashGridOptions={"enableRangeSelection":True}
        ),
    ],
)


if __name__ == "__main__":
    app.run_server(debug=True)
