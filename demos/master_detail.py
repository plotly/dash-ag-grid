"""
Nested tables.
"""

import dash_ag_grid as dag
import dash
from dash import Input, Output, html, dcc
import dash_design_kit as ddk
from demo_utils import enterprise_blurb

import time

app = dash.Dash(__name__)
masterColumnDefs = [
    {
        "headerName": "Country",
        "field": "country",
        "cellRenderer": "agGroupCellRenderer",
    },
    {"headerName": "Region", "field": "region"},
    {"headerName": "Population", "field": "population"},
]

detailColumnDefs = [
    {"headerName": "City", "field": "city"},
    {"headerName": "Pop. (City proper)", "field": "population_city"},
    {"headerName": "Pop. (Metro area)", "field": "population_metro"},
]

rowData = [
    {
        "country": "China",
        "region": "Asia",
        "population": 1411778724,
        "cities": [
            {"city": "Shanghai", "population_city": 24870895, "population_metro": "NA"},
            {"city": "Beijing", "population_city": 21893095, "population_metro": "NA"},
            {
                "city": "Chongqing",
                "population_city": 32054159,
                "population_metro": "NA",
            },
        ],
    },
    {
        "country": "India",
        "region": "Asia",
        "population": 1383524897,
        "cities": [
            {
                "city": "Delhi",
                "population_city": 16753235,
                "population_metro": 29000000,
            },
            {
                "city": "Mumbai",
                "population_city": 12478447,
                "population_metro": 24400000,
            },
            {
                "city": "Kolkata",
                "population_city": 4496694,
                "population_metro": 14035959,
            },
        ],
    },
    {
        "country": "United States",
        "region": "Americas",
        "population": 332593407,
        "cities": [
            {
                "city": "New York",
                "population_city": 8398748,
                "population_metro": 19303808,
            },
            {
                "city": "Los Angeles",
                "population_city": 3990456,
                "population_metro": 13291486,
            },
            {
                "city": "Chicago",
                "population_city": 2746388,
                "population_metro": 9618502,
            },
        ],
    },
    {
        "country": "Indonesia",
        "region": "Asia",
        "population": 271350000,
        "cities": [
            {
                "city": "Jakarta",
                "population_city": 10154134,
                "population_metro": 33430285,
            },
        ],
    },
]


app.layout = html.Div(
    [
        enterprise_blurb(),
        ddk.Card(
            dcc.Markdown(
                """
Use the Master/Detail feature to display nested grids within each row of a top-level Master Grid.
To use the Master/Detail feature, your rowData object must have a nested structure like the data in this example.
To use Master/Detail view:
  - Enable enterprise mode by setting `enableEnterpriseModules=True`. Master/Detail view is an enterprise feature.
  - Set `masterDetail=True`.
  - Pass `detailCellRendererParams` to set the display options for the detail grid. It must include at least the following keys:
    - `detailGridOptions` containing `columnDefs` for the detail grid
    - `detailColname` containing the column name in the data where the detail grid data is stored
  - Optional: Set height of detail grid
    - For fixed height, set `detailRowHeight` to a number of pixels
    - For auto height to fit all data, set `detailRowAutoHeight=True`
"""
            ),
        ),
        ddk.Card(
            dag.AgGrid(
                id="master-detail-table",
                columnDefs=masterColumnDefs,
                rowData=rowData,
                columnSize="sizeToFit",
                enableEnterpriseModules=True,
                masterDetail=True,
                detailCellRendererParams={
                    "detailGridOptions": {
                        "columnDefs": detailColumnDefs,
                    },
                    "detailColName": "cities",
                    "suppressCallback": True,
                },
                detailRowAutoHeight=True,
            ),
        ),
        html.Hr(),
        ddk.Card(
            dcc.Markdown(
                "In this example, new row data is served using a request/response model, similar to infinite scroll."
            ),
        ),
        ddk.Card(
            dag.AgGrid(
                id="master-detail-table-request",
                columnDefs=masterColumnDefs,
                rowData=rowData,
                columnSize="sizeToFit",
                enableEnterpriseModules=True,
                masterDetail=True,
                detailCellRendererParams={
                    "detailGridOptions": {
                        "columnDefs": detailColumnDefs,
                    },
                    "suppressCallback": False,
                },
                detailRowAutoHeight=True,
            ),
        ),
    ]
)


@app.callback(
    Output("master-detail-table-request", "getDetailResponse"),
    Input("master-detail-table-request", "getDetailRequest"),
    prevent_initial_call=True,
)
def handle_request(request):
    time.sleep(1)
    return request["data"]["cities"]


if __name__ == "__main__":
    app.run_server(debug=True)
