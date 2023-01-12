"""
Editing cells in-line.
"""

import dash_ag_grid as dag
import dash
from dash import Input, Output, State, html, dcc, dash_table

app = dash.Dash(__name__)

columnDefs = [
    {
        "headerName": "Make",
        "field": "make",
    },
    {"headerName": "Model", "field": "model"},
    {
        "headerName": "Price",
        "field": "price",
        "editable": True,
    },
]

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxter", "price": 72000},
]


app.layout = html.Div(
    [
        dcc.Markdown(
            'Try editing a value in the "Price" column to see that value reflected in the Dash Table and displayed in plain text.'
        ),
        html.Div(
            [
                dag.AgGrid(
                    id="editable-grid",
                    rowData=rowData,
                    columnDefs=columnDefs,
                    columnSize="sizeToFit",
                    rowSelection="multiple",
                ),
                html.Div(id="stringified-edit"),
                dash_table.DataTable(
                    id="dash-table",
                    columns=[
                        {"name": col["headerName"], "id": col["field"]}
                        for col in columnDefs
                    ],
                    data=rowData,
                ),
            ],
        ),
    ],
    style={"flex-wrap": "wrap"},
)


@app.callback(
    Output("stringified-edit", "children"),
    Input("editable-grid", "cellValueChanged"),
)
def update_text(clickEv):
    if clickEv:
        return "You edited a cell colID {}, rowIndex {}, oldValue was {}, newValue {}".format(
            clickEv["colId"],
            clickEv["rowIndex"],
            clickEv["oldValue"],
            clickEv["newValue"],
        )
    return dash.no_update


@app.callback(
    Output("dash-table", "data"),
    Input("editable-grid", "cellValueChanged"),
    State("editable-grid", "rowData"),
)
def update_table(clickEv, curData):
    if clickEv:
        return curData
    return dash.no_update


if __name__ == "__main__":
    app.run_server(debug=True)
