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

### Configuring Column Spanning  

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


### Example Column Spanning

Column spanning will typically be used for creating reports with AG Grid. Below is something that would be more typical of the column spanning feature. The following can be noted from the example:

- The data is formatted in a certain way, it is not intended for the user to sort this data or reorder the columns.
- The dataset has meta-data inside it, the data.section attribute. This meta-data, provided by the application, is used in the grid configuration in order to set the column spans and the background colours.

"""

text2 = """
### Column Spanning Constraints
Column Spanning breaks out of the row / cell calculations that a lot of features in the grid are based on. If using Column Spanning, be aware of the following:

 - Range Selection (Enterprise feature) will not work correctly when spanning cells. This is because it is not possible to cover all scenarios, as a range is no longer a perfect rectangle.

"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.columns.column_spanning", make_layout=make_tabs),
        make_md(text2),
        # up_next("text"),
    ],
)
