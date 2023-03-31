from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=3,
    description=app_description,
    title="Dash AG Grid Components - cell renderers",

)

text1 = """
# Cell Renderers

By default the grid renders values into the cells as strings. If you want something more complex you can use a cell renderer.

- `cellRenderer` (function) Provide your own cell Renderer component for this column's cells.

Please see the [AG Grid documentation](https://www.ag-grid.com/react-data-grid/component-cell-renderer/) for complete information on cell renderer components,
--------------  


Creating custom components is considered "beyond the basics" as it requires writing components in JavaScript or React. We've 
provided a few simple examples so you can see how to use custom React components with dash-ag-grid.  We hope that 
even if you're new to React, you'll be able to modify these examples for use in your own project. 

You'll find all the components used in these docs in [GitHub](https://github.com/plotly/dash-ag-grid/blob/dev/docs/assets/dashAgGridComponentFunctions.js).
We would like to build a library of components, so if you create a component, please consider sharing either on the Dash
 forum or [open an issue](https://github.com/plotly/dash-ag-grid/issues) in GitHub so we can add it to the collection.


> If you are new to React or Javascript see:
-  <dccLink href='/getting-started/beyond-the-basics' children='Beyond the Basics' />  section
- [Getting started with React](https://react.dev/learn) tutorial
- [Creating an element without JSX](https://react.dev/reference/react/createElement#creating-an-element-without-jsx).
 React components used with the `cellRenderer` in Dash need to be written without JSX, since JSX code cannot be run  directly in the browser.



#### Value Formatter vs Cell Renderer
A cell renderer allows you to put whatever HTML you want into a cell. This sounds like value formatters and a cell renderers have cross purposes, so you may be wondering, when do you use each one and not the other?

The answer is that value formatters are for text formatting and cell renderers are for when you want to include HTML markup and potentially functionality to the cell. So for example, if you want to put punctuation into a value, use a value formatter, but if you want to put buttons or HTML links use a cell renderer. It is possible to use a combination of both, in which case the result of the value formatter will be passed to the cell renderer.

#### Markdown component vs Cell Renderer
The <dccLink href='/components/markdown' children='Markdown' /> component is a convenient and easy way to  format text. 
For example, to create a heading, add number signs (#) in front of a word or phrase. You can do this safely without having
having to use raw HTML. You can also use the markdown component to render raw HTML, however, this method is vulnerable [XSS attacks.](https://owasp.org/www-community/attacks/xss/).
You can enable rendering raw HTML in the markdown component by setting the prop `dangerously_allow_code=True`.
  
Instead of rendering raw HTML in the markdown component, you can use the cell render.  The cell renderer is a safer way
 of rendering HTML in Dash.  It is not necessary to set the grid to `dangerously_allow_code=True` when using the cell renderer.
 
 
#### Provided Cell Renderers
The grid comes with some provided cell renderers out of the box. These cell renderers cover some common complex cell rendering requirements.

- Group Cell Renderer: (Enterprise only) For showing group details with expand & collapse functionality when using any of the Row Grouping, Master Detail or Tree Data.
- Show Change Cell Renderers: For animating changes when data is changing.  See examples in <dccLink href='/rendering/change-cell-renderers' children='Rendering' /> . 

## Custom Cell Renderers

### Registering custom components

In order to safely render custom components in Dash, they must be added to the dash-ag-grid namespace. See
 the <dccLink href='/getting-started/beyond-the-basics' children='Beyond the Basics' />  section for more information.

Register the component by adding the component to a `.js` file in the `assets` folder. Add it to the `dashAgGridComponentFunctions` namespace like this:

```
var dagcomponentfuncs = (window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {});

dagcomponentfuncs.StockLink = function (props) {
    return React.createElement(
        'a',
        {href: 'https://finance.yahoo.com/quote/' + props.value},
        props.value
    );
};

```

` `  
` `  


### Example 1:  Registering  custom components

This example uses a simple function to create a link to Yahoo Finance based on the stock ticker in the cell.

"""

