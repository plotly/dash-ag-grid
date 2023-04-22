

"""

Getting the virtualRowData after sort and filter

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
    {"make": "Porsche", "model": "Boxter", "price": 72000},
]


app.layout = html.Div(
        [
            dcc.Markdown("Demo of accessing grid data after sort and filter"),
            dag.AgGrid(
                id="virtualRowData-grid",
                columnSize="sizeToFit",
                rowData=rowData,
                columnDefs=columnDefs,
                defaultColDef={"filter": True, "sortable": True, "floatingFilter": True},
            ),
            html.Div(id="virtualRowData-output"),
        ]
    )


@callback(
    Output("virtualRowData-output", "children"),
    Input("virtualRowData-grid", "virtualRowData"),
)
def get_data(virtual_data):
    return str(virtual_data)



if __name__ == "__main__":
    app.run_server(debug=True)