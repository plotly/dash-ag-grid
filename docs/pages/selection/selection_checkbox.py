from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=4,
    description=app_description,
    title="Dash AG Grid - Row Selection",
    name="Row selection checkbox"
)

text1 = """

# Checkbox Row Selection

To include checkbox selection for a column, set the attribute 'checkboxSelection' to true on the column definition. You can set this attribute on as many columns as you like, however it doesn't make sense to have it in more than one column in a table.

### Example 1:  Multi-select rows with checkboxes
"""

text2 = """

### Specify Selectable Rows
It is possible to specify which rows can be selected via the `isRowSelectable` function.

- `isRowSelectable`  - Callback to be used to determine which rows are selectable. By default rows are selectable, so return false to make a row un-selectable.

For instance if we only wanted to allow rows where the 'year' property is less than 2007, we could implement the following:

```

dag.AgGrid(    
    rowSelection="multiple",
    dashGridOptions = {'isRowSelectable': {"function": "params.data ? params.data.year < 2007 : false" }},
)

```

### Example 2: Selectable Rows with Header Checkbox
This example demonstrates the following:

- The `isRowSelectable` function only allows selections on rows where the year < 2007.
- The country column has `headerCheckboxSelection: True` and `checkboxSelection: True`, but only rows which are selectable will obtain a selectable checkbox. Similarly, the header checkbox will only select selectable rows.

"""


text3= """
### Example 3: Preselected rows

This example demonstrates preselecting rows.  


"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.selection.selection_checkbox", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.selection.selectable_rows", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.selection.selection_checkbox_preselected", make_layout=make_tabs),
        # up_next("text"),
    ],
)
