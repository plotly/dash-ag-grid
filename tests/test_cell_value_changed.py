import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px
from . import utils

df = px.data.medals_wide()

columnDefs = []
for i in df.columns:
    if i == "nation":
        columnDefs.append({"field": i, "editable": False})
    else:
        columnDefs.append({"field": i})


def test_cv001_cell_value_changed(dash_duo):
    app = Dash(__name__)

    app.layout = html.Div(
        [
            dag.AgGrid(
                columnDefs=columnDefs,
                rowData=df.to_dict("records"),
                columnSize="sizeToFit",
                defaultColDef={"editable": True},
                id="information",
                getRowId="params.data.nation",
            ),
            dag.AgGrid(
                id="history",
                columnDefs=[{"field": "Key", "checkboxSelection": True}]
                           + [{"field": i} for i in ["Column", "OldValue", "NewValue"]],
                rowData=[],
            ),
        ],
        style={"margin": 20},
    )

    app.clientside_callback(
        """function (n){if (n) {return true} return window.dash_clientside.no_update}""",
        Output("show_history", "is_open"),
        Input("viewHistory", "n_clicks"),
    )

    app.clientside_callback(
        """function addToHistory(changes) {
            if (changes) {
                newData = []
                for (let i = 0; i < changes.length; i++) {
                    data = changes[i];
                    reloadData = {...data.data};
                    reloadData[data.colId] = data.oldValue;
                    newData.push({Key: data.rowId, Column: data.colId, OldValue: data.oldValue, 
                    NewValue: data.value, reloadData});
                }
                return {'add': newData}
            }
            return window.dash_clientside.no_update
        }""",
        Output("history", "rowTransaction"),
        Input("information", "cellValueChanged"),
        prevent_initial_call=True,
    )

    app.clientside_callback(
        """function reloadHistory(data) {
            if (data.length) {
                return [{'update': [data[0].reloadData], 'async': false}, {'remove': [data[0]], 'async': false}]
            }
            return [null]*2
        }""",
        Output("information", "rowTransaction"),
        Output("history", "rowTransaction", allow_duplicate=True),
        Input("history", "selectedRows"),
        prevent_initial_call=True,
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "information")
    hist = utils.Grid(dash_duo, "history")

    grid.wait_for_cell_text(0, 0, "South Korea")

    ### testing history
    grid.get_cell(0, 1).send_keys("50")
    grid.get_cell(1, 2).click()

    hist.wait_for_rendered_rows(1)

    hist.element_click_cell_checkbox(0, 0)
    hist.wait_for_rendered_rows(0)

    grid.get_cell(0, 1).send_keys("50")
    grid.get_cell(1, 2).click()

    hist.wait_for_rendered_rows(1)

    ## twice for good measure
    hist.element_click_cell_checkbox(0, 0)
    hist.wait_for_rendered_rows(0)

    grid.get_cell(0, 1).send_keys("50")
    grid.get_cell(1, 2).click()

    hist.wait_for_rendered_rows(1)


def test_cv001_cell_value_changed_multi(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div(
        [
            dag.AgGrid(
                columnDefs=columnDefs,
                rowData=df.to_dict("records"),
                columnSize="sizeToFit",
                defaultColDef={"editable": True},
                id="grid",
                getRowId="params.data.nation",
                dashGridOptions={'editType':'fullRow'}
            ),
            html.Div(id="log")
        ]
    )

    app.clientside_callback(
        """function countEvents(changes) {
            console.log("FIRE");
            return changes? changes.length : 0;
        }""",
        Output("log", "children"),
        Input("grid", "cellValueChanged"),
        prevent_initial_call=True,
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")
    grid.wait_for_cell_text(0, 0, "South Korea")

    # Test single event.
    grid.get_cell(0, 1).send_keys("50")
    grid.get_cell(1, 2).click()
    dash_duo.wait_for_text_to_equal('#log', "1")

    # Test multi event.
    grid.get_cell(0, 1).send_keys("20")
    grid.get_cell_editing_input(0, 2).send_keys("20")
    grid.get_cell(1, 2).click()
    dash_duo.wait_for_text_to_equal('#log', "2")
