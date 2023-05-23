"""
Custom Row Drag Text
"""

import dash_ag_grid as dag
from dash import Dash, dcc, html
import pandas as pd

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    {'field': 'athlete', 'rowDrag': True},
    {'field': 'country'},
    {'field': 'year', 'width': 100},
    {'field': 'date'},
    {'field': 'sport'},
    {'field': 'gold'},
    {'field': 'silver'},
    {'field': 'bronze'},
]

defaultColDef = {'width': 170, "sortable": True, "filter": True}

app.layout = html.Div(
    [
        dcc.Markdown("This grid shows a custom text of the dragged row"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            dashGridOptions={
                "rowDragManaged": True,
                "animateRows": True,
                "rowDragText": {"function": "rowDragText(params)"}
            }
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)


"""
----------------

Add the following to the dashAgGridFunctions.js file in the assets folder

----------------

var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

const hostCities = {2000: "Sydney", 2004: "Athens", 2008: "Beijing", 2012: "London",}

dagfuncs.rowDragText = function (params) {
    const {year} = params.rowNode.data;
    if (year in hostCities) {
        return `${params.defaultTextValue} (${hostCities[year]} Olympics)`
    }
    return params.defaultTextValue;
}
"""
