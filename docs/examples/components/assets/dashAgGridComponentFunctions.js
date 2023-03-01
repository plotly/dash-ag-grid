var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};

dagcomponentfuncs.stockLink = function (props) {
    return React.createElement('a',
    {
        href: 'https://finance.yahoo.com/quote/' + props.value,
        target: props.value
    }, props.value)
}

dagcomponentfuncs.customDropdown = function (props) {

    function selectionHandler() {
        const newValue = event.target.value;
        const colId = props.column.colId;
        props.node.setDataValue(colId, newValue);
    }

    const options = props.colDef.cellEditorParams.values.map((opt) => React.createElement('option', {}, opt))

    return React.createElement('div',
    {style: {'width':'100%','height':'100%', 'padding':'5px', 'display':'flex',
     'justifyContent':'center', 'alignItems':'center'}},
     React.createElement('select',
        {
            value: props.value,
            onChange: selectionHandler,
        }, options
        )
    )
}

dagcomponentfuncs.checkbox = function (props) {
    function onClick() {
        if (!('checked' in event.target)) {
            const checked = !event.target.children[0].checked;
            const colId = props.column.colId;
            props.node.setDataValue(colId, checked);
        }
    }

    function checkedHandler() {
        const checked = event.target.checked;
        const colId = props.column.colId;
        props.node.setDataValue(colId, checked);
    }
    return React.createElement('div',
    {style: {'width':'100%','height':'100%', 'padding':'5px', 'display':'flex',
     'justifyContent':'center', 'alignItems':'center'},
     onClick: onClick},
     React.createElement('input',
        {
            type: 'checkbox',
            checked: props.value,
            onChange: checkedHandler,
            style: {'cursor':'pointer'}
        })
    )
}

dagcomponentfuncs.tags = function (props) {

    if (props.value == "High") { newTag = React.createElement('div', {
        style: {"backgroundColor":"#d8f0d3", "borderRadius":"15px", "padding": "5px", "color":"black" },
        }, props.value)}
    else if (props.value == "Low") {
        newTag = React.createElement('div', {
        style: {"backgroundColor":"#f5cccc", "borderRadius":"15px", "padding": "5px", "color":"black"},
        }, props.value)
    }
    else {
        newTag = React.createElement('div', {
        style: {"backgroundColor":"#fffec8", "borderRadius":"15px", "padding": "5px", "color":"black"},
        }, props.value)
    }

    return React.createElement('div',
    {style: {'width':'100%','height':'100%', 'padding':'5px', 'display':'flex',
     'justifyContent':'center', 'alignItems':'center'}},
    newTag)
}

dagcomponentfuncs.myCustomButton = function (props) {

    if (!props.value) {
        return React.createElement('button')
    }

    function onClick() {
        let colId = props.column.colId;
        let newData = JSON.parse(JSON.stringify(props.node.data[colId]));
        newData["n_clicks"]++
        props.node.setDataValue(colId, newData);
        props.node.setDataValue('action', colId);
    }

    const id = JSON.stringify({'index': props.rowIndex, 'type':'customButton'})
    return React.createElement('div',
    {style: {'width':'100%','height':'100%', 'padding':'5px', 'display':'flex',
     'justifyContent':'center', 'alignItems':'center'}},
    React.createElement('button', {
        onClick: onClick,
        id: props.value.id,
        className: props.value.className,

    }, props.value.children))
}


dagcomponentfuncs.customButton = function (props) {
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
        className: props.className,
    }, props.children))
}


dagcomponentfuncs.myCustomTooltip = function (params) {
    info = [
    React.createElement('h4',{},params.data.ticker), React.createElement('div',{}, params.data.company),React.createElement('div',{}, params.data.price)]
    return React.createElement('div',{style: {"border":'2pt solid white', 'backgroundColor':params.color || "grey", "padding": 10}}, info);
}