from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=1,
    description=app_description,
    title="Dash AG Grid Column Definitions",
    # name="Bootstrap Utility Classes",
    # hashtags=["intro","background", "border", "color", "spacing", "text", "position"],
)

text1 = """
# Column Definitions
Each column in the grid is defined using the `columnDefs` prop . Columns are positioned in the grid according
 to the order the Column Definitions are specified in the Grid Options.
 
For example, this shows a grid with 3 columns:
  
```
columnDefs = [
    { 'field': 'athlete' },
    { 'field': 'sport' },
    { 'field': 'age' },
] 
 ```
 
You can also use the `defaultColDef` to apply props to all columns.  
 
When the grid creates a column it starts with the default column definition, then adds properties defined via 
 column types and then finally adds in properties from the specific column definition.
 
In this example, all the fields are editable except for the "athlete" field

 
```
columnDefs = [
    { 'field': 'athlete' , 'editable': False },
    { 'field': 'sport' },
    { 'field': 'age' },
] 

defaultColDef = {'editable': True}
```


` `  
` ` 

### Example of a grid with `ColumnDefs` and `defaultColDef` defined.
 
"""


text2 = """
------------------
## Grouping columns

If you want the columns to be grouped, you can include them as children like so:

```
# put the three columns into a group
columnDefs = [
    {
        'headerName': 'Group A',
        'children': [
            { 'field': 'athlete' },
            { 'field': 'sport' },
            { 'field': 'age' }
        ]
    }
]
```


"""


text3 = """

` `  
` ` 
## Column Types

The grid also provides additional ways to help simplify and avoid duplication of column definitions. This is done through the following:

- defaultColDef: contains properties that all columns will inherit.
- defaultColGroupDef: contains properties that all column groups will inherit.
- columnTypes: specific column types containing properties that column definitions can inherit.

Default columns and column types can specify any of the [column properties](https://www.ag-grid.com/react-data-grid/column-properties/) available on a column.


"""

text4 = """"

` `  
` ` 

## Right Aligned and Numeric Columns

The grid provides a handy shortcut for aligning columns to the right. Setting the column definition type to rightAligned aligns the column header and contents to the right, which makes the scanning of the data easier for the user.

Because right alignment is used for numbers, we also provided an alias numericColumn that can be used to align the header and cell text to the right.

```
columnDefs = [
    { 'headerName': 'Column A', 'field': 'a' },
    { 'headerName': 'Column B', 'field': 'b', 'type': 'rightAligned' },
    { 'headerName': 'Column C', 'field': 'c', 'type': 'numericColumn' },
]
```

The rightAligned column type works by setting the header and cell class properties as follows. If you manually set either headerClass or cellClass then you may need to include the right aligned CSS classes yourself as column type properties are overridden by explicitly defined column properties.

```
rightAligned = {
    'headerClass': 'ag-right-aligned-header',
    'cellClass': 'ag-right-aligned-cell'
}
```




"""


layout = html.Div(
    [
        #  html.Div(id="intro"),
        make_md(text1),
        example_app("examples.columns.column_definitions1", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.columns.column_definitions2", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.columns.column_definitions3", make_layout=make_tabs),
        make_md(text4),
        example_app("examples.columns.column_definitions4", make_layout=make_tabs),
        # up_next("text"),
    ],
)
