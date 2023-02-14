from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=1,
    description=app_description,
    title="Dash AG Grid Filtering",
)

text1 = """
# Column Filter
Column filters are filters that are applied to the data at the column level. Many column filters can be active at
 once (e.g. filters set on different columns) and the grid will display rows that pass every column's filter.
 
### Provided Filters

In `dash-ag-grid` community there are two provided filters:
- `agTextColumnFilter` the default text filter
- `agNumberColumnFilter` - a number filter.
- `agDateColumnFilter`  - a date filter
- `agSetColumnFilter` - Enterprise Only

### Example: Simple Filters
The example below demonstrates simple filters. Note that the "Age" column has a number filter, the
date has a date filter and the other columns have a text filter.
"""

text2 = """
### Configuring Filters on Columns
Set filtering on a column using the column definition property filter. The property can have one of the following values:

 - `boolean`: Set to `True` to enable the default filter. The default is Text Filter for AG Grid Community and Set Filter for AG Grid Enterprise.
 - `string` : Provide a specific filter to use instead of the default filter.

The date filter uses d3.time-format.  See the [Rendering section](/rendering/value-formatters) for more information.
The code below shows some column definitions with filters set:
```
columnDefs = [
    # sets the text filter
    { 'field': 'athlete', 'filter': 'agTextColumnFilter' },

    # sets the number filter
    { 'field': 'age', 'filter': 'agNumberColumnFilter' },

    # use the default filter
    { 'field': 'gold', 'filter': True },

    # use no filter (leaving unspecified means use no filter)
    { field: 'sport' },
    
    # sets the date filter
      {
        "headerName": "Date",
        "filter": "agDateColumnFilter",
        "valueGetter": {"function": "d3.timeParse('%d/%m/%Y')(data.date)"},
        "valueFormatter": {"function": "data.date"},
    },
]
```

If you want to enable filters on all columns, you should set a filter on the Default Column Definition. The following code snippet shows setting `filter=True` for all columns via the `defaultColDef` and then setting `filter=False` for the Sport column, so all columns have a filter except Sport.

```
# anything specified in defaultColDef gets applied to all columns
defaultColDef = {
    # set filtering on for all columns
    'filter': True,
}

columnDefs = [
    # filter not specified, defaultColDef setting is used
    { 'field': 'athlete' },
    { 'field': 'age' },

    # filter specifically set to 'False', i.e. use no filter
    { 'field': 'sport', 'filter': False },
]
```


### Filter Parameters
Each filter can take additional filter parameters by setting `filterParams`. The parameters each filter type accepts are specific to each filter; parameters for the provided filters are explained in their relevant sections.

The code below shows configuring the text filter on the Athlete column and providing extra filter parameters (what the buttons do is explained below-  Apply, Clear, Reset and Cancel Buttons).
```
columnDefs = [
    # column configured to use text filter
    {
        'field': 'athlete',
        'filter': 'agTextColumnFilter',
        # pass in additional parameters to the text filter
        'filterParams': {
            'buttons': ['reset', 'apply'],
            'debounceMs': 200
        }
    }
]
```

### Filtering Animation
To enable animation of the rows when filtering, set the grid property `animateRows=True`.

### Relation to Quick Filter
Column filters work independently of Quick Filter. If a quick filter is applied along with a column filter, each filter type is considered and the row will only show if it passes both types.

Column filters are tied to a specific column. Quick filter is not tied to any particular column. This section of the documentation talks about column filters only. For quick filter, click the links above to learn more.
"""


