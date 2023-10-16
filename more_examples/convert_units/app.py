"""
This app is an example of a custom number filter
https://www.ag-grid.com/react-data-grid/filter-number/#custom-number-support

"""




import dash_ag_grid as dag
from dash import Dash, html
import pandas as pd
import numpy as np

app = Dash(__name__)

df = pd.DataFrame(np.random.randint(10000000, size=(5000, 1)), columns=list("b"))

grid = dag.AgGrid(
    rowData=df.to_dict("records"),
    columnDefs=[
        {"field": "b", "headerName": "Bytes"},
        {
            "field": "b",
            "headerName": "Bytes-base_10",
            "valueFormatter": {"function": "d3.format('(.2s')(params.value)"},
        },
        {
            "field": "b",
            "headerName": "Bytes-base_2",
            "valueFormatter": {"function": "convertUnits(params.value)"},
        },
    ],
    defaultColDef={
        "sortable": True,
        "filter": "agNumberColumnFilter",
        "filterParams": {"function": "bytes()"},
        "floatingFilter": True,
    },
)

app.layout = html.Div(
    [
        html.Div(
            "Note - You may also enter 'B', 'KB', 'MB', 'GB', 'TB', 'PB' in the filter menu "
        ),
        grid,
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
