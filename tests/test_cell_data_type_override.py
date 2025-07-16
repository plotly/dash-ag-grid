from selenium.webdriver import Keys
from selenium import webdriver
import os

import dash_ag_grid as dag
from dash import Dash, html
from . import utils

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dash.testing.wait import until

def test_cd001_cell_data_types_override(dash_duo):
    os.environ['LANGUAGE'] = 'en-US'
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options) # run this test with a Chrome driver to control the locale via the environment variable set above

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
    try:
        driver.get(dash_duo.server_url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "grid-cell-data-types-override-full-JS"))
        )

        action = utils.ActionChains(driver)

        get_driver_cell = lambda id, row, col: driver.find_element(By.CSS_SELECTOR, f'#{id} .ag-center-cols-container .ag-row:nth-child({row + 1}) .ag-cell:nth-child({col + 1})')

        # same tests for both grids
        for id in ["grid-cell-data-types-override-full-JS", "grid-cell-data-types-override"]:

            until(lambda: get_driver_cell(id, 0, 0).text == "7.5%", timeout=3)

            # test overriden number cell data type
            action.double_click(get_driver_cell(id,0, 0)).perform()
            date_input_element = driver.find_element(By.CSS_SELECTOR,f'#{id} .ag-number-field-input')
            date_input_element.send_keys("0.1" + Keys.ENTER)

            until(lambda: get_driver_cell(id,0, 0).text == "10.0%", timeout=3)

            # test overriden dateString cell data type
            action.double_click(get_driver_cell(id,0, 1)).perform()
            date_input_element = driver.find_element(By.CSS_SELECTOR, f'#{id} .ag-date-field-input')
            date_input_element.send_keys("01172024" + Keys.ENTER)

            until(lambda: get_driver_cell(id,0, 1).text == "17/01/2024", timeout=3)
    finally:
        driver.quit()
