from dash import Dash, dcc, html
import dash_ag_grid as dag
import datetime

rowData=[
    {"date":"2023-01-01"},
    {"date":"2023-02-11"},
    {"date":"2023-06-10"},
    {"date":"2023-11-04"},
    {"date":"2023-21-03"},
]

# function to create a date object from  a date string "YYYY-MM-DD"
date_obj = "d3.timeParse('%Y-%m-%d')(data.date)"



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
        "headerName": "Month d, YYYY",
        "valueGetter": {"function": date_obj},
        "valueFormatter": {"function": f"d3.timeFormat('%B %e, %Y')({date_obj})"},
    },
    {
        "headerName": "MM-DD-YY",
        "valueGetter": {"function": date_obj},
        "valueFormatter": {"function": f"d3.timeFormat('%m-%d-%y')({date_obj})"},
    },

]

defaultColDef= {
        "filter": "agDateColumnFilter",
        "filterParams": {
            "buttons": ["clear", "apply"],
        },
        "sortable": True
    }


app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.Markdown("Date formatting example."),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=rowData,
            defaultColDef=defaultColDef
        )
    ],
    style={"margin":20}
)


if __name__ == "__main__":
    app.run_server(debug=True)
