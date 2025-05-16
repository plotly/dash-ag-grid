
import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import yfinance as yf
import dash_mantine_components as dmc
# need this import for the custom components
from dash_iconify import DashIconify

app = Dash(__name__)

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


def make_sparkline(ticker):
    dff_ticker_hist = stock_data[ticker].reset_index()
    dff_ticker_hist["Date"] = pd.to_datetime(dff_ticker_hist["Date"])
    dff_ticker_hist = dff_ticker_hist.head(30)

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
        showlegend=False,
        yaxis_visible=False,
        yaxis_showticklabels=False,
        xaxis_visible=False,
        xaxis_showticklabels=False,
        margin=dict(l=0, r=0, t=0, b=0),
        template="plotly_dark",
    )
    return fig


data = {
    "ticker": [ticker for ticker in equities],
    "company": [name for name in equities.values()],
    "quantity": [75, 40, 100, 50, 40, 60, 20, 40],
    "price": [last_close(ticker) for ticker in equities],
    "figure": [make_sparkline(ticker) for ticker in equities],
    "buy": ["Buy" for _ in range(len(equities))],
    "sell": ["Sell" for _ in range(len(equities))]
}
df = pd.DataFrame(data)

columnDefs = [
    {
        "headerName": "",
        "field": "buy",
        "cellRenderer": "DMC_Button",
        "cellRendererParams": {
            "variant": "outline",
            "leftIcon": "ic:baseline-shopping-cart",
            "color": "green",
            "radius": "xl",
            "margin": 5,
        },

    },
    {
        "headerName": "",
        "field": "sell",
        "cellRenderer": "DMC_Button",
        "cellRendererParams": {
            "variant": "outline",
            "leftIcon": "ic:baseline-shopping-cart",
            "color": "red",
            "radius": "xl",
            "margin": 5,
        },

    },
    {
        "headerName": "Stock Ticker",
        "field": "ticker",
        "tooltipComponent": "TooltipGraph",
        "tooltipField": "ticker",
    },
    {
        "headerName": "Company",
        "field": "company",
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
        "valueFormatter": {"function": "d3.format('$,.2f')(params.value)"},
        "cellRenderer": "agAnimateShowChangeCellRenderer",
    },
    {
        "headerName": "Market Value",
        "type": "rightAligned",
        "valueGetter": {
            "function": "Number(params.data.price) * Number(params.data.quantity)"
        },
        "valueFormatter": {"function": "d3.format('$,.2f')(params.value)"},
        "cellRenderer": "agAnimateShowChangeCellRenderer",
    },
    {
        "headerName": "Market Price Last 30 Days",
        "field": "figure",
        "cellRenderer": "DCC_Graph",
        "minWidth": 225,
    },
]


defaultColDef = {
    "resizable": True,
    "sortable": True,
    "editable": False,
    "minWidth": 125,
}

grid = dag.AgGrid(
    id="portfolio-grid",
    className="ag-theme-alpine-dark",
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    columnSize="sizeToFit",
    defaultColDef=defaultColDef,
    dashGridOptions={
        "rowSelection": "single",
        "rowHeight": "75",
    },
    style={"height": 750},
)

candlestick = dmc.Card(dcc.Graph(id="candlestick"), withBorder=True)
pie = dmc.Card(dcc.Graph(id="asset-allocation"), withBorder=True)
header = dmc.Title("My Portfolio", order=1, ta="center", p="xl", c="blue")

app.layout = dmc.MantineProvider(
    theme={"colorScheme": "dark"},
    withGlobalClasses=True,
    children=html.Div(
    [
        header,
        dmc.Grid([dmc.GridCol(candlestick, span=6), dmc.GridCol(pie, span=6)]),
        html.Div(grid),
    ], style={"padding":12}
    )
)


@app.callback(
    Output("candlestick", "figure"),
    Input("portfolio-grid", "selectedRows"),
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
    app.run(debug=False)


"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder

---------------
var dagcomponentfuncs = (window.dashAgGridComponentFunctions =
    window.dashAgGridComponentFunctions || {});

dagcomponentfuncs.DMC_Button = function (props) {
    const {setData, data} = props;

    function onClick() {
        setData();
    }
    let leftIcon, rightIcon;
    if (props.leftIcon) {
        leftIcon = React.createElement(window.dash_iconify.DashIconify, {
            icon: props.leftIcon,
        });
    }
    if (props.rightIcon) {
        rightIcon = React.createElement(window.dash_iconify.DashIconify, {
            icon: props.rightIcon,
        });
    }
    return React.createElement(
        window.dash_mantine_components.Button,
        {
            onClick,
            variant: props.variant,
            color: props.color,
            leftIcon,
            rightIcon,
            radius: props.radius,
            style: {
                margin: props.margin,
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
            },
        },
        props.value
    );
};



dagcomponentfuncs.DCC_Graph = function (props) {
    return React.createElement(window.dash_core_components.Graph, {
        figure: props.value,
        style: {height: '100%'},
        config: {displayModeBar: false},
    });
};



"""
