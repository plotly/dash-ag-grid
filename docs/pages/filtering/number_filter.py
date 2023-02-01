txt = """
# Number Filter
Number filters allow you to filter number data.

The Provided Filters and Simple Filters pages explain the parts of the Number Filter that are the same as the other Provided Filters. This page builds on that and explains some details that are specific to the Number Filter.

### Number Filter Parameters
Number Filters are configured though the filterParams attribute of the column definition (INumberFilterParams interface):

- allowedCharPattern
string
When specified, the input field will be of type text instead of number, and this will be used as a regex of all the characters that are allowed to be typed. This will be compared against any typed character and prevent the character from appearing in the input if it does not match, in supported browsers (all except Safari).
- alwaysShowBothConditions
boolean
By default, only one condition is shown, and a second is made visible once a first condition has been entered. Set this to true to always show both conditions. In this case the second condition will be disabled until a first condition has been entered.
Default: false
- buttons
FilterButtonType[]
Specifies the buttons to be shown in the filter, in the order they should be displayed in. The options are:
'apply': If the Apply button is present, the filter is only applied after the user hits the Apply button.
'clear': The Clear button will clear the (form) details of the filter without removing any active filters on the column.
'reset': The Reset button will clear the details of the filter and any active filters on that column.
'cancel': The Cancel button will discard any changes that have been made to the filter in the UI, restoring the applied model.
- closeOnApply
boolean
If the Apply button is present, the filter popup will be closed immediately when the Apply or Reset button is clicked if this is set to true.
Default: false
- debounceMs
number
Overrides the default debounce time in milliseconds for the filter. Defaults are:
TextFilter and NumberFilter: 500ms. (These filters have text field inputs, so a short delay before the input is formatted and the filtering applied is usually appropriate).
DateFilter and SetFilter: 0ms
- defaultJoinOperator
JoinOperator
By default, the two conditions are combined using AND. You can change this default by setting this property. Options: AND, OR
defaultOption
string
The default filter option to be selected.
- filterOptions
(IFilterOptionDef | ISimpleFilterModelType)[]
Array of filter options to present to the user. See Filter Options.
- filterPlaceholder
FilterPlaceholderFunction | string
Placeholder text for the filter textbox
 - inRangeInclusive
boolean
If true, the 'inRange' filter option will include values equal to the start and end of the range.
- includeBlanksInEquals
boolean
If true, blank (null or undefined) values will pass the 'equals' filter option.
- includeBlanksInGreaterThan
boolean
If true, blank (null or undefined) values will pass the 'greaterThan' and 'greaterThanOrEqual' filter options.
- includeBlanksInLessThan
boolean
If true, blank (null or undefined) values will pass the 'lessThan' and 'lessThanOrEqual' filter options.
- includeBlanksInRange
boolean
If true, blank (null or undefined) values will pass the 'inRange' filter option.
- numberParser
Function
Typically used alongside allowedCharPattern, this provides a custom parser to convert the value entered in the filter inputs into a number that can be used for comparisons.
readOnly
boolean
If set to true, disables controls in the filter to mutate its state. Normally this would be used in conjunction with the Filter API. See Read-only Filter UI.
Default: false
- suppressAndOrCondition
boolean
If true, the filter will only allow one condition.
Default: false


### Custom Number Support
By default, the Number Filter uses HTML5 number inputs. However, these have mixed browser support, particularly around locale-specific nuances, e.g. using commas rather than periods for decimal values. You might also want to allow users to type other characters e.g. currency symbols, commas for thousands, etc, and still be able to handle those values correctly.

For these reasons, the Number Filter allows you to control what characters the user is allowed to type, and provide custom logic to parse the provided value into a number to be used in the filtering. In this case, a text input is used with JavaScript controlling what characters the user is allowed (rather than the browser).

Custom number support is enabled by specifying configuration similar to the following:

```
const columnDefs = [
    {
        field: 'age',
        filter: 'agNumberColumnFilter',
        filterParams: {
            allowedCharPattern: '\\d\\-\\,', // note: ensure you escape as if you were creating a RegExp from a string
            numberParser: text => {
                return text == null ? null : parseFloat(text.replace(',', '.'));
            }
        }
    }
];
```
The `allowedCharPattern` is a regex of all the characters that are allowed to be typed. This is surrounded by square brackets [] and used as a character class to be compared against each typed character individually and prevent the character from appearing in the input if it does not match, in supported browsers (all except Safari).

The `numberParser` should take the user-entered text and return either a number if one can be interpreted, or null if not.

The example below shows custom number support in action:

- The first column shows the default behaviour, and the second column uses commas for decimals and allows a dollar sign ($) to be included.
- Floating filters are enabled and also react to the configuration of allowedCharPattern.

"""