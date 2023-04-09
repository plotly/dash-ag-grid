"""
Updating the filter in a callback and persistance

"""
import dash
import dash_ag_grid as dag
from dash import Dash, Input, Output, dcc, html, callback

app = Dash(__name__)

columnDefs = [
    {"field": "make"},
    {"field": "model"},
    {"field": "price"},
]

rowData = [
    {"make": "Toyota", "model": "Celica", "price": 35000},
    {"make": "Ford", "model": "Mondeo", "price": 32000},
    {"make": "Porsche", "model": "Boxter", "price": 72000},
]


app.layout = html.Div(
    [
        dcc.Markdown(
             "The `filterModel` prop can be used to update and read from the current filters applied in the AgGrid UI. Filters can also be peristed using `persistence`."
         ),
        html.Button("Update Filter", id="filter-model-btn", n_clicks=0),
        dag.AgGrid(
            id="filter-model-grid1",
            columnSize="sizeToFit",
            rowData=rowData,
            columnDefs=columnDefs,
            defaultColDef={"filter": True, "sortable": True, "floatingFilter": True},
            persistence=True,
            persisted_props=["filterModel"]
        ),
    ]
)


@callback(
    Output("filter-model-grid1", "filterModel"),
    Input("filter-model-btn", "n_clicks"),
)
def get_cur_filter(n):
    if n >0:
        return {'model': {'filterType': 'text', 'type': 'contains', 'filter': 'cel'}}
    return dash.no_update


if __name__ == "__main__":
    app.run_server(debug=True)
