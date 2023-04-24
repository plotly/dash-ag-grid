from dash import html, dcc, register_page
from utils.code_and_show import example_app, make_tabs, make_app_first
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=8,
    description=app_description,
    title="Dash AG Grid - Column Pinning",
    # name="Bootstrap Utility Classes",
    # hashtags=["intro","background", "border", "color", "spacing", "text", "position"],
)

text1 = """
# Column Pinning

You can pin columns by setting the pinned attribute on the column definition to either 'left' or 'right'.
```
const columnDefs = [
    { "field": 'athlete', "pinned": 'left' }
]
```


Below shows an example with two pinned columns on the left and one pinned column on the right. The example also demonstrates changing the pinning via the API at runtime.

The grid will reorder the columns so that 'left pinned' columns come first and 'right pinned' columns come last. In the example below the state of pinned columns impacts the order of the columns such that when 'Country' is pinned, it jumps to the first position.

Jump To & Pinning
Below shows jumping to rows and columns via the API. Jumping to a pinned column makes no sense, as the pinned columns, by definition, are always visible. So below, if you try to jump to a pinned column no action will be taken.

Example Pinning
"""


text2 = """

` `
` `
## Pinning Via Column Dragging

It is possible to pin a column by moving the column in the following ways:

When other columns are pinned, drag the column to the existing pinned area.
When no columns are pinned, drag the column to the edge of the grid and wait for approximately one second. The grid will then assume you want to pin and create a pinned area and place the column into it.

Lock Pinned
If you do not want the user to be able to pin using the UI, set the property lockPinned=True. This will block the UI in the following way:

- Dragging a column to the pinned section will not pin the column.
- For AG Grid Enterprise, the column menu will not have a pin option.
The example below demonstrates columns with pinning locked. The following can be noted:

- The column Athlete is pinned via the configuration and has lockPinned=true. This means the column will be pinned always, it is not possible to drag the column out of the pinned section.
- The column Age is not pinned and has lockPinned=true. This means the column cannot be pinned by dragging the column.

All other columns act as normal. They can be added and removed from the pinned section by dragging.


"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.columns.column_pinning1", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.columns.column_pinning2", make_layout=make_tabs),
        #  up_next("text"),
    ],
)
