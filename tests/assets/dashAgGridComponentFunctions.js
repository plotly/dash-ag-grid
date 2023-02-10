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

dagcomponentfuncs.myCustomButton = function (props) {

    const {setProps, data} = props;

    if (!props.value) {
        return React.createElement('button')
    }

    function onClick() {
        let colId = props.column.colId;
        let newData = JSON.parse(JSON.stringify(props.node.data[colId]));
        newData["n_clicks"]++
        props.node.setDataValue(colId, newData);
    }

    const id = JSON.stringify({'index': props.rowIndex, 'type':'customButton'})
    return React.createElement('div',
    {style: {'width':'100%','height':'100%', 'padding':'5px', 'display':'flex',
     'justifyContent':'center', 'alignItems':'center'}},
    React.createElement('button', {
        onClick: onClick,
        id: props.value.id,
        className: props.value.className,

    }, 'testing'))
}