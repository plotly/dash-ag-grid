from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description

register_page(
    __name__,
    order=9,
    description=app_description,
    title="Dash AG Grid Layout and Style - Grid Size",
)

text1 = """
# Grid Size

Under normal usage, your application should set the width and height of the grid using CSS styles. The grid will
 then fit the width you provide and use scrolling inside the grid to allow all rows and columns to be viewed.

In Dash, the grid has a default size is set with `style={"height": 400, "width": "100%"}`. Unless you want to change this,
you do not need to include the `style` prop when you define the grid.

### Changing Width and Height

These snippets show different ways to set the size of the grid:
```
# Set px size
dag.AgGrid(    
     style={"height": 600, "width": 400}
)

# set % size
dag.agGrid(
     style={"height": "100%", "width": "100%"}
)
```

> __Pitfall When Using Percent Width & Height__
> If using % for your height, then make sure the container you are putting the grid into also has height specified, as
 the browser will fit the div according to a percentage of the parents height, and if the parent has no height, then
  this % will always be zero.
>
> If your grid is not the size you think it should be then put a border on the grid's div and see if that's the size you
 want (the grid will fill this div). If it is not the size you want, then you have a CSS layout issue in your
  application. If the width and / or height change after the grid is initialised, the grid will automatically resize
   to fill the new area.

### Example 1 Changing grid size in a callback
- The Default Size button shows  `style={"height": 400, "width": "100%"}`  
- The Change Size button shows `style={"height": 600, "width": 400}`  


"""

text2 = """
### Grid Auto Height
Depending on your scenario, you may wish for the grid to auto-size it's height to the number of rows displayed inside the grid. This is useful if you have relatively few rows and don't want empty space between the last row and the bottom of the grid.

To allow the grid to auto-size it's height to fit rows, set grid property `domLayout='autoHeight'`.

> __Don't use Grid Auto Height when displaying large numbers of rows__
>
> If using Grid Auto Height, then the grid will render all rows into the DOM. This is different to normal operation where the grid will only render rows that are visible inside the grid's scrollable viewport. For large grids (eg >1,000 rows) the draw time of the grid will be slow, or for very large grids, your application can freeze. This is not a problem with the grid, it is a limitation on browsers on how much data they can easily display on one web page. For this reason, if showing large amounts of data, it is not advisable to use Grid Auto Height. Instead use the grid as normal and the grid's row virtualisation will take care of this problem for you.

### Example 2 Auto Height

This example shows a small grid.  The first grid uses the default height of `400px` and you can see the empty space
 after the last row.  The second grid sets `domLayout='autoHeight'`.
"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.layout.grid_size", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.layout.grid_size_autosize", make_layout=make_tabs),
        # up_next("text"),
    ],
)
