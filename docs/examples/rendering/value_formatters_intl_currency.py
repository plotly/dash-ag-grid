
"""
Example of currency formatting using Intl.NumberFormat
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat

"""

import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame(
    {
        "Exchange": ["Canadian Dollar", "Euro", "Japanese Yen", "US Dollar"],
        "CAD": [1, 1.3128, .000945, 1.3105],
        "EUR": [.7618, 1, .0071980, .9983],
        "JPY": [105.84, 138.94, 1, 138.76],
        "USD": [.7630, 1.0016, .00720950, 1],
    }
)
df = df.set_index("Exchange")


columnDefs = [
    {"headerName": "Currency Exchange Table", "field": "Exchange"},
    {"headerName": "Canadian Dollar", "field": "CAD", "valueFormatter": {"function": "CAD(params.value)"}},
    {"headerName": "Euro", "field": "EUR", "valueFormatter": {"function": "EUR(params.value)"}},
    {"headerName": "Japanese Yen", "field": "JPY", "valueFormatter": {"function": "JPY(params.value)"}},
    {"headerName": "US Dollar", "field": "USD", "valueFormatter": {"function": "USD(params.value)"}}
]


app.layout = html.Div(
    [
        dcc.Markdown("Example of custom functions using `Intl.NumberFormat` to format currencies"),

        html.Label("Amount to Exchange"),
        dcc.Input(id="currency-exchange-input", type="number", value=1000),
        dag.AgGrid(
            id="currency-exchange-grid",
            columnDefs=columnDefs,
            columnSize="sizeToFit",
            defaultColDef={"type": "rightAligned"}
        )

    ], style={"margin": 20}
)


@app.callback(
    Output("currency-exchange-grid", "rowData"), Input("currency-exchange-input", "value")
)
def update_table(amount):
    dff = df.multiply(amount, fill_value=0) if amount else df.copy()
    return dff.reset_index().to_dict("records")


if __name__ == "__main__":
    app.run_server(debug=True)


"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder
This will register the functions used to format the currencies.

---------------

var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.Intl = Intl

dagfuncs.EUR = function(number) {
  return Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(number);
}


dagfuncs.JPY = function(number) {
  return Intl.NumberFormat('ja-JP', { style: 'currency', currency: 'JPY' }).format(number)
}


dagfuncs.USD = function(number) {
  return Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(number);
}


dagfuncs.CAD = function(number) {
  return Intl.NumberFormat('en-CA', { style: 'currency', currency: 'CAD', currencyDisplay: 'code' }).format(number);
}



"""
