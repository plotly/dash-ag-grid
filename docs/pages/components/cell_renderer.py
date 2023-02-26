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

> In dash-ag-grid, cell renderer function must be written in JavasScript and placed in the `dashAgGridComponentFunctions.js` file in the `assets` folder.

Please see the [AG Grid documentation](https://www.ag-grid.com/react-data-grid/component-cell-renderer/) for complete information on cell renderer components,



### Value Formatter vs Cell Renderer
A cell renderer allows you to put whatever HTML you want into a cell. This sounds like value formatters and a cell renderers have cross purposes, so you may be wondering, when do you use each one and not the other?

The answer is that value formatters are for text formatting and cell renderers are for when you want to include HTML markup and potentially functionality to the cell. So for example, if you want to put punctuation into a value, use a value formatter, but if you want to put buttons or HTML links use a cell renderer. It is possible to use a combination of both, in which case the result of the value formatter will be passed to the cell renderer.

### Markdown component vs Cell Renderer
The <dccLink href='/components/markdown' children='Markdown' /> component is a .convenient and easy way to  format text. You can also use the markdown component to render
 raw HTML, however, this method is vulnerable [XSS attacks.](https://owasp.org/www-community/attacks/xss/).  The cell
 render is a safer way of using HTML, and it's not necessary to set the grid to `dangerously_allow_code=True`.
 
 
### Provided Cell Renderers
The grid comes with some provided cell renderers out of the box. These cell renderers cover some common complex cell rendering requirements.

- Group Cell Renderer: (Enterprise only) For showing group details with expand & collapse functionality when using any of the Row Grouping, Master Detail or Tree Data.
- Show Change Cell Renderers: For animating changes when data is changing.  See examples in <dccLink href='/rendering/change-cell-renderers' children='Rendering' /> . 

### Custom Cell Renderers

Here are a few examples to get you started making your own custom components.  You can see what's available so far in [GitHub]().
We would like to build a library of components, so if you create a component, please consider sharing either on the
Dash forum or open an issue in GitHub so we can add it to the collection.

### Example 1 - Add Links to the grid

This example uses a simple function to create a link to yahoo finance based on the stock ticker in the cell.
"""

text2 = """

### Example 2 - Add Buttons to the grid
This example shows how to add buttons to cells in the gird.  The function that creates this button component also updates a "n_clicks" prop which can be used in a Dash callback.
 Note that the button is styled with Bootstrap classnames.

"""

text3 = """

### Example 3 - More Custom Cell renderers

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
        example_app("examples.components.cell_renderer_custom_components", make_layout=make_tabs),
        #  up_next("text"),
    ],
)
