"""
Column Types
"""
import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd

app = Dash(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

# Column Types example
columnTypes = {
    "numberColumn": {"width": 130, "filter": "agNumberColumnFilter"},
    "medalColumn": {"width": 100, "columnGroupShow": "open", "filter": False},
    "nonEditableColumn": {"editable": False},
}

columnDefs = [
    # using default ColDef
    {"field": "athlete"},
    {"field": "sport"},
    # using number column type
    {"field": "age", "type": "numberColumn"},
    # overrides the default with a number filter
    {"field": "year", "filter": "agNumberColumnFilter"},
    # using non-editable column types
    {"field": "date", "type": "nonEditableColumn", "width": 220},
    {
        "headerName": "Medals",
        "groupId": "medalsGroup",
        "children": [
            # using medal column type
            {"headerName": "Gold", "field": "gold", "type": "medalColumn"},
            {"headerName": "Silver", "field": "silver", "type": "medalColumn"},
            {"headerName": "Bronze", "field": "bronze", "type": "medalColumn"},
            {"headerName": "Total", "field": "total", "type": "medalColumn", "columnGroupShow": "closed"},
        ],
    },
]

defaultColDef = {
    # set the default column width
    "width": 100,
    # make every column editable
    "editable": True,
    # make every column use 'text' filter by default
    "filter": "agTextColumnFilter",
    # enable floating filters by default
    "floatingFilter": True,
    # make columns resizable
    "resizable": True,
}

defaultColGroupDef = {
    # Moving the columns outside the group (and hence breaking the group) is not allowed
    "marryChildren": True,
}

app.layout = html.Div(
    [
        dcc.Markdown("This grid has different column types defined"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            dashGridOptions={
                'defaultColGroupDef': defaultColGroupDef,
                'columnTypes': columnTypes,
            }
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)
