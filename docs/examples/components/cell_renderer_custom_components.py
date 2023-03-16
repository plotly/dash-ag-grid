"""
styling with custom cell renderer

Note:
Custom components  must be defined in the dashAgGridComponentFunctions.js in assets folder.
See the components in this example at https://github.com/plotly/dash-ag-grid/blob/dev/docs/assets/dashAgGridComponentFunctions.js
"""

import json
import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import dash_bootstrap_components as dbc


actionOptions = ["buy", "sell", "hold"]
data = {
    "ticker": ["AAPL", "MSFT", "AMZN", "GOOGL"],
    "company": ["Apple", "Microsoft", "Amazon", "Alphabet"],
    "price": [154.99, 268.65, 100.47, 96.75],
    "volume": ["Low", "High", "Average", "High"],
    "binary": [False, True, False, False],
    "buy": [{"children": "buy", "className": "btn btn-success", "n_clicks":0} for i in range(4)],
    "sell": [{"children": "sell", "className": "btn btn-danger", "n_clicks":0} for i in range(4)],
    "action": ["buy", "sell", "hold", "buy"],
}
df = pd.DataFrame(data)

columnDefs = [
    {
        "headerName": "Stock Ticker",
        "field": "ticker",
        "cellRenderer": "stockLink",
        "tooltipField": "ticker",
    },
    {"headerName": "Company", "field": "company", "filter": True},
    {
        "headerName": "Last Close Price",
        "type": "rightAligned",
        "field": "price",
        "valueFormatter": {"function": """d3.format("($,.2f")(params.value)"""},
        "editable": True,
    },
    {
        "headerName": "Volume",
        "type": "rightAligned",
        "field": "volume",
        "cellRenderer": "tags",
        "editable": True,
    },
    {
        "field": "binary",
        "cellRenderer": "checkbox",
    },
    {"field": "buy", "cellRenderer": "myCustomButton"},
    {"field": "sell", "cellRenderer": "myCustomButton"},
    {
        "field": "action",
        "cellRenderer": "customDropdown",
        "cellEditorParams": {
            "values": actionOptions,
        },
    },
]


defaultColDef = {
    "filter": "agNumberColumnFilter",
    "resizable": True,
    "sortable": True,
    "editable": False,
    "tooltipComponent": "myCustomTooltip",
}


grid = dag.AgGrid(
    id="custom-components-grid",
    className="ag-theme-alpine-dark",
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    columnSize="sizeToFit",
    defaultColDef=defaultColDef,
    dashGridOptions={"tooltipShowDelay": 100}
)


app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

app.layout = html.Div(
    [
        dcc.Markdown("Example of cellRenderer with custom components"),
        grid,
        html.Div(id="cell-renderer-value-changed"),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("cell-renderer-value-changed", "children"),
    Input("custom-components-grid", "cellRendererData"),
)
def show_change(n):
    return json.dumps(n)


if __name__ == "__main__":
    app.run_server(debug=True)