text3 = """
### Provided Filter UI

Each provided filter is displayed in a UI with optional buttons at the bottom.

![filter-UI](https://user-images.githubusercontent.com/72614349/216476776-7c16ecef-0c86-4db2-8dbe-4f5fe3d79a72.png)

### Provided Filter Params
All the provided filters have the following parameters:

- `buttons` Specifies the buttons to be shown in the filter, in the order they should be displayed in. The options are:
    - 'apply': If the Apply button is present, the filter is only applied after the user hits the Apply button.
    - 'clear': The Clear button will clear the (form) details of the filter without removing any active filters on the column.
    - 'reset': The Reset button will clear the details of the filter and any active filters on that column.
    - 'cancel': The Cancel button will discard any changes that have been made to the filter in the UI, restoring the applied model.

- `closeOnApply` (boolean) If the Apply button is present, the filter popup will be closed immediately when the Apply or Reset button is clicked if this is set to true. Default: false
- `debounceMs` (number) Overrides the default debounce time in milliseconds for the filter. Defaults are:
    - TextFilter and NumberFilter: 500ms. (These filters have text field inputs, so a short delay before the input is formatted and the filtering applied is usually appropriate).
    - DateFilter and SetFilter: 0ms
- readOnly (boolean) If set to true, disables controls in the filter to mutate its state. Normally this would be used in conjunction with the Filter API. See Read-only Filter UI. Default: false

### Apply, Clear, Reset and Cancel Buttons
Each of the provided filters can optionally include Apply, Clear, Reset and Cancel buttons.

When the Apply button is used, the filter is only applied once the Apply button is pressed. This is useful if the filtering operation will take a long time because the dataset is large, or if using server-side filtering (thus preventing unnecessary calls to the server). Pressing Enter is equivalent to pressing the Apply button.

The Clear button clears just the filter UI, whereas the Reset button clears the filter UI and removes any active filters for that column.

The Cancel button will discard any changes that have been made in the UI, restoring the state of the filter to match the applied model.

The buttons will be displayed in the order they are specified in the buttons array.

The example below demonstrates using the different buttons. It also demonstrates the relationship between the buttons and filter events. Note the following:

- The Athlete and Age columns have filters with Apply and Reset buttons, but different orders.
- The Country column has a filter with Apply and Clear buttons.
- The Year column has a filter with Apply and Cancel buttons.
- The Age and Year columns have `closeOnApply` set to `True`, so the filter popup will be closed immediately when the filter is applied, reset or cancelled. Pressing Enter will also apply the filter and close the popup.
"""

text4 = """
### Simple Filter Parts (For text, number and date filters)
Each Simple Filter follows the same layout. The only layout difference is the type of input field presented to the user: for Text and Number Filters a text field is displayed, whereas for Date Filters a date picker field is displayed.

![aggrid_filters](https://user-images.githubusercontent.com/72614349/218348069-7c6df4d5-59cb-44d1-a2a0-ae8a954a504a.png)


### Filter Options
Each filter provides a dropdown list of filter options to select from. Each filter option represents a filtering strategy, e.g. 'equals', 'not equals', etc.

Each filter's default Filter Options are listed below, as well as information on Defining Custom Filter Options.

### Filter Value
Each filter option takes zero (a possibility with custom options), one (for most) or two (for 'in range') values. The value type depends on the filter type, e.g. the Date Filter takes Date values.

### Condition 1 and Condition 2
Each filter initially only displays Condition 1. When the user completes the Condition 1 section of the filter, Condition 2 becomes visible.

### Join Operator
The Join Operator decides how Condition 1 and Condition 2 are joined, using either AND or OR.

### Simple Filters Parameters
Simple Filters are configured though the filterParams attribute of the column definition:


- `filterOptions` Array of filter options to present to the user. See Filter Options. 
- `defaultOption` (string) The default filter option to be selected.
- `defaultJoinOperator` - By default, the two conditions are combined using AND. You can change this default by setting this property. Options: AND, OR
- `suppressAndOrCondition` (boolean) If true, the filter will only allow one condition. Default: false
- `alwaysShowBothConditions` (boolean) By default, only one condition is shown, and a second is made visible once a first condition  has been entered. Set this to `True` to always show both conditions. In this case the second condition will be disabled until a first condition has been entered. Default: false
- `filterPlaceholder`  Placeholder text for the filter textbox
- `buttons` - Specifies the buttons to be shown in the filter, in the order they should be displayed in. The options are:
    - 'apply': If the Apply button is present, the filter is only applied after the user hits the Apply button.
    - 'clear': The Clear button will clear the (form) details of the filter without removing any active filters on the column.
    - 'reset': The Reset button will clear the details of the filter and any active filters on that column.
    - 'cancel': The Cancel button will discard any changes that have been made to the filter in the UI, restoring the applied model.
- `closeOnApply` (boolean) If the Apply button is present, the filter popup will be closed immediately when the Apply or Reset button is clicked if this is set to true. Default: false
- `debounceMs` (number) Overrides the default debounce time in milliseconds for the filter. Defaults are TextFilter and NumberFilter: 500ms. (These filters have text field inputs, so a short delay before the input is formatted and the filtering applied is usually appropriate).
- `readOnly` (boolean) If set to true, disables controls in the filter to mutate its state. Normally this would be used in conjunction with the Filter API. See Read-only Filter UI. Default: false


"""

