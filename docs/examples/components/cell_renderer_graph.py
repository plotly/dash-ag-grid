import dash_ag_grid as dag
from dash import Dash, Input, Output, html, dcc
import plotly.express as px
import json


app = Dash(__name__)

df = px.data.gapminder().query('continent == "Asia"')
df2 = df.groupby("country")[["lifeExp", "gdpPercap", "pop"]].mean().reset_index()

df2["graph"] = ""
for i, r in df2.iterrows():
    filterDf = df[df["country"] == r["country"]]
    fig = px.scatter(
        filterDf,
        x="year",
        y="gdpPercap",
        size="pop",
        color="lifeExp",
        color_continuous_scale=px.colors.diverging.Tealrose_r,
        trendline="ols",
        range_color=[30, 90],
    )
    fig.update_layout(
        showlegend=False,
        yaxis_visible=False,
        yaxis_showticklabels=False,
        xaxis_visible=False,
        xaxis_showticklabels=False,
        margin=dict(l=0, r=0, t=0, b=0),
        template="plotly_white",
    )
    df2.at[i, "graph"] = fig

columnDefs = [
    {"field": "country"},
    {
        "field": "lifeExp",
        "headerName": f"Avg. Life Expectancy",
        "valueFormatter": {"function": 'd3.format("(,.2f")(params.value)'},
    },
    {
        "field": "gdpPercap",
        "headerName": f"Avg. GPD per Capita",
        "valueFormatter": {"function": 'd3.format("(,.2f")(params.value)'},
    },
    {
        "field": "pop",
        "headerName": f"Avg. Population",
        "valueFormatter": {"function": 'd3.format("(,.2f")(params.value)'},
    },
    {
        "field": "graph",
        "cellRenderer": "DCC_GraphClickData",
        "headerName": "GdpPerCap / Year",
        "maxWidth": 900,
        "minWidth": 500,
    }
]


app.layout = html.Div(
    [
        dcc.Markdown("Example of grid with a custom `dcc.Graph` component"),
        dag.AgGrid(
            id="custom-component-graph-grid",
            rowData=df2.to_dict("records"),
            columnSize="sizeToFit",
            columnDefs=columnDefs,
            defaultColDef={"sortable": True, "filter": True, "minWidth": 125},
            dashGridOptions={"rowHeight": 100},
            style={"height": 800},
        ),
        html.Div(id="custom-component-graph-output"),
    ]
)


@app.callback(
    Output("custom-component-graph-output", "children"),
    Input("custom-component-graph-grid", "cellRendererData")
)
def graphClickData(d):
    return json.dumps(d)


if __name__ == "__main__":
    app.run_server(debug=True)



"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder

---------------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};

dagcomponentfuncs.DCC_GraphClickData = function (props) {
    const {setData} = props;
    function setProps() {
        const graphProps = arguments[0];
        if (graphProps['clickData']) {
            setData(graphProps);
        }
    }
    return React.createElement(window.dash_core_components.Graph, {
        figure: props.value,
        setProps,
        style: {height: '100%'},
        config: {displayModeBar: false},
    });
};
"""