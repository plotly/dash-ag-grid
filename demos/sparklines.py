"""
How to enable ag grid sparklines feature.
"""

import json

import dash
import dash_ag_grid as dag
from dash import dcc, html
from demo_utils import enterprise_blurb

app = dash.Dash(__name__)

with open(("demos/data.json")) as json_file:
    data = json.load(json_file)

columnDefs = [
    {"field": "symbol", "maxWidth": 120},
    {"field": "name", "minWidth": 250},
    {
        "field": "change",
        "cellRenderer": "agSparklineCellRenderer",
    },
    {
        "field": "volume",
        "type": "numericColumn",
        "maxWidth": 140,
    },
]
columnDefs_new = [
    {"field": "symbol", "maxWidth": 120},
    {"field": "name", "minWidth": 250},
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
    {
        "field": "volume",
        "type": "numericColumn",
        "maxWidth": 140,
    },
]

app.layout = html.Div(
    [
        enterprise_blurb(),
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
            columnDefs=columnDefs_new,
            rowData=data,
            enableEnterpriseModules=True,
            licenseKey="LICENSE_KEY_HERE",
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
