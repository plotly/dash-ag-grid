import dash_ag_grid as dag
from dash import Dash, html, dcc

app = Dash(__name__)

data = [
    {
        'localTime': '5:00am',
        'show': {'name': 'Wake Up Dublin', 'presenter': 'Andrew Connell'},
        'a': 0.231, 'b': 0.523, 'c': 0.423, 'd': 0.527, 'e': 0.342,
    },
    {'localTime': '5:15am', 'a': 0.423, 'b': 0.452, 'c': 0.523, 'd': 0.543, 'e': 0.452},
    {'localTime': '5:30am', 'a': 0.537, 'b': 0.246, 'c': 0.426, 'd': 0.421, 'e': 0.523},
    {'localTime': '5:45am', 'a': 0.893, 'b': 0.083, 'c': 0.532, 'd': 0.983, 'e': 0.543},
    {
        'localTime': '6:00am',
        'show': {'name': 'Pure Back In The Day', 'presenter': 'Kevin Flanagan'},
        'a': 0.231, 'b': 0.523, 'c': 0.423, 'd': 0.527, 'e': 0.342,
    },
    {'localTime': '6:15am', 'a': 0.423, 'b': 0.452, 'c': 0.523, 'd': 0.543, 'e': 0.452},
    {'localTime': '6:30am', 'a': 0.537, 'b': 0.246, 'c': 0.426, 'd': 0.421, 'e': 0.523},
    {'localTime': '6:45am', 'a': 0.893, 'b': 0.083, 'c': 0.532, 'd': 0.983, 'e': 0.543},
    {
        'localTime': '7:00am',
        'show': {'name': 'The Queens Breakfast', 'presenter': 'Tony Smith'},
        'a': 0.231, 'b': 0.523, 'c': 0.423, 'd': 0.527, 'e': 0.342,
    },
    {'localTime': '7:15am', 'a': 0.423, 'b': 0.452, 'c': 0.523, 'd': 0.543, 'e': 0.452},
    {'localTime': '7:30am', 'a': 0.537, 'b': 0.246, 'c': 0.426, 'd': 0.421, 'e': 0.523},
    {'localTime': '7:45am', 'a': 0.893, 'b': 0.083, 'c': 0.532, 'd': 0.983, 'e': 0.543},
    {
        'localTime': '8:00am',
        'show': {'name': 'Cosmetic Surgery', 'presenter': 'Niall Crosby'},
        'a': 0.231, 'b': 0.523, 'c': 0.423, 'd': 0.527, 'e': 0.342,
    },
    {'localTime': '8:15am', 'a': 0.423, 'b': 0.452, 'c': 0.523, 'd': 0.543, 'e': 0.452},
    {'localTime': '8:30am', 'a': 0.537, 'b': 0.246, 'c': 0.426, 'd': 0.421, 'e': 0.523},
    {'localTime': '8:45am', 'a': 0.893, 'b': 0.083, 'c': 0.532, 'd': 0.983, 'e': 0.543},
    {
        'localTime': '8:00am',
        'show': {'name': 'Brickfield Park Sessions', 'presenter': 'Bricker McGee'},
        'a': 0.231, 'b': 0.523, 'c': 0.423, 'd': 0.527, 'e': 0.342,
    },
    {'localTime': '8:15am', 'a': 0.423, 'b': 0.452, 'c': 0.523, 'd': 0.543, 'e': 0.452},
    {'localTime': '8:30am', 'a': 0.537, 'b': 0.246, 'c': 0.426, 'd': 0.421, 'e': 0.523},
    {'localTime': '8:45am', 'a': 0.893, 'b': 0.083, 'c': 0.532, 'd': 0.983, 'e': 0.543},
]

columnDefs = [
    {'field': 'localTime'},
    {
        'field': 'show',
        'cellRenderer': "ShowCellRenderer",
        'rowSpan': {"function": "rowSpanComplex(params)"},
        'cellClassRules': {"show-cell": "params.value", },
        'width': 200,
    },
    {'field': 'a'},
    {'field': 'b'},
    {'field': 'c'},
    {'field': 'd'},
    {'field': 'e'},
]
defaultColDef = {
    "width": 170,
    "resizable": True,
}

app.layout = html.Div(
    [
        dcc.Markdown("Example: Row Spanning Complex"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=data,
            defaultColDef=defaultColDef,
            dashGridOptions={"suppressRowTransform": True},
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)

"""

--------------------

Add the following to the .css file in the assets folder:

--------------------

.show-cell {
  background: white;
  border-left: 1px solid lightgrey !important;
  border-right: 1px solid lightgrey !important;
  border-bottom: 1px solid lightgrey !important;
}

.show-name {
  font-weight: bold;
}

.show-presenter {
  font-style: italic;
}

----------------

Add the following to the dashAgGridFunctions.js file in the assets folder

----------------

var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.rowSpanComplex = function (params) {
    if (params.data.show) {
        return 4;
    } else {
        return 1;
    }
}

----------------

Add the following to the dashAgGridComponentFunctions.js file in the assets folder

----------------

var dagcomponentfuncs = (window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {});

dagcomponentfuncs.ShowCellRenderer = function (props) {
    let children;
    if (props.value) {
        children = [
            React.createElement('div', {className: 'show-name'}, props.value.name),
            React.createElement('div', {className: 'show-presenter'}, props.value.presenter),
        ]
    }
    return React.createElement('div', null, children)
}
"""
