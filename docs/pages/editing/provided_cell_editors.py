from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=4,
    description=app_description,
    title="Dash AG Grid Editing",
)


text1 = """
# Provided Cell Editors
The grid comes with some cell editors provided out of the box. These cell editors are listed here.

- Text Cell Editor
- Large Text Cell Editor
- Select Cell Editor

"""

text2= """

### Text Cell Editor
Simple text editor that uses the standard HTML input. This editor is the default if none other specified.

Specified with `agTextCellEditor`

 `cellEditorParams` available for agTextCellEditor:
- `useFormatter` (boolean) If True, the editor will use the provided `colDef.valueFormatter` to format the value displayed in the editor.
- `maxLength` (number) Max number of characters to allow. Default: 524288

```
columnDefs =  [
    {
        'cellEditor': 'agTextCellEditor',
        'valueFormatter': "'£' + value",
        'cellEditorParams': {
            'useFormatter': True,
            'maxLength': 200
        }
        # ...other props
    }
]

```
### Large Text Cell Editor
Simple editor that uses the standard HTML textarea. Best used in conjunction with `cellEditorPopup`=True.

Specified with `agLargeTextCellEditor`.

cellEditorParams available for agLargeTextCellEditor:

- `maxLength` (number) Max number of characters to allow. Default: 200
- `rows` (number) Number of character rows to display. Default: 10
- `cols` (number) Number of character columns to display. Default: 60

```
columnDefs = [
    {
        'cellEditor': 'agLargeTextCellEditor',
        'cellEditorPopup': True,
        'cellEditorParams': {
            'maxLength': 100,
            'rows': 10,
            'cols': 50
        }
        # ...other props
    }
]

```
### Select Cell Editor
Simple editor that uses HTML select.

Specified with `agSelectCellEditor`.

cellEditorParams available:

- values (list) A List of values to display.

```
columnDefs= [
    {
        'cellEditor': 'agSelectCellEditor',
        'cellEditorParams': {
            'values': ['English', 'Spanish', 'French', 'Portuguese', '(other)'],
        }
        # ...other props
    }
]
```
Note there is no need to specify `cellEditorPopup=True` for Select Cell Editor as the browsers Select widget will appear on top of the grid.


> We have found the standard HTML Select doesn't have an API that's rich enough to play properly with the grid. When a cell is double clicked to start editing, it is desired that the Select is a) shown and b) opened ready for selection. There is no API to open a browsers Select. For this reason to edit there are two interactions needed 1) double click to start editing and 2) single click to open the Select.
>
> We also observed different results while using keyboard navigation to control editing, e.g. while using Enter to start editing. Some browsers would open the Select, others would not. This is down to the browser implementation and given there is no API for opening the Select, there is nothing the grid can do.
>
> If you are unhappy with the additional click required, we advise you don't depend on the browsers standard Select (ie avoid `agSelectCellEditor`) and instead use `agRichSelectCellEditor` (Available in AG Grid Enterprise).
>

"""

layout = html.Div(
    [

        make_md(text1),
        example_app("examples.editing.provided_cell_editors", make_layout=make_tabs),
        make_md(text2)

        # up_next("text"),
    ],
)
