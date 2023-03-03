from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description

register_page(
    __name__,
    order=1,
    description=app_description,
    title="Dash AG Grid Clientside Data",
)

text1 = """
# Transaction Updates
Transaction Updates allow large numbers of rows in the grid to be added, removed or updated in an efficient manner. Use Transaction Updates for fast changes to large datasets.

`rowTransaction` - Updates row data. Pass a transaction object with lists for add, remove and update.


### Identifying Rows for Update and Remove

In order to update, add or remove data with `rowTransaction` the data must have a Row ID. 
If you are providing Row IDs using `getRowId()` then the grid will match data provided in the transaction with data in the grid using the key.

> Row IDs must be unique and not editable.  See the [Row IDs](/rows/row-ids) page for more information.

For updating rows, the grid will find the row with the same key and then swap the data out for the newly provided data.

For removing rows, the grid will find the row with the same key and remove it. For this reason, the provided records within the remove array only need to have a key present.

```
rowTransaction = {
  "add": [
      # adding a row, there should be no row with ID = 4 already
      {"employeeId": "4", "name": "Billy", "age": 55}
  ],
  
  "update": [
      # updating a row, the grid will look for the row with ID = 2 to update
      {"employeeId": "2", name: "Bob", "age": 23}
  ],
  
  "remove": [
      # deleting a row, only the ID is needed, other attributes (name, age) don't serve any purpose
      {"employeeId": "5"}
  ]
}
```

### Example 1: Updating with `rowTransaction` and `rowData`

The example updates data in different ways:

- Start Over and Clear updates all the rows with the `rowData` prop
- Updated Selected, Remove Selected and Add Rows uses rowTransaction to only update certain data
"""


text2 = """
### Example 2:  Adding pre-selected rows

In this example, note the following:
- Row ids are set with `getRowId(params.data.id)`
- The ids are generated from the n_clicks counter, so they are unique
- The `"id"` column is hidden by setting `{"hide": True}` in the `columnDefs`
- The new rows are automatically selected. 

"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.clientside_data.rowTransaction", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.clientside_data.rowTransaction2", make_layout=make_tabs),
    ],
)
