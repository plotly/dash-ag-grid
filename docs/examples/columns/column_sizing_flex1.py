from dash import Dash, dcc, html
import dash_ag_grid as dag
import pandas as pd


app = Dash(__name__)

flex_widths = {
    "a": 750,
    "b": 750,
    "c": 750,
    "d": 750,
    "e": 1000,
    "f": 1000,
    "g": 1000,
    "h": 750,
    "i": 2500,
    "j": 1000,
    "k": 750,
    "l": 750,
}
df = pd.DataFrame({i: [x for x in range(12)] for i in flex_widths})

grid = dag.AgGrid(
    rowData=df.to_dict("records"),
    columnDefs=[{"headerName": i, "field": i, "flex": flex_widths[i]} for i in df.columns],
    columnSize="sizeToFit",
    defaultColDef={
        "resizable": True,
        "editable": True,
        "sortable": True,
        "floatingFilter": True,
    },
)

app.layout = html.Div(
    [
        dcc.Markdown("Example with Flex in all columns"),
        grid,
    ]
)


if __name__ == "__main__":
    app.run(debug=True)
