"""
Custom number input
"""


import dash_ag_grid as dag
from dash import Dash, html
import pandas as pd

data = {
    "item": ["A", "B", "C", "D"],
    "price": [1154.99, 268.65, 100.00, 96.75],
}
df = pd.DataFrame(data)

columnDefs = [
    {"field": "item"},
    {
        "field": "price",
        "type": "rightAligned",
        "valueFormatter": {"function": """d3.format("($,.2f")(params.value)"""},
        "editable": True,
        "cellEditor": {"function": "NumberInput"},
        "cellEditorParams" : {"placeholder": "enter a number"}
    },
]


grid = dag.AgGrid(
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
)


app = Dash(__name__)

app.layout = html.Div(grid,style={"margin": 20})


if __name__ == "__main__":
    app.run_server(debug=True)


"""
Add this to the dashAgGridFunctions.js file in the assets folder

----------------

var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.NumberInput = class {
    // gets called once before the renderer is used
  init(params) {
    // create the cell
    this.eInput = document.createElement('input');
    this.eInput.value = params.value;
    this.eInput.style.height = 'var(--ag-row-height)';
    this.eInput.style.fontSize = 'calc(var(--ag-font-size) + 1px)';
    this.eInput.style.width = '95%';
    this.eInput.type = "number";
    this.eInput.min = params.min;
    this.eInput.max = params.max;
    this.eInput.step = params.step || "any";
    this.eInput.required =  params.required;
    this.eInput.placeholder =  params.placeholder || "";
    this.eInput.name = params.name;
    this.eInput.disabled = params.disabled;
    this.eInput.title = params.title || ""
  }

  // gets called once when grid ready to insert the element
  getGui() {
    return this.eInput;
  }

  // focus and select can be done after the gui is attached
  afterGuiAttached() {
    this.eInput.focus();
    this.eInput.select();
  }

  // returns the new value after editing
  getValue() {
    return this.eInput.value;
  }

  // any cleanup we need to be done here
  destroy() {
    // but this example is simple, no cleanup, we could
    // even leave this method out as it's optional
  }

  // if true, then this editor will appear in a popup
  isPopup() {
    // and we could leave this method out also, false is the default
    return false;
  }
}


"""












"""
styling with custom cell renderer

Note:
Custom components  must be defined in the dashAgGridComponentFunctions.js in assets folder.
"""
#
# import json
# import dash_ag_grid as dag
# from dash import Dash, html, dcc, Input, Output
# import pandas as pd
# import dash_bootstrap_components as dbc
#
#
#
# data = {
#     "ticker": ["AAPL", "MSFT", "AMZN", "GOOGL"],
#     "company": ["Apple", "Microsoft", "Amazon", "Alphabet"],
#     "price": [154.99, 268.65, 100.47, 96.75],
#     "buy": ["Buy" for i in range(4)],
#     "color": ["Pick a Color" for _ in range(4)]
# }
# df = pd.DataFrame(data)
#
# columnDefs = [
#     {
#         "headerName": "Stock Ticker",
#         "field": "ticker",
#
#     },
#     {"headerName": "Company", "field": "company", "filter": True},
#     {
#         "headerName": "Last Close Price",
#         "type": "rightAligned",
#         "field": "price",
#         "valueFormatter": {"function": """d3.format("($,.2f")(params.value)"""},
#         "editable": True,
#         "cellEditor": {"function": "NumberInput"},
#         "cellEditorParams" : {"type": "number", "style": {"color": "red"}}
#     },
#     {
#         "field": "color",
#         "cellEditor": {"function": "NumberInput"},
#         "cellEditorParams": {"type": "color"},
#         "cellRenderer": "Color",
#         "editable": True,
#
#
#
#     },
#     {
#         "field": "buy",
#         "cellRenderer": "DBC_Button_Simple",
#         "cellRendererParams": {"color": "success"},
#
#     },
# ]
#
#
# defaultColDef = {
#     "resizable": True,
#     "sortable": True,
#     "editable": False,
# }
#
#
# grid = dag.AgGrid(
#     id="dbc-btn-simple-grid",
#     columnDefs=columnDefs,
#     rowData=df.to_dict("records"),
#     columnSize="autoSiz",
#     defaultColDef=defaultColDef,
#     dashGridOptions={"rowHeight": 48},
# )
#
#
# app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])
#
# app.layout = html.Div(
#     [
#         dcc.Markdown("Example of cellRenderer with custom dash-bootstrap-components Button "),
#         grid,
#         html.Div(id="dbc-btn-simple-value-changed"),
#     ],
#     style={"margin": 20},
# )
#
#
# @app.callback(
#     Output("dbc-btn-simple-value-changed", "children"),
#     Input("dbc-btn-simple-grid", "cellRendererData"),
# )
# def showChange(n):
#     return json.dumps(n)
#
#
# if __name__ == "__main__":
#     app.run_server(debug=True)
#

"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder

---------------

// Simple component to display cell value as a backgroundcolor - use with colorpicker cell editor
dagcomponentfuncs.Color = function (props) {
    return React.createElement(
        'div',
        {
            style: {
                width: '100%',
                height: '100%',
                padding: '5px',
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                backgroundColor: props.value,
            },
        },
        props.value
    );
};
----------------------------------



dagfuncs.NumberInput = class {

    // gets called once before the renderer is used
  init(params) {
    // create the cell
    this.eInput = document.createElement('input');
    this.eInput.value = params.value;
    this.eInput.style.height = 'var(--ag-row-height)';
    this.eInput.style.fontSize = 'calc(var(--ag-font-size) + 1px)';
    this.eInput.type = params.type
    this.eInput.style.width = '100%'
  }

  // gets called once when grid ready to insert the element
  getGui() {
    return this.eInput;
  }

  // focus and select can be done after the gui is attached
  afterGuiAttached() {
    this.eInput.focus();
    this.eInput.select();
  }

  // returns the new value after editing
  getValue() {
    return this.eInput.value;
  }

  // any cleanup we need to be done here
  destroy() {
    // but this example is simple, no cleanup, we could
    // even leave this method out as it's optional
  }

  // if true, then this editor will appear in a popup
  isPopup() {
    // and we could leave this method out also, false is the default
    return false;
  }

}



"""