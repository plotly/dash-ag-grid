from dash import Dash, dcc, html
import dash_ag_grid as dag

app = Dash(__name__)


columnDefs = [
    {
        "headerName": "A",
        "field": "a",
        "width": 300,
    },
    {
        "headerName": "Flexed Columns",
        "children": [
            {
                "headerName": "B",
                "field": "b",
                "minWidth": 200,
                "maxWidth": 350,
                "flex": 2,
                "wrapText": True,
                "autoHeight": True,
            },
            {
                "headerName": "C",
                "field": "c",
                "flex": 1,
            },
        ],
    },
]
defaultColDef = {
    "resizable": True,
}

rowData = [
    {"a": "width 300px", "b": "flex 2 minWidth 200px maxWidth 350px", "c": "flex 1"}
]


app.layout = html.Div(
    [
        dcc.Markdown("Demonstration of column flex"),
        dag.AgGrid(
            id="column-sizing-flex",
            columnDefs=columnDefs,
            rowData=rowData,
            defaultColDef=defaultColDef,
        ),
    ],
)


if __name__ == "__main__":
    app.run(debug=True)
