
var dagcomponentfuncs = (window.dashAgGridComponentFunctions =
    window.dashAgGridComponentFunctions || {});

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