from dash import Dash, html, Input, Output, ctx
import dash_ag_grid as dag
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

app = Dash(__name__)

grid = dag.AgGrid(
    id="size-grid",
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
    defaultColDef={"resizable": True},
    columnSize="sizeToFit",
)


app.layout = html.Div(
    [
        html.Button("Default Size", id="default-size"),
        html.Button("Change Size", id="change-size"),
        grid,
    ]
)


@app.callback(
    Output("size-grid", "style"),
    Output("size-grid", "columnSize"),
    Input("default-size", "n_clicks"),
    Input("change-size", "n_clicks"),
    prevent_initial_call=True,
)
def change_size(*_):
    if ctx.triggered_id == "default-size":
        return {"height": 400, "width": "100%"}, "sizeToFit"
    return {"height": 600, "width": 400}, None


if __name__ == "__main__":
    app.run_server(debug=True)
