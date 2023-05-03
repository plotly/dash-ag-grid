import dash_ag_grid as dag
from dash import Dash, html, dcc

app = Dash(__name__)

columnDefs = [
    {
        "field": "make",
        "checkboxSelection": True,
        "headerCheckboxSelection": True,
    },
    { "field": "model"},
    {"field": "price"},
]

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxster", "price": 72000},
]


app.layout = html.Div(
    [
        dcc.Markdown(
            "Selections support persistence. Note `persistence=True` in this example. Try selecting rows here and then refresh the page:"
        ),
        dag.AgGrid(
            id="persistence-grid",
            rowData=rowData,
            columnSize="responsiveSizeToFit",
            dashGridOptions={"rowSelection": "multiple"},
            persistence=True,
            columnDefs=columnDefs,
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)

