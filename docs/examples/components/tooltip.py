"""
Example of custom tooltip
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd

data = {
    "ticker": ["AAPL", "MSFT", "AMZN", "GOOGL"],
    "company": ["Apple", "Microsoft", "Amazon", "Alphabet"],
    "price": [154.99, 268.65, 100.47, 96.75],
}
df = pd.DataFrame(data)

columnDefs = [
    {
        "headerName": "Stock Ticker",
        "field": "ticker",
        "tooltipField": 'ticker',
        "tooltipComponentParams": { "color": '#d8f0d3' },

    },
    {
        "headerName": "Company",
        "field": "company",
    },
    {
        "headerName": "Last Close Price",
        "field": "price",
        "valueFormatter": {"function": """d3.format("($,.2f")(params.value)"""},
        "editable": True,
    },
]


table = dag.AgGrid(
    id="custom-tooltop",
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    columnSize="sizeToFit",
    defaultColDef={"editable": False,  "tooltipComponent": "myCustomTooltip"},
    tooltipShowDelay=100,
)


app = Dash(__name__)

app.layout = html.Div(
    [dcc.Markdown("Example of custom tooltip"), table],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)


"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder
This will register the myCustomTooltip function.

-----------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};

dagcomponentfuncs.myCustomTooltip = function (props) {
    info = [
    React.createElement('h4',{},props.data.ticker), React.createElement('div',{}, props.data.company),React.createElement('div',{}, props.data.price)]
    return React.createElement('div',{style: {"border":'2pt solid white', 'backgroundColor':props.color || "grey", "padding": 10}}, info);
}
"""
