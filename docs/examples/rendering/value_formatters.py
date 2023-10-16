import dash_ag_grid as dag
from dash import Dash, html, dcc


app = Dash(__name__)


columnDefs = [
    {"headerName": "Description", "field": "description", "minWidth": 300},
    {
        "headerName": "d3.format",
        "field": "format",
        "minWidth": 300,
        "cellRenderer": "markdown",
    },
    {"headerName": "Specifier", "field": "specifier", "minWidth": 10},
    {"headerName": "Value", "field": "value", "minWidth": 125},
    {
        "headerName": "Formatted Value",
        "field": "formatted",
        "valueFormatter": {"function": "d3.format(params.data.specifier)(params.value)"},
        "minWidth": 150,
    },
]

rowData = [
    {
        "description": "fixed decimal",
        "format": "`d3.format('.1f')(0.1234)`",
        "specifier": ".1f",
        "value": 0.1234,
        "formatted": 0.1234,
        "notes": "",
    },
    {
        "description": "fixed decimal",
        "format": "`d3.format('.2f')(0.1234)`",
        "specifier": ".2f",
        "value": 0.1234,
        "formatted": 0.1234,
        "notes": "",
    },
    {
        "description": "rounded percentage",
        "format": "`d3.format('.0%')(0.1234)`",
        "specifier": ".0%",
        "value": 0.1234,
        "formatted": 0.1234,
        "notes": "",
    },
    {
        "description": "rounded percentage",
        "format": "`d3.format('.1%')(0.1234)`",
        "specifier": ".1%",
        "value": 0.1234,
        "formatted": 0.1234,
        "notes": "",
    },
    {
        "description": "localized fixed-point currency",
        "format": "`d3.format('$,.2f')(1000.1234)`",
        "specifier": "$,.2f",
        "value": 1000.1234,
        "formatted": 1000.1234,
        "notes": "",
    },
    {
        "description": "localized fixed-point currency",
        "format": "`d3.format('$,.2f')(-1000.1234)`",
        "specifier": "$,.2f",
        "value": -1000.1234,
        "formatted": -1000.1234,
        "notes": "",
    },
    {
        "description": "localized fixed-point currency",
        "format": "`d3.format('($,.2f')(-1000.1234)`",
        "specifier": "($,.2f",
        "value": -1000.1234,
        "formatted": -1000.1234,
        "notes": "",
    },
    {
        "description": "signed",
        "format": "`d3.format('+')(12)`",
        "specifier": "+",
        "value": 12,
        "formatted": 12,
        "notes": "",
    },
    {
        "description": "dot filled and centered",
        "format": "`d3.format('.^20')(12)`",
        "specifier": ".^20",
        "value": 12,
        "formatted": 12,
        "notes": "",
    },
    {
        "description": "SI-prefix with two significant digits",
        "format": "`d3.format('.2s')(421e6)`",
        "specifier": ".2s",
        "value": 42e6,
        "formatted": 42e6,
        "notes": "",
    },
    {
        "description": "grouped thousands with two significant digits",
        "format": "`d3.format(',.2r')(4223)`",
        "specifier": ",.2r",
        "value": 4223,
        "formatted": 4223,
        "notes": "",
    },
]

app.layout = html.Div(
    [
        dcc.Markdown("Number formatting example"),
        dag.AgGrid(
            style={"height": "500px", "width": "100%"},
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)
