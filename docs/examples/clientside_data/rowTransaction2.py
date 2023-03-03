import dash_ag_grid as dag
from dash import Dash, dcc, html, Input, Output, State, callback

app = Dash(__name__)

random_names = [
    "Jane",
    "Joe",
    "Alex",
    "Victor",
    "Claire",
    "Clark",
    "Tim",
    "Tania",
]

data = [{"id": str(i), "name": random_names[i], "number": str(i)} for i in range(3)]

columnDefs = [
    {"field": "id", "hide": True},
    {"field": "name", "checkboxSelection": True, "headerCheckboxSelection": True},
    {"field": "number"},
]

app.layout = html.Div(
    [
        dcc.Markdown("Example of adding pre-selected rows"),
        html.Button("Add row", id="transactions2-add", n_clicks=2),
        dag.AgGrid(
            id="transactions2-grid",
            columnDefs=columnDefs,
            rowData=data,
            columnSize="sizeToFit",
            rowSelection="multiple",
            getRowId="params.data.id",
        ),
        html.Div(id="transactions2"),
    ],
    style={"margin": 20},
)


@callback(
    Output("transactions2-grid", "rowTransaction"),
    Output("transactions2-grid", "selectedRows"),
    Input("transactions2-add", "n_clicks"),
    State("transactions2-grid", "selectedRows"),
    prevent_initial_call=True,
)
def new_and_selected(n, selected):
    new_row = [{"id": str(n), "name": random_names[n % 8], "number": str(n)}]
    selected = selected + new_row if selected else new_row
    return {"add": new_row}, selected


if __name__ == "__main__":
    app.run_server(debug=True)
