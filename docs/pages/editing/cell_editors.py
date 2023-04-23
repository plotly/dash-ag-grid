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

` `  
` `  

### Dynamic Parameters
Parameters for cell editors can be dynamic to allow different selections based on what cell is being edited. For
 example, you might have a 'City' column that has values based on the 'Country' column. To do this, provide
  a function that returns parameters for the property `cellEditorParams`.
 
This function is defined in the `dashAgGridFunctions.js` file in the `assets` folder: 
```

var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.dynamicOptions = function(params) {
    const selectedCountry = params.data.country;
    if (selectedCountry === 'United States') {
        return {
            values: ['Boston', 'Chicago', 'San Francisco'],
        };
    } else {
        return {
            values: ['Montreal', 'Vancouver', 'Calgary']
        };
    }
}
```  


#### Example: Conditional options in dropdown

"""


text4 = """

` `  
` `  

### Example:  Custom Datepicker component

The example below demonstrates how to use a custom date picker as a cell editor. The 'Date' column uses a Component
 cell editor that allows you to pick a date using jQuery UI Datepicker.

Notice the following:

- the jQuery is included as external scripts and stylesheets in the app constructor.
- The Custom function `DatePicker` is defined in the `dashAgGridFunctions.js` file in the `assets` folder.
- The Custom `DatePicker` is supplied by name via `cellEditor`.  
- You can change the format of the date returned from the `DatePicker` in the `DatePicker` function.


"""

text5 = """

` `  
` ` 

### Example:  Custom Number Input component

The example below demonstrates how to use a custom number input as a cell editor. The 'Price' column uses a Component
 cell editor that is an html Input with type="number".

Notice the following:

- The Custom function  `NumberInput` is defined in the `dashAgGridFunctions.js` file in the `assets` folder.
- The Custom `NumberInput` is supplied by name via `cellEditor`.  
- When editing the number the user may only enter numbers and a decimal point.  The number is formatted for display
 using a `valueFormatter`.  See <dccLink href='/rendering/value-formatters-with-d3-format' children='Value formatters' /> in the Rendering section for more information.

"""





text6 = """
>
> Cell Editing can also be performed via Cell Editor Components.  Please see:
> - <dccLink href='/editing/provided-cell-editors' children='Provided cell editors' />  to see select (dropdown) editors, and lage text (textarea) editors
>
"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.editing.cell_editors", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.editing.cell_editors_dynamic", make_layout=make_tabs),
        make_md(text4),
        example_app("examples.components.cell_editor_datepicker", make_layout=make_tabs),
        make_md(text5),
        example_app("examples.components.cell_editor_number_input", make_layout=make_tabs),
        make_md(text6),

        # up_next("text"),
    ],
)
