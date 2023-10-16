from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description

register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid Rendering - Value Getters",
)

text1 = """
# Value Getters
Normally columns are configured with `field` attributes, so the column knows what `field` to take values from in the data. Instead of providing `field` it is possible to provide a `valueGetter` instead. A Value Getter is a function that gets called allowing values to be pulled from literally anywhere, including executing any expressions you wish along the way.

You should use `field` most of the time. Use value getters when retrieving the data requires more logic, including executing your own expressions (similar to what a spreadsheet would do).

- `valueGetter` - Function or expression. Gets the value from your data for display.

```
# example value getter, adds two fields together
columnDefs = [
    {
        "valueGetter": {"function": "params.data.firstName + params.data.lastName;"},
    },
]
```
> All valueGetters must be pure functions. That means, given the same state of your data, it should consistently return the same result. This is important as the grid will only call your valueGetter once during a redraw, even though the value may be used multiple times. For example, the value will be used to display the cell value, however it can additionally be used to provide values to an aggregation function when grouping, or can be used as input to another valueGetter via the `params.getValue()` function.

### Example Value Getters
The example below demonstrates `valueGetter`. The following can be noted from the demo:

- Columns A and B are simple columns using field
- Value Getters are used in all subsequent columns as follows:

  - Column '#' prints the row number, taken from the Row Node.
  - Column 'A+B' adds A and B.
  - Column 'A * 1000' multiplies A by 1000.
  - Column 'B * 137' multiplies B by 137.
  - Column 'Random' doesn't take any value from the data, rather it returns a random value.
  - Column 'Chain' takes the value 'A+B' and works on it further, thus chaining value getters.
  - Column 'Const' returns back the same value for each column.
"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.rendering.value_getters", make_layout=make_tabs),

    ],
)
