"""
Resetting columns with a callback.
"""
import dash_ag_grid as dag
import dash
from dash import Input, Output, html, dcc

app = dash.Dash(__name__)

columnDefs = [
    {"headerName": "Make", "field": "make"},
    {"headerName": "Model", "field": "model"},
    {"headerName": "Price", "field": "price"},
]

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxter", "price": 72000},
]

app.layout = html.Div(
    [
        dcc.Markdown(
            "Click on the reset button below to reset the column state using the internal API of AG Grid."
        ),
        html.Div(
            html.Button(
                "Reset Column State", id="reset-column-state-button", n_clicks=0
            ),
        ),
        dag.AgGrid(
            id="reset-column-state-grid",
            columnSize="sizeToFit",
            columnDefs=columnDefs,
            rowData=rowData,
        ),
    ]
)


@app.callback(
    Output("reset-column-state-grid", "enableResetColumnState"),
    [Input("reset-column-state-button", "n_clicks")],
)
def reset_column_state(n_clicks):
    if n_clicks:
        return True

    return False


if __name__ == "__main__":
    app.run_server(debug=True)
