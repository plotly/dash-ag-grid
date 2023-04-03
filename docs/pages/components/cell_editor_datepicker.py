from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=3,
    description=app_description,
    title="Dash AG Grid Components - Custom Datepicker Cell Editor",

)

text1 = """
# Cell Editor Datepicker

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
        example_app("examples.components.cell_editor_datepicker", make_layout=make_tabs),

    ],
)
