from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description
from utils.other_components import enterprise_blurb


register_page(
    __name__,

    description=app_description,
    title="Dash AG Grid Enterprise Features - Tree Data",
)

text1 = """
# Tree Data
"""

text2 = """

Use Tree Data to display data that has parent / child relationships where the parent / child relationships are provided
 as part of the data. For example, a folder can contain zero or more files as well as other folders.

### Tree Data Mode
In order to set the grid to work with Tree Data, simply enable Tree Data mode via the `dashGridOptions` using:
```
dag.AgGrid(
    dashGridOptions={"treeData": True},
    # other props
)
```
### Supplying Tree Data
When providing tree data to the grid, you will need to use a function with the `getDataPath` prop to tell the
 grid the hierarchy for each row. The function must return a string[] representing the route, with each element
  specifying a level of the tree. Below are two examples presenting the hierarchy in different ways.

```
dag.AgGrid(
    dashGridOptions={"getDataPath": {"function": "getDataPath(params)"}},
    # other props
)

```

### GetDataPath

The `getDataPath(params)` function is defined in the `dashAgGridFunctions.js` file in the assets folder.

The following are two examples with a sample hierarchy, Malcolm is child of Erica
```
#    + Erica
#         - Malcolm
```

#### Example #1 - hierarchy in the data is already a string array
```
rowData = [
    { 'orgHierarchy': ['Erica'], 'jobTitle': "CEO", 'employmentType': "Permanent" },
    { 'orgHierarchy': ['Erica', 'Malcolm'], 'jobTitle': "VP", 'employmentType': "Permanent" }    
    ...
]
```
Just return the hierarchy, no conversion required:

Defined in `/assets/dashAgGridFunctions.js`:
```
var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.getDataPath = function (data) {
    return data.orgHierarchy;
}
```

#### Example #2 - hierarchy is a path string, needs conversion
```
rowData = [
    { 'path': "Erica", jobTitle: "CEO", 'employmentType': "Permanent" },
    { 'path': "Erica/Malcolm", jobTitle: "VP", 'employmentType': "Permanent" }
    ...
]
```

This function converts "Erica/Malcolm" to \["Erica","Malcolm"\]

Defined in `/assets/dashAgGridFunctions.js`
```
var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.getDataPath = function (data) {
    return data.path.split('/'); // path: "Erica/Malcolm"
}
```

### Configuring Group Column
There are two ways to configure the Group Column:

- Auto Column Group - this is automatically selected by the grid when in Tree Data mode, however you can override the default.
- Custom Column Group - you can provide your own custom column group definition, which gives allows more control over how the Group Column is displayed.


### Example: Organisational Hierarchy
"""


layout = html.Div(
    [
        make_md(text1),
        make_md(enterprise_blurb),
        make_md(text2),
        example_app("examples.enterprise.tree_data", make_layout=make_tabs),
        # up_next("text"),
    ],
)
