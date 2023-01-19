"""
Working with infinite scroll against a backend database in AG-Grid.
"""

import dash_ag_grid as dag
from dash import Dash, Input, Output, html, no_update
import pandas as pd

app = Dash(__name__)

raw_data = {"id": [], "name": []}
for i in range(0, 10000):
    raw_data["id"].append(i)
    raw_data["name"].append(f"{i*3%5}-{i*7%15}-{i%8}")

df = pd.DataFrame(data=raw_data)

app.layout = html.Div(
    [
        dag.AgGrid(
            id="grid1",
            rowModelType="infinite",
            rowSelection="multiple",
            columnSize="sizeToFit",
            columnDefs=[{"field": "id"}, {"field": "name"}],
            defaultColDef={"sortable": True},
            enableEnterpriseModules=True,
            # The number of rows rendered outside the viewable area the grid renders.
            rowBuffer=0,
            # How many blocks to keep in the store. Default is no limit, so every requested block is kept.
            maxBlocksInCache=1,
        ),
        html.Div(id="output2"),
        html.Div(id="cell-output2"),
        html.Div(id="edit-output2"),
    ]
)


@app.callback(Output("output2", "children"), Input("grid1", "selectionChanged"))
def display_selected_car2(selectionChanged):
    if selectionChanged:
        return [
            f"You selected id {s['id']} and name {s['name']}" for s in selectionChanged
        ]

    return no_update


@app.callback(
    Output("grid1", "getRowsResponse"),
    Input("grid1", "getRowsRequest"),
)
def infinite_scroll(request):
    if request is None:
        return no_update
    partial = df.iloc[request["startRow"] : request["endRow"]]
    return {"rowData": partial.to_dict("records"), "rowCount": len(df.index)}


if __name__ == "__main__":
    app.run_server(debug=False)
