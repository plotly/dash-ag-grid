"""
custom dragger inside a custom cell renderer with custom startDragPixels
"""
import dash_ag_grid as dag
from dash import Dash, dcc, html, Input, Output, Patch
import dash_bootstrap_components as dbc
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.FONT_AWESOME])

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    {'field': 'athlete', 'cellClass': 'custom-athlete-cell',
     'cellRenderer': "CustomCellRenderer",
     },
    {'field': 'country'},
    {'field': 'year', 'width': 100},
    {'field': 'date'},
    {'field': 'sport'},
    {'field': 'gold'},
    {'field': 'silver'},
    {'field': 'bronze'},
]

defaultColDef = {'width': 170, "sortable": True, "filter": True, "resizable": True}

app.layout = html.Div(
    [
        dcc.Markdown("""This grid shows a custom dragger inside a custom cell renderer  
        The pixels threshold to drag before dragging the row can also be customized"""),
        dbc.Input(id='input-num', placeholder="Default: 4px", type="number", min=0,
                  className='text-center', style={"width": 150}),
        dag.AgGrid(
            id='grid-row-drag',
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
            dashGridOptions={
                "rowDragManaged": True,
                "animateRows": True,
            }
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("grid-row-drag", "columnDefs"),
    Input("input-num", "value"),
    prevent_initial_call=True,
)
def update_startDragPixels(pixels):
    columnDefs_patch = Patch()
    columnDefs_patch[0]["cellRendererParams"] = {"startDragPixels": pixels if pixels is not None else 4}
    return columnDefs_patch


if __name__ == "__main__":
    app.run_server(debug=True)

"""
--------------------

Add the following to the .css file in the assets folder:

--------------------

.ag-ltr .ag-cell.custom-athlete-cell.ag-cell-focus:not(.ag-cell-range-selected):focus-within {
  border: 1px solid #ff7b7b;
}
.ag-cell.custom-athlete-cell {
  padding-left: 0 !important;
  padding-right: 0 !important;
}
.ag-cell.custom-athlete-cell > div {
  height: 100%;
}

.my-custom-cell-renderer {
  display: flex;
  font-size: 0.7rem;
  background-color: #4180d6;
  color: white;
  padding: 0.25rem;
  align-items: center;
  justify-content: space-between;
  box-sizing: border-box;
  height: 100%;
}

.my-custom-cell-renderer > * {
  line-height: normal;
}

.my-custom-cell-renderer i {
  visibility: hidden;
  cursor: move;
  color: orange;
}

.my-custom-cell-renderer:hover i {
  visibility: visible;
}

.my-custom-cell-renderer .athlete-info {
  display: flex;
  flex-direction: column;
  width: 85px;
  max-width: 85px;
}

.my-custom-cell-renderer .athlete-info > span {
  overflow: hidden;
  text-overflow: ellipsis;
}

----------------

Add the following to the dashAgGridComponentFunctions.js file in the assets folder

----------------

var dagcomponentfuncs = (window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {});

dagcomponentfuncs.CustomCellRenderer = function (props) {

    const myRef = React.useRef(null);

    React.useEffect(() => {
        props.registerRowDragger(myRef.current, props.startDragPixels);
    });

    return React.createElement('div', {className: 'my-custom-cell-renderer'},
        [
            React.createElement('div', {className: 'athlete-info'}, [
                React.createElement('span', null, props.data.athlete),
                React.createElement('span', null, props.data.country),
            ]),
            React.createElement('span', null, props.data.year),
            React.createElement('i', {className: 'fas fa-arrows-alt-v', ref: myRef})
        ]
    );
};
"""
