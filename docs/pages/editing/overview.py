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

 - `editable` (boolean) Set to `True` if this column is editable, otherwise False. Default: False

```
columnDefs = [
    {
        'field': 'athlete',
        # enables editing
        'editable': True
    }
]
```

By default the grid provides simple string editing and stores the result as a string. The example below shows string editing enabled on all columns by setting `editable=True` on the `defaultColDef`.

"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.editing.overview", make_layout=make_tabs),
        # up_next("text"),
    ],
)
