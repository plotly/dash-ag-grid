# TODO -Finish jump to row and jump to column
#        - add fucionality for update column state?  or just update entire column definitions in callback?
"""
Column Pinning
You can pin columns by setting the pinned attribute on the column definition to either 'left' or 'right'.

const columnDefs = [
    { "field": 'athlete', "pinned": 'left' }
]


Below shows an example with two pinned columns on the left and one pinned column on the right. The example also demonstrates changing the pinning via the API at runtime.

The grid will reorder the columns so that 'left pinned' columns come first and 'right pinned' columns come last. In the example below the state of pinned columns impacts the order of the columns such that when 'Country' is pinned, it jumps to the first position.

Example Pinning
"""

import requests
import dash
import dash_ag_grid as dag
from dash import dcc, html, Input, Output, ctx
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

data = requests.get(
    r"https://www.ag-grid.com/example-assets/olympic-winners.json"
).json()

columnDefs1 = [
    {
        "headerName": "#",
        "colId": "rowNum",
        "valueGetter": "node.id",
        "width": 80,
        "pinned": "",
    },
    {"field": "athlete", "width": 240, "pinned": ""},
    {"field": "age", "width": 90, "pinned": ""},
    {"field": "country", "width": 150, "pinned": ""},
    {"field": "year", "width": 90},
    {"field": "date", "width": 110},
    {"field": "sport", "width": 150},
    {"field": "gold", "width": 100},
    {"field": "silver", "width": 100},
    {"field": "bronze", "width": 100},
    {"field": "total", "width": 100, "pinned": ""},
]


columnDefs2 = [
    {
        "headerName": "#",
        "colId": "rowNum",
        "valueGetter": "node.id",
        "width": 80,
        "pinned": "left",
    },
    {"field": "athlete", "width": 240, "pinned": "left"},
    {"field": "age", "width": 90, "pinned": "left"},
    {"field": "country", "width": 150},
    {"field": "year", "width": 90},
    {"field": "date", "width": 110},
    {"field": "sport", "width": 150},
    {"field": "gold", "width": 100},
    {"field": "silver", "width": 100},
    {"field": "bronze", "width": 100},
    {"field": "total", "width": 100, "pinned": "right"},
]


columnDefs3 = [
    {
        "headerName": "#",
        "colId": "rowNum",
        "valueGetter": "node.id",
        "width": 80,
    },
    {"field": "athlete", "width": 240},
    {"field": "age", "width": 90},
    {"field": "country", "width": 150, "pinned": "left"},
    {"field": "year", "width": 90},
    {"field": "date", "width": 110},
    {"field": "sport", "width": 150},
    {"field": "gold", "width": 100},
    {"field": "silver", "width": 100},
    {"field": "bronze", "width": 100},
    {"field": "total", "width": 100},
]


defaultColDef = {"resizable": True}

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration of Pinning via Column Dragging and lock pin"),
        dbc.Button("clear pinned", id="clear-pinned"),
        dbc.Button(
            " Left = #, Athlete, Age; Right = Total",
            id="reset-pinned",
            className="mx-1",
        ),
        dbc.Button("Left = Country", id="pin-country"),
        dag.AgGrid(
            id="column-pinning",
            columnDefs=columnDefs1,
            rowData=data,
            defaultColDef=defaultColDef,
        ),
    ]
)


@app.callback(
    Output("column-pinning", "columnDefs"),
    Input("clear-pinned", "n_clicks"),
    Input("reset-pinned", "n_clicks"),
    Input("pin-country", "n_clicks"),
    prevent_initial_call=True,
)
def update_col_def(*_):
    if ctx.triggered_id == "clear-pinned":
        return columnDefs1
    if ctx.triggered_id == "reset-pinned":
        return columnDefs2
    if ctx.triggered_id == "pin-country":
        return columnDefs3


if __name__ == "__main__":
    app.run_server(debug=True)


"""

  clearPinned = () => {
    this.gridColumnApi.applyColumnState({ defaultState: { pinned: null } });
  };

  resetPinned = () => {
    this.gridColumnApi.applyColumnState({
      state: [
        { colId: 'rowNum', pinned: 'left' },
        { colId: 'athlete', pinned: 'left' },
        { colId: 'age', pinned: 'left' },
        { colId: 'total', pinned: 'right' },
      ],
      defaultState: { pinned: null },
    });
  };

  pinCountry = () => {
    this.gridColumnApi.applyColumnState({
      state: [{ colId: 'country', pinned: 'left' }],
      defaultState: { pinned: null },
    });
  };

  jumpToCol = () => {
    const value = document.getElementById('col').value;
    if (typeof value !== 'string' || value === '') {
      return;
    }
    const index = Number(value);
    if (typeof index !== 'number' || isNaN(index)) {
      return;
    }
    // it's actually a column the api needs, so look the column up
    const allColumns = this.gridColumnApi.getColumns();
    if (allColumns) {
      const column = allColumns[index];
      if (column) {
        this.gridApi.ensureColumnVisible(column);
      }
    }
  };

  jumpToRow = () => {
    var value = document.getElementById('row').value;
    const index = Number(value);
    if (typeof index === 'number' && !isNaN(index)) {
      this.gridApi.ensureIndexVisible(index);
    }
  };

  render() {
    return (
      <div style={{ width: '100%', height: '100%' }}>
        <div className="example-wrapper">
          <div className="example-header">
            <div style={{ padding: '4px' }}>
              <button onClick={() => this.clearPinned()}>Clear Pinned</button>
              <button onClick={() => this.resetPinned()}>
                Left = #, Athlete, Age; Right = Total
              </button>
              <button onClick={() => this.pinCountry()}>Left = Country</button>
            </div>

            <div style={{ padding: '4px' }}>
              Jump to:
              <input
                placeholder="row"
                type="text"
                style={{ width: '40px' }}
                id="row"
                onInput={() => this.jumpToRow()}
              />
              <input
                placeholder="col"
                type="text"
                style={{ width: '40px' }}
                id="col"
                onInput={() => this.jumpToCol()}
              />
            </div>
          </div>
          <div
            style={{
              height: '100%',
              width: '100%',
            }}
            className="ag-theme-alpine"
          >
            <AgGridReact
              columnDefs={this.state.columnDefs}
              defaultColDef={this.state.defaultColDef}
              rowData={this.state.rowData}
              onGridReady={this.onGridReady}
            />
          </div>
        </div>
      </div>
    );
  }
}
"""
