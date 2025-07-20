import dash_ag_grid as dag
from dash import Dash
import pandas as pd

app = Dash()

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [{"field": i} for i in ["country", "year", "athlete", "age", "sport", "total"]]

app.layout = dag.AgGrid(
    id="grid-row-selection-remove-checkboxes",
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    columnSize="sizeToFit",
    dashGridOptions={
        "rowSelection": {
            'mode': 'singleRow',
            # test selection checkboxes as function
            'checkboxes': {"function": "params.data.year > 2007"}
        },
    }
)

if __name__ == "__main__":
    app.run(debug=True)
