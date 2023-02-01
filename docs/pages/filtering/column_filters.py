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

In `dash-ag-grid` community there are two provided filters, the default text filter `agTextColumnFilter` and
`agNumberColumnFilter`, a number filter.

### Example: Simple Filters
The example below demonstrates simple filters. Note that the "Age" column has a number filter and the
other columns have a text filter.
"""

text2 = """
### Configuring Filters on Columns
Set filtering on a column using the column definition property filter. The property can have one of the following values:

 - boolean: Set to true to enable the default filter. The default is Text Filter for AG Grid Community and Set Filter for AG Grid Enterprise.
 - string : Provide a specific filter to use instead of the default filter.

The code below shows some column definitions with filters set:
```
columnDefs = [
    # sets the text filter
    { 'field': 'athlete', 'filter': 'agTextColumnFilter' },

    # sets the number filter
    { 'field': 'age', 'filter': 'agNumberColumnFilter' },

    # use the default filter
    { 'field': 'gold', 'filter': true },

    # use no filter (leaving unspecified means use no filter)
    { field: 'sport' },
]
```

If you want to enable filters on all columns, you should set a filter on the Default Column Definition. The following code snippet shows setting `filter=True` for all columns via the `defaultColDef` and then setting filter=false for the Sport column, so all columns have a filter except Sport.

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

    # filter specifically set to 'false', i.e. use no filter
    { 'field': 'sport', 'filter': false },
]
```


### Filter Parameters
Each filter can take additional filter parameters by setting `filterParams`. The parameters each filter type accepts are specific to each filter; parameters for the provided filters are explained in their relevant sections.

The code below shows configuring the text filter on the Athlete column and providing extra filter parameters (what the buttons do is explained in Apply, Clear, Reset and Cancel Buttons).
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

### Relation to Quick Filter
Column filters work independently of Quick Filter. If a quick filter is applied along with a column filter, each filter type is considered and the row will only show if it passes both types.

Column filters are tied to a specific column. Quick filter is not tied to any particular column. This section of the documentation talks about column filters only. For quick filter, click the links above to learn more.
"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.filtering.column_filters", make_layout=make_tabs),
        make_md(text2)

    ],
)
