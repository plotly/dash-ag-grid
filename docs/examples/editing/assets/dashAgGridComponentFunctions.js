var dagcomponentfuncs = (window.dashAgGridComponentFunctions =
    window.dashAgGridComponentFunctions || {});

dagcomponentfuncs.EditButton = function (props) {
    function onButtonClicked() {
        // start editing this cell. see the docs on the params that this method takes
        props.api.startEditingCell({
            rowIndex: props.rowIndex,
            colKey: props.column.getId(),
        });
    }

    return React.createElement('span', {}, [
        React.createElement(
            'button',
            {
                onClick: onButtonClicked,
                style: {height: '30px'},
            },
            '✎'
        ),
        React.createElement(
            'span',
            {
                style: {paddingLeft: '4px'},
            },
            props.value
        ),
    ]);
};
