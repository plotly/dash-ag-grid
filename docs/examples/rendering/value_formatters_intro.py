"""
String formatting with basic JavaScript function
"""
import dash_ag_grid as dag
from dash import Dash, html, dcc

app = Dash(__name__)

rowData = [
    dict(account='account a',  balance=522.31, name='Homer', grade="25"),
    dict(account='account b',  balance=1607.9, name='Marge', grade=90),
    dict(account='account c',  balance=-228.41, name='Lisa', grade=100),
]


columnDefs = [
    {
        "field": "account",
        "valueFormatter": {"function": "(params.value).toUpperCase();"},
    },
    {
        "field": "balance",
        "valueFormatter": {"function": "'$' + (params.value)"},
    },
    {
        "field": "name",
        "valueFormatter": {"function": "`Hello ${params.value}!`"},
    },
    {
        "field": "grade",
        "valueFormatter": {"function": "params.value >= 60 ? 'Pass' : 'Fail'"},
    },

]

defaultColDef = {
    "resizable": True,
    "editable": True,
}

app.layout = html.Div(
    [
        dcc.Markdown(
            "This demonstrates some basic string formatting functions"
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
