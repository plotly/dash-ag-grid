import dash_ag_grid as dag
from dash import Dash, Input, Output, html, dcc
import plotly.express as px
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
df = px.data.gapminder()
df2 = df.groupby("country")[["lifeExp", "gdpPercap", "pop"]].mean().reset_index()

df2["graph"] = ""
df2["change"] = ""
for i, r in df2.iterrows():
    filterDf = df[df["country"] == r["country"]]
    fig = px.line(
        filterDf,
        x="year",
        y="gdpPercap",
        hover_data=['year', 'gdpPercap', 'lifeExp', 'pop']
    )
    fig.update_traces(hovertemplate="""_year_: %{x}<br>
    _year_: %{y}<br>
    _lifeExp_: %{customdata[0]}<br>
    _pop_: %{customdata[1]}<br>
    """)
    fig.update_layout(
        showlegend=False,
        yaxis_visible=False,
        yaxis_showticklabels=False,
        xaxis_visible=False,
        xaxis_showticklabels=False,
        margin=dict(l=0, r=0, t=0, b=0),
        template="plotly_white",
        hovermode='x unified'
    )
    df2.at[i, "graph"] = fig
    df2.at[i, "change"] = filterDf['gdpPercap'].to_list()

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
    }
]

columnDefs2 = [
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
        "field": "change",
        "cellRenderer": "agSparklineCellRenderer",
        "headerName": "GdpPerCap / Year",
        "maxWidth": 900,
    }
]

app.layout = html.Div(
    [
        dcc.Markdown("Example of grid with a custom `dcc.Graph` component"),
        dbc.Row([
            dbc.Col([
        dag.AgGrid(
            id="custom-component-graph-grid",
            rowData=df2.to_dict("records"),
            columnDefs=columnDefs,
            style={"height": 800},
        )]
            )
    ]
)])

if __name__ == "__main__":
    app.run(debug=True)

"""
Add the following to the dashAgGridComponents.js file in the /assets folder:

------------------
dagcomponentfuncs.DCC_GraphClickData = function (props) {
    const {setData} = props;

    this.oldY = 0;

    function init_tooltip(make) {
        if (make) {
            newTooltip = document.createElement("div");
            newTooltip.id = 'grid_graph_tooltip'
            document.body.appendChild(newTooltip)
        }
        else {
            tooltipHolder = document.getElementById('grid_graph_tooltip')
            if (tooltipHolder) {
                document.body.removeChild(tooltipHolder)
            }
        }
    }

    function hoverTemplateToMarkdown(hovertemplate, customData, data) {
        info = hovertemplate
        info = info.replaceAll('<br>', '  \r')
        info = info.replaceAll('%{x}', data['points'][0]['x'])
        info = info.replaceAll('%{y}', data['points'][0]['y'])
        for (var y = 0; y < customData[0].length; y++) {
            info = info.replaceAll('%{customdata['+y+']}', props.value.data[0].customdata[data.points[0].pointNumber][y])
        }
        info = info.replaceAll('<extra></extra>', '')
        return info
    }

    function tooltip(data) {
        tooltipHolder = document.getElementById('grid_graph_tooltip')
        if (!(tooltipHolder)) {
            init_tooltip(true)
            tooltipHolder = document.getElementById('grid_graph_tooltip')
        }
        graphHolder = document.getElementsByClassName('grid-graph-holder')[0]
        bbox = data['points'][0]['bbox']
        if (window.event) {
            this.oldY = window.event.clientY
        }
        bbox['x0'] = bbox['x0'] + graphHolder.getBoundingClientRect().left - 10
        bbox['y0'] = this.oldY
        direction = 'right'
        if (bbox['x0'] + bbox['x1'] > (window.innerWidth - 50)) {
            direction = 'left'
            bbox['x0'] = bbox['x0'] - 15
        }
        if (props.value.data[0].hovertemplate) {
            info = hoverTemplateToMarkdown(props.value.data[0].hovertemplate, props.value.data[0].customdata, data)
        } else {
            info = data['points'][0]['x'] + '  \r' + data['points'][0]['y']
        }
        ReactDOM.render(
            React.createElement(
                window.dash_core_components.Tooltip,
                    {
                        show: true,
                        bbox,
                        direction
                    }
                ,
                React.createElement(
                window.dash_core_components.Markdown, {},
                    info
                )
            )
        , tooltipHolder)
    }

    function setProps() {
        const graphProps = arguments[0];
        if (graphProps['clickData']) {
            setData(graphProps);
        }

        if ('hoverData' in graphProps) {
            tooltip(graphProps['hoverData'])
        }
    }

    return React.createElement('div', {
            onMouseLeave: () => {init_tooltip(false)},
            onMouseEnter: () => {init_tooltip(true)},
            className: "grid-graph-holder",
            style: {width: '100%', height: '100%'}
        },
        React.createElement(window.dash_core_components.Graph, {
            figure: props.value,
            setProps,
            style: {height: '100%'},
            config: {displayModeBar: false},
        }
        ))
};
"""
