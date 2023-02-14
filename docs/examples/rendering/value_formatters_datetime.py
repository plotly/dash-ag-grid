from dash import Dash, dcc, html
import dash_ag_grid as dag
from datetime import datetime

rowData = [
    {"date": datetime(2023, 1, 1, 1, 0, 0)},
    {"date": datetime(2023, 1, 2, 2, 0, 0)},
    {"date": datetime(2023, 1, 3, 3, 0, 0)},
    {"date": datetime(2023, 1, 4, 18, 0, 0)},
    {"date": datetime(2023, 1, 5, 22, 0, 0)},
]

# function to create a date object from  a date string "YYYY-MM-DD"
date_obj = "d3.timeParse('%Y-%m-%dT%H:%M:%S')(data.date)"

# if the time is in utc:
# date_obj = "d3.utcParse('%Y-%m-%dT%H:%M:%S')(data.date)"


columnDefs = [
    {
        "field": "date",
    },
    {
        "headerName": "MM/DD/YYYY",
        "valueGetter": {"function": date_obj},
        "valueFormatter": {"function": f"d3.timeFormat('%m/%d/%Y')({date_obj})"},
    },
    {
        "headerName": "Mon DD, YYYY",
        "valueGetter": {"function": date_obj},
        "valueFormatter": {"function": f"d3.timeFormat('%b %d, %Y')({date_obj})"},
    },
    {
        "headerName": "day, Mon DD, YYYY",
        "valueGetter": {"function": date_obj},
        "valueFormatter": {"function": f"d3.timeFormat('%a %b %d, %Y')({date_obj})"},
    },
    {
        "headerName": "yyyy-mm-dd HH:MM:SS tt",
        "valueGetter": {"function": date_obj},
        "valueFormatter": {
            "function": f"d3.timeFormat('%Y-%m-%d %I:%M:%S %p')({date_obj})"
        },
    },
    {
        "headerName": "yyyy-mm-dd hh:mm:ss",
        "valueGetter": {"function": date_obj},
        "valueFormatter": {
            "function": f"d3.timeFormat('%Y-%m-%d %H:%M:%S')({date_obj})"
        },
    },
]

defaultColDef = {
    "filter": "agDateColumnFilter",
    "filterParams": {
        "buttons": ["clear", "apply"],
    },
    "sortable": True,
}


app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.Markdown("Datetime formatting example."),
        dag.AgGrid(columnDefs=columnDefs, rowData=rowData, defaultColDef=defaultColDef),
    ],
    style={"margin": 20},
)


if __name__ == "__main__":
    app.run_server(debug=True)
