var dagcomponentfuncs = (window.dashAgGridComponentFunctions =
    window.dashAgGridComponentFunctions || {});

// Simple component to create a custom link
dagcomponentfuncs.StockLink = function (props) {
    return React.createElement(
        'a',
        {href: 'https://finance.yahoo.com/quote/' + props.value},
        props.value
    );
};

// Simple html.Button
dagcomponentfuncs.Button = function (props) {
    const {setData, data} = props;

    function onClick() {
        setData();
    }
    return React.createElement(
        'button',
        {
            onClick: onClick,
            className: props.className,
        },
        props.value
    );
};

// Simple dbc.Button
dagcomponentfuncs.DBC_Button_Simple = function (props) {
    const {setData, data} = props;

    function onClick() {
        setData();
    }
    return React.createElement(
        window.dash_bootstrap_components.Button,
        {
            onClick: onClick,
            color: props.color,
        },
        props.value
    );
};

// Custom  HTML select component
dagcomponentfuncs.Dropdown = function (props) {
    const {setData, data} = props;

    function selectionHandler() {
        // update data in the grid
        const newValue = event.target.value;
        const colId = props.column.colId;
        props.node.setDataValue(colId, newValue);
        // update cellRendererData prop so it can be used to trigger a callback
        setData(event.target.value);
    }

    const options = props.colDef.cellRendererParams.values.map((opt) =>
        React.createElement('option', {value: opt}, opt)
    );
    return React.createElement(
        'select',
        {
            value: props.value,
            onChange: selectionHandler,
            style: {padding: 10},
        },
        options
    );
};

// custom component to display boolean data as a checkbox
dagcomponentfuncs.Checkbox = function (props) {
    const {setData, data} = props;
    function onClick() {
        if (!('checked' in event.target)) {
            const checked = !event.target.children[0].checked;
            const colId = props.column.colId;
            props.node.setDataValue(colId, checked);
        }
    }
    function checkedHandler() {
        // update grid data
        const checked = event.target.checked;
        const colId = props.column.colId;
        props.node.setDataValue(colId, checked);
        // update cellRendererData prop so it can be used to trigger a callback
        setData(checked);
    }
    return React.createElement(
        'div',
        {onClick: onClick},
        React.createElement('input', {
            type: 'checkbox',
            checked: props.value,
            onChange: checkedHandler,
            style: {cursor: 'pointer'},
        })
    );
};

//custom component for displaying content different colored tags based on the cell value
dagcomponentfuncs.Tags = function (props) {
    if (props.value == 'High') {
        backgroundColor = '#d8f0d3';
    } else if (props.value == 'Low') {
        backgroundColor = '#f5cccc';
    } else {
        backgroundColor = '#fffec8';
    }
    return React.createElement(
        'div',
        {
            style: {
                width: '100%',
                height: '100%',
                padding: '5px',
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
            },
        },
        React.createElement(
            'div',
            {
                style: {
                    backgroundColor: backgroundColor,
                    borderRadius: '15px',
                    padding: '5px',
                    color: 'black',
                },
            },
            props.value
        )
    );
};

// custom html img component to display an image thumbnail in the grid
dagcomponentfuncs.ImgThumbnail = function (props) {
    const {setData, data} = props;

    function onClick() {
        setData(props.value);
    }

    return React.createElement(
        'div',
        {
            style: {
                width: '100%',
                height: '100%',
                display: 'flex',
                alignItems: 'center',
            },
        },
        React.createElement('img', {
            onClick: onClick,
            style: {width: '100%', height: 'auto'},
            src: props.value,
        })
    );
};

// Custom button that when clicked updates other columns in the grid
dagcomponentfuncs.CustomButton = function (props) {
    const {setData, data} = props;
    function onClick() {
        // update data in the grid
        let colId = props.column.colId;
        let newData = JSON.parse(JSON.stringify(props.node.data[colId]));
        newData['n_clicks']++;
        props.node.setDataValue(colId, newData);
        // Update the dropdown value based on which button was clicked
        props.node.setDataValue('action', colId);
        // update cellRendererData prop so it can be used to trigger a callback - include n_clicks
        setData({n_clicks: newData['n_clicks']});
    }
    return React.createElement(
        'button',
        {
            onClick: onClick,
            className: props.value.className,
        },
        props.value.children
    );
};

