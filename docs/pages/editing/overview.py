from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=1,
    description=app_description,
    title="Dash AG Grid Editing",
)

text1 = """
# Cell Editing

### Enable Editing
To enable Cell Editing for a Column use the editable property on the Column Definition.

 - `editable` (boolean) Set to `True` if this column is editable, otherwise `False`. Default: `False`

```
columnDefs = [
    {
        'field': 'athlete',
        # enables editing
        'editable': True
    }
]
```

To enable Cell Editing for all Columns, set `editable` to `True` in the default column definitions:

```
defaultColDef = {'editable': True}
```

"""


text2 = """

### Conditional Editing
To dynamically determine which cells are editable, a function can be supplied to the editable property on the Column Definition:

```
columnDefs = [
    {
        'field': 'athlete',
        # conditionally enables editing for data for 2012
         "editable": {"function": "params.data.year == 2012"},
    }
]
```

In the snippet above, Athlete cells will be editable on rows where the Year is 2012.

"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.editing.overview", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.editing.conditional_editing", make_layout=make_tabs),
        # up_next("text"),
    ],
)
