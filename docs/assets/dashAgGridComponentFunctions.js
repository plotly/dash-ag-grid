var dagcomponentfuncs = (window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {});

dagcomponentfuncs.StockLink = function (props) {
    return React.createElement(
        'a',
        {href: 'https://finance.yahoo.com/quote/' + props.value},
        props.value
    );
};

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
            'select',
            {
                value: props.value,
                onChange: selectionHandler,
            },
            options
        )
    );
};

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
        {
            style: {
                width: '100%',
                height: '100%',
                padding: '5px',
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
            },
            onClick: onClick,
        },
        React.createElement('input', {
            type: 'checkbox',
            checked: props.value,
            onChange: checkedHandler,
            style: {cursor: 'pointer'},
        })
    );
};

dagcomponentfuncs.Tags = function (props) {
    if (props.value == 'High') {
        newTag = React.createElement(
            'div',
            {
                style: {
                    backgroundColor: '#d8f0d3',
                    borderRadius: '15px',
                    padding: '5px',
                    color: 'black',
                },
            },
            props.value
        );
    } else if (props.value == 'Low') {
        newTag = React.createElement(
            'div',
            {
                style: {
                    backgroundColor: '#f5cccc',
                    borderRadius: '15px',
                    padding: '5px',
                    color: 'black',
                },
            },
            props.value
        );
    } else {
        newTag = React.createElement(
            'div',
            {
                style: {
                    backgroundColor: '#fffec8',
                    borderRadius: '15px',
                    padding: '5px',
                    color: 'black',
                },
            },
            props.value
        );
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
        newTag
    );
};

dagcomponentfuncs.Button = function (props) {
    const {setData, data} = props;

    if (!props.value) {
        return React.createElement('button');
    }

    function onClick() {
        setData();
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
            'button',
            {
                onClick: onClick,
                className: props.className,
            },
            props.children
        )
    );
};

dagcomponentfuncs.CustomButton = function (props) {
    const {setData, data} = props;

    if (!props.value) {
        return React.createElement('button');
    }

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
            'button',
            {
                onClick: onClick,
                className: props.value.className,
            },
            props.value.children
        )
    );
};

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
