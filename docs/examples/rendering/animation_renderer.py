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
        "dangerously_allow_html": True,
    },
    {
        "headerName": "Total",
        "valueGetter": "Number(data.a) + Number(data.b) + Number(data.c)",
        "cellRenderer": "agAnimateShowChangeCellRenderer",
        "dangerously_allow_html": True,
    },
    {
        "headerName": "Average",
        "valueGetter": "Math.round((Number(data.a) + Number(data.b) + Number(data.c)) * 10 / 3) /10",
        "cellRenderer": "agAnimateShowChangeCellRenderer",
        "dangerously_allow_html": True,
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
        dcc.Markdown(
            "This grid demonstrates the renderer for animating changes.  Try entering new values into the editable columns and press the button to update column c in a callback"
        ),
        html.Button("Update column C", id="live-data-grid-btn"),
        dag.AgGrid(
            id="live-data-grid",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef=defaultColDef,
            # setting a row ID is required when updating data in a callback
            setRowId="index",
            dangerously_allow_html=True,
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("live-data-grid", "rowData"),
    Input("live-data-grid-btn", "n_clicks"),
    State("live-data-grid", "rowData"),
)
def update_col_c(_, rows):
    for r in rows:
        r["c"] = random.randint(1, 1000)
    return rows


if __name__ == "__main__":
    app.run_server(debug=True)
