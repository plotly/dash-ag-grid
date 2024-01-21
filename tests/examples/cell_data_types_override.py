import dash_ag_grid as dag
from dash import Dash, html

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
        "valueParser": {"function": "valueParser(params)"},
        "valueFormatter": {"function": "valueFormatter(params)"},
        "dataTypeMatcher": {"function": "dataTypeMatcher(params)"},
        "dateParser": {"function": "dateParser(params)"},
        "dateFormatter": {"function": "dateFormatter(params)"},
    },
}

app.layout = html.Div(
    [
        dag.AgGrid(
            id="grid-cell-data-types-custom",
            columnDefs=columnDefs,
            rowData=rowData,
            defaultColDef={"filter": True, "editable": True},
            dashGridOptions={"dataTypeDefinitions": dataTypeDefinitions},
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)


#     dash_duo.driver.implicitly_wait(4000)
#     action = utils.ActionChains(dash_duo.driver)
#     action.double_click(grid.get_cell(0, 0)).perform()
#     until(
#         lambda: "January"
#         in dash_duo.find_element(".ui-datepicker-month").get_attribute("innerText"),
#         timeout=3,
#     )
#     until(
#         lambda: "2023"
#         in dash_duo.find_element(".ui-datepicker-year").get_attribute("innerText"),
#         timeout=3,
#     )
#     until(
#         lambda: "1"
#         in dash_duo.find_element(".ui-state-active").get_attribute("innerText"),
#         timeout=3,
#     )
#     grid.get_cell(2, 1).send_keys("50")
#     grid.get_cell(2, 2).click()
