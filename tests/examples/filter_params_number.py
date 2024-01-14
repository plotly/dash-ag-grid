"""
Example to test filterParams.numberParser and filterParams.numberFormatter functions
"""

import dash_ag_grid as dag
from dash import Dash, html

app = Dash(__name__)

rowData = [{"sale": (i - 3) * 100} for i in range(50)]

columnDefs = [
    {
        "field": "sale",
        "filter": "agNumberColumnFilter",
        "filterParams": {
            "filterOptions": ["greaterThan"],
            "allowedCharPattern": "\\d\\-\\,\\$",
            "numberParser": {"function": "myNumberParser(params)"},
            "numberFormatter": {"function": "myNumberFormatter(params)"},
        },
        "valueFormatter": {
            "function": "d3.formatLocale({'decimal': ',', 'thousands': '.', 'currency': ['$', '']}).format('$,.2f')(params.value)"
        },
    },
]

app.layout = html.Div(
    [
        dag.AgGrid(
            id="filter-number",
            columnDefs=columnDefs,
            defaultColDef={"floatingFilter": True},
            rowData=rowData,
            columnSize="sizeToFit",
        ),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
