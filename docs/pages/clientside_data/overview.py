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

# Client-Side Data
Client-Side Data means all of the data you want to show is loaded inside the data grid in one go. The data is provided to the grid using the `rowData` attribute in a list.

There are four Row Models in the grid, of which the Client-Side Row Model is one. The Client-Side Row Model is the one that uses the `rowData` attribute.

The remaining three Row Models are [Server-Side Row Models](https://www.ag-grid.com/react-data-grid/row-models/) that can be used where data is mostly kept on the server and loaded into the grid in parts.

This section of the documentation describes how to work with data when using the Client-Side Row Model.


### Row Models
The grid can be configured with different strategies for loading row data into the grid, which are encapsulated into different Row Models. Changing which Row Model the grid is using means changing the strategy the grid is using for loading rows.

The grid comes with four row models:

1. Client-Side
2. Server-Side
3. Infinite
4. Viewport

The Client-Side Row Model deals with client-side data. The Server-Side, Infinite and Viewport Row Models deal with server-side data. The following is a summary of each:

- Client-Side
This is the default. The grid will load all of the data into the grid in one go. The grid can then perform filtering, sorting, grouping, pivoting and aggregation all in memory.

- Infinite
This will present the data to the user and load more data as the user scrolls down. Use this if you want to display a large, flat (not grouped) list of data.


- Server-Side
The Server-Side Row Model builds on the Infinite Row Model. In addition to lazy-loading the data as the user scrolls down, it also allows lazy-loading of grouped data with server-side grouping and aggregation. Advanced users will use Server-Side Row Model to do ad-hoc slice and dice of data with server-side aggregations.


- Viewport
The grid will inform the server exactly what data it is displaying (first and last row) and the server will provide data for exactly those rows only. Use this if you want the server to know exactly what the user is viewing, useful for updates in very large live datastreams where the server only sends updates to clients viewing the impacted rows.


Which row model you use is set by the grid property rowModelType.

### When to Use
Which row model you use will depend on your application. Here are some quick rules of thumb:

- If using AG Grid Community, use Client-Side Row Model if you want to load all your data into the browser, or Infinite Row Model if you want to load it in blocks.
- If using AG Grid Enterprise, use Client-Side Row Model if you want to load all your data into the browser, or Server-Side Row Model if you want to load it in blocks. Server-Side Row Model is Infinite Row Model plus more. So if you are an AG Grid Enterprise customer, you should prefer Server-Side Row Model over Infinite Row Model.
- Don't use Viewport Row Model unless you understand what its advantages are and when you need them. We find many of our users use Viewport Row Model when they don't need to and end up with more complicated applications as a result.

Here are more detailed rules of thumb.

- If you are not sure, use default Client-Side. The grid can handle massive amounts of data (100k+ rows). The grid will only render what's visible on the screen (40 rows approximately, depending on your screen size) even if you have thousands of rows returned from your server. You will not kill the grid with too much data - rather your browser will run out of memory before the grid gets into problems. So if you are unsure, go with Client-Side Row Model first and only change if you need to. With Client-Side, you get sorting, filtering, grouping, pivoting and aggregation all done for you by the grid. All of the examples in the documentation use the Client-Side model unless specified otherwise.

- If you do not want to shift all the data from your server to your client, as the amount of data is too large to shift over the network or to extract from the underlying datasource, then use either Infinite, Server-Side or Viewport. Each one takes data from the server in different ways.

- Use Infinite or Server-Side to bring back a list of data one block at a time from the server. As the user scrolls, the grid will ask for more rows. Server-Side has more features than Infinite and will allow row grouping, aggregation, lazy-loading of groups and slice and dice of data.
- Use Viewport if you want the server to know exactly what the user is looking at. This is best when you have a large amount of changing data and want to push updates to the client when the server-side data changes. Knowing exactly what the user is looking at means you only have to push updates to the relevant users. All the row models can receive updates but only the Viewport row model provides the server with the information of the rows the users currently sees on screen without scrolling.

See the [AG Grid Docs- Row Models](https://www.ag-grid.com/react-data-grid/row-models/) for more details.


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
    ],
)
