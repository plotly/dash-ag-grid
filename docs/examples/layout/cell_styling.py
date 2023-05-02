"""
AG-grid styling Cells.
"""

import dash_ag_grid as dag
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

columnDefs = [
    {"headerName": "Make", "field": "make"},
    {"headerName": "Model", "field": "model"},
    {"headerName": "Price", "field": "price"},
]

cellStylColumnDefs = [
    {"headerName": "Make", "field": "make", "cellStyle": {"color": "purple"}},
    {"headerName": "Model", "field": "model"},
    {"headerName": "Price", "field": "price"},
]

cellClassRules = {
    "bg-primary": "params.value == 'Toyota'",
    "bg-secondary": "params.value == 'Ford'",
    "bg-success": "params.value == 'Porsche'",
}
cellClassRulesColumnDefs = [
    {"headerName": "Make", "field": "make", "cellClassRules": cellClassRules},
    {"headerName": "Model", "field": "model"},
    {"headerName": "Price", "field": "price"},
]

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxster", "price": 72000},
]

grid_with_default_cell_styles = html.Div(
    [
        html.H5(children="Grid with Conditional Cell Style and  Default Style"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            defaultColDef=dict(
                resizable=True,
                cellStyle={
                    "styleConditions": [
                        {"condition": "params.value == 72000", "style": {"color": "orange"}},
                    ],
                    "defaultStyle": {"color": "blue"}
                },
            ),
        ),
        html.Hr(),
    ]
)

grid_with_cell_style = html.Div(
    [
        html.H5(children="Grid with Individual Cell Style"),
        dag.AgGrid(
            columnDefs=cellStylColumnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            defaultColDef=dict(
                resizable=True,
            ),
        ),
        html.Hr(),
    ]
)

grid_with_conditional_cell_styles = html.Div(
    [
        html.H5(children="Grid with Conditional Cell Styles"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            defaultColDef=dict(
                resizable=True,
                cellStyle={
                    "styleConditions": [
                        {"condition": "params.value == 72000", "style": {"color": "orange"}},
                        {
                            "condition": "params.value == 'Celica'",
                            "style": {"backgroundColor": "purple", "color": "white"},
                        },
                        {
                            "condition": "params.colDef.headerName == 'Make'",
                            "style": {"backgroundColor": "red", "color": "green"},
                        },
                    ]
                },
            )
        ),
        html.Hr(),
    ]
)


grid_with_cell_class_rules = html.Div(
    [
        html.H5(children="Grid with Cell Class Rules"),
        dag.AgGrid(
            columnDefs=cellClassRulesColumnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            defaultColDef=dict(
                resizable=True,
            ),
        ),
        html.Hr(),
    ]
)



app.layout = html.Div(
    [
        grid_with_cell_style,
        grid_with_conditional_cell_styles,
        grid_with_default_cell_styles,
        grid_with_cell_class_rules,
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
