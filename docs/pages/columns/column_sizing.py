from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=6,
    description=app_description,
    title="Dash AG Grid Column Definitions",
)


text1 = """
# Column Sizing

__All columns can be resized by dragging the top right portion of the column.__

## Enable Sizing

Turn column resizing on for the grid by setting `'resizable'=True` for each column. To set resizing default  for all columns, set `'resizable'=True` on the default column definition.

The snippet below allows all columns except Address to be resized by explicitly setting each column.

```
columnDefs = [
    { "field": "name", "resizable": True },
    { "field": "age", "resizable": True },
    { "field": "address" },
]
```

The snippet below allows all columns except Address to be resized by setting `'resizable'=True` on the default column definition and then `'resizable'=False` on the Address column.

```
defaultColDef = {
    "resizable": True,
}
columnDefs = [
    { "field": "name" },
    { "field": "age" },
    { "field": "address", "resizable": False },
]
```


## Size Columns to Fit

The `columnSize="sizeToFit"` prop makes the currently visible columns fit the screen. The columns will scale (growing or shrinking) to fit the available width.

If you don't want a particular column to be included in the auto resize, then set the width of that column in the column definition.

Column default widths, rather than current widths, are used while calculating the new widths. This insures the result is deterministic and not depend on any Column resizing the user may have manually done.

## Auto-Size Columns

Just like Excel, each column can be 'auto resized' by double clicking the right side of the header rather than dragging it. When you do this, the grid will work out the best width to fit the contents of the cells in the column.

Note the following with regards autosizing columns:

- The grid works out the best width by considering the virtually rendered rows only. For example, if your grid has 10,000 rows, but only 50 rendered due to virtualisation of rows, then only these 50 will be considered for working out the width to display. The rendered rows are all the rows you can see on the screen through the vertical scroll plus a small buffer (default buffer size is 20).
- Autosizing columns looks at the rendered cells on the screen, and works out the width based on what it sees. It cannot see the columns that are not rendered due to column virtualisation. Thus it is not possible to autosize a column that is not visible on the screen.

Column Virtualisation is the technique the grid uses to render large amounts of columns without degrading performance by only rendering columns that are visible due to the horizontal scroll positions. For example, the grid can have 1,000 columns with only 10 rendered if the horizontal scroll is only showing 10 columns.

To get around this, you can turn off column virtualisation by setting grid property `suppressColumnVirtualisation=True`. The choice is yours, whether you want column virtualisation working OR auto-size working using off-screen columns.
By default the grid will also resize the column to fit the header. If you do not want the headers to be included in the autosize calculation, set the grid property `skipHeaderOnAutoSize=True`.

## Autosize Column API
The `columnSize="autoSizeAll"` prop auto-sizes  all columns based on its contents.

Autosizing columns can also be done using the following column API methods. If `skipHeader=True`, the header won't be included when calculating the column widths.

Column Groups are never considered when calculating the column widths.


The Example below shows how to make columns adjust to fit either the screen or their contents.
"""


text2 = """

` `
` `
## Shift Resizing
If you hold the Shift key while dragging the resize handle, the column will take space away from the column adjacent to it. This means the total width for all columns will be constant.

You can also change the default behaviour for resizing. Set the grid property colResizeDefault='shift' to have shift resizing as the default and normal resizing to happen when the Shift key is pressed.



## Resizing Groups

When you resize a group, it will distribute the extra room to all columns in the group equally. In the example below the groups can be resized as follows:

- The group 'Everything Resizes' will resize all columns.
- The group 'Only Year Resizes' will resize only year, because the other columns have `resizable=False`.
- The group 'Nothing Resizes' cannot be resized at all because all the columns in the groups have `resizable=False`.


"""

text3 = """
### Column Flex
It's often required that one or more columns fill the entire available space in the grid. For this scenario, it is possible to use the flex config. Some columns could be set with a regular width config, while other columns would have a flex config.

Flex sizing works by dividing the remaining space in the grid among all flex columns in proportion to their flex value. For example, suppose the grid has a total width of 450px and it has three columns: the first with width: 150; the second with flex: 1; and third with flex: 2. The first column will be 150px wide, leaving 300px remaining. The column with flex: 2 has twice the size with flex: 1. So final sizes will be: 150px, 100px, 200px.

> The flex config does not work with a width config in the same column. If you need to provide a minimum width for a column, you should use flex and the `minWidth` config. Flex will also take `maxWidth` into account.

> If you manually resize a column with flex either via the API or by dragging the resize handle, flex will automatically be disabled for that column.

#### Column Flex examples
In the example below, note the following:
- Column A is fixed size. You can resize it with the drag handle and the other two columns will adjust to fill the available space
- Column B has flex: 2, `minWidth: 200` and `maxWidth: 350`, so it should be constrained to this max/min width.
- Column C has flex: 1 so should be half the size of column B, unless column B is being constrained by its minWidth/maxWidth rules, in which case it should take up the remaining available space.
"""



text4 = """

This example has flex in all columns.  Try changing the browser window size and note how the proportions of the columns are maintained.
"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.columns.column_sizing1", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.columns.column_sizing2", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.columns.column_sizing_flex2", make_layout=make_tabs),
        make_md(text4),
        example_app("examples.columns.column_sizing_flex1", make_layout=make_tabs),
        #  up_next("text"),
    ],
)
