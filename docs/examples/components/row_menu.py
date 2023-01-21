"""
Working with  row menus.
"""
import dash_ag_grid as dag
import dash
from dash import Input, Output, html, dcc

app = dash.Dash(__name__)


row_menu_example = html.Div(
    [
        dcc.Markdown(
            "Custom menus can be added to rows by specifying menu options with  labels & values. Row metadata and the selected option from a menu are accessible in callbacks."
        ),
        dag.AgGrid(
            id="cell-renderer-table",
            columnSize="sizeToFit",
            columnDefs=[
                {"headerName": "Make", "field": "make", "sortable": True},
                {"headerName": "Model", "field": "model"},
                {"headerName": "Price", "field": "price"},
                {"headerName": "Menu", "field": "menu", "cellRenderer": "rowMenu"},
            ],
            rowData=[
                {
                    "make": "Toyota",
                    "model": "Celica",
                    "price": 35000,
                    "menu": [
                        {"label": "Option 1", "value": 1},
                        {"label": "Option 2", "value": 2},
                        {"label": "Option 3", "value": 3},
                    ],
                },
                {
                    "make": "Ford",
                    "model": "Mondeo",
                    "price": 32000,
                    "menu": [
                        {"label": "Option 4", "value": 4},
                        {"label": "Option 5", "value": 5},
                        {"label": "Option 6", "value": 6},
                    ],
                },
                {
                    "make": "Porsche",
                    "model": "Boxter",
                    "price": 72000,
                    "menu": [
                        {"label": "Option 7", "value": 7},
                        {"label": "Option 8", "value": 8},
                        {"label": "Option 9", "value": 9},
                    ],
                },
            ],
        ),
        html.P(id="click-data"),
        html.Hr(),
    ]
)

app.layout = html.Div(
    row_menu_example,
    style={"flexWrap": "wrap"},
)


@app.callback(
    Output("click-data", "children"),
    Input("cell-renderer-table", "clickData"),
)
def show_click_data(clickData):
    if clickData:
        return "You selected option {} from the row with make {}, model {}, and price {}.".format(
            clickData["value"],
            clickData["data"]["make"],
            clickData["data"]["model"],
            clickData["data"]["price"],
        )
    return "No menu item selected."


if __name__ == "__main__":
    app.run_server(debug=True)
