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

Enable sorting for columns by setting the `sortable` column definition attribute. You can then sort a column by clicking
on the column header.

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
## Custom Sorting

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

Here are the functions added to the dashAgGridFunctions.js file in the assets folder:
```js
var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.dateComparator = function (date1, date2) {
  const date1Number = monthToComparableNumber(date1);
  const date2Number = monthToComparableNumber(date2);
  if (date1Number === null && date2Number === null) {
    return 0;
  }
  if (date1Number === null) {
    return -1;
  }
  if (date2Number === null) {
    return 1;
  }
  return date1Number - date2Number;
}

// eg 29/08/2004 gets converted to 20040829
function monthToComparableNumber(date) {
  if (date === undefined || date === null) {
    return null;
  }
  const yearNumber = parseInt(date.split('/')[2]);
  const monthNumber = parseInt(date.split('/')[1]);
  const dayNumber = parseInt(date.split('/')[0]);
  return (yearNumber * 10000) + (monthNumber * 100) + dayNumber;
}
```
"""

text3 = """
## Multi Column Sorting

It is possible to sort by multiple columns. The default action for multiple column sorting is for the user to hold down
<kbd>Shift</kbd> while clicking the column header.

To change the default action to use the <kbd>Ctrl</kbd> key (or <kbd>Command</kbd> key on Apple) instead set the
property `multiSortKey`:

```python
dashGridOptions = {'multiSortKey': 'ctrl'}
```

Try it in the example above. This image shows sorting by Country, then by Date, then by Athlete.


"""
img = "https://user-images.githubusercontent.com/72614349/228972127-c40b3c31-03fe-45c7-877d-41bb321b97af.png"


text4 = """
It is also possible to disable the multi sorting behaviour
the options:

```python
dashGridOptions = {'suppressMultiSort': True}
```

Or force the multi sorting behaviour without key press with

```python
dashGridOptions = {'alwaysMultiSort': True}
```

## Sorting Animation

To enable animation of the rows after sorting, set grid property:

```python
dashGridOptions = {'animateRows': True}
```

## Sorting Order

By default, the sorting order is as follows:

**ascending -> descending -> none**

In other words, when you click a column that is not sorted, it will sort ascending. The next click will make it sort
descending. Another click will remove the sort.

It is possible to override this behaviour by providing your own `sortingOrder` on either the `dashGridOptions` or
the `columnDefs`. If defined both in `columnDefs` and `dashGridOptions`, the `columnDefs` will get preference, allowing
you to define a common default, and then tailor per column.

## Example: Sorting Order and Animation
The example below shows animation of the rows plus different combinations of sorting orders as follows:

- **Default Columns**: descending -> ascending -> no sort
- Column **Athlete**: ascending -> descending
- Column **Age**: descending -> ascending
- Column **Country**: descending -> no sort
- Column **Year**: ascending only

"""

text5 = """
## Sorting API
What sorting is applied is controlled via [Column State](https://dashaggrid.pythonanywhere.com/columns/column-state). The below examples uses the Column State API to control column
sorting.
"""

text6 = """
## Accented Sort

By default, sorting doesn't take into consideration locale-specific characters. If you need to make your sort
locale-specific you can configure this by setting the grid option 
```python
`dashGridOptions={"accentedSort" : True}`
```

Using this feature is more expensive; if you need to sort a very large amount of data, you might find that this causes
the sort to be noticeably slower.

The following example is configured to use this feature.
"""

text7 = """
## Post-Sort

It is also possible to perform some post-sorting if you require additional control over the sorted rows.

This is provided via the grid callback function as shown below:

```python
dashGridOptions = {"postSortRows": {"function": "postSort(params)"}}
```

> `postSortRows` (Function) Callback to perform additional sorting after the grid has sorted the rows.

The following example uses this configuration to perform a post-sort on the rows. The custom function puts rows with
Michael Phelps at the top always.

Here is the function added to the dashAgGridFunctions.js file in the assets folder:

```js
dagfuncs.postSort = function (params) {
    const rowNodes = params.nodes;
    // here we put Michael Phelps rows on top while preserving the sort order
    let nextInsertPos = 0;
    for (let i = 0; i < rowNodes.length; i++) {
        const athlete = rowNodes[i].data ? rowNodes[i].data.athlete : undefined;
        if (athlete === 'Michael Phelps') {
            rowNodes.splice(nextInsertPos, 0, rowNodes.splice(i, 1)[0]);
            nextInsertPos++;
        }
    }
}
```
"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.rows.row_sorting", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.rows.row_sorting_date", make_layout=make_tabs),
        make_md(text2a),
        example_app("examples.rows.row_sorting_custom", make_layout=make_tabs),
        make_md(text3),
        make_feature_card(img, ""),
        make_md(text4),
        example_app("examples.rows.row_sorting_order_and_animation", make_layout=make_tabs),
        make_md(text5),
        example_app("examples.rows.row_sorting_api", make_layout=make_tabs),
        make_md(text6),
        example_app("examples.rows.row_sorting_accented", make_layout=make_tabs),
        make_md(text7),
        example_app("examples.rows.row_sorting_post_sort", make_layout=make_tabs),
        # up_next("text"),
    ],
)
