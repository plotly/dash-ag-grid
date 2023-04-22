from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=5,
    description=app_description,
    title="Dash AG Grid Column Definitions",
    # name="Bootstrap Utility Classes",
    # hashtags=["intro","background", "border", "color", "spacing", "text", "position"],
)

text1 = """
## Column Groups

Grouping columns allows you to have multiple levels of columns in your header and the ability, if you want, to 'open and close' column groups to show and hide additional columns.

Grouping columns is done by providing the columns in a tree hierarchy to the grid. There is no limit to the number of levels you can provide.

Here is a code snippet of providing two groups of columns.

```

columnDefs= [
        {
            'headerName': 'Athlete Details',
            'children': [
                { 'field': 'athlete' },
                { 'field': 'age' },
                { 'field': 'country' },
            ]
        },
        {
            'headerName': 'Sports Results',
            'children': [
                { 'field': 'sport' },
                { 'field': 'total', 'columnGroupShow': 'closed' },
                { 'field': 'gold', 'columnGroupShow': 'open' },
                { 'field': 'silver', 'columnGroupShow': 'open' },
                { 'field': 'bronze', 'columnGroupShow': 'open' },
            ]
        }
    ]
```

"""


text2 = """

` `
` `
## Column Definitions vs Column Group Definitions


The list of Columns in `columnDefs` can be a mix of Columns and Column Groups. You can mix and match at will, every level can have any number of Columns and Column Groups and in any order. The difference in Column vs Column Group definitions is as follows:

- The children attribute is mandatory for Column Groups and not applicable for Columns.
- If a definition has a children attribute, it is treated as a Column Group. If it does not have a children attribute, it is treated as a Column.
- Most other attributes are not common across groups and columns (eg groupId is only used for groups). If you provide attributes that are not applicable (eg you give a column a groupId) they will be ignored.

### Showing / Hiding Columns

A group can have children initially hidden. If you want to show or hide children, set `columnGroupShow` to either 'open' or 'closed' to one or more of the children. When a children set has `columnGroupShow` set, it behaves in the following way:

- open: The child is only shown when the group is open.
- closed: The child is only shown when the group is closed.
- everything else: Any other value, including null and undefined, the child is always shown.

If a group has any child that is dependent on the open / closed state, the open / close icon will appear. Otherwise the icon will not be shown.

Having columns only show when closed is useful when you want to replace a column with others. For example, in the code snippet above (and the example below), the 'Total' column is replaced with other columns when the group is opened.

If a group has an 'incompatible' set of children, then the group opening / closing will not be activated. An incompatible set is one which will have no columns visible at some point (i.e. all are set to 'open' or 'closed').

### Pinning and Groups

Pinned columns break groups. So if you have a group with 10 columns, 4 of which are inside the pinned area, two groups will be created, one with 4 (pinned) and one with 6 (not pinned).

### Moving Columns and Groups

If you move columns so that columns in a group are no longer adjacent, then the group will again be broken and displayed as one or more groups in the grid.

### Resizing Groups
If you grab the group resize bar, it resizes each child in the group evenly distributing the new additional width. If you grab the child resize bar, only that one column will be resized.


### Colouring Groups
The grid doesn't colour the groups for you. However you can use the column definition headerClass for this purpose. The `headerClass` attribute is available on both columns and column groups.

```
columnDefs = [
    # the CSS class name supplied to 'headerClass' will get applied to the header group
    { "headerName": 'Athlete Details', "headerClass": 'my-css-class', "children": []}
]
```


### Align the Header Group Label To The Right
The labels in the grouping headers are positioned with display: flex. To make the group headers right-aligned, add the following rule set in your application, after the grid's stylesheets. Change the theme class to the one you use.

```
.ag-theme-alpine .ag-header-group-cell-label {
    flex-direction: row-reverse;
}
```

### Marry Children
Sometimes you want columns of the group to always stick together. To achieve this, set the column group property `marryChildren=True`. The example below demonstrates the following:

- Both 'Athlete Details' and 'Sports Results' have `marryChildren=True`.
- If you move columns inside these groups, you will not be able to move the column out of the group. For example, if you drag 'Athlete', it is not possible to drag it out of the 'Athlete Details' group.
- If you move a non group column, e.g. Age, it will not be possible to place it in the middle of a group and hence impossible to break the group apart.
- It is possible to place a column between groups (e.g. you can place 'Age' between the 'Athlete Details' and 'Sports Results').


Here is the class added to the .css file in the assets folder
```
.header3 .ag-header-group-cell-with-group {
  background-color: #00e7b1 !important;
}
```

"""

text3="""
### Sticky Label
When Column Groups are too wide, it might be useful to have the Header Label to be always visible while scrolling the grid horizontally. To achieve this, set the column group property `stickyLabel=True`. The example below demonstrates the following:

- Both 'Athlete Details' and 'Sport Results' have `stickyLabel=True`.
- If you scroll the grid horizontally, the header label will always be visible until it's completely out of view.


"""

text4 = """

` `
` `

## Group Changes


Similar to adding and removing columns, you can also add and remove column groups. If the column definitions passed in have column groups, then the columns will be grouped to the new configuration.

The example below shows adding and removing groups to columns. Note the following:

- Select No Groups to show all columns without any grouping.
- Select Participant in Group to show all participant columns only in a group.
- Select Medals in Group to show all medal columns only in a group.
- Select Participant and Medals in Group to show participant and medal columns in groups.
- As groups are added and removed, note that the state of the individual columns is preserved. To observe this, try moving, resizing, sorting, filtering etc and then add and remove groups, all the changed state will be preserved.
"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.columns.column_groups1", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.columns.column_groups2", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.columns.column_groups_sticky_label", make_layout=make_tabs),
        make_md(text4),
        example_app("examples.columns.column_groups3", make_layout=make_tabs),
        #  up_next("text"),
    ],
)
