var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};

dagcomponentfuncs.stockLink = function (props) {
    return React.createElement('a',
    {
        href: 'https://finance.yahoo.com/quote/' + props.value,
        target: props.value
    }, props.value)
}

dagcomponentfuncs.checkbox = function (props) {
    function checkedHandler() {
        let checked = event.target.checked;
        let colId = props.column.colId;
        props.node.setDataValue(colId, checked);
    }
    return React.createElement('input',
    {
        type: 'checkbox',
        checked: props.value,
        onChange: checkedHandler,
        style: {'cursor':'pointer'}
    })
}