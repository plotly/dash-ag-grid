"""
number formatting with d3-format for different locales
"""
import dash_ag_grid as dag
from dash import Dash, html, dcc

app = Dash(__name__)


rowData = [
    {"specifier": "$,.2f", "Default": 1000, "France": 1000, "Japan": 1000, "UK": 1000},
]


# find locals at https://cdn.jsdelivr.net/npm/d3-format@1/locale/
locale_fr_FR = """d3.formatLocale({
  "decimal": ",",
  "thousands": "\u00a0",
  "grouping": [3],
  "currency": ["", "\u00a0€"],
  "percent": "\u202f%"
})"""


locale_ja_JP = """d3.formatLocale({
 "decimal": ".",
  "thousands": ",",
  "grouping": [3],
  "currency": ["", "円"]

})"""


locale_en_GB = """d3.formatLocale({
 "decimal": ".",
  "thousands": ",",
  "grouping": [3],
  "currency": ["£", ""]
})"""


columnDefs = [
    {"field": "specifier", "headerName": "d3 specifier"},
    {
        "field": "Default",
        "valueFormatter": {"function": "d3.format(data.specifier)(value)"},
    },
    {
        "field": "France",
        "valueFormatter": {"function": f"{locale_fr_FR}.format(data.specifier)(value)"},
    },
    {
        "field": "Japan",
        "valueFormatter": {"function": f"{locale_ja_JP}.format(data.specifier)(value)"},
    },
    {
        "field": "UK",
        "valueFormatter": {"function": f"{locale_en_GB}.format(data.specifier)(value)"},
    },
]

defaultColDef = {
    "type": ["numberColumn", "rightAligned"],
    "resizable": True,
    "editable": True,
}

app.layout = html.Div(
    [
        dcc.Markdown(
            "This editable grid demonstrates formatting numbers for different locales using d3-format.  Try changing the specifier and/or the values!"
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            defaultColDef=defaultColDef,
            dashGridOptions={"singleClickEdit": True},
        ),
    ],
    style={"margin": 20},
)


if __name__ == "__main__":
    app.run_server(debug=True)
