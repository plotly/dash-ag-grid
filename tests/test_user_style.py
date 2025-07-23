from dash import Dash, html, Output, Input, no_update, State, ctx
import dash_ag_grid as dag
import plotly.express as px
import json
import pytest

from . import utils
from dash.testing.wait import until


df = px.data.election()
default_display_cols = ["district_id", "district", "winner"]


def test_us001_user_style(dash_duo):
    app = Dash(__name__)
    columnDefs = [
        {"headerName": "Make", "field": "make"},
        {"headerName": "Model", "field": "model"},
        {"headerName": "Price", "field": "price"},
    ]

    defaultColDef = {
        "initialWidth": 150,
        "sortable": True,
        "resizable": True,
        "filter": True,
    }

    rowData = [
        {"make": "Toyota", "model": "Celica", "price": 35000},
        {"make": "Ford", "model": "Mondeo", "price": 32000},
        {"make": "Porsche", "model": "Boxster", "price": 72000},
    ]

    app.layout = html.Div(
        [
            dag.AgGrid(
                id="grid",
                columnSize="autoSize",
                columnDefs=columnDefs,
                defaultColDef=defaultColDef,
                rowData=rowData,
                style={"height": "500px", "width": "500px"},
                className="ag-theme-alpine",
            ),
        ]
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Toyota")
    until(
        lambda: "height: 500px"
        in dash_duo.find_element("div.ag-theme-alpine").get_attribute("style"),
        timeout=3,
    )
    until(
        lambda: "width: 500px"
        in dash_duo.find_element("div.ag-theme-alpine").get_attribute("style"),
        timeout=3,
    )


@pytest.mark.parametrize("theme", ["alpine", "balham", "material", "quartz"])
def test_us002_legacy_themes(dash_duo, theme):
    app = Dash(
        __name__,
        external_stylesheets=[
            dag.themes.BASE,
            dag.themes.ALPINE,
            dag.themes.BALHAM,
            dag.themes.MATERIAL,
            dag.themes.QUARTZ,
        ],
    )

    columnDefs = [
        {"field": "name", "width": "500"},
    ]

    rowData = [
        {"name": "a"},
        {"name": "b"},
        {"name": "c"},
    ]

    app.layout = html.Div(
        [
            dag.AgGrid(
                id="grid",
                columnDefs=columnDefs,
                rowData=rowData,
                dashGridOptions={"theme": "legacy"},
                className=f"ag-theme-{theme}",
            ),
        ]
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "a")

    # Test that the CSS files are actually loaded and applied

    # Base styles: assert that the grid height is <= 400px because an unstyled
    # grid is very "tall"
    root_wrapper = dash_duo.find_element(".ag-root-wrapper")
    wrapper_height = root_wrapper.size["height"]
    assert wrapper_height <= 400, f"Grid appears to be unstyled: height is too tall ({wrapper_height}px)"

    # Specific themes: Assert that cell headers are bold
    header_cell_text = dash_duo.find_element(".ag-header-cell-text")
    font_weight = header_cell_text.value_of_css_property("font-weight")
    assert font_weight in ["bold", "700", "600", "500",], "Grid appears to be unstyled: cell headers are not bold"
