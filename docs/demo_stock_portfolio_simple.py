import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import yfinance as yf

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

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
        "filter": True,
    },
    {
        "headerName": "Company",
        "field": "company",
        "filter": True,
    },
    {
        "headerName": "Shares",
        "field": "quantity",
        "editable": True,
        "type": "rightAligned",
    },
    {
        "headerName": "Last Close Price",
        "field": "price",
        "type": "rightAligned",
        "valueFormatter": "Number(value).toFixed(2)",
        "dangerously_allow_html": True,
        "cellRenderer": "agAnimateShowChangeCellRenderer",
    },
    {
        "headerName": "Market Value",
        "type": "rightAligned",
        "valueGetter": "Number(data.price) * Number(data.quantity)",
        "valueFormatter": "Number(value).toFixed(2)",
        "dangerously_allow_html": True,
        "cellRenderer": "agAnimateShowChangeCellRenderer",
    },
]


defaultColDef = {
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
    columnSize="sizeToFit",
    defaultColDef=defaultColDef,
    dangerously_allow_html=True,
    dashGridOptions={"undoRedoCellEditing": True, "rowSelection": "single"},
)

candlestick = dbc.Card(dcc.Graph(id="candlestick"), body=True)
pie = dbc.Card(dcc.Graph(id="asset-allocation"), body=True)
header = html.Div("My Portfolio", className="h2 p-2 text-white bg-primary text-center")

app.layout = dbc.Container(
    [
        header,
        dbc.Row([dbc.Col(candlestick), dbc.Col(pie)]),
        dbc.Row(dbc.Col(table, className="py-4")),
    ],
)


@app.callback(
    Output("candlestick", "figure"),
    Input("portfolio-grid", "selectionChanged"),
)
def update_candlestick(selected_row):
    if selected_row is None:
        ticker = "AAPL"
        company = "Apple"
    else:
        ticker = selected_row[0]["ticker"]
        company = selected_row[0]["company"]

    dff_ticker_hist = stock_data[ticker].reset_index()
    dff_ticker_hist["Date"] = pd.to_datetime(dff_ticker_hist["Date"])

    fig = go.Figure(
        go.Candlestick(
            x=dff_ticker_hist["Date"],
            open=dff_ticker_hist["Open"],
            high=dff_ticker_hist["High"],
            low=dff_ticker_hist["Low"],
            close=dff_ticker_hist["Close"],
        )
    )
    fig.update_layout(
        title_text=f"{ticker} {company} Daily Price", template="plotly_dark"
    )
    return fig


@app.callback(
    Output("asset-allocation", "figure"),
    Input("portfolio-grid", "cellValueChanged"),
    State("portfolio-grid", "rowData"),
)
def update_portfolio_stats(_, data):
    dff = pd.DataFrame(data)
    dff["total"] = dff["quantity"].astype(float) * dff["price"].astype(float)
    portfolio_total = dff["total"].sum()

    return px.pie(
        dff,
        values="total",
        names="ticker",
        hole=0.3,
        title=f"Portfolio Total ${portfolio_total:,.2f}",
        template="plotly_dark",
    )


if __name__ == "__main__":
    app.run_server(debug=True)