text2 = """
### Triggering callbacks with custom components
To use the custom components in a callback, the component must call the `setData()` function, which will update the
 Dash prop `cellRendererData`.  You can then use the Dash prop `cellRendererData` as an input of a callback.  The 
 `cellRendererData` dict contains information on which component triggered the callback, including arbitrary data sent from the component.

`cellRendererData` (dict; optional): Special prop to allow feedback from cell renderer to the grid. `cellRendererData` is a dict with keys:

- `colId` (string; optional): Column ID from where the event was fired.

- `rowId` (boolean | number | string | dict | list; optional): Row Id from the grid, this could be a number automatically, or set via getRowId.

- `rowIndex` (number; optional): Row Index from the grid, this is associated with the row count.

- `timestamp` (boolean | number | string | dict | list; optional): Timestamp of when the event was fired.

- `value` (boolean | number | string | dict | list; optional): Value set from the function.

Update the `cellRendererData` prop in the custom component by calling the `setData()` function.
You may also include arbitrary data which will be included  the `value` key, for example:  `setData(<myData>)`


` `  
` `  


### Example 2: Triggering callbacks
This example shows how to add buttons to cells in the grid.  Use the `cellRendererData` prop in the callback
to see which button triggered the callback.

Note the following:
 - `cellRendererData` prop is updated by calling `setData()` in the custom `Button` component
 - The button is styled with Bootstrap class names passed to the component in the `cellRendererParm` prop from the Dash app.
 - The `cellRendererData` prop is used as an Input of a Dash callback, and it contains information on which button was clicked. 
 
"""



text3 = """

` `  
` `  

### Example 3:  Including extra data in `cellRenderData`

This example shows how to pass extra data from a custom component to Dash for use in a callback.  We pass the state of
 the checkbox to the `value` key of the `cellRendererData` prop.   We do this by calling the function `setData(checked) in the component;`
 
Compare the data in the callback in this example to the Button example above.  You will see that the in the Button example,
there is no `value` key in the `cellRendererData`.

"""

text4 = """

` `  
` `  

### Example 4:  Custom Image Component

This example is similar to Example 2 and 3. It shows how you can create other custom components.

The `ImgThumbnail` custom component renders an `img` HTML tag and uses the cell value in the `scr` attribute. The CSS in the `style`
makes the image responsive.  The size of the image is determined by the column width and row height of the grid.
```
React.createElement(
    'img',
    {        
        src: props.value,
        onClick: onClick,
        style: {width: '100%', height: 'auto'},

    },
)
```
The `onClick` is a function that calls `setData(props.value)`.  This adds the cell value (the img URL) to 
the `cellRendererData` prop, making it easy to use in a Dash callback.

```
function onClick() {
    setData(props.value);
}
```

Here is the Dash callback that renders a fullsize image in a modal component when you click on the Thumbnail:

```
@app.callback(
    Output("custom-component-img-modal", "is_open"),
    Output("custom-component-img-modal", "children"),
    Input("custom-component-img-grid", "cellRendererData"),
)
def show_change(data):
    if data:
        return True, html.Img(src=data["value"])
    return False, None
```
"""



text5 = """

` `  
` `  

### Example 5:  More Custom Cell renderers

In this example we show several components:
- The Stock Ticker column uses the `stockLink` function from Example 1 to create the links.  It also has a custom tooltip component.
- The Last Close Price column does not use a cell renderer. Since it's only formatting text, it's using a `valueFormatter`. See more info in the <dccLink href='/rendering/value-formatters' children='Rendering' /> section.
- Volume column uses a cell render for conditional formatting.  The color of the badge changes based on the value of the cell.  This column
is editable, so try changing the values - (Low, High, Average) and note how the color changes.
- The Binary column renders True or False values as a checkbox.
- The Buy and Sell column uses a different custom function to create the buttons than in Example 2.  This function also
updates the value in the Action column.
- The Action column is a simple dropdown made with HTML Select.

"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.components.cell_renderer_link", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.components.cell_renderer_button", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.components.cell_renderer_checkbox", make_layout=make_tabs),
        make_md(text4),
        example_app("examples.components.cell_renderer_img", make_layout=make_tabs),
        make_md(text5),
        example_app("examples.components.cell_renderer_custom_components", make_layout=make_tabs),
        #  up_next("text"),
    ],
)
