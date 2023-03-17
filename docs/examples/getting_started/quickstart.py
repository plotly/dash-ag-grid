from dash import Dash, html, Input, Output
import dash_ag_grid as dag
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")

app = Dash(__name__)

grid = dag.AgGrid(
    id="quickstart-grid",
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i, "id": i} for i in df.columns],
    defaultColDef={"resizable": True, "sortable": True, "filter": True},
    columnSize="sizeToFit",
    getRowId="params.data.State"
)

app.layout = html.Div([grid, html.Div(id="quickstart-output")])


@app.callback(
    Output("quickstart-output", "children"), Input("quickstart-grid", "cellClicked")
)
def display_cell_clicked_on(cell):
    if cell is None:
        return "Click on a cell"
    return f"clicked on cell value:  {cell['value']}, column:   {cell['colId']}, row index:   {cell['rowIndex']}"


if __name__ == "__main__":
    app.run_server(debug=True)
