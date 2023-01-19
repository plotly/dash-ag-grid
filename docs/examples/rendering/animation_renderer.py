import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd
import numpy as np

app = Dash(__name__)

df = pd.DataFrame(np.random.randint(0, 1000, size=(15, 3)), columns=list("abc"))

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
        "valueGetter": "Number(data.a) + Number(data.b) + Number(data.c)",
        "cellRenderer": "agAnimateShowChangeCellRenderer",
    },
    {
        "headerName": "Average",
        "valueGetter": "Math.round((Number(data.a) + Number(data.b) + Number(data.c)) * 10 / 3) /10",
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
        dcc.Markdown(
            "This grid updates totals and average columns and animates the changed values"
        ),
        dag.AgGrid(
            id="live-data-grid",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef=defaultColDef,
        ),
    ],
    style={"margin": 20},
)


if __name__ == "__main__":
    app.run_server(debug=True)
