from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md, make_feature_card
from utils.utils import app_description


register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid - Row Sorting",
)

text1 = """

# Row Sorting
This page describes how to sort row data in the grid and how you can customise that sorting to match your requirements.

## Enable Sorting
Enable sorting for columns by setting the sortable column definition attribute. You can then sort a column by clicking on the column header.

```
# enable sorting on 'name' and 'age' columns only
columnDefs = [
    { 'field': 'name', 'sortable': True },
    { 'field': 'age', 'sortable': True },
    { 'field': 'address' },
]
```

To enable sorting for all columns, set sorting in the default column definition.

```
# enable sorting on all columns by default
defaultColDef = {
    'sortable': True
}

columnDefs = [
    { 'field': 'name' },
    { 'field': 'age' },
    # suppress sorting on address column
    { 'field': 'address', 'sortable': false },
];
```

### Example 1: Sorting

"""

text2 = """
### Example 2: Sorting Dates

The dates in the grid are strings, however, to sort them correctly they must be date objects. To convert them, use
 the JavaScript function `d3.timeParse()`.  This is similar to the Python `strptime()` function.
 
```
date_obj= d3.timeParse(specifier)(date string)
```
 
> Please see <dccLink href= '/rendering/value-formatters-with-d3-format' children='Formatting Dates and Times with `d3-time-format`' /> 
 for more info and examples.
 
 

In this dataset, the date is a string dd/mm/yyyy.  We turn it into a date object using  `valueGetter` with the `d3.timeParse()`

```
"valueGetter": {"function": "d3.timeParse('%d/%m/%Y')(params.data.date)"},
```

In the example below, try clicking on the date column header, and you will see the date sorts correctly.
This example also demonstrates the date filter.  For more information, see <dccLink href="/filtering/date-filter" children="Date Filter" /> page.
"""

text2a = """
### Custom Sorting

Custom sorting is provided at a column level by configuring a comparator on the column definition.

- `comparator` (Function) Override the default sorting order by providing a custom sort comparator.
    - `valueA`, `valueB` are the values to compare.
    - `nodeA`, `nodeB` are the corresponding RowNodes. Useful if additional details are required by the sort.
    - `isDescending` - true if sort direction is desc. Not to be used for inverting the return value as the grid already applies asc or desc ordering.
    Return:
    - `0`  valueA is the same as valueB
    - `> 0` Sort valueA after valueB
    - `< 0` Sort valueA before valueB

### Custom Sorting Example
This is the example from the [AG Grid docs](https://www.ag-grid.com/react-data-grid/row-sorting/#custom-sorting-example). 
 It shows a custom sorting using the `comparator` prop and a custom  function to determine the sort order.  The example 
 parses a string date field.  Note that with Dash it's easier to  use the provided `d3` functions as shown in the example
  above rather than write your own custom function.

Example below shows the following:

- Default sorting on the **Athlete** column.
- When the **Year** column is not sorted, it shows a custom icon (up/down arrow).
- The **Date** column has strings as the row data, but has a custom comparator so that when you sort this column it sorts as dates, not as strings.

"""

text3 = """
### Multi Column Sorting

It is possible to sort by multiple columns. The default action for multiple column sorting is for the user to hold down
 `Shift` while clicking the column header. To change the default action to use the `Ctrl` key (or `Command` key on Apple)
  instead set the property `multiSortKey='ctrl'`.

Try it in the example above.  This image shows sorting by Country, then by Date, then by Athlete.


"""
img = "https://user-images.githubusercontent.com/72614349/228972127-c40b3c31-03fe-45c7-877d-41bb321b97af.png"





layout = html.Div(
    [
        make_md(text1),
        example_app("examples.rows.row_sorting", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.rows.row_sorting_date", make_layout=make_tabs),
        make_md(text2a),
        example_app("examples.rows.row_sorting_custom", make_layout=make_tabs),
        make_md(text3),
        make_feature_card(img, "")
        # up_next("text"),
    ],
)
