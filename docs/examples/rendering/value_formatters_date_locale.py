"""

This doesn't work yet
"""


from dash import Dash, dcc, html
import dash_ag_grid as dag
import datetime

rowData = [
    {"date": "2023-01-01"},
    {"date": "2023-02-11"},
    {"date": "2023-06-10"},
    {"date": "2023-11-04"},
    {"date": "2023-21-03"},
]

# d3 datetime locales: https://cdn.jsdelivr.net/npm/d3-time-format@3.0.0/locale
# d3.timeFormatLocale(definition)
locale_fr_FR = """d3.timeFormatLocale{
  "dateTime": "%A %e %B %Y à %X",
  "date": "%d/%m/%Y",
  "time": "%H:%M:%S",
  "periods": ["AM", "PM"],
  "days": ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"],
  "shortDays": ["dim.", "lun.", "mar.", "mer.", "jeu.", "ven.", "sam."],
  "months": ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"],
  "shortMonths": ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."]
}"""


# function to create a date object from  a date string "YYYY-MM-DD"
date_obj = f"({locale_fr_FR}).parse('%Y-%m-%d')(data.date)"

# d3.timeFormatLocale(definition)


columnDefs = [
    {
        "field": "date",
        "valueFormatter": {
            "function": f"{locale_fr_FR}.format('%B %e, %Y')({date_obj})"
        },
    },
    {
        "headerName": "MM/DD/YYYY",
        "valueGetter": {"function": date_obj},
        "valueFormatter": {
            "function": f"{locale_fr_FR}.timeFormat('%m/%d/%Y')({date_obj})"
        },
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
        "valueFormatter": {
            "function": f"{locale_fr_FR}.timeFormat('%B %e, %Y')({date_obj})"
        },
    },
    {
        "headerName": "MM-DD-YY",
        "valueGetter": {"function": date_obj},
        "valueFormatter": {"function": f"d3.timeFormat('%m-%d-%y')({date_obj})"},
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
    [dag.AgGrid(columnDefs=columnDefs, rowData=rowData, defaultColDef=defaultColDef)],
    style={"margin": 20},
)


if __name__ == "__main__":
    app.run_server(debug=True)
