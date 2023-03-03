import dash_ag_grid as dag
from dash import Dash, html, Input, Output
import pandas as pd
import yfinance as yf
from . import utils
import json
import os
import time

def test_cr001_custom_row_selectable(dash_duo):

    app = Dash(__name__,
               meta_tags=[{'http-equiv': 'content-security-policy',
                           'content': "default-src 'self'; script-src 'self' 'unsafe-inline';"
                                      " style-src https://* 'self' 'unsafe-inline'; "
                                      "font-src data: https://* 'self' 'unsafe-inline';"
                                      "img-src data: https://* 'self'"}],
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
        return yf.download(tickers=list(equities.keys()), period="30d", interval="1h", group_by="ticker")

    if os.path.exists('./tests/assets/stock_data.csv'):
        stock_data = pd.read_csv('./tests/assets/stock_data.csv')
    else:
        stock_data = get_stock_data()
        stock_data = stock_data.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)
        stock_data.to_csv('./tests/assets/stock_data.csv')


    def last_close(ticker):
        return stock_data[stock_data['Ticker'] == ticker]["Close"].iloc[-1]

    def last_volume(ticker):
        if stock_data[stock_data['Ticker'] == ticker]["Volume"].iloc[-1] >\
                stock_data[stock_data['Ticker'] == ticker]["Volume"].mean():
            return "High"
        elif stock_data[stock_data['Ticker'] == ticker]["Volume"].iloc[-1] <\
                stock_data[stock_data['Ticker'] == ticker]["Volume"].mean():
            return "Low"
        return "Average"

    actionOptions = ['buy', 'sell', 'hold']


    data = {
        "ticker": [ticker for ticker in equities],
        "company": [name for name in equities.values()],
        "price": [last_close(ticker) for ticker in equities],
    }
    df = pd.DataFrame(data)

    columnDefs = [
        {
            "headerName": "Stock Ticker",
            "field": "ticker",
            "headerCheckboxSelection": True,
            "checkboxSelection": True,
            "showDisabledCheckboxes": True,
        },
        {
            "headerName": "Company",
            "field": "company",
            "filter": True
        },
        {
            "headerName": "Last Close Price",
            "type": "rightAligned",
            "field": "price",
            "valueFormatter": {"function":"""d3.format("($,.2f")(params.value)"""},
            "editable":True
        },
    ]


    defaultColDef = {
        "filter": "agNumberColumnFilter",
        "resizable": True,
        "sortable": True,
        "editable": False,
    }

    df2 = df.copy()
    df2 = df2.to_dict('records')
    df2[0]['quantity'] = 30

    table = dag.AgGrid(
        id="grid",
        className="ag-theme-alpine-dark",
        columnDefs=columnDefs,
        rowData=df.to_dict("records"),
        columnSize="sizeToFit",
        defaultColDef=defaultColDef,
        dashGridOptions={'isRowSelectable': {'function': 'params.data.ticker == "AAPL" ? true: false'}},
        rowSelection="multiple"
    )

    app.layout = html.Div([table,
            html.Div(id='cellValueChanged')
        ],
    )

    @app.callback(Output('cellValueChanged', 'children'), Input('portfolio-grid','cellValueChanged'), prevent_initial_call=True)
    def showChange(n):
        return json.dumps(n)

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 1, "Apple")

    assert dash_duo.find_element('#grid [row-index="0"] [aria-colindex="1"] '
                                 '.ag-selection-checkbox input').get_attribute('disabled') == None
    assert dash_duo.find_element('#grid [row-index="1"] [aria-colindex="1"] '
                                 '.ag-selection-checkbox input').get_attribute('disabled')