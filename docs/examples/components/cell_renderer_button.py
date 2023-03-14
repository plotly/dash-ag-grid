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


actionOptions = ["buy", "sell", "hold"]
data = {
    "ticker": ["AAPL", "MSFT", "AMZN", "GOOGL"],
    "company": ["Apple", "Microsoft", "Amazon", "Alphabet"],
    "price": [154.99, 268.65, 100.47, 96.75],
    "buy": [{"n_clicks": 0} for i in range(4)],
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
        "cellRenderer": "customButton",
        "cellRendererParams": {"className": "btn btn-success", "children": "Buy"},
    },
]


defaultColDef = {
    "resizable": True,
    "sortable": True,
    "editable": False,
}


table = dag.AgGrid(
    id="custom-component-btn-grid",
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    columnSize="autoSizeAll",
    defaultColDef=defaultColDef,
)


app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

app.layout = html.Div(
    [
        dcc.Markdown("Example of cellRenderer with custom button component"),
        table,
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
This will register the customButton function used in the cellRenderer

---------------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};


dagcomponentfuncs.customButton = function (props) {
    const {setData, data} = props;

    if (!props.value) {
        return React.createElement('button');
    }

    function onClick() {
        setData();
    }

    const id = JSON.stringify({index: props.rowIndex, type: 'customButton'});
    return React.createElement(
        'div',
        {
            style: {
                width: '100%',
                height: '100%',
                padding: '5px',
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
            },
        },
        React.createElement(
            'button',
            {
                onClick: onClick,
                id: props.value.id,
                className: props.className,
            },
            props.children
        )
    );
};


"""