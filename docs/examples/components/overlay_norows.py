"""
Example of custom no rows overlay component
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
    rowData=[],
    dashGridOptions={
        "noRowsOverlayComponent": "CustomNoRowsOverlay",
        "noRowsOverlayComponentParams": {
            "message": "TaskAPI is not available now, please check again later",
            "fontSize": 12,
        },
    },
)


app = Dash(__name__)

app.layout = html.Div(
    [dcc.Markdown("Example of custom no rows overlay"), grid],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)


"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder

-----------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};


dagcomponentfuncs.CustomNoRowsOverlay = function (props) {
    return React.createElement(
        'div',
        {
            style: {
                border: '1pt solid grey',
                color: 'grey',
                padding: 10,
                fontSize: props.fontSize
            },
        },
        React.createElement('div', {}, props.message),
    );
};


"""
