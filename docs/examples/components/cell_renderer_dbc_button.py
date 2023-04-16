"""
styling with custom cell renderer

Note:
Custom components  must be defined in the dashAgGridComponentFunctions.js in assets folder.
"""

import json
import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import dash_bootstrap_components as dbc




data = {
    "ticker": ["AAPL", "MSFT", "AMZN", "GOOGL"],
    "info": ["Info" for _ in range(4)],
    "buy": ["Buy" for _ in range(4)],
    "sell": ["Sell" for _ in range(4)],
    "watch": ["Watch" for _ in range(4)],
    "info": ["Info" for _ in range(4)],
}
df = pd.DataFrame(data)

columnDefs = [
    {
        "headerName": "Stock Ticker link",
        "field": "ticker",
        "cellRenderer": "DBC_Button",
        "cellRendererParams": {
            "leftIcon": "bi bi-box-arrow-up-right me-2",
            "color": "danger",
            "href": True, # href is defined in the component
            "external_link": True,
            "target": "_blank",
            "title": "Go To Yahoo Finance"
        },
    },

    {
        "field": "buy",
        "cellRenderer": "DBC_Button",
        "cellRendererParams": {
            "variant": "outline",
            "leftIcon": "bi bi-bag me-2",
            "color": "primary",

        },
    },
    {
        "field": "sell",
        "cellRenderer": "DBC_Button",
        "cellRendererParams": {
            "variant": "outline",
            "leftIcon": "bi bi-trash me-2",
            "color": "secondary",

        },
    },
    {
        "field": "watch",
        "cellRenderer": "DBC_Button",
        "cellRendererParams": {
            "rightIcon": "fa-solid fa-eye ms-2",
            "outline": True,
            "color": "success"
        },
    },
{
        "field": "info",
        "cellRenderer": "DBC_Button",
        "cellRendererParams": {
            "rightIcon": "fa-solid fa-circle-info ms-2",
            "outline": True,
            "color": "info"
        },
    },

]


defaultColDef = {
    "resizable": True,
    "sortable": True,
    "editable": False,
}


grid = dag.AgGrid(
    id="custom-component-dbc-btn2-grid",
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    columnSize="autoSizeAll",
    defaultColDef=defaultColDef,
    dashGridOptions={"rowHeight": 48, "suppressRowHoverHighlight":True},
)


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME, dbc.icons.BOOTSTRAP])

app.layout = html.Div(
    [

        dcc.Markdown(
            """
            ### `dbc.Button` with icons
            Example of cellRenderer with dash-bootstrap-components `dbc.Button`  and Font Awesome and Bootstrap icons
            """
        ),
        grid,
        html.Div(id="custom-component-dbc-btn2-value-changed"),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("custom-component-dbc-btn2-value-changed", "children"),
    Input("custom-component-dbc-btn2-grid", "cellRendererData"),
)
def showChange(n):
    return json.dumps(n)


if __name__ == "__main__":
    app.run_server(debug=True)


"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder

---------------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};

// use for making dbc.Button with FontAwesome or Bootstrap icons
dagcomponentfuncs.DBC_Button = function (props) {
    const {setData, data} = props;

    function onClick() {
        setData();
    }
    let leftIcon, rightIcon;
    if (props.leftIcon) {
        leftIcon = React.createElement("i", {
            className: props.leftIcon,
        });
    }
    if (props.rightIcon) {
        rightIcon = React.createElement("i", {
            className: props.rightIcon,
        });
    }
    return React.createElement(
        window.dash_bootstrap_components.Button,
        {
            onClick,
            color: props.color,
            disabled: props.disabled,
            download: props.download,
            external_link: props.external_link,
            // change this link for your application:
            href: (props.href === undefined) ? null : 'https://finance.yahoo.com/quote/' + props.value,
            outline: props.outline,
            size: props.size,
            style: {
                margin: props.margin,
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
            },
            target: props.target,
            title: props.title,
            type: props.type
        },
        leftIcon,
        props.value,
        rightIcon,
    );
};


"""