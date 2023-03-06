import dash_ag_grid as dag
from dash import Dash, html, Input, Output
from . import utils
import json


def test_cc001_custom_components(dash_duo):

    app = Dash(__name__)

    data = [{
        "ticker": "AAPL",
        "company": "Apple",
        "price": 154.98500061035156,
        "volume": "Low",
        "binary": False,
        "buy": {"children":"buy", "className":"btn btn-success"},
        "sell": {"children":"sell", "className":"btn btn-danger"},
        "action": "buy"
    }]


    columnDefs = [
        {
            "headerName": "Stock Ticker",
            "field": "ticker",
            "cellRenderer": "stockLink",
            "tooltipField": "ticker",
        },
        {
            "headerName": "Company",
            "field": "company",
            "filter": True
        },
        {
            "headerName": "Last Close Price",
            "type": "rightAligned",
            "field": "price",
            "valueFormatter": {"function":"""d3.format("($,.2f")(params.value)"""},
            "editable":True
        },
        {
            "headerName": "Volume",
            "type": "rightAligned",
            "field": "volume",
            "cellRenderer": "tags",
            "editable":True
        },
        {
            "field":"binary",
            "cellRenderer": "checkbox",
        },
        {
            "field": "buy",
            "cellRenderer": "myCustomButton"
        },
        {
            "field": "sell",
            "cellRenderer": "myCustomButton"
        },
        {
            "field":"action",
            "cellRenderer": "customDropdown",
            'cellEditorParams': {
                        'values': ["buy", "sell", "hold"],
                    }
        }
    ]


    defaultColDef = {
        "filter": "agNumberColumnFilter",
        "resizable": True,
        "sortable": True,
        "editable": False,
        "tooltipComponent": "myCustomTooltip"
    }



    table = dag.AgGrid(
        id="portfolio-grid",
        className="ag-theme-alpine-dark",
        columnDefs=columnDefs,
        rowData=data,
        columnSize="sizeToFit",
        defaultColDef=defaultColDef,
    )


    app.layout = html.Div([table,
            html.Div(id='cellValueChanged')
        ],
    )

    @app.callback(Output('cellValueChanged', 'children'), Input('portfolio-grid','cellValueChanged'), prevent_initial_call=True)
    def showChange(n):
        return json.dumps(n)

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "portfolio-grid")

    grid.wait_for_cell_text(0, 1, "Apple")

    ### testing components
    assert grid.get_cell_html(0,0).strip() == """<a href="https://finance.yahoo.com/quote/AAPL" target="AAPL">AAPL</a>"""
    assert grid.get_cell_html(0,
                              3).strip() == """<div style="width: 100%; height: 100%; padding: 5px; display: flex; justify-content: center; align-items: center;"><div style="background-color: red; border-radius: 15px;">Low</div></div>"""
    assert grid.get_cell_html(0,
                              4).strip() == """<div style="width: 100%; height: 100%; padding: 5px; display: flex; justify-content: center; align-items: center;"><input type="checkbox" style="cursor: pointer;"></div>"""
    assert grid.get_cell_html(0,
                              5).strip() == """<div style="width: 100%; height: 100%; padding: 5px; display: flex; justify-content: center; align-items: center;"><button class="btn btn-success">buy</button></div>"""
    assert grid.get_cell_html(0,
                              6).strip() == """<div style="width: 100%; height: 100%; padding: 5px; display: flex; justify-content: center; align-items: center;"><button class="btn btn-danger">sell</button></div>"""
    assert grid.get_cell_html(0,
                             7).strip() == """<div style="width: 100%; height: 100%; padding: 5px; display: flex; justify-content: center; align-items: center;"><select><option>buy</option><option>sell</option><option>hold</option></select></div>"""
    grid.element_click_cell_button(0,6)
    dash_duo.wait_for_text_to_equal("#cellValueChanged", '{"rowIndex": 0, "nodeId": "0", "data": {"ticker": '
                                                                '"AAPL", "company": "Apple", "price": 154.98500061035'
                                                                '156, "volume": "Low", "binary": false, "buy": {"child'
                                                                'ren": "buy", "className": "btn btn-success"}, "sell":'
                                                                ' {"children": "sell", "className": "btn btn-danger", '
                                                                '"n_clicks": null}, "action": "sell"}, "oldValue": "bu'
                                                                'y", "newValue": "sell", "colId": "action"}')