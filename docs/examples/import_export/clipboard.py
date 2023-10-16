"""
Copy to clipboard
"""

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
        dcc.Markdown("Example of copying selected rows to the clipboard"),
        html.Span("copy selected "),
        dcc.Clipboard(id="clipboard", style={"display": "inline-block"}),
        dag.AgGrid(
            id="clipboard-grid",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
            dashGridOptions={"rowSelection": "multiple"},
        ),
        dcc.Textarea(
            placeholder="paste area",
            id="clipboard-output",
            style={"width": "100%", "height": 200},
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("clipboard", "content"),
    Input("clipboard", "n_clicks"),
    State("clipboard-grid", "selectedRows"),
)
def selected(n, selected):
    if selected is None:
        return "No selections"
    dff = pd.DataFrame(selected)
    dff = dff[["country", "continent", "year", "lifeExp", "pop", "gdpPercap"]]
    return dff.to_string()


if __name__ == "__main__":
    app.run_server(debug=True)
