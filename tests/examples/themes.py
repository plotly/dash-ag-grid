import dash_ag_grid as dag
from dash import Dash, Input, Output, State, dcc, html
import json

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
        dcc.Dropdown(options=[
            {"label": "Quartz", "value": "themeQuartz"},
            {"label": "Balham", "value": "themeBalham"},
            {"label": "Material", "value": "themeMaterial"},
            {"label": "Alpine", "value": "themeAlpine"},
            {"label": "Custom Balham with red accent", "value": '{ "function": "themeBalham.withParams({ accentColor: \'red\' })"}'},
            {"label": "Invalid theme name", "value": "invalidTheme"},
        ], value="", id="themeSelector"),
        dag.AgGrid(
            id="grid",
            columnDefs=columnDefs,
            rowData=rowData,
            defaultColDef={"filter": True, "editable": True},
            dashGridOptions={"dataTypeDefinitions": dataTypeDefinitions},
        ),
    ],
)

@app.callback(
    Output("grid", "dashGridOptions"),
    Input("themeSelector", "value"),
    State("grid", "dashGridOptions"),
    prevent_initial_call=True,
)
def addGrid(selected_theme, dash_grid_options):
    try:
        selected_theme = json.loads(selected_theme)
    except json.JSONDecodeError:
        ...

    if not dash_grid_options:
        dash_grid_options = {}

    dash_grid_options["theme"] = selected_theme
    return dash_grid_options

if __name__ == "__main__":
    app.run(debug=True)
