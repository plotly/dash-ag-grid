from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid Editing",
)


intro = """
# Start / Stop Cell Editing
This page discusses the different ways in which Cell Editing can be started and stopped.

### Start Editing
Assuming `editable=True`, editing will start upon any of the following:

- Edit Key Pressed: One of the following is pressed: Enter, F2.
- Backspace: The default editor will start and clear the contents of the cell if Backspace is pressed on Windows. To mimic this behaviour on MacOS, use the enableCellEditingOnBackspace=true grid option.
- Printable Key Pressed: Any of the following characters are pressed: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"£$%^&amp;*()_+-=[];\'#,./\|<>?:@~{}
The default editor places this character into the edit field so that the user experience is they are typing into the cell.
- Mouse Double Click: If the mouse is double-clicked. There is a grid property `singleClickEdit` that will allow single-click to start editing instead of double-click. Another property `suppressClickEdit` will prevent both single-click and double-click from starting the edit; use this if you only want to have your own way of starting editing, such as clicking a button in your custom cell renderer.

### Stop Editing
The grid will stop editing when any of the following happen:

- Other Cell Focus: If focus in the grid goes to another cell, the editing will stop.
- Enter Key Down: If the grid receives an Enter key press event on the cell.
- Escape Key Down: Similar to Enter, if Esc key is pressed, editing will stop. Unlike Enter, the Esc action will discard changes rather than taking the new value.
- Tab Key Down: Editing will stop, accepting changes, and editing will move to the next cell, or the previous cell if Shift is also pressed.
- Popup Editor Closed: If using popup editor, the popup is configured to close if you click outside the editor. Closing the popup triggers the grid to stop editing.

### Tab Navigation
While editing, if you hit Tab, the editing will stop for the current cell and start on the next cell. If you hold down Shift+Tab, the same will happen except the previous cell will start editing rather than the next. This is in line with editing data in Excel.

"""

text1 = """
### Enter Key Navigation

By default pressing Enter will start editing on a cell, or stop editing on an editing cell. It will not navigate to the cell below.

To allow consistency with Excel the grid has the following properties:

- `enterMovesDown`: Set to `True` to have Enter key move focus to the cell below if not editing. The default is Enter key starts editing the currently focused cell.
- `enterMovesDownAfterEdit`: Set to `True` to have Enter key move focus to the cell below after Enter is pressed while editing. The default is editing will stop and focus will remain on the editing cell.
The example below demonstrates the focus moving down when Enter is pressed.

"""


text2 = """
### Single-Click Editing
The default is for the grid to enter editing when you Double-Click on a cell. To change the default so that a single-click starts editing, set the property `dashGridOptions={"singleClickEdit": True},`. This is useful when you want a cell to enter edit mode as soon as you click on it, similar to the experience you get when inside Excel.

It is also possible to define single-click editing on a per-column basis using `singleClickEdit = True in the `columnDefs` prop.

The grid below has `singleClickEdit = True` so that editing will start on a cell when you single-click on it.

"""


text3 = """
### Stop Editing When Grid Loses Focus
By default, the grid will not stop editing the currently editing cell when the cell loses focus, unless another cell is clicked on. This means clicking on the grid header, or another part of your application, will not stop editing. This can be bad if, for example, you have a save button, and you need the grid to stop editing before you execute your save function (e.g. you want to make sure the edit is saved into the grid's state).

If you want the grid to stop editing when focus leaves the cell or the grid, set the grid property `dashGridOptions={"stopEditingWhenCellsLoseFocus": True}`

The example below shows the editing with `dashGridOptions={"stopEditingWhenCellsLoseFocus": True}`. Notice the following:

Double-click a cell to start editing, then click outside the grid (or on a header) and the grid will stop editing.


"""

text4 = """
>
> Cell Editing can also be performed via Cell Editor Components; please see:
> - <dccLink href='/editing/cell-editors' children='Cell editors' /> to see regular and popup cell editors.
> - <dccLink href='/editing/provided-cell-editors' children='Provided cell editors' />  to see select (dropdown) editors, and lage text (textarea) editors
>

"""


layout = html.Div(
    [
        make_md(intro),
        make_md(text1),
        example_app("examples.editing.start_stop_editing", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.editing.start_stop_editing2", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.editing.start_stop_editing3", make_layout=make_tabs),
        make_md(text4)
        # up_next("text"),
    ],
)
