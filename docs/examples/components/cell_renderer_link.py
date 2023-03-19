"""
styling with custom cell renderer
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd

data = {
    "ticker": ["AAPL", "MSFT", "AMZN", "GOOGL"],
    "company": ["Apple", "Microsoft", "Amazon", "Alphabet"],
    "quantity": [75, 40, 100, 50],
}
df = pd.DataFrame(data)

columnDefs = [
    {
        "headerName": "Stock Ticker",
        "field": "ticker",
        # stockLink function is defined in the dashAgGridComponentFunctions.js in assets folder
        "cellRenderer": "StockLink",
    },
    {
        "headerName": "Company",
        "field": "company",
    },
    {
        "headerName": "Shares",
        "field": "quantity",
        "editable": True,
    },
]


grid = dag.AgGrid(
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    columnSize="sizeToFit",
    defaultColDef={"editable": False},
)


app = Dash(__name__)

app.layout = html.Div(
    [dcc.Markdown("Adding links with cellRenderer"), grid],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)


"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder

-----------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};

dagcomponentfuncs.StockLink = function (props) {
    return React.createElement('a',
    {
        href: 'https://finance.yahoo.com/quote/' + props.value    
    }, props.value)
}
"""
