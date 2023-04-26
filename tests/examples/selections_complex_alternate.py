"""
Preserve selections in an ag-grid where the table has a custom key.
"""
import dash
from dash import dcc, html, Input, Output, State
import dash_design_kit as ddk
import dash_ag_grid as dag
import random

app = dash.Dash()

app.layout = html.Div(
    [
        ddk.Card(
            dcc.Markdown(
                """In this example, `make` and `year` represent the unique keys for the data. The selection persistence mechanism built into `dag.AgGrid` is being overridden by the use of `dcc.Store` and dictionary comparisons to make sure selections are preserved as expected when the user refreshes the page or changes any associated filters.

The built-in persistence mechanism here is not sufficient because one column of the dataset changes every time the data is filtered (`rank`).

Try making selections, then filtering up or down and refreshing the page. Notice that `rank` changes but the selections persist.
            """
            ),
        ),
        ddk.ControlCard(
            [
                ddk.ControlItem(
                    dcc.Dropdown(
                        options=[
                            {"label": i, "value": i}
                            for i in ["Celica", "Mondeo", "Boxster"]
                        ],
                        id="model-selector",
                        multi=True,
                        value=["Celica", "Mondeo", "Boxster"],
                    ),
                    label="Filter by model",
                ),
                ddk.ControlItem(
                    dcc.RangeSlider(
                        id="year-selector",
                        min=1980,
                        max=2010,
                        step=1,
                        value=[1990, 2000],
                    ),
                    label="Filter by year",
                ),
                ddk.ControlItem(
                    html.Button(id="generate-data", children="Generate data"),
                ),
            ],
            label_position="left",
        ),
        ddk.Card(
            dag.AgGrid(
                id="selectable-grid-alternate",
                columnSize="sizeToFit",
                rowSelection="multiple",
                children=[
                    dag.AgGridColumn(
                        field="rank",
                    ),
                    dag.AgGridColumn(
                        field="make",
                    ),
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
            ),
        ),
        dcc.Store(storage_type="local", id="store-selections-alternate"),
    ]
)


@app.callback(
    Output("selectable-grid-alternate", "selectionChanged"),
    Output("store-selections-alternate", "data"),
    Input("selectable-grid-alternate", "selectionChanged"),
    Input("selectable-grid-alternate", "rowData"),
    State("store-selections-alternate", "data"),
)
def preserve_selections(
    selection_changed,
    rowData,
    persisted_selections,
):
    if not rowData:
        return dash.no_update, dash.no_update

    ctx = dash.callback_context
    trigger = ctx.triggered[0]["prop_id"]

    if trigger == "selectable-grid-alternate.selectionChanged":
        return dash.no_update, selection_changed

    if not persisted_selections:
        return dash.no_update, dash.no_update

    elif trigger == "selectable-grid-alternate.rowData":
        new_selections = []
        # This nested for loop checks if the selections are still in the grid and if so, grabs the proper rank from the new rowData.
        for i in rowData:
            for j in persisted_selections:
                if i["make"] == j["make"] and i["year"] == j["year"]:
                    new_selections.append(i.copy())

        return new_selections, dash.no_update


#
# This callback can generally be ignored for the purposes of this demo. It serves to generate a dataset and handle filtering.
#
@app.callback(
    Output("selectable-grid-alternate", "rowData"),
    Input("generate-data", "n_clicks"),
    Input("model-selector", "value"),
    Input("year-selector", "value"),
)
def generate_data(n_clicks, values, years):
    data = [
        {"make": "Toyota", "model": "Celica", "price": 35000},
        {"make": "Ford", "model": "Mondeo", "price": 32000},
        {"make": "Porsche", "model": "Boxster", "price": 72000},
    ] * 10
    new_data = []
    for i, row in enumerate(data):
        cur_row = row.copy()
        cur_row["year"] = i + 1980
        cur_row["rank"] = random.randint(0, 150)
        new_data.append(cur_row)

    data = [
        i
        for i in new_data
        if i["model"] in values and i["year"] <= years[1] and i["year"] >= years[0]
    ]

    return data


server = app.server

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
