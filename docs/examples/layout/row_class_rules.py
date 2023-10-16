"""
Row Class Rules
"""


import dash_ag_grid as dag
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])


columnDefs = [
    {"headerName": "Employee", "field": "employee"},
    {"headerName": "Number Sick Days", "field": "sickDays", "editable": True},
]

rowData = [
    {"employee": "Josh Finch", "sickDays": 4},
    {"employee": "Flavia Mccloskey", "sickDays": 1},
    {"employee": "Marine Creason", "sickDays": 8},
    {"employee": "Carey Livingstone", "sickDays": 2},
    {"employee": "Brande Giorgi", "sickDays": 5},
    {"employee": "Beatrice Kugler", "sickDays": 3},
    {"employee": "Elvia Macko", "sickDays": 7},
    {"employee": "Santiago Little", "sickDays": 1},
    {"employee": "Mary Clifton", "sickDays": 2},
    {"employee": "Norris Iniguez", "sickDays": 1},
    {"employee": "Flavia Mccloskey", "sickDays": 5},
    {"employee": "Kristi Nawrocki", "sickDays": 2},
    {"employee": "Elliot Malo", "sickDays": 3},
    {"employee": "Paul Switzer", "sickDays": 11},
    {"employee": "Lilly Boaz", "sickDays": 6},
    {"employee": "Frank Kimura", "sickDays": 1},
    {"employee": "Alena Wages", "sickDays": 5},
]

rowClassRules={
    "text-success fw-bold fs-4": "params.data.employee == 'Elvia Macko'",
    "text-warning fw-bold fs-4": "['Flavia Mccloskey', 'Lilly Boaz'].includes(params.data.employee)"
}


app.layout = html.Div(
    [
        dcc.Markdown(
            "This grid demonstrates conditional row formatting using the `rowClassRules` prop."
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            rowClassRules=rowClassRules,
        ),

        dcc.Markdown(
            "This grid demonstrates highlighting sick days >=5.  Try editing the sick days and note the background color is updated.",
            style={"marginTop": 50}
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            rowClassRules={"bg-danger": "params.data.sickDays >= 5"}
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=False)
