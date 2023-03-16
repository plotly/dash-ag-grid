"""
Copy to clipboard with column state
"""
import dash
import pandas as pd
import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px

df = px.data.gapminder()

app = Dash(__name__)

columnDefs = [
    {
        "headerName": "Country",
        "field": "country",
        "checkboxSelection": True,
        "headerCheckboxSelection": True,
    },
    {"headerName": "Continent", "field": "continent"},
    {"headerName": "Year", "field": "year"},
    {"headerName": "Life Expectancy", "field": "lifeExp"},
    {"headerName": "Population", "field": "pop"},
    {"headerName": "GDP per Capita", "field": "gdpPercap"},
]


app.layout = html.Div(
    [
        dcc.Markdown(
            "Example of copying data to the clipboard with column order matching the grid"
        ),
        html.Span("copy selected "),
        dcc.Clipboard(id="clipboard-state", style={"display": "inline-block"}),
        dag.AgGrid(
            id="clipboard-state-grid",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
            dashGridOptions={"rowSelection": "multiple"},
        ),
        dcc.Textarea(
            placeholder="paste area",
            id="clipboard-state-output",
            style={"width": "100%", "height": 200},
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("clipboard-state-grid", "updateColumnState"),
    Input("clipboard-state", "n_clicks"),
    prevent_initial_call=True,
)
def selected(_):
    return True


@app.callback(
    Output("clipboard-state", "content"),
    Input("clipboard-state", "n_clicks"),
    Input("clipboard-state-grid", "columnState"),
    State("clipboard-state-grid", "selectedRows"),
    prevent_initial_call=True,
)
def selected(n, col_state, selected):
    if selected is None:
        return "No selections"
    if col_state is None:
        return dash.no_update

    dff = pd.DataFrame(selected)

    # get current column order in grid
    columns = [row["colId"] for row in col_state]
    dff = dff[columns]

    return dff.to_string()


if __name__ == "__main__":
    app.run_server(debug=True)
