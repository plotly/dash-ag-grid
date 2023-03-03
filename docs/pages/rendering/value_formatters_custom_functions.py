from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description

register_page(
    __name__,
    order=5,
    description=app_description,
    title="Dash AG Grid Rendering - valueFormatter with custom functions",
)

text1 = """
# Value Formatters with custom functions

For more information on `valueFormatter` see:

- The [Value Formatter Intro] section.
- The number and date formatting in the [Value Formatters with d3.format section]().

### Example 1: Using `Intl.NumberFormat`

Rather than using `d3.format`, this example formats currency in different locales using [Intl.NumberFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat)

The custom functions are registered in the `dashAgGridComponentFunctions.js` file in the `assets` folder.

Here is an example:
```
var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.EUR = function(number) {
  return Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(number);
}
```

Then use the function in the `columnDefs` like this:
```
columnDefs = [
     {"headerName": "Euro", "field": "EUR", "valueFormatter": {"function": "EUR(params.value)"}},
 ]
```

"""

text2= """
### Example 2:  Custom Function for blank when NaN

This example adds more features to the function that formats currency and percentages.  It will return blanks
instead of NaN when text or other invalid numbers are entered in the January or Budget columns.


"""

text3 ="""
### More examples
More examples coming soon!   If you have written a custom function, please consider sharing.  Simply open a [GitHub issue](https://github.com/plotly/dash-ag-grid/issues) and post a minimal example there, then we'll add it to the docs. 

"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.rendering.value_formatters_intl_currency", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.rendering.value_formatters_intl_budget", make_layout=make_tabs),
        make_md(text3)

        # up_next("text"),
    ],
)
