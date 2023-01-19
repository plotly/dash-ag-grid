"""
Conditional formatting in AG-grid.
"""

import dash_ag_grid as dag
import dash
from dash import html, dcc

app = dash.Dash(__name__)

columnDefs = [
    {"headerName": "Make", "field": "make"},
    {"headerName": "Model", "field": "model"},
    {"headerName": "Price", "field": "price"},
]

individualStyledColumnDefs = [
    {"headerName": "Make", "field": "make", "cellStyle": {"color": "purple"}},
    {"headerName": "Model", "field": "model"},
    {"headerName": "Price", "field": "price"},
]

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxter", "price": 72000},
]

grid_with_default_cell_styles = html.Div(
    [
        html.H3(children="Grid with Default Cell Styles"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            defaultColDef=dict(
                resizable=True,
            ),
            cellStyle={"defaultStyle": {"color": "blue"}},
        ),
        html.Hr(),
    ]
)

grid_with_individual_cell_style = html.Div(
    [
        html.H3(children="Grid with Individual Cell Style"),
        dag.AgGrid(
            columnDefs=individualStyledColumnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            defaultColDef=dict(
                resizable=True,
            ),
        ),
        html.Hr(),
    ]
)

grid_with_basic_row_style = html.Div(
    [
        html.H3(children="Grid with Basic Row Style"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            defaultColDef=dict(
                resizable=True,
            ),
            rowStyle={"background": "yellow"},
        ),
        html.Hr(),
    ]
)

grid_with_conditional_cell_styles = html.Div(
    [
        html.H3(children="Grid with Conditional Cell Styles"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            defaultColDef=dict(
                resizable=True,
            ),
            cellStyle={
                "styleConditions": [
                    {"condition": "value == 72000", "style": {"color": "orange"}},
                    {
                        "condition": "value == 'Celica'",
                        "style": {"backgroundColor": "purple", "color": "white"},
                    },
                    {
                        "condition": "colDef.headerName == 'Make'",
                        "style": {"backgroundColor": "red", "color": "green"},
                    },
                ]
            },
        ),
        html.Hr(),
    ]
)


app.layout = html.Div(
    [
        dcc.Markdown("Examples of cell styling using the AG-Grid Cell Style approach."),
        grid_with_default_cell_styles,
        grid_with_basic_row_style,
        grid_with_individual_cell_style,
        grid_with_conditional_cell_styles,
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
