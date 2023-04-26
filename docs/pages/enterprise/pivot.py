from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description
from utils.other_components import enterprise_blurb


register_page(
    __name__,

    description=app_description,
    title="Dash AG Grid Enterprise Features - Pivot",
)

text1 = """
# Pivot
"""

text2 = """


Pivoting allows you to take a columns values and turn them into columns. For example you can pivot on Country to make columns for Ireland, United Kingdom, USA etc.

Pivoting only makes sense when mixed with aggregation. If you turn a column into a pivot column, you must have at least one aggregation (value) active for the configuration to make sense. For example, if pivoting by country, you must provide something you are measuring such as 'gold medals per country'.

### Pivot Mode
Pivot mode is required to be turned on for pivoting to work. When the grid is in pivot mode, the following will happen:

- Only columns with Group, Pivot or Value active will be included in the grid.
- Only aggregated rows will be shown, the lowest level rowData will not be displayed.

If pivot mode is off, then adding or removing pivot columns will have no effect.

> To allow a column to be used as pivot column via the Tool Panel, set enablePivot=true on the required columns. Otherwise you won't be able to drag and drop the columns to the pivot drop zone from the Tool Panel.

### Specifying Pivot Columns

To pivot rows by a particular column, mark the column you want to group with pivot=true. There is no limit on the number of columns that the grid can pivot by. For example, the following will pivot the rows in the grid by country and then sport:

```
columnDefs = [
    { "field": "country", "pivot": True },
    { "field": "sport", "pivot": True }
]
```
### Example: Simple Pivot
The example below shows a simple pivot on the Sport column using the Gold, Silver and Bronze columns for values.

Columns Date and Year, although defined as columns, are not displayed in the grid as they have no group, pivot or value associated with them.

"""

text3 = """
### Other examples


Please see the [AG Grid Docs Pivot](https://www.ag-grid.com/react-data-grid/pivoting/) section  for all other examples.


"""


layout = html.Div(
    [
        make_md(text1),
        make_md(enterprise_blurb),
        make_md(text2),
        example_app("examples.enterprise.pivot", make_layout=make_tabs),
        make_md(text3)
        # up_next("text"),
    ],
)
