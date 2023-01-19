"""
Working with images and row menus.
"""
import dash_ag_grid as dag
import dash
from dash import Input, Output, html, dcc

app = dash.Dash(__name__)


row_menu_example = html.Div(
    [
        dcc.Markdown(
            "Custom menus can be added to rows by specifying menu labels & options using the same API as `dcc.Dropdown`. Row metadata and the selected option from a menu are accessible in callbacks."
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

columnDefs = [
    {"headerName": "Make", "field": "make", "sortable": True},
    {"headerName": "Model", "field": "model"},
    {"headerName": "Price", "field": "price"},
    {"headerName": "Link", "field": "link", "cellRenderer": "markdown"},
    {"headerName": "Image", "field": "image", "cellRenderer": "markdown"},
]

"""
Note that here, images are loaded from a remote source. They can also be loaded locally using:
    f"![image alt text]({app.get_asset_url('sun.png')})"
as the cell value.
"""
rowData = [
    {
        "make": "Toyota",
        "model": "Celica",
        "price": 35000,
        "link": "[Example](#)",
        "image": "{0} {0} {0} {0} {0}".format(
            "![alt text: rain](https://www.ag-grid.com/example-assets/weather/rain.png)"
        ),
    },
    {
        "make": "Ford",
        "model": "Mondeo",
        "price": 32000,
        "link": "[Example](#)",
        "image": "![alt text: sun](https://www.ag-grid.com/example-assets/weather/sun.png)",
    },
    {
        "make": "Porsche",
        "model": "Boxter",
        "price": 72000,
        "link": "[Example](#)",
        "image": "![alt text: rain](https://www.ag-grid.com/example-assets/weather/rain.png)",
    },
]

declarative_api_example = html.Div(
    [
        dcc.Markdown(
            "Images, links, and other special cell values can be formatted in Markdown by specifying the `cellRenderer` property to be `'markdown'` in the column definition."
        ),
        dag.AgGrid(
            id="cell-renderer-table-4",
            columnSize="sizeToFit",
            columnDefs=columnDefs,
            rowData=rowData,
        ),
        html.Hr(),
    ]
)

children_api_example = html.Div(
    [
        dcc.Markdown(
            "This example is the same as above but passes column definitions as children of the parent grid."
        ),
        dag.AgGrid(
            id="cell-renderer-table-2",
            columnSize="sizeToFit",
            rowData=rowData,
            children=[
                dag.AgGridColumn(
                    id="column1",
                    field="make",
                    sortable=True,
                ),
                dag.AgGridColumn(id="column2", field="model"),
                dag.AgGridColumn(
                    id="column3",
                    field="price",
                ),
                dag.AgGridColumn(
                    id="column4",
                    field="link",
                    cellRenderer="markdown",
                ),
                dag.AgGridColumn(
                    id="column5",
                    field="image",
                    cellRenderer="markdown",
                ),
            ],
        ),
        html.Hr(),
    ],
    style={"marginTop": "10px"},
)

raw_html_example = html.Div(
    [
        dcc.Markdown(
            "Markdown supports a variety of formats beyond images and links, including raw HTML."
        ),
        dag.AgGrid(
            id="cell-renderer-table-3",
            columnSize="sizeToFit",
            columnDefs=[
                {
                    "headerName": "Make",
                    "field": "make",
                    "sortable": True,
                    "cellRenderer": "markdown",
                },
                {"headerName": "Model", "field": "model", "cellRenderer": "markdown"},
                {"headerName": "Link", "field": "link", "cellRenderer": "markdown"},
                {"headerName": "Image", "field": "image", "cellRenderer": "markdown"},
            ],
            rowData=[
                {
                    "make": "*Toyota* in italics",
                    "model": "`code snippet`",
                    "link": "**[Bold link](#)**",
                    "image": "{0} {0} {0} {0} {0}".format(
                        "![alt text: rain](https://www.ag-grid.com/example-assets/weather/rain.png)"
                    ),
                },
                {
                    "make": "**Ford** in bold",
                    "model": "Mondeo",
                    "link": '<a href="#" target="_blank">Link to new tab</a>',
                    "image": "{0} {0} {0} {0}".format(
                        "![alt text: sun](https://www.ag-grid.com/example-assets/weather/sun.png)"
                    ),
                },
                {
                    "make": "***Porsche*** in both",
                    "model": "<b>Boxter</b> in HTML bold",
                    "link": "[Example](#)",
                    "image": "![alt text: rain](https://www.ag-grid.com/example-assets/weather/rain.png)",
                },
            ],
        ),
        html.Hr(),
    ]
)


app.layout = html.Div(
    [
        row_menu_example,
        declarative_api_example,
        children_api_example,
        raw_html_example,
    ],
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
