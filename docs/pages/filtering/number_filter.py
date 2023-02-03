"""
AG Grid Number Filters
"""
from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=3,
    description=app_description,
    title="Dash AG Grid Filtering",
)


text1 = """
# Number Filter
Number filters allow you to filter number data.

The Provided Filters and Simple Filters pages explain the parts of the Number Filter that are the same as the other Provided Filters. This page builds on that and explains some details that are specific to the Number Filter.

### Number Filter Parameters
Number Filters are configured though the filterParams attribute of the column definition (INumberFilterParams interface):

- allowedCharPattern (string) When specified, the input field will be of type text instead of number, and this will be used as a regex of all the characters that are allowed to be typed. This will be compared against any typed character and prevent the character from appearing in the input if it does not match, in supported browsers (all except Safari).
- alwaysShowBothConditions (boolean) By default, only one condition is shown, and a second is made visible once a first condition has been entered. Set this to true to always show both conditions. In this case the second condition will be disabled until a first condition has been entered. Default: false
- `buttons` Specifies the buttons to be shown in the filter, in the order they should be displayed in. The options are:
    - 'apply': If the Apply button is present, the filter is only applied after the user hits the Apply button.
    - 'clear': The Clear button will clear the (form) details of the filter without removing any active filters on the column.
    - 'reset': The Reset button will clear the details of the filter and any active filters on that column.
    - 'cancel': The Cancel button will discard any changes that have been made to the filter in the UI, restoring the applied model.
- `closeOnApply` (boolean) If the Apply button is present, the filter popup will be closed immediately when the Apply or Reset button is clicked if this is set to true. Default: false
- `debounceMs` (number) Overrides the default debounce time in milliseconds for the filter. Defaults are:
    - TextFilter and NumberFilter: 500ms. (These filters have text field inputs, so a short delay before the input is formatted and the filtering applied is usually appropriate).
    - DateFilter and SetFilter: 0ms
- `defaultJoinOperator` By default, the two conditions are combined using AND. You can change this default by setting this property. Options: AND, OR
- `defaultOption` (string) The default filter option to be selected.
- `filterOptions` Array of filter options to present to the user. See Filter Options.
- `filterPlaceholder` (string) Placeholder text for the filter textbox
- `inRangeInclusive` (boolean) If true, the 'inRange' filter option will include values equal to the start and end of the range.
- `includeBlanksInEquals` (boolean) If true, blank (null or undefined) values will pass the 'equals' filter option.
- `includeBlanksInGreaterThan` (boolean) If true, blank (null or undefined) values will pass the 'greaterThan' and 'greaterThanOrEqual' filter options.
- `includeBlanksInLessThan` (boolean) If true, blank (null or undefined) values will pass the 'lessThan' and 'lessThanOrEqual' filter options.
- `includeBlanksInRange` (boolean) If true, blank (null or undefined) values will pass the 'inRange' filter option.
- `numberParser` (Function) Typically used alongside allowedCharPattern, this provides a custom parser to convert the value entered in the filter inputs into a number that can be used for comparisons.
- `readOnly` (boolean) If set to true, disables controls in the filter to mutate its state. Normally this would be used in conjunction with the Filter API. See Read-only Filter UI. Default: false
- `suppressAndOrCondition` (boolean) If true, the filter will only allow one condition.Default: false


### Custom Number Support
By default, the Number Filter uses HTML5 number inputs. However, these have mixed browser support, particularly around locale-specific nuances, e.g. using commas rather than periods for decimal values. You might also want to allow users to type other characters e.g. currency symbols, commas for thousands, etc, and still be able to handle those values correctly.

For these reasons, the Number Filter allows you to control what characters the user is allowed to type, and provide custom logic to parse the provided value into a number to be used in the filtering. In this case, a text input is used with JavaScript controlling what characters the user is allowed (rather than the browser).

> Note - the custom number support is is not yet available in Dash.  This feature and example comming soon. Please see Column Filters Overview and the Text filter Sections for more examples.

"""



layout = html.Div(
    [
        make_md(text1),

    ],
)
