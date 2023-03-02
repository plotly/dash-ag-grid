import dash_ag_grid as dag
from dash import Dash, html, dcc


rowData = [{"a": i % 4, "b": i % 7} for i in range(100)]

columnDefs = [
    {
        "headerName": "#",
        "maxWidth": 100,
        "valueGetter": {"function": "params.node ? params.node.rowIndex : null;"},
    },
    {"field": "a"},
    {"field": "b"},
    {
        "headerName": "A + B",
        "colId": "a&b",
        "valueGetter": {"function": "params.data.a + params.data.b;"},
    },
    {
        "headerName": "A * 1000",
        "minWidth": 95,
        "valueGetter": {"function": "params.data.a * 1000"},
    },
    {
        "headerName": "B * 137",
        "minWidth": 90,
        "valueGetter": {"function": "params.data.b * 137;"},
    },
    {
        "headerName": "Random",
        "minWidth": 90,
        "valueGetter": {"function": "Math.floor(Math.random() * 1000);"},
    },
    {
        "headerName": "Chain",
        "valueGetter": {"function": "params.getValue('a&b') * 1000;"},
    },
    {"headerName": "Const", "minWidth": 85, "valueGetter": {"function": "9999"}},
]

defaultColDef = {
    "flex": 1,
    "minWidth": 75,
}

app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.Markdown("Value Getters Example"),
        dag.AgGrid(columnDefs=columnDefs, rowData=rowData, defaultColDef=defaultColDef),
    ],
    style={"margin": 20},
)


if __name__ == "__main__":
    app.run_server(debug=True)
