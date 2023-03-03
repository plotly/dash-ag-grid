from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description

register_page(
    __name__,
    order=3,
    description=app_description,
    title="Dash AG Grid Rendering - valueFormatter: Introduction",
)

text1 = """
# Value Formatters
Value formatters allow you to format values for display. This is useful when data is one type (e.g. numeric) but needs to be converted for human reading (e.g. putting in currency symbols and number formatting).
Note that it does not change the data, only how it appears in the grid.


- `valueFormatter` (string | ValueFormatterFunc) A function or expression to format a value, should return a string. Not used for CSV export or copy to clipboard, only for UI cell rendering.

You can supply your own custom function for displaying values, or you can use the functions defined in `d3-format` and the `d3-time-format` libraries.

### Value Formatter vs Cell Renderer
A cell renderer allows you to put whatever HTML you want into a cell. This sounds like value formatters and a cell renderers have cross purposes, so you may be wondering, when do you use each one and not the other?

The answer is that value formatters are for text formatting and cell renderers are for when you want to include HTML markup and potentially functionality to the cell. So for example, if you want to put punctuation into a value, use a value formatter, but if you want to put buttons or HTML links use a cell renderer. It is possible to use a combination of both, in which case the result of the value formatter will be passed to the cell renderer.


### Example:  Formatting text with functions

In this example note that:

- The "Account" column displays the text in upper case
- The "Balance" column prepends a $ sign before the number
- The "Name" column displays the name within other text
- The "Grade" column displays the number grades as either "Pass" or "Fail"

To see more advanced formatting, see:
  - The number and date formatting with the [Value Formatters with d3.format section]()
  - [Value Formatters with Custom functions]() section.


"""



layout = html.Div(
    [
        make_md(text1),
        example_app("examples.rendering.value_formatters_intro", make_layout=make_tabs),

        # up_next("text"),
    ],
)
