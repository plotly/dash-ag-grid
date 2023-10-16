from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=8,
    description=app_description,
    title="Dash AG Grid -  Row Dragging",
)

text1 = """
# Row Dragging

Row dragging is used to rearrange rows by dragging the row with the mouse.

## Enabling Row Dragging

> `rowDrag` (boolean) Set to `True` to allow row dragging. Default: `False`

To enable row dragging on all columns, set the column property `rowDrag=True` on one (typically the first) column.

```
const columnDefs = [
    # make all rows draggable
    { 'field': 'athlete', 'rowDrag': True },
]
```

There are two ways in which row dragging works in the grid, managed and unmanaged:

- Managed Dragging: This is the simplest, where the grid will rearrange rows as you drag them.
- Unmanaged Dragging: This is more complex and more powerful. The grid will not rearrange rows as you drag. Instead the
  application is responsible for responding to events fired by the grid and rows are rearranged by the application.

## Managed Dragging

In managed dragging, the grid is responsible for rearranging the rows as the rows are dragged. To enable the managed
dragging set the grid option:

```python
dashGridOptions = {"rowDragManaged": True}
```

### Dragging Animation

To enable animation of the rows while dragging, set the grid option:

```python
dashGridOptions = {'animateRows': True}
```

### Suppress Move When Dragging

By default, the managed row dragging moves the rows while you are dragging them. This effect might not be desirable due
to your application design. To prevent this default behaviour, set the grid option:

```python
dashGridOptions = {"suppressMoveWhenRowDragging": True}
```

### Multi-Row Dragging

It is possible to drag multiple rows at the same time, set the grid options:

```python
dashGridOptions = {"rowDragMultiRow": True, "rowSelection": "multiple"}
```

The example below shows simple managed dragging. The following can be noted:

- The first column has `rowDrag=True` which results in a draggable area being included in the cell.
- The property `rowDragManaged` is enabled, to tell the grid to move the row as the row is dragged.
- If a sort (click on the header) or filter (open up the column menu) is applied to the column, the draggable icon for
  row
  dragging is hidden. This is consistent with the constraints explained after the example.

When multi-row dragging is enabled:

- When you select multiple items and drag one of them, all items in the selection will be dragged.
- When you drag an item that is not selected while other items are selected, only the unselected item will be dragged.
"""

text2 = """
The logic for managed dragging is simple and has the following constraints:

- Works with <dccLink href='/clientside-data/overview' children='Client-Side' /> row model only; not with
  the <dccLink href='/serverside-data/infinite-row-model' children='Infinite' />, Server-Side or Viewport row
  models.
- Does not work if <dccLink href='/scrolling/pagination' children='Pagination' /> is enabled.
- Does not work when sorting is applied. This is because the sort order of the rows depends on the data and moving the
  data would break the sort order.
- Does not work when filtering is applied. This is because a filter removes rows making it impossible to know what '
  real' order of rows when some are missing.
- Does not work when row grouping or pivot is active. This is because moving rows between groups would require a
  knowledge of the underlying data which only your application knows.

These constraints can be bypassed by using unmanaged row dragging.

## Entire Row Dragging

When using row dragging it is also possible to reorder rows by clicking and dragging anywhere on the row without the
need for a drag handle by enabling the grid option:

```python
dashGridOptions = {"rowDragEntireRow": True}
```

The drag handle can be removed by not setting `rowDrag=True` in columns definition.

> [Range Selection](https://dashaggrid.pythonanywhere.com/selection/range-selection) is not supported
> when `rowDragEntireRow` is enabled.

The example below demonstrates entire row dragging with Multi-Row Dragging. Note the following:

- Reordering rows by clicking and dragging anywhere on a row is possible as `rowDragEntireRow` enabled.
- Multiple rows can be selected and dragged as `rowDragMultiRow` is also enabled with `rowSelection = 'multiple'`.
- Row Drag Managed is being used, but it is not a requirement for Entire Row Dragging.
"""

text3 = """
## Customisation

There are some options that can be used to customise the Row Drag experience, so it has a better integration with your
application.

### Custom Row Drag Text

When a row drag starts, a "floating" DOM element is created to indicate which row is being dragged. By default, this DOM
element will contain the same value as the cell that started the row drag. It's possible to override that text by using
the grid option `rowDragText` callback.

```python
dashGridOptions = {"rowDragText": {"function": "params.defaultTextValue + ' (age: ' + params.rowNode.data.age + ')'"}}
```

> `rowDragText` (Function) A callback that should return a string to be displayed by the `rowDragComp` while dragging a
> row. If this callback is not set, the current cell value will be used. If the `rowDragText` callback is set in the
> ColDef it will take precedence over this, except when `rowDragEntireRow=True`.

The example below shows dragging with custom text. The following can be noted:

- When you drag a row, the `rowDragText` callback will add the host city depending on the year to the floating drag
  element, like "(London Olympics)" if year of the dragged row is 2012

Here is the function added to the dashAgGridFunctions.js file in the assets folder:

```js
const hostCities = {2000: "Sydney", 2004: "Athens", 2008: "Beijing", 2012: "London",}

dagfuncs.rowDragText = function (params) {
    const {year} = params.rowNode.data;
    if (year in hostCities) {
        return `${params.defaultTextValue} (${hostCities[year]} Olympics)`
    }
    return params.defaultTextValue;
}
```
"""

