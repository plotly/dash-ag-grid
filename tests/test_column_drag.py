from dash import Dash, html, Output, Input, no_update
from dash_ag_grid import AgGrid
import plotly.express as px
import pandas as pd

from . import utils


df = px.data.election()
default_display_cols = ["district_id", "district", "winner"]


def test_cd001_drag_columns(dash_duo):
    app = Dash()
    app.layout = html.Div([
        AgGrid(
            id="grid",
            rowData=df.to_dict("records"),
            columnDefs=[
                {"headerName": col.capitalize(), "field": col}
                for col in default_display_cols
            ],
        )
    ])

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_all_header_texts(["District_id", "District", "Winner"])
    grid.wait_for_pinned_cols(0)
    grid.wait_for_viewport_cols(3)

    grid.drag_col(2, 0)  # last column first but not pinned

    grid.wait_for_all_header_texts(["Winner", "District_id", "District"])
    grid.wait_for_pinned_cols(0)
    grid.wait_for_viewport_cols(3)

    grid.pin_col(1)  # middle column pinned

    grid.wait_for_all_header_texts(["District_id", "Winner", "District"])
    grid.wait_for_pinned_cols(1)
    grid.wait_for_viewport_cols(2)

    # pin first non-pinned column by dragging it to its own left edge
    grid.pin_col(1, 1)

    grid.wait_for_all_header_texts(["District_id", "Winner", "District"])
    grid.wait_for_pinned_cols(2)
    grid.wait_for_viewport_cols(1)

def test_cd002_column_drag(dash_duo):
    data = {
        "ticker": ["AAPL", "MSFT", "AMZN", "GOOGL"],
        "company": ["Apple", "Microsoft", "Amazon", "Alphabet"],
        "price": [154.99, 268.65, 100.47, 96.75],
        "buy": ["Buy" for _ in range(4)],
        "sell": ["Sell" for _ in range(4)],
        "watch": ["Watch" for _ in range(4)],
    }
    df = pd.DataFrame(data)

    columnDefs = [
        {
            "headerName": "Stock Ticker",
            "field": "ticker",
        },
        {"headerName": "Company", "field": "company", "filter": True},
        {
            "headerName": "Last Close Price",
            "type": "rightAligned",
            "field": "price",
            "valueFormatter": {"function": """d3.format("($,.2f")(params.value)"""},
        },
    ]

    defaultColDef = {
        "resizable": True,
        "sortable": True,
        "editable": False,
    }

    grid = AgGrid(
        id="topGrid",
        columnDefs=columnDefs,
        rowData=df.to_dict("records"),
        columnSize="autoSize",
        defaultColDef=defaultColDef,
        dashGridOptions={'alignedGrids': ['middleGrid', 'bottomGrid']}
    )
    grid2 = AgGrid(
        id="middleGrid",
        columnDefs=columnDefs,
        rowData=df.to_dict("records"),
        columnSize="autoSize",
        defaultColDef=defaultColDef,
        dashGridOptions={'alignedGrids':'bottomGrid'}
    )
    gridBot = AgGrid(
        id="bottomGrid",
        columnDefs=columnDefs,
        rowData=df.to_dict("records"),
        columnSize="autoSize",
        defaultColDef=defaultColDef,
    )

    app = Dash(__name__)

    app.layout = html.Div(
        [
            grid,
            grid2,
            gridBot,
            html.Button(id='link')
        ],
        style={"margin": 20},
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "topGrid")
    midGrid = utils.Grid(dash_duo, "middleGrid")
    botGrid = utils.Grid(dash_duo, "bottomGrid")

    grid.wait_for_all_header_texts(["Stock Ticker", "Company", "Last Close Price"])
    botGrid.wait_for_all_header_texts(["Stock Ticker", "Company", "Last Close Price"])
    grid.wait_for_pinned_cols(0)
    grid.wait_for_viewport_cols(3)
    botGrid.wait_for_pinned_cols(0)
    botGrid.wait_for_viewport_cols(3)

    grid.drag_col(2, 0)  # last column first but not pinned

    grid.wait_for_all_header_texts(["Last Close Price", "Stock Ticker", "Company"])
    botGrid.wait_for_all_header_texts(["Last Close Price", "Stock Ticker", "Company"])
    grid.wait_for_pinned_cols(0)
    grid.wait_for_viewport_cols(3)
    botGrid.wait_for_pinned_cols(0)
    botGrid.wait_for_viewport_cols(3)

    grid.pin_col(1)  # middle column pinned

    grid.wait_for_all_header_texts(["Stock Ticker", "Last Close Price", "Company"])
    botGrid.wait_for_all_header_texts(["Stock Ticker", "Last Close Price", "Company"])
    grid.wait_for_pinned_cols(1)
    botGrid.wait_for_pinned_cols(1)
    grid.wait_for_viewport_cols(2)
    botGrid.wait_for_viewport_cols(2)

    # pin first non-pinned column by dragging it to its own left edge
    grid.pin_col(1, 1)

    grid.wait_for_all_header_texts(["Stock Ticker", "Last Close Price", "Company"])
    botGrid.wait_for_all_header_texts(["Stock Ticker", "Last Close Price", "Company"])
    grid.wait_for_pinned_cols(2)
    grid.wait_for_viewport_cols(1)
    botGrid.wait_for_pinned_cols(2)
    botGrid.wait_for_viewport_cols(1)

    # pin first non-pinned column by dragging it to its own left edge
    midGrid.pin_col(2, 2)

    grid.wait_for_all_header_texts(["Stock Ticker", "Last Close Price", "Company"])
    botGrid.wait_for_all_header_texts(["Stock Ticker", "Last Close Price", "Company"])
    grid.wait_for_pinned_cols(2)
    grid.wait_for_viewport_cols(1)
    botGrid.wait_for_pinned_cols(3)
    botGrid.wait_for_viewport_cols(0)