// Custom Tootlip component
dagcomponentfuncs.CustomTooltip = function (props) {
    info = [
        React.createElement('h4', {}, props.data.ticker),
        React.createElement('div', {}, props.data.company),
        React.createElement('div', {}, props.data.price),
    ];
    return React.createElement(
        'div',
        {
            style: {
                border: '2pt solid white',
                backgroundColor: props.color || 'grey',
                padding: 10,
            },
        },
        info
    );
};

// Used in the conditional rendering example
dagcomponentfuncs.MoodRenderer = function (props) {
    const imgForMood =
        'https://www.ag-grid.com/example-assets/smileys/' +
        (props.value === 'Happy' ? 'happy.png' : 'sad.png');

    return React.createElement('img', {src: imgForMood, width: '20px'});
};

dagcomponentfuncs.GenderRenderer = function (props) {
    const image = props.value === 'Male' ? 'male.png' : 'female.png';
    const imageSource = `https://www.ag-grid.com/example-assets/genders/${image}`;
    return React.createElement('img', {src: imageSource, width: '20px'});
};

// use for adding a dcc.Graph to the grid with clickData available in a callback
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

// use for displaying sparklines made with dcc.Graph.  Note - the figure has no no user interaction
dagcomponentfuncs.DCC_Graph = function (props) {
    return React.createElement(window.dash_core_components.Graph, {
        figure: props.value,
        style: {height: '100%'},
        config: {displayModeBar: false},
    });
};

// use for making dbc.Button with FontAwesome or Bootstrap icons
dagcomponentfuncs.DBC_Button = function (props) {
    const {setData, data} = props;

    function onClick() {
        setData();
    }
    let leftIcon, rightIcon;
    if (props.leftIcon) {
        leftIcon = React.createElement('i', {
            className: props.leftIcon,
        });
    }
    if (props.rightIcon) {
        rightIcon = React.createElement('i', {
            className: props.rightIcon,
        });
    }
    return React.createElement(
        window.dash_bootstrap_components.Button,
        {
            onClick,
            color: props.color,
            disabled: props.disabled,
            download: props.download,
            external_link: props.external_link,
            href: props.href,
            outline: props.outline,
            size: props.size,
            style: {
                margin: props.margin,
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
            },
            target: props.target,
            title: props.title,
            type: props.type,
        },
        leftIcon,
        props.value,
        rightIcon
    );
};

// use for making dmc.Button with DashIconify icons
dagcomponentfuncs.DMC_Button = function (props) {
    const {setData, data} = props;

    function onClick() {
        setData();
    }
    let leftIcon, rightIcon;
    if (props.leftIcon) {
        leftIcon = React.createElement(window.dash_iconify.DashIconify, {
            icon: props.leftIcon,
        });
    }
    if (props.rightIcon) {
        rightIcon = React.createElement(window.dash_iconify.DashIconify, {
            icon: props.rightIcon,
        });
    }
    return React.createElement(
        window.dash_mantine_components.Button,
        {
            onClick,
            variant: props.variant,
            color: props.color,
            leftIcon,
            rightIcon,
            radius: props.radius,
            style: {
                margin: props.margin,
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
            },
        },
        props.value
    );
};

// Custom Loading Overlay
dagcomponentfuncs.CustomLoadingOverlay = function (props) {
    return React.createElement(
        'div',
        {
            style: {
                border: '1pt solid grey',
                color: props.color || 'grey',
                padding: 10,
            },
        },
        props.loadingMessage
    );
};

// Custom overlay for No Rows
dagcomponentfuncs.CustomNoRowsOverlay = function (props) {
    return React.createElement(
        'div',
        {
            style: {
                border: '1pt solid grey',
                color: 'grey',
                padding: 10,
                fontSize: props.fontSize,
            },
        },
        props.message
    );
};
