from dash import Dash, html
from dash_ag_grid import AgGrid
import pandas as pd
import colorlover


wide_data = [
    {"Firm": "Acme", "2017": 13, "2018": 5, "2019": 10, "2020": 4},
    {"Firm": "Olive", "2017": 3, "2018": 3, "2019": 13, "2020": 3},
    {"Firm": "Barnwood", "2017": 6, "2018": 7, "2019": 3, "2020": 6},
    {"Firm": "Henrietta", "2017": -3, "2018": -10, "2019": -5, "2020": -6},
]
df = pd.DataFrame(wide_data)

app = Dash(__name__)


def discrete_background_color_bins(df, n_bins=5, columns="all"):
    bounds = [i * (1.0 / n_bins) for i in range(n_bins + 1)]
    if columns == "all":
        df_numeric_columns = df.select_dtypes("number")
    else:
        df_numeric_columns = df[columns]
    df_max = df_numeric_columns.max().max()
    df_min = df_numeric_columns.min().min()
    ranges = [((df_max - df_min) * i) + df_min for i in bounds]
    styleConditions = []
    legend = []
    for i in range(1, len(bounds)):
        min_bound = ranges[i - 1]
        max_bound = ranges[i]
        if i == len(bounds) - 1:
            max_bound += 1

        backgroundColor = colorlover.scales[str(n_bins)]["seq"]["Blues"][i - 1]
        color = "white" if i > len(bounds) / 2.0 else "inherit"

        styleConditions.append(
            {
                "condition": f"params.value >= {min_bound} && params.value < {max_bound}",
                "style": {"backgroundColor": backgroundColor, "color": color},
            }
        )

        legend.append(
            html.Div(
                [
                    html.Div(
                        style={
                            "backgroundColor": backgroundColor,
                            "borderLeft": "1px rgb(50, 50, 50) solid",
                            "height": "10px",
                        }
                    ),
                    html.Small(round(min_bound, 2), style={"paddingLeft": "2px"}),
                ],
                style={"display": "inline-block", "width": "60px"},
            )
        )

    return styleConditions, html.Div(legend, style={"padding": "5px 0 5px 0"})


styleConditions, legend = discrete_background_color_bins(df)

app.layout = html.Div(
    [
        html.H5("Highlighting Cells by Value with a Colorscale Like a Heatmap"),
        legend,
        AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[{"field": i} for i in df.columns],
            defaultColDef={"cellStyle": {"styleConditions": styleConditions}, "sortable": True},
            columnSize="responsiveSizeToFit",
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
