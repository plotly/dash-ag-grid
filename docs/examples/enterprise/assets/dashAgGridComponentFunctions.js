var dagcomponentfuncs = (window.dashAgGridComponentFunctions =
    window.dashAgGridComponentFunctions || {});

// Used in  Enterprise Group Cell Renderer example
dagcomponentfuncs.SimpleCellRenderer = function (props) {
    return React.createElement(
        'span',
        {
            style: {
                backgroundColor: props.node.group ? 'coral' : 'lightgreen',
                padding: 2,
            },
        },
        props.value
    );
};
