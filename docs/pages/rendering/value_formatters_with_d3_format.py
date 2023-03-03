from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description

register_page(
    __name__,
    order=3,
    description=app_description,
    title="Dash AG Grid Rendering - Number and Date Formatting with d3.format",
)

text1 = """
# Formatting numbers and dates with d3.Format

See the [Value Formatters Intro]() for more information on getting started with `valueFormatter`.


### Formatting Numbers with `d3-format`
Dash AG Grid includes the d3-format library, so you have access to all [d3-format](https://github.com/d3/d3-format) functions to use with `valueFormatter`.

The basic syntax for the d3 function is: `d3.format(specifier)(value)`  

The specifier is based on the [Python's Format Specification](https://docs.python.org/3/library/string.html#format-specification-mini-language).


For example:
```
d3.format(".0%")(0.123);  # rounded percentage, "12%"
d3.format("($.2f")(-3.5); # localized fixed-point currency, "(£3.50)"
d3.format("+20")(42);     # space-filled and signed, "                 +42"
d3.format(".^20")(42);    # dot-filled and centered, ".........42........."
d3.format(".2s")(42e6);   # SI-prefix with two significant digits, "42M"
d3.format("#x")(48879);   # prefixed lowercase hexadecimal, "0xbeef"
d3.format(",.2r")(4223);  # grouped thousands with two significant digits, "4,200"
```
For more options, see [d3-format examples](https://observablehq.com/@d3/d3-format)


In dash-ag-grid, use the d3.format function in the column definitions like this:

```
# example valueFormatter for currency
columnDefs = [
    {
        "valueFormatter": {"function": "d3.format('($,.2f')(params.value)"},
    },
]
```


### Example:  Number formatting

Here is a simple example of formatting numbers with d3.format function:
- The "Quantity" column has commas for the thousands seperators and is rounded to 1 decimal place.
- The "Balance" column is currency with negative numbers in ( )
- The "Rate" column is percentage, rounded to 1 decimal place.

"""

text1b= """
### Example: d3.format specifiers
Here are examples of formatting numbers with some of the specifiers available in the `d3.format` function.
"""

text2 = (
    """
### Locales
Locales adapt the behavior of d3-format to various languages and places. 

The definition may include the following properties:

- `decimal` - the decimal point (e.g., ".").
- `thousands` - the group separator (e.g., `","`).
- `grouping` - the array of group sizes (e.g., `[3]`), cycled as needed.
- `currency` - the currency prefix and suffix (e.g., `["$", ""]`).
- `numerals` - optional; an array of ten strings to replace the numerals `0-9`.
- `percent` - optional; the percent sign (defaults to `"%"`).
- `minus` - optional; the minus sign (defaults to `"−"`).
- `nan` - optional; the not-a-number value (defaults `"NaN"`).

Note that the `thousands` property is a misnomer, as the grouping definition allows groups other than thousands.




The default locale for `d3.format` is U.S. English, which sets:

```
{
  "decimal": ".",
  "thousands": ",",
  "grouping": [3],
  "currency": ["$", ""]
}
```

To render currency numbers in French, you could override these default marks by specifying instead a locale such as:

```
{
  "decimal": ",",
  "thousands": " ",
  "grouping": [3],
  "currency": ["", "€"],
  "nan": "",
}
```
The decimal separator becomes a comma, thousands are separated by a space, and the default currency mark, the euro symbol, appears after the number.
This example includes changing the default for not-a-number from `NaN` to `""`

Locales are not loaded by default - you can find them [here](https://github.com/d3/d3-format/tree/main/locale). Their definition can be fed to `d3.formatLocale`:

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
"valueFormatter": {"function": f"{locale_en_GB}.format('$,.2f')(params.value)"},
```

  
### Example Formatting with locale
    
In this example, each column is formatted with the specifier `'$,.2f'`  The  locale determines how the numbers will be displayed.
Note that we also set a custom NaN value in the "France" column. In stead of displaying "NaN" it will be blank

"""

)

text3 = """
### Editable example

In this table try changing the specifier and the values.

"""


text4 = """
### Formatting Dates and Times with `d3-time-format`

Dash AG Grid includes the d3-time-format library, so you have access to all [d3-time-format](https://github.com/d3/d3-time-format) functions to use with `valueFormatter`

The basic syntax for formatting a date object is:
```
formatted_date_string = d3.timeFormat(specifier)(date object)
```

Note that even if your datetime data is an object on the server, when it's sent to the grid in the browser it's converted to a string. 
In order to convert the string back to a date on the client, use a parser:
```
date_obj= d2.timeParse(specifier)(date string)
``` 
When the date is converted to a JavaScript date object, then the AG Grid date filter `agDateColumnFilter` will work out
 of the box, and no additional date filter comparator functions are required.

Here are the specifiers:

- %a - abbreviated weekday name.*
- %A - full weekday name.*
- %b - abbreviated month name.*
- %B - full month name.*
- %c - the locale’s date and time, such as %x, %X.*
- %d - zero-padded day of the month as a decimal number `[01,31]`.
- %e - space-padded day of the month as a decimal number `[ 1,31]`; equivalent to `%_d`.
- %f - microseconds as a decimal number `[000000, 999999]`.
- %g - ISO 8601 week-based year without century as a decimal number `[00,99]`.
- %G - ISO 8601 week-based year with century as a decimal number.
- %H - hour (24-hour clock) as a decimal number `[00,23]`.
- %I - hour (12-hour clock) as a decimal number `[01,12]`.
- %j - day of the year as a decimal number `[001,366]`.
- %m - month as a decimal number `[01,12]`.
- %M - minute as a decimal number `[00,59]`.
- %L - milliseconds as a decimal number `[000, 999]`.
- %p - either AM or PM.*
- %q - quarter of the year as a decimal number `[1,4]`.
- %Q - milliseconds since UNIX epoch.
- %s - seconds since UNIX epoch.
- %S - second as a decimal number `[00,61]`.
- %u - Monday-based (ISO 8601) weekday as a decimal number `[1,7]`.
- %U - Sunday-based week of the year as a decimal number `[00,53]`.
- %V - ISO 8601 week of the year as a decimal number `[01, 53]`.
- %w - Sunday-based weekday as a decimal number `[0,6]`.
- %W - Monday-based week of the year as a decimal number `[00,53]`.
- %x - the locale’s date, such as `%-m/%-d/%Y.*`
- %X - the locale’s time, such as `%-I:%M:%S %p.*`
- %y - year without century as a decimal number `[00,99]`.
- %Y - year with century as a decimal number, such as 1999.
- %Z - time zone offset, such as -0700, -07:00, -07, or Z.
- %% - a literal percent sign (%).
"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.rendering.value_formatters_d3_intro", make_layout=make_tabs),
        example_app("examples.rendering.value_formatters_gapminder", make_layout=make_tabs),
        make_md(text1b),
        example_app("examples.rendering.value_formatters", make_layout=make_tabs),
        make_md(text2),
        example_app(
            "examples.rendering.value_formatters_locale", make_layout=make_tabs
        ),
        make_md(text3),
        example_app(
            "examples.rendering.value_formatters_locale_editable", make_layout=make_tabs
        ),
        make_md(text4),
        example_app("examples.rendering.value_formatters_date", make_layout=make_tabs),
        example_app(
            "examples.rendering.value_formatters_datetime", make_layout=make_tabs
        ),
        # up_next("text"),
    ],
)
