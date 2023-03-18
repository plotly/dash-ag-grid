"""
number formatting with d3-format - debugging functions
"""
import dash_ag_grid as dag
from dash import Dash, html, dcc

app = Dash(__name__)

rowData = [
    dict(account="A", quantity=522.31, balance=522.31, rate=0.139),
    dict(account="B", quantity=1607.9, balance=1607.9, rate=0.104444),
    dict(account="C", quantity=-228.41, balance=-228.41, rate=0.19999),
]


columnDefs = [
    {"field": "account"},
    {
        "field": "quantity",
        #  "valueFormatter": {"function": "d3.format(',.1f')(params.value)"},
        "valueFormatter": {
            "function": "log('params.value:', params.value, 'All valueFormatter params:', params)"
        },
    },
    {
        "field": "balance",
        "valueFormatter": {"function": "d3.format('($,.2f')(params.value)"},
    },
    {
        "field": "rate",
        "valueFormatter": {"function": "d3.format(',.1%')(params.value)"},
    },
]

defaultColDef = {
    "type": ["rightAligned"],
    "resizable": True,
    "editable": True,
}

app.layout = html.Div(
    [
        dcc.Markdown(
            "This demonstrates the `log()` function for debugging - open the browser console to see the message"
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            defaultColDef=defaultColDef,
            dashGridOptions={"singleClickEdit": True},
        ),
    ],
    style={"margin": 20},
)


if __name__ == "__main__":
    app.run_server(debug=True)
