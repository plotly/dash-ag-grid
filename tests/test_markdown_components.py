"""
Working with raw html in Markdown component
"""
import dash_ag_grid as dag
import dash
from dash import html, dcc
from . import utils
from dash.testing.wait import until


def test_mc001_markdown_components(dash_duo):
    app = dash.Dash(__name__)

    columnDefs = [
        {
            "headerName": "Make",
            "field": "make",
            "sortable": True,
            "cellRenderer": "markdown",
        },
        {"headerName": "Model", "field": "model", "cellRenderer": "markdown"},
        {
            "headerName": "Link",
            "field": "link",
            "cellRenderer": "markdown",
            "linkTarget": "_blank",
        },
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
        },
        {
            "headerName": "Link",
            "field": "link",
            "cellRenderer": "markdown",
            "linkTarget": "_self",
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
            "model": "<b>Boxster</b> in HTML bold",
            "link": "[Example](#)",
            "image": "![alt text: rain](https://www.ag-grid.com/example-assets/weather/rain.png)",
        },
    ]

    rowData2 = [{k: row[k] for k in row if k != "link"} for row in rowData]

    raw_html_example1 = html.Div(
        [
            dcc.Markdown(
                "This grid has both Markdown and raw HTML. By default, raw HTML is not rendered."
            ),
            dag.AgGrid(
                id="not_dangerous",
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
                "This grid has both Markdown and raw HTML. `dangerously_allow_code=True` so the links render"
            ),
            dag.AgGrid(
                id="dangerous",
                columnSize="sizeToFit",
                columnDefs=columnDefs_allow_html,
                rowData=rowData,
                dangerously_allow_code=True,
            ),
        ]
    )

    raw_html_example3 = html.Div(
        [
            dcc.Markdown(
                "This grid has both Markdown and raw HTML. By default, raw HTML is not rendered."
            ),
            dag.AgGrid(
                id="not_dangerous2",
                columnSize="sizeToFit",
                columnDefs=columnDefs,
                rowData=rowData2,
            ),
            html.Hr(),
        ]
    )

    app.layout = html.Div(
        [raw_html_example1, raw_html_example2, raw_html_example3],
        style={"flexWrap": "wrap"},
    )

    dash_duo.start_server(app)

    safe_grid = utils.Grid(dash_duo, "not_dangerous")
    dangerous_grid = utils.Grid(dash_duo, "dangerous")
    safe2_grid = utils.Grid(dash_duo, "not_dangerous2")

    for grid in [safe_grid, dangerous_grid]:
        grid.wait_for_cell_text(0, 0, "Toyota in italics")
        assert (
            grid.get_cell(0, 0).get_attribute("innerHTML")
            == '<div class="agGrid-Markdown"><div><em>Toyota</em> in italics</div></div>'
        )
        grid.wait_for_cell_text(1, 1, "Mondeo")
        grid.wait_for_cell_text(2, 2, "Example")
        assert (
            grid.get_cell(2, 3).get_attribute("innerHTML")
            == '<div class="agGrid-Markdown">'
            '<div><img src="https://www.ag-g'
            'rid.com/example-assets/weather/rain.png" '
            'alt="alt text: rain"></div></div>'
        )

    assert (
        safe_grid.get_cell(2, 2).get_attribute("innerHTML")
        == '<div class="agGrid-Markdown"><div><a href="#" target="_blank">Example</a></div></div>'
    )
    safe_grid.wait_for_cell_text(
        1, 2, '<a href="#" target="_blank">Link to new tab</a>'
    )

    assert (
        dangerous_grid.get_cell(2, 2).get_attribute("innerHTML")
        == '<div class="agGrid-Markdown"><div><a href="#">Example</a></div></div>'
    )
    dangerous_grid.wait_for_cell_text(1, 2, "Link to new tab")
    assert (
        dangerous_grid.get_cell(1, 2).get_attribute("innerHTML")
        == '<div class="agGrid-Markdown"><div><a href="#" target="_blank">Link to new tab</a></div></div>'
    )

    assert safe2_grid.get_cell(0, 2).text == ""
    assert safe2_grid.get_cell(1, 2).text == ""
    assert safe2_grid.get_cell(2, 2).text == ""
