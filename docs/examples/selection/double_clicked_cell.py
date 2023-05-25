from dash import Dash, html, Input, Output
import dash_ag_grid as dag
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")

app = Dash(__name__)

grid = dag.AgGrid(
    id="grid",
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
    defaultColDef={
        "resizable": True,
        "sortable": True,
        "filter": True,
        "minWidth": 125,
    },
    columnSize="sizeToFit",
)

app.layout = html.Div([grid, html.Div(id="output")])


@app.callback(Output("output", "children"), Input("grid", "cellDoubleClicked"))
def display_cell_double_clicked_on(cell):
    if cell is None:
        return "Double click on a cell"
    return f"Double clicked on cell value: {cell['value']}, column: {cell['colId']}, row index: {cell['rowIndex']}"


if __name__ == "__main__":
    app.run_server(debug=True)
