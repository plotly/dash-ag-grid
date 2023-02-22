"""
Row styling conditional
"""


import dash_ag_grid as dag
from dash import Dash, html, dcc

app = Dash(__name__)


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
    {"employee": "Shellie Umland", "sickDays": 5},
    {"employee": "Kristi Nawrocki", "sickDays": 2},
    {"employee": "Elliot Malo", "sickDays": 3},
    {"employee": "Paul Switzer", "sickDays": 11},
    {"employee": "Lilly Boaz", "sickDays": 6},
    {"employee": "Frank Kimura", "sickDays": 1},
    {"employee": "Alena Wages", "sickDays": 5},
]


getRowStyle = {
    "styleConditions": [
        {
            "condition": "params.data.sickDays > 5 && params.data.sickDays <= 7",
            "style": {"backgroundColor": "sandybrown"},
        },
        {"condition": "params.data.sickDays >= 8", "style": {"backgroundColor": "lightcoral"}},
    ]
}


app.layout = html.Div(
    [
        dcc.Markdown(
            "This grid demonstrates conditional row formatting using the `getRowStyle` prop."
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            getRowStyle=getRowStyle,
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=False)
