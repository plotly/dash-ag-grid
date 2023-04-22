"""
styling with custom cell renderer

Note:
Custom components  must be defined in the dashAgGridComponentFunctions.js in assets folder.
"""

import json
import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import dash_bootstrap_components as dbc



data = {
    "ticker": ["AAPL", "MSFT", "AMZN", "GOOGL"],
    "company": ["Apple", "Microsoft", "Amazon", "Alphabet"],
    "price": [154.99, 268.65, 100.47, 96.75],
    "buy": ["Buy" for i in range(4)],
}
df = pd.DataFrame(data)

columnDefs = [
    {
        "headerName": "Stock Ticker",
        "field": "ticker",
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
        "field": "buy",
        "cellRenderer": "Button",
        "cellRendererParams": {"className": "btn btn-success"},
    },
]


defaultColDef = {
    "resizable": True,
    "sortable": True,
    "editable": False,
}


grid = dag.AgGrid(
    id="custom-component-btn-grid",
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    columnSize="autoSize",
    defaultColDef=defaultColDef,
    dashGridOptions={"rowHeight": 48},
)


app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

app.layout = html.Div(
    [
        dcc.Markdown("Example of cellRenderer with custom button component"),
        grid,
        html.Div(id="custom-component-btn-value-changed"),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("custom-component-btn-value-changed", "children"),
    Input("custom-component-btn-grid", "cellRendererData"),
)
def showChange(n):
    return json.dumps(n)


if __name__ == "__main__":
    app.run_server(debug=True)


"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder

---------------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};

dagcomponentfuncs.Button = function (props) {
    const {setData, data} = props;

    function onClick() {
        setData();
    }
    return React.createElement(
        'button',
        {
            onClick: onClick,
            className: props.className,
        },
        props.value
    );
};

"""