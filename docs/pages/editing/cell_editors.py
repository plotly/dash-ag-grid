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


const columnDefs = [
    { 
        field: 'name', 
        editable: true, 
        # uses the provided Text Cell Editor (which is the default)
        cellEditor: 'agTextCellEditor' 
    },

        # show this editor in a popup
        cellEditorPopup: true,
        # position the popup under the cell
        cellEditorPopupPosition: 'under'
    }
];

### Popup vs In Cell
An editor can be in a popup or in cell.

In Cell
In Cell editing means the contents of the cell will be cleared and the editor will appear inside the cell. The editor will be constrained to the boundaries of the cell, so if it is larger than the provided area it will be clipped. When editing is finished, the editor will be removed and the renderer will be placed back inside the cell again.

Popup
If you want your editor to appear in a popup (such as a dropdown list), then you can have it appear in a popup. The popup will appear over the cell, however it will not change the contents of the cell. Behind the popup the cell will remain intact until after editing is finished which will result in the cell being refreshed.

>
>  See the Provided Cell Editors section for examples of built-in Text Cell Editor Large Text Cell Editor and Select Cell Editor
>
"""

layout = html.Div(
    [

        make_md(text1),
        example_app("examples.editing.cell_editors", make_layout=make_tabs),

        # up_next("text"),
    ],
)
