from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid - Text Filter",
)

text1 = """
# Text Filter
Text filters allow you to filter string data.

The Provided Filters and Simple Filters pages explain the parts of the Text Filter that are the same as the other Provided Filters. This page builds on that and explains some details that are specific to the Text Filter.

### Text Filter Parameters
Text Filters are configured though the filterParams attribute of the column definition (ITextFilterParams interface):

- `alwaysShowBothConditions` (boolean) By default, only one condition is shown, and a second is made visible once a first condition has been entered. Set this to true to always show both conditions. In this case the second condition will be disabled until a first condition has been entered. Default: False
- `buttons` Specifies the buttons to be shown in the filter, in the order they should be displayed in. The options are:
    - 'apply': If the Apply button is present, the filter is only applied after the user hits the Apply button.
    - 'clear': The Clear button will clear the (form) details of the filter without removing any active filters on the column.
    - 'reset': The Reset button will clear the details of the filter and any active filters on that column.
    - 'cancel': The Cancel button will discard any changes that have been made to the filter in the UI, restoring the applied model.
- `caseSensitive` (boolean) By default, text filtering is case-insensitive. Set this to true to make text filtering case-sensitive. Default: false
- `closeOnApply` (boolean) If the Apply button is present, the filter popup will be closed immediately when the Apply or Reset button is clicked if this is set to true. Default: false
- `debounceMs` (number) Overrides the default debounce time in milliseconds for the filter. Defaults are:
    - TextFilter and NumberFilter: 500ms. (These filters have text field inputs, so a short delay before the input is formatted and the filtering applied is usually appropriate).
    - DateFilter and SetFilter: 0ms
- readOnly (boolean) If set to true, disables controls in the filter to mutate its state. Normally this would be used in conjunction with the Filter API. See Read-only Filter UI. Default: false
- `defaultJoinOperator` By default, the two conditions are combined using AND. You can change this default by setting this property. Options: AND, OR
- `defaultOption` (string) The default filter option to be selected.
- `filterOptions`  Array of filter options to present to the user. See Filter Options.
- `filterPlaceholder` Placeholder text for the filter textbox
- `suppressAndOrCondition` (boolean) If true, the filter will only allow one condition. Default: false
- `textFormatter` (Function) Formats the text before applying the filter compare logic. Useful if you want to substitute accented characters, for example.
- `textMatcher` (Function) Used to override how to filter based on the user input.
- `trimInput` (boolean) If true, the input that the user enters will be trimmed when the filter is applied, so any leading or trailing whitespace will be removed. If only whitespace is entered, it will be left as-is. If you enable trimInput, it is best to also increase the debounceMs to give users more time to enter text. Default: false


### Text Matcher
By default the text filter performs strict case-insensitive text filtering, i.e. if you provide `\['1,234.5USD','345GBP'\]` as data for a text column:

- __contains '1,2'__ will show 1 value: ['1,234.5USD']
- __contains '12'__ will show 0 values
- __contains '$'__ will show 0 values
- __contains 'gbp'__ will show 1 value ['345GBP']

You can change the default behaviour by providing your own `textMatcher`, which allows you to provide your own logic to decide when to include a row in the filtered results.
(Note - not available in dash yet)

### Text Formatter
By default, the grid compares the text filter with the values in a case-insensitive way, by converting both the filter text and the values to lower-case and comparing them; for example, 'o' will match 'Olivia' and 'Salmon'. If you instead want to have case-sensitive matches, you can set `caseSensitive = True` in the `filterParams`, so that no lower-casing is performed. In this case, 'o' would no longer match 'Olivia'.


### Example: Text Filter
- The Athlete column has only two filter options: `filterOptions = ['contains', 'notContains']`
- The Athlete column has a debounce of 200ms (`debounceMs = 200`).
- The Athlete column filter has the AND/OR additional filter suppressed (`suppressAndOrCondition = True`)
- The Country column has only one filter option: `filterOptions = ['contains']`
- The Country column will trim the input when the filter is applied (`trimInput = True`)
- The Country column filter has a debounce of 1000ms (`debounceMs = 1000`)
- The Sport column has a different default option (`defaultOption = 'startsWith'`)
- The Sport column filter is case-sensitive (`caseSensitive = True`)

> Note:  See the Column Filters Overview section for more filter options

"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.filtering.text_filter", make_layout=make_tabs),
    ],
)
