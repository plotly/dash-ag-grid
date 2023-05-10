"""
styling with custom cell renderer

Note:
Custom components  must be defined in the dashAgGridComponentFunctions.js in assets folder.
"""

import json
import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc

df = pd.DataFrame(np.random.randint(0, 100, size=(10, 6)), columns=list("abcdef"))


columnDefs = [
    {

        "field": "a",
        "cellRenderer": "DBC_Progress",
        "cellRendererParams": {
            "color": "primary",
            "className": "mt-2",
             "label": True,
        },
    },

    {
        "field": "b",
        "cellRenderer": "DBC_Progress",
        "cellRendererParams": {
            "color": "secondary",
        },
    },
    {
        "field": "c",
        "cellRenderer": "DBC_Progress",
        "cellRendererParams": {
            "color": "info",
            "animated": True,
        },
    },
    {
        "field": "d",
        "cellRenderer": "DBC_Progress",
        "cellRendererParams": {
            "color": "success",
            "label": True,
        },
    },
    {
        "field": "e",
        "cellRenderer": "DBC_Progress",
        "cellRendererParams": {
            "color": "warning",
            "label": True,
            "striped": True,
        },
    },
    {
        "field": "f",
        "cellRenderer": "DBC_Progress",
        "cellRendererParams": {
            "color": "danger",
            "label": True,
            "striped": True,
            "style": {"height":30}
        },
    },
]


defaultColDef = {
    "resizable": True,
    "sortable": True,
    "editable": False,
    "minWidth": 200,
}


grid = dag.AgGrid(
    id="custom-component-dbc-progress-grid",
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    columnSize="sizeToFit",
    defaultColDef=defaultColDef,
    dashGridOptions={"suppressRowHoverHighlight":True},
)


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        dcc.Markdown(
            """
            ### `dbc.Progress`
            Example of cellRenderer with dash-bootstrap-components `dbc.Progress`  and Font Awesome and Bootstrap icons
            """
        ),
        grid,
        html.Div(id="custom-component-dbc-progress-value-changed"),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("custom-component-dbc-progress-value-changed", "children"),
    Input("custom-component-dbc-progress-grid", "cellRendererData"),
)
def showChange(n):
    return json.dumps(n)


if __name__ == "__main__":
    app.run_server(debug=True)


"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder

---------------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};


// use for making dbc.Progress
dagcomponentfuncs.DBC_Progress = function (props) {
    const {setData, data} = props;

    function onClick() {
        setData(props.value);
    }
    return React.createElement(
        window.dash_bootstrap_components.Progress,
        {
            onClick,
            animated: props.animated,
            className: props.className,
            color: props.color,
            label: (props.label === undefined) ? "": props.value + '%',
            max: props.max,
            min: props.min,
            striped: props.striped,
            style: props.style,
            value: props.value
        },
    );
};




"""