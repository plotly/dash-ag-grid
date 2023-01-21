from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=2,
    description=app_description,
    title="Dash AG Grid Column Definitions",
)

text1 = """

# Updating Column Definitions
The section Column Definitions explained how to configure columns. It is possible to change the configuration of the Columns after they are initially set. This section goes through how to update Column Definitions.


## Adding & Removing Columns
It is possible to add and remove columns by updating the list of Column Definitions provided to the grid.

When new columns are set, the grid will compare with current columns and work out which columns are old (to be removed), new (new columns created) or kept.

The example below demonstrates adding and removing columns from a grid. Note the following:

- Selecting the buttons to toggle between including or excluding the medal columns.
- Any state applied to any column (e.g. sort, filter, width) will be kept if the column still exists after the new definitions are applied. 
For example try the following:
   - Resize Country column. Note changing columns doesn't impact its width.
   - Sort Country column. Note changing columns doesn't impact its sort.
"""

text2 = """

` `  
` ` 

## Updating Column Definitions

All properties of a column definition can be updated. For example if you want to change the Header Name of a column, you update the headerName on the Column Definition and then set the list of Column Definitions into the grid again.

It is not possible to update the Column Definition of just one column in isolation. Only a new set of Column Definitions can be applied.

The example below demonstrates updating column definitions to change how columns are configured. Note the following:

All Columns are provided with just the field attribute set on the Column Definition.
'Set Header Names' and 'Remove Header Names' sets and then subsequently removes the headerName attribute on all Columns.

Note that any resizing, sorting etc of the Columns is kept intact between updates to the Column Definitions.

"""


text3 = """

` `  
` `

##  Column Definition State Retrieval

There will be times when you'll want to retrieve the current Column Definition in order to perhaps persist them, or perhaps retrieve, alter and then re-apply the modified columns.

The current column state can be retrieved with columnState
"""


text4 = """

` `  
` `

##  Updating Column Groups

Column Groups can be updated in the same way as Columns, you just update the Column Group Definition. For expandable groups, to have open / closed state to be maintained, you need to assign groupId in the Column Group Definition.

```
columnDefs = [
    {
        "headerName": "Group A",
        "groupId": "groupA",
        "children": [
            { "field": "name" },
            { "field": 'age', "columnGroupShow": "open" }
        ]
    }
];
```

In the example below, note the following:

- Clicking the top buttons alternates the columns from two sets of definitions.
- Column Group A - groupId is provided, so expand / collapse is preserved. The Header Name also changes.
- Column Group B - groupId is NOT provided, so expand / collapse is lost, group always closes when updates happen.
- Column Group C - groupId is provided, so expand / collapse is preserved. Child columns are changed.

"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.columns.updating_definitions1", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.columns.updating_definitions2", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.columns.updating_definitions3", make_layout=make_tabs),
        make_md(text4),
        example_app("examples.columns.updating_definitions4", make_layout=make_tabs),
        # up_next("text"),
    ],
)
