import random
import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import pandas as pd
import numpy as np

app = Dash(__name__)

df = pd.DataFrame(np.random.randint(0, 1000, size=(15, 3)), columns=list("abc"))
df.reset_index(inplace=True)

columnDefs = [
    {
        "headerName": "Editable A",
        "field": "a",
        "editable": True,
        "resizable": True,
    },
    {
        "headerName": "Editable B",
        "field": "b",
        "editable": True,
    },
    {
        "headerName": "API C",
        "field": "c",
        "cellRenderer": "agAnimateShowChangeCellRenderer",
    },
    {
        "headerName": "Total",
        "valueGetter": {
            "function": "Number(params.data.a) + Number(params.data.b) + Number(params.data.c)"
        },
        "cellRenderer": "agAnimateShowChangeCellRenderer",
    },
    {
        "headerName": "Average",
        "valueGetter": {
            "function": "Math.round((Number(params.data.a) + Number(params.data.b) + Number(params.data.c)) * 10 / 3) /10"
        },
        "cellRenderer": "agAnimateShowChangeCellRenderer",
    },
]

defaultColDef = {
    "type": ["numberColumn", "rightAligned"],
    "filter": "agNumberColumnFilter",
    "resizable": True,
    "sortable": True,
}

app.layout = html.Div(
    [
        dcc.Markdown("Example of Asyn updates"),
      #  html.Button("Update column C", id="transactions-async-btn"),
        dcc.Interval("transactions-async-interval", interval=1, max_intervals=100),
        dag.AgGrid(
            id="transactions-async-grid",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef=defaultColDef,
            # setting a row ID is required when updating data in a callback
            getRowId="params.data.index",
            style={"height": 800},
        ),
    ],
    style={"margin": 20},
)


app.clientside_callback(
    """
        function (n, d) {
        if (n) {
            row = d[n%d.length]
            row['c'] = Math.floor(Math.random() * 100)
            return {'async': true, 'update': [row]}
        }
        return window.dash_clientside.no_update
    }
    """,
    Output("transactions-async-grid", "rowTransaction"),
    Input("transactions-async-interval", "n_intervals"),
    State("transactions-async-grid", "rowData"),
    prevent_initial_call=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)

