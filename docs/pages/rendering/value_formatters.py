from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description

register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid Rendering - Number Formatting",
)

text1 = """
# Value Formatters
Value formatters allow you to format values for display. This is useful when data is one type (e.g. numeric) but needs to be converted for human reading (e.g. putting in currency symbols and number formatting).
Note that it does not change the data, only how it appears in the grid.


`valueFormatter` (string | ValueFormatterFunc) A function or expression to format a value, should return a string. Not used for CSV export or copy to clipboard, only for UI cell rendering.

### Formatting Numbers
Dash AG Grid includes the d3-format library, so you have access to all [d3-format](https://github.com/d3/d3-format) functions to use with `valueFormatter`

The basic syntax for the function is:
`d3.format(specifier)(value)`

For example 
```
d3.format(".0%")(0.123);  # rounded percentage, "12%"
d3.format("($.2f")(-3.5); # localized fixed-point currency, "(£3.50)"
d3.format("+20")(42);     # space-filled and signed, "                 +42"
d3.format(".^20")(42);    # dot-filled and centered, ".........42........."
d3.format(".2s")(42e6);   # SI-prefix with two significant digits, "42M"
d3.format("#x")(48879);   # prefixed lowercase hexadecimal, "0xbeef"
d3.format(",.2r")(4223);  # grouped thousands with two significant digits, "4,200"
```

See also this site for more [d3-format examples](https://observablehq.com/@d3/d3-format)
"""

text2 = (
    """
### Locales
Locales adapt the behavior of d3-format to various languages and places. The default locale for `d3.format` is U.S. English, which sets:

```
{
  "decimal": ".",
  "thousands": ",",
  "grouping": [3],
  "currency": ["$", ""]
}
```

To render numbers in French, you could override these default marks by specifying instead a locale such as:

```
{
  "decimal": ",",
  "thousands": " ",
  "grouping": [3],
  "currency": ["", "€"]
}
```
The decimal separator becomes a comma, thousands are separated by a space, and the default currency mark, the euro symbol, appears after the number. (The actual locale for French is more complicated than that, as it also contains non-breaking spaces in accordance with French typography rules.)

Locales are not loaded by default. Their definition can be fed to `d3.formatLocale`:

```
locale_en_GB = """
    """d3.formatLocale({
 "decimal": ".",
  "thousands": ",",
  "grouping": [3],
  "currency": ["£", ""]
})"""
    """
```
Then in can be used in the `valueFormatter` like this:
```
"valueFormatter": {"function": f"{locale_en_GB}.format('$,.2f')(value)"},
```"""
)

text3 = """
### Editable example

In this table try changing the specifier and the values.

"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.rendering.value_formatters", make_layout=make_tabs),
        make_md(text2),
        example_app(
            "examples.rendering.value_formatters_locale", make_layout=make_tabs
        ),
        make_md(text3),
        example_app(
            "examples.rendering.value_formatters_locale_editable", make_layout=make_tabs
        ),
        # up_next("text"),
    ],
)
