"""
No click editing example
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

cellStyle = {
    "styleConditions": [
        {
            "condition": "params.data.year == 2012",
            "style": {"backgroundColor": "lightBlue"},
        },
    ]
}

columnDefs = [
    {"field": "sport"},
    {
        "field": "athlete",
        "editable": True,
        "cellRenderer": "EditButton",
    },
    {"field": "age"},
    {"field": "country"},
    {"field": "year", "maxWidth": 120},
    {"field": "date"},
    {"field": "gold"},
    {"field": "silver"},
    {"field": "bronze"},
    {"field": "total"},
]

defaultColDef = {
    "flex": 1,
    "minWidth": 150,
}


app.layout = html.Div(
    [
        dcc.Markdown(
            "Example: No click Editing - Editing starts when clicking the button "
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            dashGridOptions={"suppressClickEdit": True},
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)


"""
Add the following to the dashAgGridComponentFunctions.js file in the assets folder

-----------

var dagcomponentfuncs = (window.dashAgGridComponentFunctions =
    window.dashAgGridComponentFunctions || {});

dagcomponentfuncs.EditButton = function (props) {
    function onButtonClicked() {
        // start editing this cell. see the docs on the params that this method takes
        props.api.startEditingCell({
            rowIndex: props.rowIndex,
            colKey: props.column.getId(),
        });
    }

    return React.createElement('span', {}, [
        React.createElement(
            'button',
            {
                onClick: onButtonClicked,
                style: {height: '30px'},
            },
            '✎'
        ),
        React.createElement(
            'span',
            {
                style: {paddingLeft: '4px'},
            },
            props.value
        ),
    ]);
};


"""