text4 = """
### Custom Row Drag Text with Multiple Draggers

If the grid has more than one column set with `rowDrag=True`, the `rowDragText` callback can be set in the `colDef`.

```python
columnDefs = [
    {'field': 'athlete', 'rowDrag': True, "rowDragText": {"function": "athleteRowDragText(params)"}},
    {'field': 'country', 'rowDrag': True},
]
```

The example below shows dragging with custom text and multiple column draggers. The following can be noted:

- When you drag a row by the **country** row dragger, the `rowDragText` callback will add the host city depending on the
  year to the floating drag element, like "(London Olympics)" if year of the dragged row is 2012
- When you drag the row by the **athlete** row dragger, the `rowDragText` callback in the grid options will be
  overridden by the one in the `colDef` and will display the number of athletes selected.

Here are the functions added to the dashAgGridFunctions.js file in the assets folder:

```js
const hostCities = {2000: "Sydney", 2004: "Athens", 2008: "Beijing", 2012: "London",}

dagfuncs.rowDragText = function (params) {
    const {year} = params.rowNode.data;
    if (year in hostCities) {
        return `${params.defaultTextValue} (${hostCities[year]} Olympics)`
    }
    return params.defaultTextValue;
}

dagfuncs.athleteRowDragText = function (params) {
    return `${params.rowNodes.length} athlete(s) selected`
}
"""

text5 = """
### Row Dragger inside Custom Cell Renderers

Due to the complexity of some applications, it could be handy to render the Row Drag Component inside of a Custom Cell
Renderer. This can be achieved, by using the `registerRowDragger` method in
the [ICellRendererParams](https://www.ag-grid.com/react-data-grid/component-cell-renderer/?#reference-ICellRendererParams-registerRowDragger)
as follows:

```js
// this will hold the reference to the element you want to act as row dragger.
const myRef = React.useRef(null);

// synchronize the element with the registerRowDragger function
React.useEffect(() => {
    props.registerRowDragger(myRef.current, props.startDragPixels);
});

// then use the reference in the actual element
React.createElement('i', {className: 'fas fa-arrows-alt-v', ref: myRef})
```

> When using `registerRowDragger` you should **not** set the property `rowDrag=True` in the Column Definition. Doing
> that will cause the cell to have two row draggers.

### Row Dragger with Custom Start Drag Pixels 

By default, the drag event only starts after the **Row Drag Element** has been dragged by `4px`, but sometimes it might
be
useful to start the drag with a different drag threshold, for example, start dragging as soon as the `mousedown` event
happens (dragged by `0px`). For that reason, the `registerRowDragger` takes a second parameter to specify the number of
pixels that will start the drag event.

The example below shows a custom cell renderer, with using the `registerRowDragger` callback to render the Row Dragger
inside itself.

Here are the classes added to the .css file in the assets folder:

```css
.ag-ltr .ag-cell.custom-athlete-cell.ag-cell-focus:not(.ag-cell-range-selected):focus-within {
  border: 1px solid #ff7b7b;
}
.ag-cell.custom-athlete-cell {
  padding-left: 0 !important;
  padding-right: 0 !important;
}
.ag-cell.custom-athlete-cell > div {
  height: 100%;
}

.my-custom-cell-renderer {
  display: flex;
  font-size: 0.7rem;
  background-color: #4180d6;
  color: white;
  padding: 0.25rem;
  align-items: center;
  justify-content: space-between;
  box-sizing: border-box;
  height: 100%;
}

.my-custom-cell-renderer > * {
  line-height: normal;
}

.my-custom-cell-renderer i {
  visibility: hidden;
  cursor: move;
  color: orange;
}

.my-custom-cell-renderer:hover i {
  visibility: visible;
}

.my-custom-cell-renderer .athlete-info {
  display: flex;
  flex-direction: column;
  width: 85px;
  max-width: 85px;
}

.my-custom-cell-renderer .athlete-info > span {
  overflow: hidden;
  text-overflow: ellipsis;
}
```

Here is the custom cell renderer added to the dashAgGridComponentFunctions.js file in the assets folder:

```js
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
```
Note the following:
- When you hover the cells, an arrow will appear, and this arrow can be used to drag the rows.
- Try to set the parameter `dragStartPixels` of `registerRowDragger` callback to `0px` using the input
component, the drag event will start as soon as `mousedown` is fired.
"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.rows.row_dragging", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.rows.row_dragging_entire_row", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.rows.row_dragging_drag_text", make_layout=make_tabs),
        make_md(text4),
        example_app("examples.rows.row_dragging_drag_text_multi_dragger", make_layout=make_tabs),
        make_md(text5),
        example_app("examples.rows.row_dragging_custom_dragger", make_layout=make_tabs),
        # up_next("text"),
    ],
)
