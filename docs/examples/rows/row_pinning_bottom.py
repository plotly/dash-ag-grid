import dash_ag_grid as dag
import dash
from dash import html, dcc, Input, Output, State
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = px.data.gapminder()

columnDefs = [
    {"field": "country"},
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
        dcc.Markdown("Example:  Summary row pinned to the bottom of the grid"),
        dag.AgGrid(
            id="pinning-avg-grid",
            columnDefs=columnDefs,
            defaultColDef={
                "editable": True,
                "sortable": True,
                "filter": True,
                "resizable": True,
            },
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            dashGridOptions={"pinnedBottomRowData": [{}]},
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("pinning-avg-grid", "dashGridOptions"),
    Input("pinning-avg-grid", "virtualRowData"),
    State("pinning-avg-grid", "dashGridOptions"),
)
def pin_avg_row(data, grid_options):
    if data == []:
        dff_avg_row = [{}]
    else:
        dff = df if data is None else pd.DataFrame(data)
        dff_avg_row = dict(dff[["lifeExp", "pop", "gdpPercap"]].mean())
        dff_avg_row["country"] = "Average"

    grid_options["pinnedBottomRowData"] = [dff_avg_row]
    return grid_options


if __name__ == "__main__":
    app.run_server(debug=True)
