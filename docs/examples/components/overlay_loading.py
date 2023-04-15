"""
Example of custom loading component
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc


columnDefs = [
    {
        "headerName": "Stock Ticker",
        "field": "ticker",
    },
    {
        "headerName": "Company",
        "field": "company",
    },
    {
        "headerName": "Last Close Price",
        "field": "price",
        "valueFormatter": {"function": """d3.format("($,.2f")(params.value)"""},
    },
]


grid = dag.AgGrid(
    columnDefs=columnDefs,
    columnSize="sizeToFit",
    dashGridOptions={
        "loadingOverlayComponent": "CustomLoadingOverlay",
        "loadingOverlayComponentParams": {
            "loadingMessage": "One moment please...",
            "color": "red",
        },
    },
)


app = Dash(__name__)

app.layout = html.Div(
    [dcc.Markdown("Example of custom loading overlay"), grid],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)


"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder


-----------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};

dagcomponentfuncs.CustomLoadingOverlay = function (props) {
    return React.createElement(
        'div',
        {
            style: {
                border: '1pt solid grey',
                color: props.color || 'grey',
                padding: 10,
            },
        },
        props.loadingMessage
    );
};


"""
