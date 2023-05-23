from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=9,
    description=app_description,
    title="Dash AG Grid Column Definitions - Column Spanning",
)

text1 = """
# Column Spanning
By default, each cell will take up the width of one column. You can change this behaviour to allow cells to span multiple columns. This feature is similar to 'cell merging' in Excel or 'column spanning' in HTML tables.

## Configuring Column Spanning  

Column spanning is configured at the column definition level. To have a cell span more than one column, return how many columns to span in the `colSpan` prop.
```
columnDefs = [
    {
        'field': 'country',
        # col span is 2 for rows with Russia, but 1 for everything else
        'colSpan': {"function": "params.data.country === 'Russia' ? 2 : 1"},
    }
]
```

- `colSpan` (function) - By default, each cell will take up the width of one column. You can change this behaviour to allow cells to span multiple columns.

## Column Spanning Simple Example

Below shows a simple example using column spanning. The example doesn't make much sense, it just arbitrarily sets column
span on some cells for demonstration purposes, however we thought it easier to show column spanning with the familiar
Olympic winners data before going a bit deeper into its usages. The following can be noted:

- The **Country** column is configured to span 2 columns when 'Russia' and 4 columns when 'United States'. All other times
  it's normal (1 column).
- To help demonstrate the spanned column, the **Country** column is shaded using CSS styling.
- Resizing any columns that are spanned over will also resize the spanned cells. For example, resizing the column
  immediately to the right of **Country** will resize all cells spanning over the resized column.
- The first two columns are pinned. If you drag the country column into the pinned area, you will notice that the
  spanning is constrained within the pinned section, e.g. if you place **Country** as the last pinned column, no spanning
  will occur, as the spanning can only happen over cells in the same region, and **Country** now has no further columns
  inside the pinned region.

Here is the class added to the .css file in the assets folder:
```css
.colSpanning .ag-body-viewport [col-id='country'] {
    background-color: #a6e1ec;
}
```

Here are the functions added to the dashAgGridFunctions.js file in the assets folder:
```js
var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.simpleSpanning = function (params) {
    const country = params.data.country;
    if (country === 'Russia') {
        // have all Russia cells in column country of width of 2 columns
        return 2;
    } else if (country === 'United States') {
        // have all United States cells in column country of width of 4 columns
        return 4;
    } else {
        // all other rows should be just normal
        return 1;
    }
}
"""

text2 = """
## Column Spanning Complex Example

Column spanning will typically be used for creating reports with AG Grid. Below is something that would be more typical of the column spanning feature. The following can be noted from the example:

- The data is formatted in a certain way, it is not intended for the user to sort this data or reorder the columns.
- The dataset has meta-data inside it, the `data.section` attribute. This meta-data, provided by the application, is used in the grid configuration in order to set the column spans and the background colours.

Here are the classes added to the .css file in the assets folder:
```css
.header-cell {
  background-color: #a6e1ec;
  font-size: 25px;
  font-weight: bold;
  text-align: center;
}
.quarters-cell {
  background-color: #5bc0de;
  font-weight: bold;
}
```

Here are the functions added to the dashAgGridFunctions.js file in the assets folder:
```js
var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

function isHeaderRow(params) {
  return params.data.section === 'big-title';
}
function isQuarterRow(params) {
  return params.data.section === 'quarters';
}

dagfuncs.janColSpan = function(params) {
    if (isHeaderRow(params)) {
      return 6;
    } else if (isQuarterRow(params)) {
      return 3;
    } else {
      return 1;
    }
}

dagfuncs.aprColSpan = function(params) {
    if (isQuarterRow(params)) {
      return 3;
    } else {
      return 1;
    }
}
```

"""

text3 = """
## Column Spanning Constraints
Column Spanning breaks out of the row / cell calculations that a lot of features in the grid are based on. If using Column Spanning, be aware of the following:

 - Range Selection (Enterprise feature) will not work correctly when spanning cells. This is because it is not possible to cover all scenarios, as a range is no longer a perfect rectangle.

"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.columns.column_spanning1", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.columns.column_spanning2", make_layout=make_tabs),
        make_md(text3),
        # up_next("text"),
    ],
)
