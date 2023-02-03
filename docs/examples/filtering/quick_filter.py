import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])


columnDefs = [
    {"headerName": "Employee", "field": "employee", "sortable": True},
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
    {"employee": "Shellie Umland", "sickDays": 5},
    {"employee": "Kristi Nawrocki", "sickDays": 2},
    {"employee": "Elliot Malo", "sickDays": 3},
    {"employee": "Paul Switzer", "sickDays": 11},
    {"employee": "Lilly Boaz", "sickDays": 6},
    {"employee": "Frank Kimura", "sickDays": 1},
    {"employee": "Alena Wages", "sickDays": 5},
]


app.layout = html.Div(
    [
        dcc.Markdown(
            "This grid demonstrates the quick filter, which will check all words provided against the full row."
        ),
        dcc.Input(id="quick-filter-input", placeholder="filter..."),
        dag.AgGrid(
            id="quick-filter-grid",
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("quick-filter-grid", "quickFilterText"), Input("quick-filter-input", "value")
)
def update_filter(filter_value):
    return filter_value


if __name__ == "__main__":
    app.run_server(debug=False)
