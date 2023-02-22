import dash_ag_grid as dag
from dash import Dash, html, Input, Output
import pandas as pd
import yfinance as yf
from . import utils
import json
import os
import time

def test_cc001_custom_components(dash_duo):

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
        "volume": [last_volume(ticker) for ticker in equities],
        "binary": [False for ticker in equities],
        "buy": [{"children":"buy", "className":"btn btn-success"} for i in equities],
        "sell": [{"children":"sell", "className":"btn btn-danger"} for i in equities],
        "action": [actionOptions[i % 3] for i in range(len(equities))]
    }
    df = pd.DataFrame(data)

    columnDefs = [
        {
            "headerName": "Stock Ticker",
            "field": "ticker",
            "cellRenderer": "stockLink",
            "tooltipField": "ticker",
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
        {
            "headerName": "Volume",
            "type": "rightAligned",
            "field": "volume",
            "cellRenderer": "tags",
            "editable":True
        },
        {
            "field":"binary",
            "cellRenderer": "checkbox",
        },
        {
            "field": "buy",
            "cellRenderer": "myCustomButton"
        },
        {
            "field": "sell",
            "cellRenderer": "myCustomButton"
        },
        {
            "field":"action",
            "cellRenderer": "customDropdown",
            'cellEditorParams': {
                        'values': actionOptions,
                    }
        }
    ]


    defaultColDef = {
        "filter": "agNumberColumnFilter",
        "resizable": True,
        "sortable": True,
        "editable": False,
        "tooltipComponent": "myCustomTooltip"
    }

    df2 = df.copy()
    df2 = df2.to_dict('records')
    df2[0]['quantity'] = 30

    table = dag.AgGrid(
        id="portfolio-grid",
        className="ag-theme-alpine-dark",
        columnDefs=columnDefs,
        rowData=df.to_dict("records"),
        columnSize="sizeToFit",
        defaultColDef=defaultColDef,
    )

    header = html.Div("My Portfolio", className="h2 p-2 text-white bg-primary text-center")

    app.layout = html.Div([table,
            html.Div(id='cellValueChanged')
        ],
    )

    @app.callback(Output('cellValueChanged', 'children'), Input('portfolio-grid','cellValueChanged'), prevent_initial_call=True)
    def showChange(n):
        return json.dumps(n)

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "portfolio-grid")

    grid.wait_for_cell_text(0, 1, "Apple")

    ### testing components
    assert grid.get_cell_html(0,0).strip() == """<a href="https://finance.yahoo.com/quote/AAPL" target="AAPL">AAPL</a>"""
    assert grid.get_cell_html(0,
                              3).strip() == """<div style="width: 100%; height: 100%; padding: 5px; display: flex; justify-content: center; align-items: center;"><div style="background-color: red; border-radius: 15px;">Low</div></div>"""
    assert grid.get_cell_html(0,
                              4).strip() == """<div style="width: 100%; height: 100%; padding: 5px; display: flex; justify-content: center; align-items: center;"><input type="checkbox" style="cursor: pointer;"></div>"""
    assert grid.get_cell_html(0,
                              5).strip() == """<div style="width: 100%; height: 100%; padding: 5px; display: flex; justify-content: center; align-items: center;"><button class="btn btn-success">buy</button></div>"""
    assert grid.get_cell_html(0,
                              6).strip() == """<div style="width: 100%; height: 100%; padding: 5px; display: flex; justify-content: center; align-items: center;"><button class="btn btn-danger">sell</button></div>"""
    assert grid.get_cell_html(0,
                             7).strip() == """<div style="width: 100%; height: 100%; padding: 5px; display: flex; justify-content: center; align-items: center;"><select><option>buy</option><option>sell</option><option>hold</option></select></div>"""
    grid.element_click_cell_button(0,6)
    dash_duo.wait_for_text_to_equal("#cellValueChanged", '{"rowIndex": 0, "nodeId": "0", "data": {"ticker": '
                                                                '"AAPL", "company": "Apple", "price": 154.98500061035'
                                                                '156, "volume": "Low", "binary": false, "buy": {"child'
                                                                'ren": "buy", "className": "btn btn-success"}, "sell":'
                                                                ' {"children": "sell", "className": "btn btn-danger", '
                                                                '"n_clicks": null}, "action": "sell"}, "oldValue": "bu'
                                                                'y", "newValue": "sell", "colId": "action"}')