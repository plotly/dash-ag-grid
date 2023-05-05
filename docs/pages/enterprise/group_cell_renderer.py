from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description
from utils.other_components import enterprise_blurb


register_page(
    __name__,
    order=3,
    description=app_description,
    title="Dash AG Grid Enterprise Features - Group Cell Renderers",
)

text1 = """
# Group Cell Renderer

"""

text2 = """

If you are grouping in the grid, then you will need to provide a group cell renderer as the group cell renderer is what provides the user with the expand and collapse functionality.

#### Group Cell Renderer Configuration

The key for the group cell renderer is `agGroupCellRenderer`.

The grid's group cell renderer takes many parameters to configure it. Here is an example of a column and its configuration:

```

    columnDefs= [
        # column definition configured to show group values with the cell renderer set to 'group'
        {
            "showRowGroup": True,
            "cellRenderer":'agGroupCellRenderer',
            # provide extra params to the cellRenderer
            'cellRendererParams': {
                # turn off the row count
                'suppressCount': true,
                # turn off double click for expand
                'suppressDoubleClickExpand': True,
                # enable checkbox selection
                'checkbox': True,
                # provide an inner renderer
                'innerRenderer': 'myInnerRenderer',
                # provide an inner renderer
                'innerRendererParams': {'foo': 'bar'},
                # provide a footer value getter
                'footerValueGetter': 'myFooterValueGetter'
            }
        }
    ]

```

The full set of parameters for the group cell renderer are defined on [`GroupCellRendererParams`](https://www.ag-grid.com/react-data-grid/group-cell-renderer/) 

Below shows an example of configuring a group cell renderer. The example setup is not realistic as it has many columns configured for showing the groups. The reason for this is to demonstrate different group column configurations side by side. In your application, you will typically have one column for showing the groups.

The example is built up as follows:

- The data is grouped by two columns: **Type** (one of 'Fiction' or 'Non-Fiction') and **Country** (a country name, eg Ireland or United Kingdom).

- The column **'Country Group - No Renderer'** configures the grid to put the 'Country' group data only into this column by setting `showRowGroup='country'`. All rows that are not this group are blank. There is no cell renderer configured, so the grid just places the text for the group into the cell, there is not expand / collapse functionality.

- The column **'All Groups - no Renderer'** builds on before, but adds all groups by setting `showRowGroup=true`. This gets the column to display all groups, but again no cell renderer so not expand / collapse functionality.

- The column **Group Renderer A** builds on before, but adds the group cell renderer with `cellRenderer='agGroupCellRenderer'`. The values are exactly as per the previous column, except now we have expand and collapse functionality.

- The column **Group Renderer B** builds on before, but adds `field=city` so that the city is displayed in the leaf nodes in the group column.

- The column **Group Renderer C** builds on before, but adds the following `cellRendererParams`:

    - `suppressCount=True`: Suppresses the row count.
    - `suppressDoubleClickExpand=True`: Suppress double click for expanding.
    - `checkbox=True`: Adds a selection checkbox.
    - `innerRenderer="SimpleCellRenderer"`: Puts custom rendering for displaying the value. The group cellRenderer will take care of all the expand / collapse, selection etc, but then allow you to customise the display of the value. In this example we add a border when the value is a group, and we set the colour based on whether the cell is a leaf node or not.

<grid-example title='Group Cell Renderer Configuration' name='group-renderer' type='mixed' options='{"enterprise": true, "modules": ["clientside", "rowgrouping"]}'></grid-example>

"""


text3 = """
#### Conditionally Hide Group Cell Renderer

It is possible to conditionally hide the Group Cell Renderer. This might be useful in cases where the Expand / Collapse
chevron should not be displayed in certain group cells.

See the [AG Grid Docs](https://www.ag-grid.com/react-data-grid/group-cell-renderer/) for an example.
"""


layout = html.Div(
    [
        make_md(text1),
        make_md(enterprise_blurb),
        make_md(text2),
        example_app("examples.enterprise.group_cell_renderer", make_layout=make_tabs),
        make_md(text3),
        # up_next("text"),
    ],
)
