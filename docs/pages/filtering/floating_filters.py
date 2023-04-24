from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=4,
    description=app_description,
    title="Dash AG Grid - Floating Filters",
)


text1 = """

# Floating Filters
Floating Filters are an additional row under the column headers where the user will be able to see and optionally edit the filters associated with each column.

Floating filters are activated by setting the property floatingFilter = true on the colDef:

const columnDefs = [
    #  column definition with floating filter enabled
    {
        'field': 'country',
        'filter': True,
        'floatingFilter': True
    }
];


To have floating filters on for all columns by default, you should set `floatingFilter` on the `defaultColDef`. You can then disable floating filters on a per-column basis by setting `floatingFilter = False` on an individual colDef.

Floating filters depend on and co-ordinate with the main column filters. They do not have their own state, but rather display the state of the main filter and set state on the main filter if they are editable. For this reason, there is no API for getting or setting state of the floating filters.

Every floating filter takes a parameter to show/hide automatically a button that will open the main filter.

To see how floating filters work see Floating Filter Components.

The following example shows the following features of floating filters:

- Text filter: has out of the box read/write floating filter (Sport column)
- Number filter: have out of the box read/write floating filters for all filters except when switching to in-range filtering, where the floating filter is read-only (Age columns)
- Columns with buttons containing 'apply' require the user to press Enter on the floating filter for the filter to take effect (Gold column). (Note: this does not apply to floating Date Filters, which are always applied as soon as a valid date is entered.)
- Changes made directly to the main filter are reflected automatically in the floating filters (change any main filter)
- The Year column has a filter, but has the floating filter disabled
- The Total column has no filter and therefore no floating filter either
- Combining `suppressMenu = True` and `filter = False` lets you control where the user can access the full filter. In this example `suppressMenu = Yrue` for all the columns except Year, Silver and Bronze

"""

text2 = """
### Provided Floating Filters
All the default filters provided by the grid provide their own implementation of a floating filter. All you need to do to enable these floating filters is set the floatingFilter = true column property. The features of the provided floating filters are as follows:

 | Filter  | 	Editable  | 	Description | 
  | ----- | -------- | ----------- | 
 | Text | 	Sometimes | 	Provides a text input field to display the filter value, or a read-only label if read-only. | 
 | Number | 	Sometimes | 	Provides a text input field to display the filter value, or a read-only label if read-only. | 
 | Date	 | Sometimes | 	Provides a date input field to display the filter value, or a read-only label if read-only. | 
 | Set	 | No | 	Provides a read-only label by concatenating all selected values. | 


The floating filters for Text, Number and Date (the simple filters) are editable when the filter has one condition and one value. If the floating filter has a) two conditions or b) zero (custom option) or two ('In Range') values, the floating filter is read-only.

The screen shots below show example scenarios where the provided Number floating filter is editable and read-only.

![image](https://user-images.githubusercontent.com/72614349/216128136-440a471a-0383-4262-bdbe-7c95e50faf5a.png)
"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.filtering.floating_filters", make_layout=make_tabs),
        make_md(text2),
    ],
)
