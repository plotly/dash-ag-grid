"""
String formatting with basic JavaScript function
"""
import dash_ag_grid as dag
from dash import Dash, html, dcc

app = Dash(__name__)

rowData = [
    dict(account='Salaries',  January=103567.34, Budget=110000),
    dict(account='Rent',  January=8745.00, Budget=7000),
    dict(account='Utilities',  January=-3745.34, Budget=2000),
    dict(account='Bad Debt',  January=2546.78, Budget=3000),
    dict(account='Depreciation',  January=4000.00, Budget=4000),
]


columnDefs = [
    {
        "field": "account",
    },
    {
        "field": "January",
        "valueFormatter": {"function": "MoneyFilna(params.value)"},
        "editable": True
    },
    {
        "field": "Budget",
        "valueFormatter": {"function": "MoneyFilna(params.value)"},
        "editable":True
    },
    {
        "headerName": "Variance",
        "valueGetter": {"function": "(Number(params.data.January) - Number(params.data.Budget)) / Number(params.data.Budget)"},
        "valueFormatter": {"function": "PercentageFilna(params.value)"},

    },
]

defaultColDef = {
    "resizable": True,
    "editable": False,
}

app.layout = html.Div(
    [
        dcc.Markdown(
            """
            This example demonstrates a custom function that replaces NaN with blanks.
            Try entering invalid number in the January or Budget columns.  
            
            -----------
            
            """,

        ),
        html.H4("Expense Summary for January"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            defaultColDef=defaultColDef,
        ),
    ],
    style={"margin": 20},
)


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


dagfuncs.PercentageFilna = function(number, filna="") {
    if (isNaN(number)){
        return filna
    }
    return Intl.NumberFormat("en-US", {style: "percent"}).format(number)
}



dagfuncs.MoneyFilna = function(number, filna="") {
    if (isNaN(number)){
        return filna
    }
    return Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(number);
}


"""
