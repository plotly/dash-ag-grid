from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md, make_feature_card
from utils.utils import app_description


register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid Components - cell renderers",

)

text1 = """
# Cell Renderers

By default the grid renders values in the cells as strings. If you want something more complex you can use a cell renderer.

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

-------------------
` `  
` `  

## Custom Cell Renderers

### Registering custom components

In order to safely render custom components in Dash, they must be added to the dash-ag-grid namespace. Dash will register
 the components defined in the `window.dashAgGridComponentFunctions` namespace with the grid. See the  <dccLink href='/getting-started/beyond-the-basics' children='Beyond the Basics' />  section for more information.

Before running Example 1, create a file called `dashAgGridComponentFunctions.js` in the `assets` folder then add this component:

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

The code snippet above creates the `dashAgGridComponentFunctions` namespace and defines the `Stocklink` component that we will use in Example 1.

When the component is registered, the grid will make the grid APIs, a number of utility methods as well as the cell & row values available to you via `props`.
For more information see the [AG Grid docs](https://www.ag-grid.com/react-data-grid/component-cell-renderer/#cell-renderer-component-2).
  We will cover this in more detail later, but for now, note that `props.value` is the cell value in the "Stock Ticker" column in Example 1.


Create elements in the component using: 
```text
React.createElement(element type, {element props}, children)
```

In Example 1  we make the link by creating an html "a" element with an `href` prop like this:
```
React.createElement(
        'a',
        {href: 'https://finance.yahoo.com/quote/' + props.value},
        props.value
);
```



` `  
` `  


#### Example 1:  Simple Custom Component

This is a simple example of registering a custom component to render the stock ticker as a link to Yahoo Finance.

"""

text2 = """

` `  
` `  

### Callbacks with custom components
To use the custom components in a callback, the component must call the `setData()` function, which will update the
 Dash prop `cellRendererData`.  Use this prop to get information on which component triggered the callback.

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


#### Example 2: Button component with callback
This example shows how to add HTML buttons to cells in the grid and use the `cellRendererData` prop in the callback
to see which button triggered the callback.

Note the following:
 - The button component is defined as `Button` in the `dashAgGridComponentFunctions.js` file in the assets folder. 
 - `cellRendererData` prop is updated by calling `setData()` in the component
 - The `cellRendererData` prop is used as an Input of a Dash callback, and it contains information on which button was clicked. 
 - The HTML button is styled with Bootstrap class names passed to the component in the `cellRendererParams` prop from the Dash app.
 
"""

text3 = """

` `  
` `  

### Using other component libraries.

It's possible to make custom components for use with the `cellRenderer` using any of the component modules you have
 imported in your Dash app. In this section we will show how to add the following components:
 - Button from Dash Bootstrap Components
 - Graph from Dash Core Components
 - Button from Dash Mantine Components
 - Icons from Dash Iconify
  
  

#### Example 3: Cell Renderer with `dbc.Button` 
This is the same app as Example 2 above, except instead of creating an HTML button, we'll use the `Button` component from the `dash-bootstrap-components` library. 
 
Since we have imported `dash_bootstrap_components` in our app, we can access the `dbc.Button` component like this:
```
window.dash_bootstrap_components.Button
```
You can make a custom component with `React.createElement` with a `dbc.Button` instead of a regular HTML Button like this:  
 
```
React.createElement(window.dash_bootstrap_components.Button, {dbc.Button props}, children)
```

Note the following:
 - The button is defined as `DBC_Button_Simple` in the `dashAgGridComponentFunctions.js` file in the assets folder. 
 - The callback works the same way as the button in Example 2
 - The button is styled with the `dbc.Button` component's `color` prop, and is passed to the component in the
  `cellRendererParams` prop from the Dash app.


"""


text4 = """

` `  
` `  

#### Example 4:  Cell Renderer with `dcc.Graph` 

In this example we will render a plotly figure in a custom `dcc.Graph` component in the grid. Since we have imported
 `dash_core_components` in our app, we can access the `dcc.Graph` component like this:
```
window.dash_core_components.Graph
```
So now we can make a component with `React.createElement` with `dcc.Graph` like this:

```
React.createElement(window.dash_core_components.Graph, {dcc.Graph props}, children)
```

 
In the example below note the following:
 - The graph component is defined as `DCC_GraphClickData` in the `dashAgGridComponentFunctions.js` file in the assets folder
 - `cellRendererData` prop is updated by calling `setData()` with the clickData in the figure.
 - The figure is a plotly figure from the "graph" column of the dataframe. 

"""

text5 = """

` `  
` `  

### Example 5:  Cell Render with `dmc.Button` with DashIconify icons.

This example is similar to Example 3 and 4, but uses the Dash Mantine Components and Dash Iconify libraries.

In this example, note the following:
- The button is defined as `DMC_Button` in the `dashAgGridComponentFunctions.js` file in the assets folder. 
- All three buttons use the same component, and are customized for the color, icons, etc buy passing props to the component using the
 `cellRendererParams` prop.

"""


text6 = """

` `  
` `  

#### Example 6:  Including extra data in `cellRenderData`

This example shows how to pass extra data from a custom component to Dash for use in a callback.  We pass the state of
 the checkbox to the `value` key of the `cellRendererData` prop.   We do this by calling the function `setData(checked)` in the component.

Compare the data in the callback in this example to the Button example above.  You will see that the in the Button example,
there is no `value` key in the `cellRendererData`.

"""

text7 = """

` `  
` `  

#### Example 7:  Custom Image Component

This example is another simple example of creating a custom component with data passed back to Dash in the callback. 

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

text8 = """

` `  
` `  

#### Example 8:  More Custom Cell renderers

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

img9="https://user-images.githubusercontent.com/72614349/231599764-fc0a54ce-9957-4f2c-a2d6-a8254b5588f9.png"

text9= """
` `  
` `  

#### Example 9:  My Portfolio Demo

Here is another example app with custom components- this one is made with dash-mantine-components.   
This is just an image since it includes live stock data.  Please see the code in [Github](https://github.com/plotly/dash-ag-grid/tree/dev/more_examples/demo_stock_portfolio_dmc)

"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.components.cell_renderer_link", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.components.cell_renderer_button", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.components.cell_renderer_dbc_button_simple", make_layout=make_tabs),
        make_md(text4),
        example_app("examples.components.cell_renderer_graph", make_layout=make_tabs),
        make_md(text5),
        example_app("examples.components.cell_renderer_dmc_button", make_layout=make_tabs),
        make_md(text6),
        example_app("examples.components.cell_renderer_checkbox", make_layout=make_tabs),
        make_md(text7),
        example_app("examples.components.cell_renderer_img", make_layout=make_tabs),


        make_md(text8),
        example_app("examples.components.cell_renderer_custom_components", make_layout=make_tabs),
        make_md(text9),
        make_feature_card(img9, "")

        #  up_next("text"),
    ],
)
