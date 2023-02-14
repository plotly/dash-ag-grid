import dash
from dash import dcc, html, Input, Output, State
import dash_design_kit as ddk
import dash_ag_grid as dag


app = dash.Dash()


app.layout = html.Div(
    [
        ddk.Card(
            dcc.Markdown(
                """This example shows how row groups are remain open if they were originally open when `rowData` is changed in a callback. """
            ),
        ),
        ddk.ControlCard(
            [
                ddk.ControlItem(
                    dcc.Dropdown(
                        options=[
                            {"label": i, "value": i}
                            for i in ["Celica", "Mondeo", "Boxter"]
                        ],
                        id="model-selector",
                        multi=True,
                        value=["Celica", "Mondeo", "Boxter"],
                    ),
                    label="Filter by model",
                ),
                ddk.ControlItem(
                    dcc.RangeSlider(
                        id="year-selector",
                        min=1980,
                        max=2010,
                        step=1,
                        value=[1980, 2040],
                    ),
                    label="Filter by year",
                ),
            ],
            label_position="left",
        ),
        ddk.Card(
            dag.AgGrid(
                id="persist-open-groups",
                columnSize="sizeToFit",
                rowSelection="multiple",
                children=[
                    dag.AgGridColumn(field="make", rowGroup=True),
                    dag.AgGridColumn(
                        field="model",
                    ),
                    dag.AgGridColumn(
                        field="price",
                    ),
                    dag.AgGridColumn(
                        field="year",
                    ),
                ],
                enableEnterpriseModules=True,
                defaultColDef={"filter": True, "sort": True},
            ),
        ),
    ]
)


data = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxter", "price": 72000},
]
new_data = []

for i in range(1980, 2040):
    for row in data:
        new_row = row.copy()
        new_row["year"] = i
        new_data.append(new_row)


@app.callback(
    Output("persist-open-groups", "rowData"),
    Input("model-selector", "value"),
    Input("year-selector", "value"),
)
def generate_data(values, years):
    data = [
        i
        for i in new_data
        if i["model"] in values and i["year"] <= years[1] and i["year"] >= years[0]
    ]

    return data


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
