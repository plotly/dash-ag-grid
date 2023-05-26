var dagcomponentfuncs = (window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {});

// Used in Row Spanning Complex Example

dagcomponentfuncs.ShowCellRenderer = function (props) {
    let children;
    if (props.value) {
        children = [
            React.createElement('div', {className: 'show-name'}, props.value.name),
            React.createElement('div', {className: 'show-presenter'}, props.value.presenter),
        ]
    }
    return React.createElement('div', null, children)
}

// Used in Row Dragging - Row Dragger inside Custom Cell Renderers
dagcomponentfuncs.CustomCellRenderer = function (props) {

    const myRef = React.useRef(null);

    React.useEffect(() => {
        props.registerRowDragger(myRef.current, props.startDragPixels);
    });

    return React.createElement('div', {className: 'my-custom-cell-renderer'},
        [
            React.createElement('div', {className: 'athlete-info'}, [
                React.createElement('span', null, props.data.athlete),
                React.createElement('span', null, props.data.country),
            ]),
            React.createElement('span', null, props.data.year),
            React.createElement('i', {className: 'fas fa-arrows-alt-v', ref: myRef})
        ]
    );
};
