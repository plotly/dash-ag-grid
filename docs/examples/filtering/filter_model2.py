

"""
Setting filters when the app starts
Getting the filterModel in a callback

"""


import dash_ag_grid as dag
from dash import Dash, Input, Output, html, callback, dcc


app = Dash(__name__)


columnDefs = [
    {"field": "make"},
    {"field": "model"},
    {"field": "price"},
]

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxster", "price": 72000},
]


app.layout = html.Div(
        [
            dcc.Markdown("This grid has a filter set initially"),
            dag.AgGrid(
                id="filter-model-grid2",
                columnSize="sizeToFit",
                rowData=rowData,
                columnDefs=columnDefs,
                defaultColDef={"filter": True, "sortable": True, "floatingFilter": True},
                filterModel={'model': {'filterType': 'text', 'type': 'contains', 'filter': 'cel'}}
            ),
            html.Div(id="filter-model-output2"),
        ]
    )


@callback(
    Output("filter-model-output2", "children"),
    Input("filter-model-grid2", "filterModel"),
)
def get_cur_filter(selection_changed):
    return str(selection_changed)



if __name__ == "__main__":
    app.run_server(debug=True)