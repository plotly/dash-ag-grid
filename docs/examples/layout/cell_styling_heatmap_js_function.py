"""
styling with custom function

Note:
Custom functions  must be defined in the dashAgGridFunctions.js in assets folder.
"""


import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc

df = pd.DataFrame(np.random.randint(-100, 100, size=(10, 3)), columns=list("abc"))
df["items"] = [f"Item {i}" for i in range(len(df))]
df_numeric_columns = df.select_dtypes("number")
min = df_numeric_columns.min().min()
max = df_numeric_columns.max().max()


columnDefs = [{"field": "items"},] + [
    {
        "field": field,
        "cellStyle": {"function": "heatMap(params)"},
        "cellRendererParams": {"min": min, "max": max},
    }
    for field in ["a", "b", "c"]
]


defaultColDef = {
    "resizable": True,
    "sortable": True,
    "editable": True,
    "minWidth": 100,
}


grid = dag.AgGrid(
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    columnSize="responsiveSizeToFit",
    defaultColDef=defaultColDef,
    dashGridOptions={"suppressRowHoverHighlight": True},
)


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        html.H5("Styling cells like a Heatmap with custom function"),
        grid,
    ],
    style={"margin": 20},
)


if __name__ == "__main__":
    app.run_server(debug=True)


"""
Put the following in the dashAgGridFunctions.js file in the assets folder

---------------------------------

var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

function rgbToHex(r, g, b) {
    return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
};

dagfuncs.heatMap = function (props) {
    const min = props.colDef.cellRendererParams.min;
    const max = props.colDef.cellRendererParams.max;
    const val = props.value;

    if(val) {
        if(val > 0) {
            g = 255;
            r = b = Math.round(255 * (1 - val / max));
        }
        else {
            r = 255;
            g = b = Math.round(255 * (1 - val / min));
        };

        return {
            backgroundColor: rgbToHex(r, g, b),
            color: 'black',
        }
    }
    else {
        return {};
    }
};
"""
