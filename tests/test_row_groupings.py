import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
from . import utils
from dash.testing.wait import until
import pandas as pd
import json


def test_rg001_row_groupings(dash_duo):
    app = Dash(__name__)

    df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
    )

    columnDefs = [
        {"field": "country", "enableRowGroup": True, "rowGroup": True, "hide": True},
        {"field": "year", "enableRowGroup": True, "rowGroup": True, "hide": True},
        {"field": "sport", "enableRowGroup": True},
        {"field": "gold"},
        {"field": "silver"},
        {"field": "bronze"},
    ]

    app.layout = html.Div(
        [
            dag.AgGrid(
                columnDefs=columnDefs,
                rowData=df.to_dict("records")[:20],
                columnSize="sizeToFit",
                defaultColDef={"resizable": True, "sortable": True, "filter": True},
                enableEnterpriseModules=True,
                dashGridOptions={"rowGroupPanelShow": "always"},
                id="grid",
            ),
            html.Div(id="columnState"),
        ],
        style={"margin": 20},
    )

    @app.callback(Output("columnState", "children"), Input("grid", "columnState"))
    def columnState(s):
        return json.dumps(s)

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    until(lambda: "United States" in grid.get_cell(0, 0).text, timeout=3)

    ## grouped columns are hidden
    grid.add_column_drop(3)

    until(lambda: "Country" in dash_duo.find_element(".ag-column-drop").text, timeout=3)
    until(lambda: "Year" in dash_duo.find_element(".ag-column-drop").text, timeout=3)
    until(lambda: "Sport" in dash_duo.find_element(".ag-column-drop").text, timeout=3)
    assert ["Country", "Year", "Sport"] == dash_duo.find_element(
        ".ag-column-drop"
    ).text.split("\n")

    grid.drag_column_list(2, 0)
    assert ["Sport", "Country", "Year"] == dash_duo.find_element(
        ".ag-column-drop"
    ).text.split("\n")
    until(lambda: "Swimming" in grid.get_cell(0, 0).text, timeout=3)
    grid.get_cell_expandable(0, 0).click()
    until(lambda: "United States" in grid.get_cell(1, 0).text, timeout=3)
