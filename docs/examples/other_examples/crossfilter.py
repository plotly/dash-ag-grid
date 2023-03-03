import dash_ag_grid as dag
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

app = Dash(__name__)

columnDefs = [
    {
        "field": "country",
        "checkboxSelection": True,
        "headerCheckboxSelection": True,
    },
    {"headerName": "Continent", "field": "continent"},
    {
        "headerName": "Life Expectancy",
        "field": "lifeExp",
        "type": "rightAligned",
        "valueFormatter": {"function": "d3.format('.1f')(params.value)"},
    },
    {
        "headerName": "Population",
        "field": "pop",
        "type": "rightAligned",
        "valueFormatter": {"function": "d3.format(',.0f')(params.value)"},
    },
    {
        "headerName": "GDP per Capita",
        "field": "gdpPercap",
        "type": "rightAligned",
        "valueFormatter": {"function": "d3.format('$,.1f')(params.value)"},
    },
]

app.layout = html.Div(
    [
        dag.AgGrid(
            id="datatable-interactivity",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            rowSelection="multiple",
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True},
        ),
        html.Div(id="datatable-interactivity-container"),
    ]
)


@app.callback(
    Output("datatable-interactivity-container", "children"),
    Input("datatable-interactivity", "virtualRowData"),
    Input("datatable-interactivity", "selectedRows"),
)
def update_graphs(rows, selected):
    dff = df if rows is None else pd.DataFrame(rows)
    selected = [s["country"] for s in selected] if selected else []

    colors = ["#7FDBFF" if i in selected else "#0074D9" for i in dff.country]

    graphs = []
    for column in ["pop", "lifeExp", "gdpPercap"]:
        if column in dff:
            fig = px.bar(dff, x="country", y=column, height=250)
            fig.update_traces(marker={"color": colors})
            fig.update_layout(
                margin={"t": 10, "l": 10, "r": 10},
                xaxis={"automargin": True},
                yaxis={"automargin": True, "title": {"text": column}},
            )
            graphs.append(dcc.Graph(id=column, figure=fig))
    return graphs


if __name__ == "__main__":
    app.run_server(debug=True)
