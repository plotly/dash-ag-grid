import dash_ag_grid as dag
import dash
from dash import html, dcc, Input, Output, State
import plotly.express as px

app = dash.Dash(__name__)

df = px.data.gapminder()


columnDefs = [
    {
        "field": "country",
        "checkboxSelection": True,
    },
    {"field": "continent"},
    {"field": "year"},
    {
        "field": "lifeExp",
        "type": "rightAligned",
        "valueFormatter": {"function": "d3.format('.1f')(params.value)"},
    },
    {
        "field": "pop",
        "type": "rightAligned",
        "valueFormatter": {"function": "d3.format(',.0f')(params.value)"},
    },
    {
        "field": "gdpPercap",
        "type": "rightAligned",
        "valueFormatter": {"function": "d3.format('$,.2f')(params.value)"},
    },
]


app.layout = html.Div(
    [
        dcc.Markdown("Example:  Select a row to pin it to the top of the grid"),
        dag.AgGrid(
            id="pinning-rows-grid",
            columnDefs=columnDefs,
            defaultColDef={"editable": True, "sortable": True, "filter": True},
            rowData=df.to_dict("records"),
            dashGridOptions={"rowSelection": "single"},
            columnSize="sizeToFit",
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("pinning-rows-grid", "dashGridOptions"),
    Input("pinning-rows-grid", "selectedRows"),
    State("pinning-rows-grid", "dashGridOptions"),
)
def pin_rows(row, grid_options):
    grid_options["pinnedTopRowData"] = row
    return grid_options


if __name__ == "__main__":
    app.run_server(debug=True)
