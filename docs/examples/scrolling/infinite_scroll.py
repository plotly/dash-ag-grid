"""
Working with infinite scroll in AG-Grid.
"""

import dash_ag_grid as dag
from dash import Dash, Input, Output, dcc, html, no_update
import pandas as pd

app = Dash(__name__)

raw_data = {"id": [], "name": []}
for i in range(0, 10000):
    raw_data["id"].append(i)
    raw_data["name"].append(f"{i*3%5}-{i*7%15}-{i%8}")

df = pd.DataFrame(data=raw_data)

app.layout = html.Div(
    [
        dcc.Markdown("Infinite scroll with selectable rows"),
        dag.AgGrid(
            id="infinite-grid",
            columnSize="sizeToFit",
            columnDefs=[{"field": "id"}, {"field": "name"}],
            defaultColDef={"sortable": True},
            rowModelType="infinite",
            dashGridOptions={
                # The number of rows rendered outside the viewable area the grid renders.
                "rowBuffer": 0,
                # How many blocks to keep in the store. Default is no limit, so every requested block is kept.
                "maxBlocksInCache": 1,
                "rowSelection": "multiple",
            },
        ),
        html.Div(id="infinite-output"),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("infinite-output", "children"), Input("infinite-grid", "selectedRows")
)
def display_selected_car2(selectedRows):
    if selectedRows:
        return [f"You selected id {s['id']} and name {s['name']}" for s in selectedRows]
    return no_update


@app.callback(
    Output("infinite-grid", "getRowsResponse"),
    Input("infinite-grid", "getRowsRequest"),
)
def infinite_scroll(request):
    if request is None:
        return no_update
    partial = df.iloc[request["startRow"] : request["endRow"]]
    return {"rowData": partial.to_dict("records"), "rowCount": len(df.index)}


if __name__ == "__main__":
    app.run_server(debug=False)
