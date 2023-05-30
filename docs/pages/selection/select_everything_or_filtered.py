from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=5,
    description=app_description,
    title="Dash AG Grid - Select Everything or Just Filtered",
)

text1 = """
## Select Everything or Just Filtered

The header checkbox has three modes of operation, `'normal'`, `'filtered only'` and `'current page'`.

- `headerCheckboxSelectionFilteredOnly=False`: The checkbox will select all rows when checked, and un-select all rows when unchecked. The checkbox will update its state based on all rows.

- `headerCheckboxSelectionFilteredOnly=True`: The checkbox will select only filtered rows when checked and un-select only filtered rows when unchecked. The checkbox will update its state based only on filtered rows.

- `headerCheckboxSelectionCurrentPageOnly=True`: The checkbox will select only the rows on the current page when checked, and un-select only the rows on the current page when unchecked.

The examples below demonstrate all of these options.

### Example: Just Filtered

This example has the following characteristics:

- The checkbox works on filtered rows only. That means if you filter first, then hit the checkbox to select or un-select, then only the filtered rows are affected.

- The checkbox is always on the athlete column, even if the athlete column is moved.

"""

text2 = """

### Example: Select Everything

The next example is similar to the one above with the following changes:

- The checkbox selects everything, not just filtered.
- __The column that the selection checkbox appears in is always the first column.__ This can be observed by dragging the columns to reorder them.
"""

text3 = """

### Example: Select Only the Current Page

The next example demonstrates the `headerCheckboxSelectionCurrentPageOnly` property, note the following:

- Only items on the current page are selected.  Try going to a different page after clicking on the header checkbox.

"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.selection.select_just_filtered", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.selection.select_everything", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.selection.select_current_page", make_layout=make_tabs),
        # up_next("text"),
    ],
)
