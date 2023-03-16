"""
Working with link targets in Markdown component
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
    {"headerName": "Link", "field": "link", "cellRenderer": "markdown", "linkTarget":"_self"},
    {"headerName": "Image", "field": "image", "cellRenderer": "markdown"},
]



columnDefs_target_blank = [
    {
        "headerName": "Make",
        "field": "make",
        "sortable": True,
        "cellRenderer": "markdown",
    },
    {"headerName": "Model", "field": "model", "cellRenderer": "markdown"},
    {"headerName": "Link", "field": "link", "cellRenderer": "markdown", "linkTarget":"_blank"},
    {"headerName": "Image", "field": "image", "cellRenderer": "markdown"},
]

rain =  "![alt text: rain](https://www.ag-grid.com/example-assets/weather/rain.png)"
sun = "![alt text: sun](https://www.ag-grid.com/example-assets/weather/sun.png)"


rowData = [
    {
        "make": "*Toyota* in italics",
        "model": "`code snippet`",
        "link": "**[Bold link](#)**",
        "image": f"{rain} {rain} {rain} {rain} {rain}"
    },
    {
        "make": "**Ford** in bold",
        "model": "Mondeo",
        "link": '<a href="#" target="_blank">Link to new tab</a>',
        "image": f"{sun} {sun} {sun} {sun}"
    },
    {
        "make": "***Porsche*** in both",
        "model": "<b>Boxter</b> in HTML bold",
        "link": "[Example](#)",
        "image": rain,
    },
]

raw_html_example1 = html.Div(
    [
        dcc.Markdown(
            "This grid has both Markdown and raw HTML. LinkTarget='self'"
        ),
        dag.AgGrid(
            columnSize="sizeToFit",
            columnDefs=columnDefs,
            rowData=rowData,
            dangerously_allow_code=True
        ),
        html.Hr(),
    ]
)


raw_html_example2 = html.Div(
    [
        dcc.Markdown(
            "This grid has both Markdown and raw HTML. linkTarget='_blank'"
        ),
        dag.AgGrid(
            columnSize="sizeToFit",
            columnDefs=columnDefs_target_blank,
            rowData=rowData,
            dangerously_allow_code=True,
        ),
    ]
)


app.layout = html.Div(
    [raw_html_example1, raw_html_example2],
    style={"flexWrap": "wrap"},
)


if __name__ == "__main__":
    app.run_server(debug=True)
