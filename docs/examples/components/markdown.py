"""
Working with Markdown.
"""
import dash_ag_grid as dag
import dash
from dash import Input, Output, html, dcc

app = dash.Dash(__name__)


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
rain =  "![alt text: rain](https://www.ag-grid.com/example-assets/weather/rain.png)"
sun = "![alt text: sun](https://www.ag-grid.com/example-assets/weather/sun.png)"

rowData = [
    {
        "make": "Toyota",
        "model": "Celica",
        "price": 35000,
        "link": "[Example](#)",
        "image": f"{rain} {rain} {rain} {rain} {rain}"
    },
    {
        "make": "Ford",
        "model": "Mondeo",
        "price": 32000,
        "link": "[Example](#)",
        "image": sun,
    },
    {
        "make": "Porsche",
        "model": "Boxter",
        "price": 72000,
        "link": "[Example](#)",
        "image": rain
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


app.layout = html.Div(
    declarative_api_example,
    style={"flexWrap": "wrap"},
)


if __name__ == "__main__":
    app.run_server(debug=True)
