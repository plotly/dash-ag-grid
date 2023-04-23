from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=3,
    description=app_description,
    title="Dash AG Grid Components - Custom  Cell Editor components",

)

text1 = """
# Cell Editor Components

This section covers custom cell editor components.  See more information in the Editing section of the docs.


### Example:  Custom Date Picker

The example below demonstrates how to use a custom date picker as a cell editor. The 'Date' column uses a Component
 cell editor that allows you to pick a date using jQuery UI Datepicker.

Notice the following:

- the jQuery is included as external scripts and stylesheets in the app constructor.
- The Custom `DatePicker` is defined in the `dashAgGridFunctions.js` file in the `assets` folder.
- The Custom `DatePicker` is supplied by name via `cellEditor`.  
- You can change the format of the date returned from the `DatePicker` in the `DatePicker` function.


"""


text2 = """

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



layout = html.Div(
    [
        make_md(text1),
        example_app("examples.components.cell_editor_datepicker", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.components.cell_editor_number_input", make_layout=make_tabs),

    ],
)
