from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=3,
    description=app_description,
    title="Dash AG Grid Editing",
)

text1 = """
# Cell Editors
A Cell Editor Component is the UI that appears, normally inside the Cell, that takes care of the Edit operation. 

` `
` `


### Popup vs In Cell
An editor can be in a popup or in cell.

In Cell
In Cell editing means the contents of the cell will be cleared and the editor will appear inside the cell. The editor will be constrained to the boundaries of the cell, so if it is larger than the provided area it will be clipped. When editing is finished, the editor will be removed and the renderer will be placed back inside the cell again.

Popup
If you want your editor to appear in a popup (such as a dropdown list), then you can have it appear in a popup. The popup will appear over the cell, however it will not change the contents of the cell. Behind the popup the cell will remain intact until after editing is finished which will result in the cell being refreshed.


```
const columnDefs = [
    { 
        field: 'name', 
        editable: True, 
        # uses the provided Text Cell Editor (which is the default)
        cellEditor: 'agTextCellEditor' 
    },

        # show this editor in a popup
        cellEditorPopup: True,
        # position the popup under the cell
        cellEditorPopupPosition: 'under'
    }
]
```

"""


text3 = """
>
> Cell Editing can also be performed via Cell Editor Components; please see:
> - <dccLink href='/editing/provided-cell-editors' children='Provided cell editors' />  to see select (dropdown) editors, and lage text (textarea) editors
>
"""



text2 = """

` `  
` `  

#### Datepicker Example

The example below demonstrates how to use a custom date picker as a cell editor. The 'Date' column uses a Component
 cell editor that allows you to pick a date using jQuery UI Datepicker.

Notice the following:

- the jQuery is included as external scripts and stylesheets in the app constructor.
- The Custom function to use the DatePicker with AG Grid is defined is defined in the `dashAgGridFunctions.js` file in the `assets` folder.
- The Custom DatePicker is supplied by name via `cellEditor`.  
- Change the format of the date returned from the DatePicker in the DatePicker function.


"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.editing.cell_editors", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.components.cell_editor_datepicker", make_layout=make_tabs),
        make_md(text3),

        # up_next("text"),
    ],
)
