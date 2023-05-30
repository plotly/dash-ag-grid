from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description

from pages.serverside_data.row_models import  text1 as row_models
register_page(
    __name__,
    order=1,
    description=app_description,
    title="Dash AG Grid Clientside Data",
)

text1 = """

# Client-Side Data
Client-Side Data means all of the data you want to show is loaded inside the data grid in one go. The data is provided to the grid using the `rowData` attribute in a list.

There are four Row Models in the grid, of which the Client-Side Row Model is one. The Client-Side Row Model is the one that uses the `rowData` attribute.

The remaining three Row Models are [Server-Side Row Models](https://www.ag-grid.com/react-data-grid/row-models/) that can be used where data is mostly kept on the server and loaded into the grid in parts.

This section of the documentation describes how to work with data when using the Client-Side Row Model.
"""


text3 = """
### Updating Data
There are many ways in which data can change in your application, and as a result many ways in which you can inform the grid of data changes. This section explains the different ways of how you can update data inside the grid using the grid's API.


#### Updates vs Edits vs Refresh
This page talks about updating data via the grid's API. It does not talk about the following:

1. Editing data inside the grid using the grid's UI, e.g. by the user double-clicking on a cell and editing the cell's value. When this happens the grid is in control and there is no need to explicitly tell the grid data has changed. See Cell Editing on how to edit via the grid's UI.
2. The grid's data is updated from elsewhere in your application. This can happen if you pass data to the grid and then subsequently change that data outside of the grid. This leaves the grid's view out of sync with the data that it has. In this instance what you want to do is View Refresh to have the grid's UI redraw to display the data changes.

#### Updating Data
Updating data in the grid can be done in the following ways:

- Row Data
The easiest way to update data inside the grid is to replace the data you gave it with a fresh set of data. This is done by either updating the rowData bound property (if using a framework) or calling api.setRowData(newData).


- Transaction
The grid takes a transaction containing rows to add, remove and update. This is done using api.applyTransaction(transaction).

Use transactions for doing add, remove or update operations on a large number of rows that are infrequent.

If you are frequently updating rows (e.g. 5 or more updates a second), consider moving to High Frequency instead (achieved with Async Transactions).


- High Frequency
High Frequency (achieved with Async Transactions) is a mechanism of applying many transactions over a small space of time and have the grid apply all the transactions in batches. The high frequency / batch method is for when you need the fastest possible way to process many continuous updates, such as providing a stream of updates to the grid. This is done setting `async` to True in the rowTransaction({"async" :True}).

Use Async Transactions for doing add, remove or update operations that are frequent, e.g. for managing streaming updates into the grid of tens, hundreds or thousands of updates a second.

"""

layout = html.Div(
    [
        make_md(text1),
        make_md(row_models),
        make_md(text3)
    ],
)
