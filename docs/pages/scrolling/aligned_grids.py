from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid - Aligned Grids",
)

text1 = """
# Aligned Grids
Aligning two or more grids means columns will be kept aligned in all grids. In other words, column changes to one grid (column width, column order, column visibility etc) are reflected in the other grid. This is useful if you have two grids, one above the other such that their columns are vertically aligned, and you want to keep the columns aligned.

### Configuration
To have one (the first) grid react to column changes in another grid (the second), provide the second grid with a reference to the first grid.
```
grid_two = dag.AgGrid(
    id="grid-two",    
    # other props
)

grid_one = dag.AgGrid(
    id="grid-one",
    dashGridOptions={'alignedGrids': ['grid-2'],
    # other props
)
```


### Example 1 : Aligned Grids
Below shows two grids, both aligned with the other (so any column change to one will be reflected in the other). The following should be noted:

- When either grid is scrolled horizontally, the other grid follows.
- When a column is resized on either grid, the other grid follows.
- When a column group is opened on either grid, the other grid follows.
- When a column is dragged off the grid on either grid, the other grid follows.  Set `suppressDragLeaveHidesColumns=False` to allow dragging columns off the grid.
- The grids don't serve much purpose (why would you show the same grid twice???) however it demonstrates the features in an easy to understand way.
"""

text2 = """

` `  
` `  

### Events
The events which are fired as part of the grid alignment relationship are as follows:

- Horizontal Scroll
- Column Hidden / Shown
- Column Moved
- Column Group Opened / Closed
- Column Resized
- Column Pinned


### Pivots
The pivot functionality does not work with aligned grids. This is because pivoting data changes the columns, which would make the aligned grids incompatible, as they are no longer sharing the same set of columns.

### Example 2 : Aligned Grid as Footer
So why would you want to align grids like this? It's great for aligning grids that have different data but similar columns. Maybe you want to include a footer grid with 'summary' data. Maybe you have two sets of data, but one is aggregated differently to the other.

This example is a bit more useful. In the bottom grid, we show a summary row. Also note the following:

- The top grid has no horizontal scroll bar, suppressed via a `dashGridOptions`.
- The bottom grid has no header, suppressed via a `dashGridOptions`. 

"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.scrolling.aligned_grids1", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.scrolling.aligned_grids2", make_layout=make_tabs),


        # up_next("text"),
    ],
)
