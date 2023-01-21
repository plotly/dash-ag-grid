from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=5,
    description=app_description,
    title="Dash AG Grid Editing",
)

text1="""
# Undo / Redo Edits
This section covers how to allow users to undo / redo their cell edits.

When Cell Editing is enabled in the grid, it is usually desirable to allow users to undo / redo any edits.

>
> This Undo / Redo feature is designed to be a recovery mechanism for user editing mistakes. Performing grid operations that change the row / column order, e.g. sorting, filtering and grouping, will clear the undo / redo stacks.
>

### Enabling Undo / Redo
The following undo / redo properties are provided in the grid options interface:

```

dag.AgGrid(   
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    dashGridOptions={
        'undoRedoCellEditing': True, 
        'undoRedoCellEditingLimit': 20
    }
)

```
As shown in the snippet above, undo / redo is enabled through the `undoRedoCellEditing` property.

The default number of undo / redo steps is 10. To change this default the `undoRedoCellEditingLimit` property can be used.

Undo / Redo Shortcuts
The following keyboard shortcuts are available when undo / redo is enabled:

- Ctrl+Z / Command+Z: will undo the last cell edit(s).
- Ctrl+Y / Command+Y: will redo the last undo.

Note that the grid needs focus for these shortcuts to have an effect.

"""


layout = html.Div(
    [

        make_md(text1),
        example_app("examples.editing.undo_redo", make_layout=make_tabs),

        # up_next("text"),
    ],
)