text5 = """

### Simple Filter Options
Each simple filter presents a list of options to the user. The list of options for each filter are as follows:

| Option Name  | 	Option Key	 | Supported Filters  | 
| ------------ | --------------- | ----------------- |  
| Equals  | 	equals	 | Text, Number, Date | 
| Not Equals | 	notEqual	 | Text, Number, Date | 
| Contains	 | contains	 | Text | 
| Not Contains | 	notContains	 | Text | 
| Starts With	 | startsWith	 | Text | 
| Ends With	 | endsWith	 | Text | 
| Less Than	 | lessThan	 | Number, Date | 
| Less Than or Equal | 	lessThanOrEqual	 | Number | 
| Greater Than | 	greaterThan	 | Number, Date | 
| Greater Than or Equal	 | greaterThanOrEqual	 | Number | 
| In Range	 | inRange	 | Number, Date | 
| Blank	 | blank	Text,  | Number, Date | 
| Not blank | 	notBlank	 | Text, Number, Date | 
| Choose One | 	empty	 | Text, Number, Date | 

Note that the empty filter option is primarily used when creating Custom Filter Options. When 'Choose One' is displayed, the filter is not active.

### Default Filter Options
Each of the filter types has the following default options and default selected option.

 | Filter  | 	Default List of Options	 | Default Selected Option | 
  | ------ | -------------------------- | ------------------------ | 
 | Text	 | Contains, Not Contains, Equals, Not Equals, Starts With, Ends With.	 | Contains | 
 | Number  | 	Equals, Not Equals, Less Than, Less Than or Equal, Greater Than, Greater Than or Equal, In Range.	 | Equals | 
 | Date  | 	Equals, Greater Than, Less Than, Not Equals, In Range.	 | Equals | 



### Data Updates
Grid data can be updated in a number of ways, including:

- Cell Editing.
- Updating Data.
- Clipboard Operations. (enterprise)
Simple filters are not affected by data changes.



### Example: Simple Filter Options
The following example demonstrates those configuration options that can be applied to any Simple Filter.

- The Athlete column shows a Text Filter with default behavior for all options.
- The Country column shows a Text Filter with filterOptions set to show a different list of available options, and defaultOption set to change the default option selected.
- The Age column has a Number Filter with alwaysShowBothConditions set to true so that both condition are always shown. The defaultJoinOperator is also set to 'OR' rather than the default ('AND').

"""

text6 = """"
### Style Header on Filter
Each time a filter is applied to a column the CSS class ag-header-cell-filtered is added to the header. This can be used for adding style to headers that are filtered.

In the example above, we've added some styling to `ag-header-cell-filtered`, so when you filter a column you will notice the column header change.

CSS

```
.ag-header-cell-filtered {
  background-color: #1b6d85 !important;
  color: #fff !important;
}

.ag-header-cell-filtered span {
  color: #fff !important;
}

```

### Customising Filter Placeholder Text
Filter placeholder text can be customised on a per column basis using filterParams.filterPlaceholder within the grid option columnDefs. The example above has a custom placeholder in the Age column


"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.filtering.column_filters", make_layout=make_tabs),
        make_md(text2),
        make_md(text3),
        example_app("examples.filtering.column_filter_buttons", make_layout=make_tabs),
        make_md(text4),
        make_md(text5),
        example_app("examples.filtering.filter_options", make_layout=make_tabs),
        make_md(text6),
    ],
)
