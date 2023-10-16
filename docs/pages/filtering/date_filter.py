"""
AG Grid Date Filters
"""
from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=4,
    description=app_description,
    title="Dash AG Grid - Date Filtering",
)


text1 = """

# Date Filter
Date filters allow you to filter date data. The Provided Filters and Simple Filters pages explain the parts of the date filter that are the same as the other provided filters. This page builds on that and explains some details that are specific to the date filter.

### Date Filter Parameters
Date Filters are configured though the filterParams attribute of the column definition:

- `alwaysShowBothConditions` (boolean) By default, only one condition is shown, and a second is made visible once a first condition has been entered. Set this to true to always show both conditions. In this case the second condition will be disabled until a first condition has been entered. Default: false
- `buttons` Specifies the buttons to be shown in the filter, in the order they should be displayed in. The options are:
    - 'apply': If the Apply button is present, the filter is only applied after the user hits the Apply button.
    - 'clear': The Clear button will clear the (form) details of the filter without removing any active filters on the column.
    - 'reset': The Reset button will clear the details of the filter and any active filters on that column.
    - 'cancel': The Cancel button will discard any changes that have been made to the filter in the UI, restoring the applied model.
- `closeOnApply` (boolean) If the Apply button is present, the filter popup will be closed immediately when the Apply or Reset button is clicked if this is set to true. Default: false

- `browserDatePicker` (boolean) This is only used if a date component is not provided. By default the grid will use the browser date picker in Chrome and Firefox and a plain text box for all other browsers (This is because Chrome and Firefox are the only current browsers providing a decent out-of-the-box date picker). If this property is set to true, the browser date picker will be used regardless of the browser type. If set to false, a plain text box will be used for all browsers.
- `comparator` (Function) -Required if the data for the column are not native JS Date objects.
- `debounceMs` (number) Overrides the default debounce time in milliseconds for the filter. Defaults are:
    - TextFilter and NumberFilter: 500ms. (These filters have text field inputs, so a short delay before the input is formatted and the filtering applied is usually appropriate).
    - DateFilter and SetFilter: 0ms
- `defaultJoinOperator` By default, the two conditions are combined using AND. You can change this default by setting this property. Options: AND, OR
- `defaultOption` (string) The default filter option to be selected.
- `filterOptions` (IFilterOptionDef | ISimpleFilterModelType) Array of filter options to present to the user. See Filter Options.
- `filterPlaceholder` (FilterPlaceholderFunction | string) Placeholder text for the filter textbox
- `inRangeFloatingFilterDateFormat` (string) Defines the date format for the floating filter text when an in range filter has been applied. Default: YYYY-MM-DD
- `inRangeInclusive` (boolean) If true, the 'inRange' filter option will include values equal to the start and end of the range.
- `includeBlanksInEquals` (boolean) If true, blank (null or undefined) values will pass the 'equals' filter option.
- `includeBlanksInGreaterThan` (boolean) If true, blank (null or undefined) values will pass the 'greaterThan' and 'greaterThanOrEqual' filter options.
- `includeBlanksInLessThan` (boolean) If true, blank (null or undefined) values will pass the 'lessThan' and 'lessThanOrEqual' filter options.
- `includeBlanksInRange` (boolean) If true, blank (null or undefined) values will pass the 'inRange' filter option.
- `maxValidYear` (number) This is the maximum year that may be entered in a date field for the value to be considered valid. Default is no restriction.
- `minValidYear` (number) This is the minimum year that may be entered in a date field for the value to be considered valid. Default: 1000
- `readOnly` (boolean) If set to true, disables controls in the filter to mutate its state. Normally this would be used in conjunction with the Filter API. See Read-only Filter UI. Default: false
- `suppressAndOrCondition` (boolean) If true, the filter will only allow one condition. Default: false

### Date Selection Component
By default the grid will use the browser-provided date picker for Chrome and Firefox (as we think it's nice), but for all other browsers it will provide a simple text field. To override this and provide a custom date picker, see [Date Component](https://www.ag-grid.com/react-data-grid/component-date/).

### Date Filter Comparator

Dates can be represented in your data in many ways e.g. as a Date object, as a string in a particular format such as '26-MAR-2020', or something else. How you represent dates will be particular to your application.

By default, the date filter assumes you are using JavaScript Date objects. If this is the case, the date filter will work
 out of the box. However, in Dash,  when a date object is sent from the server to the client it is serialized to JSON 
 and becomes a string.  To turn a date string into a JavaScript Date object, `dash-ag-grid` has included the [d3-time-format]() library.
 
You can use `d3.timeParse` to create a JavaScript Date object from a string.  

```
date_obj= d3.timeParse(specifier)(date string)
```

For example, if you had a column with a `date` field, here are ways to create a date object based on the date string:

```
# date string "2023-01-30"
date_obj = "d3.timeParse('%Y-%m-%d')(data.date)"

# date string "Sun Jan 01, 2023"
date_obj = "d3.timeParse(%a %b %d, %Y')(data.date)"

```


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


To see examples of displaying dates in various formats please see the [Value Formatters](/rendering/value-formatters) section
 

> Note - the filter works for dates only, not datetime.  So if your date string looks like "2023-01-01T22:00:00" you will
first need to change it to date string i.e. "2023-01-01"

 
If you prefer to write your own date filter comparator function in JavaScript to perform the date comparison, please see the [AG Grid docs](https://www.ag-grid.com/react-data-grid/filter-date/#date-filter-comparator).

### Example: Date Filter
The example below shows the date filter in action, using some of the configuration options discussed above:

- The Date column is using a Date Filter.
- We use d3.timeParse to create a JavaScript Date object so the filter works correctly.
- The native date picker is forced to be used in every browser.
- The minimum valid year is set to 2000, and maximum valid year is 2021. Dates outside this range will be considered invalid, and will:
    - Deactivate the column filter. This avoids the filter getting applied as the user is typing a year - for example suppose the user is typing the year 2008, the filter doesn't execute for values 2, 20 or 200 (as the text 2008 is partially typed).
    - Be highlighted with a red border (default theme) or other theme-appropriate highlight.


> #### See more date filter examples:
> - <dccLink href='/rendering/value-formatters-with-d3-format' children='Rendering - Value formatters with d3' /> (last 3 examples)
> - <dccLink href='/filtering/column-filters-overview' children='Filtering - Column filters overview' />  (first example)
> - <dccLink href='/rows/row-sorting' children='Rows - Row Sorting' /> (Example 2 sorting dates)
> 


"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.filtering.date_filter", make_layout=make_tabs),
    ],
)
