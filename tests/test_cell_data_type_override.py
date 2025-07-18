from selenium.webdriver import Keys

import dash_ag_grid as dag
from dash import Dash, html
from . import utils

def test_cd001_cell_data_types_override(enforced_locale, dash_duo):
    app = Dash(__name__)

    rowData = [
        {"weight": 0.074657, "date": "01/01/2024"},
        {"weight": 0.06948567, "date": "02/01/2024"},
        {"weight": 0.02730574, "date": "03/01/2024"},
        {"weight": 0.0182345, "date": "04/01/2024"},
    ]

    columnDefs = [
        {"field": "weight", "cellDataType": "percentage"},
        {"field": "date", "cellDataType": "dateString"},
    ]

    # Only for second grid
    dataTypeDefinitions = {
        "percentage": {
            "baseDataType": "number",
            "extendsDataType": "number",
            "valueFormatter": {
                "function": "params.value == null ? '' :  d3.format(',.1%')(params.value)"
            },
        },
        "dateString": {
            "baseDataType": 'dateString',
            "extendsDataType": 'dateString',
            "valueParser": {
                "function": r"params.newValue != null && !!params.newValue.match(/\d{2}\/\d{2}\/\d{4}/) ? params.newValue : null"
            },
            "valueFormatter": {"function": "params.value == null ? '' : params.value"},
            "dataTypeMatcher": {"function": r"params != null && !!params.match(/\d{2}\/\d{2}\/\d{4}/)"},
            "dateParser": {"function": "dateParser(params)"},
            "dateFormatter": {"function": "dateFormatter(params)"},
        },
    }
    app.layout = html.Div(
        [
            dag.AgGrid(
                id="grid-cell-data-types-override-full-JS",
                columnDefs=columnDefs,
                rowData=rowData,
                defaultColDef={"filter": True, "editable": True},
                dashGridOptions={"dataTypeDefinitions": {"function": "dataTypeDefinitions"}},
            ),
            dag.AgGrid(
                id="grid-cell-data-types-override",
                columnDefs=columnDefs,
                rowData=rowData,
                defaultColDef={"filter": True, "editable": True},
                dashGridOptions={"dataTypeDefinitions": dataTypeDefinitions},
            ),
        ],
    )

    dash_duo.start_server(app)

    action = utils.ActionChains(dash_duo.driver)

    # same tests for both grids
    for id in ["grid-cell-data-types-override-full-JS", "grid-cell-data-types-override"]:
        grid = utils.Grid(dash_duo, id)

        # test overriden number cell data type
        action.double_click(grid.get_cell(0, 0)).perform()
        date_input_element = dash_duo.find_element(f'#{grid.id} .ag-number-field-input')
        date_input_element.send_keys("0.1" + Keys.ENTER)

        grid.wait_for_cell_text(0, 0, "10.0%")

        # test overriden dateString cell data type
        action.double_click(grid.get_cell(0, 1)).perform()
        date_input_element = dash_duo.find_element(f'#{grid.id} .ag-date-field-input')
        date_input_element.send_keys("01172024" + Keys.ENTER)

        grid.wait_for_cell_text(0, 1, "17/01/2024")
