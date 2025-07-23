# Test for dag v32.3.4, supporting the new Selection API and still supporting the deprecated Selection API
import dash_ag_grid as dag
from dash import Dash, html
import pandas as pd

app = Dash()

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [{"field": i} for i in ["country", "year", "athlete", "age", "sport", "total"]]

app.layout = html.Div(
    [
        'New Selection API',
        dag.AgGrid(
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
            },
            style={'margin-bottom': '10px'},
        ),
        'Deprecated Selection API',
        dag.AgGrid(
            id="grid-row-selection-remove-checkboxes-deprecated",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef={
                "filter": True,
                "checkboxSelection": {
                    "function": 'params.column == params.api.getAllDisplayedColumns()[0]'
                },
                "headerCheckboxSelection": {
                    "function": 'params.column == params.api.getAllDisplayedColumns()[0]'
                }
            },
            dashGridOptions={"rowSelection": "multiple"},
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
