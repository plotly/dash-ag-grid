import dash_ag_grid as dag
from dash import Dash, html, dcc
from . import utils
from dash.testing.wait import until
import pandas as pd
import time


def test_ce001_custom_cell_editor(dash_duo):
    rowData = [
        {"date": "2023-01-01"},
        {"date": "2023-02-11"},
        {"date": "2023-06-10"},
        {"date": "2023-11-04"},
        {"date": "2023-21-03"},
    ]

    # function to create a date object from  a date string "YYYY-MM-DD"
    date_obj = "d3.timeParse('%Y-%m-%d')(params.data.date)"

    columnDefs = [
        {"field": "date", "cellEditor": {"function": "DatePicker"}},
        {
            "headerName": "MM/DD/YYYY",
            "valueGetter": {"function": date_obj},
            "valueFormatter": {"function": f"d3.timeFormat('%m/%d/%Y')({date_obj})"},
        },
        {
            "headerName": "Mon DD, YYYY",
            "valueGetter": {"function": date_obj},
            "valueFormatter": {"function": f"d3.timeFormat('%b %d, %Y')({date_obj})"},
        },
        {
            "headerName": "day, Mon DD, YYYY",
            "valueGetter": {"function": date_obj},
            "valueFormatter": {
                "function": f"d3.timeFormat('%a %b %d, %Y')({date_obj})"
            },
        },
        {
            "headerName": "Month d, YYYY",
            "valueGetter": {"function": date_obj},
            "valueFormatter": {"function": f"d3.timeFormat('%B %e, %Y')({date_obj})"},
        },
        {
            "headerName": "MM-DD-YY",
            "valueGetter": {"function": date_obj},
            "valueFormatter": {"function": f"d3.timeFormat('%m-%d-%y')({date_obj})"},
        },
    ]

    defaultColDef = {
        "filter": "agDateColumnFilter",
        "filterParams": {
            "buttons": ["clear", "apply"],
        },
        "sortable": True,
        "editable": True,
    }

    app = Dash(
        __name__,
        external_scripts=[
            "https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.1/jquery.min.js",
            "https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js",
        ],
        external_stylesheets=[
            "https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.css"
        ],
    )

    app.layout = html.Div(
        [
            dcc.Markdown("Date formatting example."),
            dag.AgGrid(
                columnDefs=columnDefs,
                rowData=rowData,
                defaultColDef=defaultColDef,
                id="grid",
            ),
        ],
        style={"margin": 20},
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "2023-01-01")

    ### testing animations
    action = utils.ActionChains(dash_duo.driver)
    action.double_click(grid.get_cell(0, 0)).perform()
    until(
        lambda: "January"
        in dash_duo.find_element(".ui-datepicker-month").get_attribute("innerText"),
        timeout=3,
    )
    until(
        lambda: "2023"
        in dash_duo.find_element(".ui-datepicker-year").get_attribute("innerText"),
        timeout=3,
    )
    until(
        lambda: "1"
        in dash_duo.find_element(".ui-state-active").get_attribute("innerText"),
        timeout=3,
    )

    # set date to 2023-01-11
    dash_duo.find_element(
        "#ui-datepicker-div .ui-datepicker-calendar >"
        " tbody > tr:nth-child(2) > td:nth-child(4) > a"
    ).click()
    grid.get_cell(1, 0).click()
    grid.wait_for_cell_text(0, 0, "2023-01-11")
