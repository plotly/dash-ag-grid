"""
How to enable ag grid sparklines feature.
"""


import json
import pathlib

import dash
import dash_ag_grid as dag
from dash import dcc, html

app = dash.Dash(__name__)

# set relative path
PATH = pathlib.Path(__file__).parents[2]
DATA_PATH = PATH.joinpath("data").resolve()

with open(DATA_PATH.joinpath("data.json")) as json_file:
    data = json.load(json_file)


columnDefs = [
    {"field": "symbol", "maxWidth": 120},
    {"field": "name", "minWidth": 250},
    {
        "field": "volume",
        "type": "numericColumn",
        "maxWidth": 140,
    },
    {
        "field": "change",
        "cellRenderer": "agSparklineCellRenderer",
    },
]
columnDefs_new = [
    {"field": "symbol", "maxWidth": 120},
    {"field": "name", "minWidth": 250},
    {
        "field": "volume",
        "type": "numericColumn",
        "maxWidth": 140,
    },
    {
        "field": "change",
        "cellRenderer": "agSparklineCellRenderer",
        "cellRendererParams": {
            "sparklineOptions": {
                "type": "area",
                "marker": {
                    "size": 2,
                    "shape": "circle",
                    "fill": "blue",
                    "stroke": "blue",
                    "strokeWidth": 2,
                },
                "fill": "rgba(216, 204, 235, 0.3)",
                "line": {
                    "stroke": "rgb(119,77,185)",
                },
                "highlightStyle": {
                    "fill": "rgb(143,185,77)",
                },
                "axis": {
                    "stroke": "rgb(204, 204, 235)",
                },
                "crosshairs": {
                    "xLine": {
                        "enabled": "true",
                        "lineDash": "dash",
                        "stroke": "rgba(0, 0, 0, 0.5)",
                    },
                    "yLine": {
                        "enabled": "true",
                        "lineDash": "dash",
                        "stroke": "rgba(0, 0, 0, 0.5)",
                    },
                },
            },
        },
    },
]

app.layout = html.Div(
    [
        dcc.Markdown(
            "Demonstration of how to enable sparklines feature in a Dash AG Grid."
        ),
        dcc.Markdown(
            """
        To enable sparklines on a particular column, the data format of this column can be array of numbers, tuples, or dictionaries. The `agSparklineCellRenderer` needs to be added to ths column. 
        By default the data is displayed using `line` sparkline as shown below:
        """
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=data,
            enableEnterpriseModules=True,
            licenseKey="LICENSE_KEY_HERE",
            columnSize="sizeToFit",
        ),
        dcc.Markdown(
            """
        Sparklines can be customized by supplying `sparklineOptions` to the `cellRendererParams` on the `agSparklineCellRenderer` in this following example.
        """
        ),
        dcc.Markdown(
            """
        The complete AG Grid Sparklines documentation can be found [here](https://www.ag-grid.com/react-data-grid/sparklines-overview/).
        """
        ),
        dag.AgGrid(
            className="ag-theme-alpine-dark",
            columnDefs=columnDefs_new,
            rowData=data,
            enableEnterpriseModules=True,
            licenseKey="LICENSE_KEY_HERE",
            columnSize="sizeToFit",
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
