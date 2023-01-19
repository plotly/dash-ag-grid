from dash import html, dcc, register_page
from utils.code_and_show import example_app, make_tabs, make_app_first
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=7,
    description=app_description,
    title="Dash AG Grid Column Definitions",
)

text1 = """
# Column Moving

Columns can be moved in the grid in the following ways:

- Dragging the column header with the mouse or through touch.
- updating the `columnDefs` in a callback


### Moving Animation
Column animations happen when you move a column. The default is for animations to be turned on. It is recommended that you leave the column move animations on unless your target platform (browser and hardware) is too slow to manage the animations. To turn OFF column animations, set the grid property suppressColumnMoveAnimation=true.

The move column animation transitions the column's position only, so when you move a column, it animates to the new position. No other attribute apart from position is animated.

### Suppress Hide Leave
The grid property suppressDragLeaveHidesColumns will stop columns getting removed from the grid if they are dragged outside of the grid. This is handy if the user moves a column outside of the grid by accident while moving a column but doesn't intend to make it hidden.

### Suppress Movable
The column property suppressMovable changes whether the column can be dragged. The column header cannot be dragged by the user to move the columns when suppressMovable=true. However the column can be inadvertently moved by placing other columns around it thus only making it practical if all columns have this property.

### Lock Position
> Requires ag-grid>=V28.0

The column property lockPosition locks columns to one side of the grid. When lockPosition is set as either "left" or "right", the column will always be locked to that position, cannot be dragged by the user, and cannot be moved out of position by dragging other columns.

#### Suppress Movable Example
The example below demonstrates these properties as follows:
- The Athlete column has moving suppressed. It is not possible to move this column, but it is possible to move other columns around it.
- The grid has suppressDragLeaveHidesColumns set to true so columns dragged outside of the grid are not hidden (normally dragging a column out of the grid will hide the column).
- The defaultColDef has lockPinned set to true so it is not possible to pin columns.

"""

text2 = """
` `
` `
` `
### Suppress Movable & Lock Position Example

> Requires ag-grid>=V28.0

The example below demonstrates these properties as follows:

- The Age column is locked "left" as the first column in the scrollable area of the grid. It is not possible to move this column, or have other columns moved over it to impact its position. As a result the Age column marks the beginning of the scrollable area regardless of its position within the column definitions.
- The Total column is locked "right" and likewise its position can not be impacted by moving other columns.
- The Athlete column has moving suppressed. It is not possible to move this column, but it is possible to move other columns around it.
- The grid has suppressDragLeaveHidesColumns set to true so columns dragged outside of the grid are not hidden (normally dragging a column out of the grid will hide the column).
- The defaultColDef has lockPinned set to true so it is not possible to pin columns to the left or right of the locked columns.

"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.columns.column_moving", make_layout=make_tabs),
        make_md(text2)
        #  up_next("text"),
    ],
)
