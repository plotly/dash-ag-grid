import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import pandas as pd
import yfinance as yf
import dash

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY],
           meta_tags=[{'http-equiv': 'content-security-policy',
                       'content': "default-src 'self'; script-src 'self' 'unsafe-inline';"
                                  " style-src https://* 'self' 'unsafe-inline'; "
                                  "font-src data: https://* 'self' 'unsafe-inline';"
                                  "img-src data: https://* 'self'"}],
           external_scripts=['https://cdn.jsdelivr.net/npm/d3-format@3']
           )

equities = {
    "AAPL": "Apple",
    "MSFT": "Microsoft",
    "AMZN": "Amazon",
    "GOOGL": "Alphabet",
    "TSLA": "Tesla",
    "BRK-B": "Berkshire Hathaway",
    "UNH": "United Health Group",
    "JNJ": "Johnson & Johnson",
}


def get_stock_data():
    return yf.download(tickers=list(equities.keys()), period="2y", group_by="ticker")


stock_data = get_stock_data()


def last_close(ticker):
    return stock_data[ticker]["Close"].iloc[-1]


data = {
    "ticker": [ticker for ticker in equities],
    "company": [name for name in equities.values()],
    "quantity": [75, 40, 100, 50, 40, 60, 20, 40],
    "price": [last_close(ticker) for ticker in equities],
}
df = pd.DataFrame(data)

columnDefs = [
    {
        "headerName": "Stock Ticker",
        "field": "ticker",
        "type": "textAligned",
        "filter": True
    },
    {
        "headerName": "Company",
        "field": "company",
        "type": "textAligned",
        "filter": True
    },
    {
        "headerName": "Shares",
        "field": "quantity",
        "editable": True,
    },
    {
        "headerName": "Last Close Price",
        "field": "price",
        "valueFormatter": {"function":"""toFixed(value)"""},
        "cellRenderer": "agAnimateShowChangeCellRenderer",
    },
    {
        "headerName": "Market Value",
        "valueGetter": {"function":"Round(data.price * data.quantity)"},
        "valueFormatter": {"function":"toFixed(value)"},
        "cellRenderer": "agAnimateShowChangeCellRenderer",
    },
]


defaultColDef = {
    "type": ["rightAligned"],
    "filter": "agNumberColumnFilter",
    "resizable": True,
    "sortable": True,
    "editable": False,
    "floatingFilter": True,
}

table = dag.AgGrid(
    id="portfolio-grid",
    className="ag-theme-alpine-dark",
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    columnSize=None,
    defaultColDef=defaultColDef,
    rowSelection="single",
    setRowId='ticker',
    dashGridOptions={'undoRedoCellEditing':True, 'undoRedoCellEditingLimit': 20},
    getRowStyle={
                "styleConditions": [
                    {"condition": "data.quantity > 50", "style": {"color": "orange"}},
                ]
            },

)

header = html.Div("My Portfolio", className="h2 p-2 text-white bg-primary text-center")

app.layout = dbc.Container(
    [
        header,
        dbc.Button('Add Row', id='addRow'),
        dbc.Button('Add BORR', id='addBORR'),
        dbc.Button('Update TSLA', id='updateTSLA'),
        dbc.Button('Sell Selected', id='deleteSelections', color='danger'),
        dbc.Row(dbc.Col(table, className="py-4")),
    ],
)

@app.callback(
    Output('portfolio-grid','enableUpdateRows'),
    Input('updateTSLA','n_clicks')
)
def updateRows(n1):
    ### here we are updating a single row, this can also be many rows linking upon the rowID (ticker)
    if n1:
        return [{'ticker':'TSLA', 'company':'Testing', 'quantity':500, 'price':5.00}]
    return dash.no_update

@app.callback(
    Output('portfolio-grid','enableAddRows'),
    Input('addRow','n_clicks'),
    Input('addBORR','n_clicks')
)
def updateRows(n1,n2):
    if ctx.triggered:
        if ctx.triggered_id == 'addRow':
            ### here we are telling the grid to add a single blank row
            return True
        else:
            ### here we are telling the grid to add a single row with information, this can also be many
            return [{'ticker':'BORR', 'company':'Testing', 'quantity':500, 'price':5.00}]
    return dash.no_update

@app.callback(
    Output('portfolio-grid', 'enableDeleteSelectedRows'),
    Input('deleteSelections', 'n_clicks')
)
def deleteRows(n1):
    ### here we are telling the grid to delete the currently selected rows
    if n1:
        return True
    return dash.no_update

if __name__ == "__main__":
    app.run_server(debug=True, port=12345)