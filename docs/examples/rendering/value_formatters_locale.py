"""
number formatting with d3-format for different locales
"""
import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd
import numpy as np

app = Dash(__name__)

df = pd.DataFrame(
    np.random.uniform(-10000, 10000, size=(15, 4)),
    columns=["Default", "France", "Japan", "UK"],
)

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
    {
        "field": "Default",
        "valueFormatter": {"function": "d3.format('$,.2f')(params.value)"},
    },
    {
        "field": "France",
        "valueFormatter": {"function": f"{locale_fr_FR}.format('$,.2f')(params.value)"},
    },
    {
        "field": "Japan",
        "valueFormatter": {"function": f"{locale_ja_JP}.format('$,.2f')(params.value)"},
    },
    {
        "field": "UK",
        "valueFormatter": {"function": f"{locale_en_GB}.format('$,.2f')(params.value)"},
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
            "This grid demonstrates formatting numbers for different locales using d3-format."
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef=defaultColDef,
        ),
    ],
    style={"margin": 20},
)


if __name__ == "__main__":
    app.run_server(debug=True)
