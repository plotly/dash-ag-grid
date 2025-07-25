import dash_ag_grid as dag
from dash import Dash, Input, Output, State, dcc, html

"""
Note the custom assets_folder in this app!
Change the `className` theme to one of the options in that folder to see the
legacy theme in action.
"""

app = Dash(__name__, external_stylesheets=[dag.themes.BASE, dag.themes.MATERIAL])

rowData = [
    {"weight": 0.074657, "date": "01/01/2024"},
    {"weight": 0.06948567, "date": "02/01/2024"},
    {"weight": 0.02730574, "date": "03/01/2024"},
    {"weight": 0.0182345, "date": "04/01/2024"},
]

columnDefs = [
    {"field": "weight"},
    {"field": "date"},
]

app.layout = html.Div(
    [
        dag.AgGrid(
            id="grid",
            columnDefs=columnDefs,
            rowData=rowData,
            defaultColDef={"filter": True, "editable": True},
            dashGridOptions={"theme": "legacy"},
            className="ag-theme-material",
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
