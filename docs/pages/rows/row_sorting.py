from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid Rows",
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
"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.rows.row_sorting", make_layout=make_tabs),
        # up_next("text"),
    ],
)
