"""
Preserve selections in an ag-grid where the table has a custom key, and where sometimes rows remain the same after updates.
"""
import dash
from dash import dcc, html, Input, Output, State
import dash_design_kit as ddk
import dash_ag_grid as dag

app = dash.Dash()

app.layout = html.Div(
    [
        ddk.Card(
            dcc.Markdown(
                """Note that when making selections, if only selections are made where rank changes, they stick. If only selections are made where rank is consistent, they stick. But if a selection across both categories is made, the rows with new ranks are dropped from selections.
            """
            ),
        ),
        ddk.ControlCard(
            [
                ddk.ControlItem(
                    dcc.Dropdown(
                        options=[{"label": i, "value": i} for i in ["pruned", "all"]],
                        id="picker",
                        value="pruned",
                    ),
                    label="Filter by model",
                ),
            ],
            label_position="left",
        ),
        ddk.Card(
            dag.AgGrid(
                id="selectable-grid-edge-case",
                columnSize="sizeToFit",
                rowSelection="multiple",
                children=[
                    dag.AgGridColumn(field=i) for i in ["rank", "feature", "rating"]
                ],
            ),
        ),
        dcc.Store(storage_type="local", id="store-selections-edge-case", data=[]),
        html.Hr(),
        dcc.Markdown("Selections are persisted when data is updated."),
        html.Button(id="generate-data", children="Generate data"),
        dcc.Dropdown(
            options=[{"label": i, "value": i} for i in ["Celica", "Mondeo", "Boxter"]],
            id="model-picker",
            multi=True,
            value=["Celica", "Mondeo", "Boxter"],
        ),
        dag.AgGrid(
            id="persisting-selectable-grid-callbacks",
            columnSize="sizeToFit",
            rowSelection="multiple",
            persistence=True,
            children=[
                dag.AgGridColumn(
                    field="make",
                ),
                dag.AgGridColumn(
                    field="model",
                ),
                dag.AgGridColumn(
                    field="price",
                ),
            ],
        ),
    ]
)


@app.callback(
    Output("persisting-selectable-grid-callbacks", "rowData"),
    Input("generate-data", "n_clicks"),
    Input("model-picker", "value"),
)
def generate_data(n_clicks, values):
    rowData = [
        {"make": "Toyota", "model": "Celica", "price": 35000},
        {"make": "Ford", "model": "Mondeo", "price": 32000},
        {"make": "Porsche", "model": "Boxter", "price": 72000},
    ]
    if n_clicks:
        return [i for i in rowData if i["model"] in values]


@app.callback(
    Output("selectable-grid-edge-case", "selectionChanged"),
    Output("store-selections-edge-case", "data"),
    Input("selectable-grid-edge-case", "selectionChanged"),
    Input("selectable-grid-edge-case", "rowData"),
    State("store-selections-edge-case", "data"),
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

    if trigger == "selectable-grid-edge-case.selectionChanged":
        return dash.no_update, selection_changed

    elif trigger == "selectable-grid-edge-case.rowData":
        new_selections = []
        # This nested for loop checks if the selections are still in the grid and if so, grabs the proper rank from the new rowData.
        for i in rowData:
            for j in persisted_selections:
                if i["feature"] == j["feature"]:
                    new_selections.append(i.copy())
        return new_selections, dash.no_update


#
# This callback can generally be ignored for the purposes of this demo. It serves to generate a dataset and handle filtering.
#
@app.callback(
    Output("selectable-grid-edge-case", "rowData"),
    Input("picker", "value"),
)
def generate_data(picker):
    pruned = [
        {"rank": 1, "feature": "hello", "rating": 37},
        {"rank": 2, "feature": "goodbye", "rating": 30},
        {"rank": 3, "feature": "see you", "rating": 22},
    ]
    all = [
        {"rank": 1, "feature": "hello", "rating": 37},
        {"rank": 2, "feature": "goodbye", "rating": 30},
        {"rank": 6, "feature": "see you", "rating": 12},
    ]

    if picker == "pruned":
        return pruned
    return all


server = app.server

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
