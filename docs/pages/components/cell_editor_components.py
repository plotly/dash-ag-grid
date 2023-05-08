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

Note the following:

- the jQuery is included as external scripts and stylesheets in the app constructor.
- The Custom `DatePicker` is defined in the `dashAgGridFunctions.js` file in the `assets` folder.
- The Custom `DatePicker` is supplied by name via `cellEditor`.  
- You can change the format of the date returned from the `DatePicker` in the `DatePicker` function.


"""


text2 = """

### Example:  Custom Number Input component

The example below demonstrates how to use a custom number input as a cell editor. The 'Price' column uses a Component
 cell editor that is an html Input with type="number".

Note the following:

- The Custom function  `NumberInput` is defined in the `dashAgGridFunctions.js` file in the `assets` folder.
- The Custom `NumberInput` is supplied by name via `cellEditor`.  
- When editing the number the user may only enter numbers and a decimal point.  The number is formatted for display
 using a `valueFormatter`.  See <dccLink href='/rendering/value-formatters-with-d3-format' children='Value formatters' /> in the Rendering section for more information.

"""

text3 = """

### Example:  Custom Dropdown Component dmc.Select

This example shows how to make a custom cell editor using the `dmc.Select` component from the [Dash Mantine Components](https://www.dash-mantine-components.com/) Library.
This is an excellent dropdown component and works well with AG Grid.  It has all the features of a `dcc.Dropdown` and more!
Check out the [dmc docs](https://www.dash-mantine-components.com/components/select) for more information.

If you are not already using Dash Mantine Components in your app:
```
pip install dash-mantine-components
```
Then import into your app:
```
import dash_mantine_components as dmc
```


In the example below, note the following:

- The Custom function  `DMC_Select` is defined in the `dashAgGridFunctions.js` file in the `assets` folder.
- The `DMC_Select` is supplied by name via `cellEditor`.  


- The dropdown is available on the Country and the Sport columns with a single click
- The Input field is clearable in the Country column and the Sport column is not clearable
- The Sport column allows for arbitrary data to be entered by setting `creatable=True` 
- You can pass any of the props to the dmc.Select component using `cellEditorParams`.  No need to modify the JavaScript code!

    - `className` (string; optional):
        Often used with CSS to style elements with common properties.
    
    - `clearable` (boolean; optional):
        Allow to clear item.
    
    - `creatable` (boolean; optional):
        Allow creatable option.
    
    - `options`  (list of strings; optional):
        Note - `options` is passed to the dmc.Select `data` prop
        Select data used to renderer items in dropdown.
    
    - `debounce` (number; optional):
        Debounce time.
    
    - `disabled` (boolean; optional):
        Whether the input is disabled   Disabled input state.
    
    - `filterDataOnExactSearchMatch` (boolean; optional):
        Should data be filtered when search value exactly matches selected
        item.
    
    - `limit` (number; optional):
        Limit amount of items displayed at a time for searchable select.
    
    - `maxDropdownHeight` (number; optional):
        Maximum dropdown height in px.
    
    - `placeholder` (string; optional):
        Placeholder.
    
    - `required` (boolean; optional):
        Adds required attribute to the input and red asterisk on the right
        side of label   Sets required on input element.
    
    - `searchValue` (string; optional):
        Controlled search input value.
    
    - `searchable` (boolean; optional):
        Enable items searching.
    
    - `shadow` (boolean | number | string | dict | list; optional):
        Dropdown shadow from theme or any value to set box-shadow.
    
    - `style` (boolean | number | string | dict | list; optional):
        Inline style.
    
    - `styles` (boolean | number | string | dict | list; optional):
        Mantine styles API.
    
    - `value` (string; optional):
        Controlled input value.
    
    - `variant` (a value equal to: 'default', 'filled', 'unstyled'; optional):
        Defines input appearance, defaults to default in light color
        scheme and filled in dark.  
"""


text4 = """

### Example:  Custom Dropdown Component dmc.Select  with different Options

This example shows how to use more features of the dmc.Select component.

Note the following:
 - In the City column, the `labels` and `values` in the dropdown options are different.  For example the `value` "SFO" is displayed as
  "San Francisco".  We do this with the `valueFormatter`.   See more information in the <dccLink href="/rendering/value-formatters-intro" children="Value Formatters" /> section.
 - The Custom function  `filterArray` used with the `valueFormatter` is defined in the `dashAgGridFunctions.js` file in the `assets` folder.
 - One of the options in the City dropdown is not selectable
 - See how to organize the dropdown options into categories in the Things To Do column dropdown
"""

text5 = """
Thanks to @alistair.welch for the DMC_Select component.  See the [Dash Community Forum posts](https://community.plotly.com/t/using-dash-mantine-components-dmc-select-as-an-ag-grid-cell-editor/74988)
for more information, and also this [forum post](https://community.plotly.com/t/using-dash-core-components-dropdown-as-an-ag-grid-cell-editor/74898/15) for more background on how this component was developed.
"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.components.cell_editor_datepicker", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.components.cell_editor_number_input", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.components.cell_editor_dmc_select", make_layout=make_tabs),
        make_md(text4),
        example_app("examples.components.cell_editor_dmc_select_labels_and_vals", make_layout=make_tabs),
        make_md(text5)

    ],
)
