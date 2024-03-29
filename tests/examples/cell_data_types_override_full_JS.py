import dash_ag_grid as dag
from dash import Dash, html

app = Dash(__name__)

rowData = [
    {"weight": 0.074657, "date": "01/01/2024"},
    {"weight": 0.06948567, "date": "02/01/2024"},
    {"weight": 0.02730574, "date": "03/01/2024"},
    {"weight": 0.0182345, "date": "04/01/2024"},
]

columnDefs = [
    {"field": "weight", "cellDataType": "percentage"},
    {"field": "date", "cellDataType": "dateString"},
]

app.layout = html.Div(
    [
        dag.AgGrid(
            id="grid-cell-data-types-custom-full-JS",
            columnDefs=columnDefs,
            rowData=rowData,
            defaultColDef={"filter": True, "editable": True},
            dashGridOptions={"dataTypeDefinitions": {"function": "dataTypeDefinitions"}},
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
