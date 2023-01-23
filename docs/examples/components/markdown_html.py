"""
Working with raw html in Markdown component
"""
import dash_ag_grid as dag
import dash
from dash import Input, Output, html, dcc

app = dash.Dash(__name__)

columnDefs = [
    {
        "headerName": "Make",
        "field": "make",
        "sortable": True,
        "cellRenderer": "markdown",
    },
    {"headerName": "Model", "field": "model", "cellRenderer": "markdown"},
    {"headerName": "Link", "field": "link", "cellRenderer": "markdown"},
    {"headerName": "Image", "field": "image", "cellRenderer": "markdown"},
]


columnDefs_allow_html = [
    {
        "headerName": "Make",
        "field": "make",
        "sortable": True,
        "cellRenderer": "markdown",
    },
    {
        "headerName": "Model",
        "field": "model",
        "cellRenderer": "markdown",
        "dangerously_allow_html": True,
    },
    {
        "headerName": "Link",
        "field": "link",
        "cellRenderer": "markdown",
        "dangerously_allow_html": True,
    },
    {"headerName": "Image", "field": "image", "cellRenderer": "markdown"},
]


rowData = [
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
]

raw_html_example1 = html.Div(
    [
        dcc.Markdown(
            "This grid has both Markdown and raw HTML. By default, raw HTML is not rendered."
        ),
        dag.AgGrid(
            id="cell-renderer-table-3",
            columnSize="sizeToFit",
            columnDefs=columnDefs,
            rowData=rowData,
        ),
        html.Hr(),
    ]
)


raw_html_example2 = html.Div(
    [
        dcc.Markdown(
            "This grid has both Markdown and raw HTML. `dangerously_allow_html=True` so the links render"
        ),
        dag.AgGrid(
            id="cell-renderer-table-3",
            columnSize="sizeToFit",
            columnDefs=columnDefs_allow_html,
            rowData=rowData,
            dangerously_allow_html=True,
        ),
    ]
)


app.layout = html.Div(
    [raw_html_example1, raw_html_example2],
    style={"flexWrap": "wrap"},
)


if __name__ == "__main__":
    app.run_server(debug=True)
