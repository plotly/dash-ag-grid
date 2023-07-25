import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
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

def test_rg002_row_groupings(dash_duo):
    app = Dash(__name__)

    data = {
        "Ireland": ["Dublin", "Galway", "Cork"],
        "UK": ["London", "Bristol", "Manchester", "Liverpool"],
        "USA": ["New York", "Boston", "L.A.", "San Fransisco", "Detroit"],
        "MiddleEarth": ["The Shire", "Rohan", "Rivendell", "Mordor"],
        "Midkemia": ["Darkmoor", "Crydee", "Elvandar", "LaMut", "Ylith"],
    }

    rowData = []
    for country, cities in data.items():
        for city in cities:
            rowData.append(
                {
                    "country": country,
                    "type": "Non Fiction"
                    if country in ["Ireland", "UK", "USA"]
                    else "Fiction",
                    "city": city,
                }
            )

    columnDefs = [
        # this column shows just the country group values, but has not group renderer, so there is no expand / collapse functionality
        {
            "headerName": "Country Group - No Renderer",
            "showRowGroup": "country",
        },
        # same as before, but we show all group values, again with no cell renderer
        {
            "headerName": "All Groups - No Renderer",
            "showRowGroup": True,
        },
        # add in a cell renderer
        {
            "headerName": "Group Renderer A",
            "showRowGroup": True,
            "cellRenderer": "agGroupCellRenderer",
        },
        # add in a field
        {
            "headerName": "Group Renderer B",
            "field": "city",
            "showRowGroup": True,
            "cellRenderer": "agGroupCellRenderer",
        },
        # add in a cell renderer params
        {
            "headerName": "Group Renderer C",
            "field": "city",
            "showRowGroup": True,
            "cellRenderer": "agGroupCellRenderer",
            "cellRendererParams": {
                "suppressCount": True,
                "checkbox": True,
                'innerRenderer': "SimpleCellRenderer",
                "suppressDoubleClickExpand": True,
                "suppressEnterExpand": True,
            },
        },
        {"headerName": "Type", "field": "type", "rowGroup": True},
        {"headerName": "Country", "field": "country", "rowGroup": True},
        {"headerName": "City", "field": "city", "editable": True},
    ]

    @app.callback(
        Output("grid-virtualRowData-info", "children"),
        Input("group-cell-renderer-example", "cellValueChanged"),
        State("group-cell-renderer-example", "rowData"),
        State("group-cell-renderer-example", "virtualRowData"),
        prevent_initial_call=True
    )
    def update(cell_changed, row_data, virtual_row_data):
        return f"{virtual_row_data[0]}"

    app.layout = html.Div(
        [
            dag.AgGrid(
                id="group-cell-renderer-example",
                columnDefs=columnDefs,
                rowData=rowData,
                columnSize="sizeToFit",
                defaultColDef={"resizable": True},
                enableEnterpriseModules=True,
                dangerously_allow_code=True,
                dashGridOptions={
                    "groupSelectsChildren": True,
                    "groupDisplayType": "custom",
                    "groupDefaultExpanded": 1,
                    "rowSelection": "multiple",
                }
            ),
            html.Div(id="grid-virtualRowData-info"),
        ],
        style={"margin": 20},
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "group-cell-renderer-example")

    grid.wait_for_cell_text(1,1, 'Ireland')

    grid.get_cell_expandable(1,4).click()

    grid.wait_for_cell_text(2, 7, 'Dublin')

    grid.get_cell(2, 7).send_keys("texas")
    grid.get_cell(0, 0).click()
    grid.wait_for_cell_text(2, 7, 'texas')

    until(lambda: dash_duo.find_element('#grid-virtualRowData-info').text
                  == "{'country': 'Ireland', 'type': 'Non Fiction', 'city': 'texas'}",
          timeout=3)