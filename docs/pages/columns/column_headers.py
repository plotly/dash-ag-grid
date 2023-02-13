from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=4,
    description=app_description,
    title="Dash AG Grid Column Definitions",
    # name="Bootstrap Utility Classes",
    # hashtags=["intro","background", "border", "color", "spacing", "text", "position"],
)

text1 = """
## React Data Grid: Column Headers
Each column has a header at the top that typically displays the column name and has access to column features,
 such as sorting, filtering and a column menu. This page explains how you can manage the headers.

### Header Height

These properties can be used to change the different heights used in the headers.

- `headerHeight`   The height in pixels for the row containing the column label header. If not specified, it uses the theme value of header-height.
- `groupHeaderHeight` The height in pixels for the rows containing header column groups. If not specified, it uses headerHeight.
- `floatingFiltersHeight`  The height in pixels for the row containing the floating filters. If not specified, it uses the theme value of header-height.
- `pivotHeaderHeight` (enterprise) The height in pixels for the row containing the columns when in pivot mode. If not specified, it uses headerHeight.
- `pivotGroupHeaderHeight`  (enterprise) The height in pixels for the row containing header column groups when in pivot mode. If not specified, it uses groupHeaderHeight.

### Text Orientation

By default, the text label for the header is display horizontally, i.e. as normal readable text. To display the text in
 another orientation you have to provide your own CSS to change the orientation and also provide the adequate header
  heights using the appropriate grid property.

Example: Header Height and Text Orientation
The following example shows how you can provide a unique look and feel to the headers. Note that:

The header heights have all been changed via grid options:
```
groupHeaderHeight= 75,
headerHeight= 150,
```
"""

text1a = """
The following class was added to a .css file in the assets folder

```
.header1 .ag-header-cell-label {
  /*Necessary to allow for text to grow vertically*/
  height: 100%;
  padding: 0 !important;
}

.header1 .ag-header-group-cell {
  font-size: 50px;
}

.header1 .ag-header-cell-label .ag-header-cell-text {
  /*Force the width corresponding at how much width
    we need once the text is laid out vertically*/
  width: 55px;
  writing-mode: vertical-lr;
  -ms-writing-mode: tb-lr;
  line-height: 2em;
  margin-top: 60px;
}


```

"""


text2 = """

` `
` `
` `  
` ` 


## Auto Header Height


The column header row can have its height set automatically based on the content of the header cells. This is most useful when used together with Custom Header Components or when using the `wrapHeaderText` column property.

To enable this, set `autoHeaderHeight=True` on the column definition you want to adjust the header height for. If more than one column has this property enabled, then the header row will be sized to the maximum of these column's header cells so no content overflows.

The example below demonstrates using the `autoHeaderHeight` property in conjunction with the `wrapHeaderText` property, so that long column names are fully displayed.

Note that the long column header names wrap onto another line
Try making a column smaller by dragging the resize handle on the column header, observe that the header will expand so the full header content is still visible.

"""


text3 = """

` `
` `
` `  
` ` 


## Header Tooltips
You can provide a tooltip to the header using colDef.headerTooltip.

The example below shows header tooltips. Note the following:

All the columns, apart from Country and Year, have a header tooltip set.
We have set the Grid `tooltipShowDelay` property to 500ms to make the tooltips appear quicker.


"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.columns.column_headers1", make_layout=make_tabs),
        make_md(text1a),
        make_md(text2),
        example_app("examples.columns.column_headers2", make_layout=make_tabs),
        make_md(text3),
        example_app("examples.columns.column_headers3", make_layout=make_tabs),
        #  up_next("text"),
    ],
)
