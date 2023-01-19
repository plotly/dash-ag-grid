"""

Right Aligned and Numeric Columns

"""

import dash
import dash_ag_grid as dag
from dash import dcc, html
import pandas as pd


app = dash.Dash(__name__)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")


columnDefs = [{"field": "State"}] + [
    {"field": i, "type": "rightAligned"} for i in df.columns if i != "State"
]

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration of right aligned columns."),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=False)
