from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=3,
    description=app_description,
    title="Dash AG Grid - Column State",
)

text1 = """
# Column State

Column Definitions contain both stateful and non-stateful attributes. Stateful attributes can have
 their values changed by the grid (e.g. Column sort can be changed by the user clicking on the column
  header). Non-stateful attributes do not change from what is set in the Column Definition
   (e.g. once the Header Name is set as part of a Column Definition, it typically does not change).


The DOM also has stateful vs non-stateful attributes. For example consider a DOM element
 and setting `element.style.width="100px"` will indefinitely set width to 100 pixels,
  the browser will not change this value. However setting `element.scrollTop=200` will
   set the scroll position, but the browser can change the scroll position further following user
    interaction, thus scroll position is stateful as the browser can change the state.

The full list of stateful attributes of Columns are represented by the `columnState` interface:

Properties available on the `columnState` interface.

- `hide` (boolean | null) True if the column is hidden
- `width` (number) Width of the column in pixels
- `flex` (number | null) Column's flex if flex is set
- `sort` ('asc' | 'desc' | null) Sort applied to the column
- `sortIndex` (number | null) The order of the sort, if sorting by many columns
- `aggFunc` (string | IAggFunc | null) The aggregation function applied
- `pivot` (boolean | null) True if pivot active
- `pivotIndex` (number | null) The order of the pivot, if pivoting by many columns
- `pinned` (ColumnPinnedType) Set if column is pinned
- `rowGroup` (boolean | null) True if row group active
- `rowGroupIndex` (number | null) The order of the row group, if grouping by many columns


` `
` `
### Save and Apply State

The example below demonstrates saving and restoring column state. Try the following:

- Click 'Save State' to save the Column State.
- Change some column state e.g. resize columns, move columns around, apply column sorting or row grouping etc.
- Click 'Restore State' and the column's state is set back to where it was when you clicked 'Save State'.
- Click 'Reset State' and the state will go back to what was defined in the Column Definitions.
"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.columns.column_state", make_layout=make_tabs),
        # up_next("text"),
    ],
)
