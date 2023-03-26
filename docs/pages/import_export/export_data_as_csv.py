from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md, ComponentReference
from utils.utils import app_description


register_page(
    __name__,
    order=1,
    description=app_description,
    title="Dash AG Grid Import Export",
    # name="Bootstrap Utility Classes",
    # hashtags=["intro","background", "border", "color", "spacing", "text", "position"],
)

text1 = """

#  CSV Export
The grid data can be exported to CSV with an API call, or using the right-click context menu (Enterprise only) on the Grid.

### What Gets Exported
The same data that is in the grid gets exported, but none of the GUI representation of the data will be. What this means is:

- The raw values, and not the result of cell renderer will get used, meaning:

  - Value Getters will be used.
  - Cell Renderers will NOT be used.
  - Cell Formatters will NOT be used (use `processCellCallback` instead).
- Cell styles are not exported.

- If row grouping (Enterprise only):

  - All data will be exported regardless of whether groups are open in the UI.
  - By default, group names will be in the format "-> Parent Name -> Child Name" (use `processRowGroupCallback` to change this).
  - Row group footers (`groupIncludeFooter=True`) will NOT be exported - this is a GUI addition only.

> The CSV export will be enabled by default. If you want to disable it, you can set the property `suppressCsvExport = True` in your gridOptions.

### Security Concerns
When opening CSV files, spreadsheet applications like Excel, Apple Numbers, Google Sheets and others will automatically execute cell values that start with the following symbols as formulas: +, -, =, @, Tab (0x09) and Carriage Return (0x0D). In order to prevent any malicious content from being exported we recommend using the callback methods shown in the CSV Export Params to modify the exported cell values so that they do NOT start with any of the characters listed above. This way the applications will not execute the cell value directly if it starts with the characters listed above. If you'd like to keep the cell values unchanged when exporting, please allow exporting to Excel only.

Detailed info regarding CSV Injection can be found in the [OWASP CSV Injection](https://owasp.org/www-community/attacks/CSV_Injection) website.

### Example 1 CSV Standard Export

The example below shows the default behaviour when exporting the grid's data to CSV.

"""


text2 = """
### Example 2 CSV Export with options

See the reference section below and the [AG Grid docs](https://www.ag-grid.com/react-data-grid/csv-export/) for more
 details and examples of the options you can set for the CSV export.  

This example demos how to exclude the headings on export and include hidden columns on export.

"""


text3 = """

### Reference

`csvExportParams` (dict; optional): Object with properties to pass to the exportDataAsCsv() method. `csvExportParams` is a dict with keys:

- `allColumns` (boolean; optional): If True, all columns will be exported in the order they appear in the columnDefs.

- `appendContent` (string; optional): Content to put at the bottom of the file export.

- `columnKeys` (list of strings; optional): Provide a list (an array) of column keys or Column objects if you want to export specific columns.

- `columnSeparator` (string; optional): Delimiter to insert between cell values.

- `fileName` (string; optional): String to use as the file name.

- `onlySelected` (boolean; optional): Export only selected rows.

- `onlySelectedAllPages` (boolean; optional): Only export selected rows including other pages (only makes sense when using pagination).

- `prependContent` (string; optional): Content to put at the top of the file export. A 2D array of CsvCell objects.

- `skipColumnGroupHeaders` (boolean; optional): Set to True to skip include header column groups.

- `skipColumnHeaders` (boolean; optional): Set to True if you don't want to export column headers.

- `skipPinnedBottom` (boolean; optional): Set to True to suppress exporting rows pinned to the bottom of the grid.

- `skipPinnedTop` (boolean; optional): Set to True to suppress exporting rows pinned to the top of the grid.

- `skipRowGroups` (boolean; optional): Set to True to skip row group headers if grouping rows. Only relevant when grouping rows.

- `suppressQuotes` (boolean; optional): Pass True to insert the value into the CSV file without escaping. In this case it is your responsibility to ensure that no cells contain the columnSeparator character.

"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.import_export.export_data_as_csv", make_layout=make_tabs),
        make_md(text2),
        example_app("examples.import_export.export_data_as_csv_options", make_layout=make_tabs),
        make_md(text3),
        #  up_next("text"),
    ],
)
