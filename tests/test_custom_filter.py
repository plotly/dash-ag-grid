from dash import Dash, html
import dash_ag_grid as dag
import plotly.express as px
import pandas as pd

from . import utils

df = px.data.election()
default_display_cols = ["district_id"]
other_cols = ["district", "winner"]

df = pd.concat([df, pd.DataFrame({"district": ["test"]})])


def test_fi002_custom_filter(dash_duo):
    app = Dash(__name__)

    app.layout = html.Div(
        [
            dag.AgGrid(
                id="grid",
                rowData=df.to_dict("records"),
                columnDefs=[
                               {
                                   "headerName": col.capitalize(),
                                   "field": col,
                                   "filterParams": {"function": "filterParams()"},
                                   "filter": "agNumberColumnFilter",
                               }
                               for col in default_display_cols
                           ] + [
                               {
                                   "headerName": col.capitalize(),
                                   "field": col,
                                   "filterParams": {
                                       "filterOptions": ["contains", "startsWith", "endsWith"],
                                       "defaultOption": "endsWith",
                                   },
                                   "filter": True,
                               }
                               for col in other_cols
                           ],
                defaultColDef={"floatingFilter": True},
            )
        ]
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 1, "101-Bois-de-Liesse")

    grid.set_filter(0, "12")

    grid.wait_for_cell_text(0, 1, "11-Sault-au-Récollet")
    grid.wait_for_rendered_rows(2)

    grid.set_filter(0, "")
    grid.wait_for_cell_text(0, 1, "101-Bois-de-Liesse")

    grid.set_filter(1, "t")
    grid.set_filter(2, "e")
    grid.wait_for_cell_text(0, 1, "11-Sault-au-Récollet")
    grid.wait_for_rendered_rows(8)


def test_fi003_custom_filter(dash_duo):
    app = Dash(__name__)

    df = pd.read_json('https://www.ag-grid.com/example-assets/olympic-winners.json', convert_dates=False)

    rowData = df.to_dict('records')

    columnDefs = [
        {'field': 'age', 'filter': 'agNumberColumnFilter'},
        {'field': 'country', 'minWidth': 150},
        {'field': 'year', 'filter': {'function': 'YearFilter'}},
        {
            'field': 'date',
            'minWidth': 130,
            'filter': 'agDateColumnFilter',
        },
        {'field': 'sport'},
        {'field': 'gold', 'filter': 'agNumberColumnFilter'},
        {'field': 'silver', 'filter': 'agNumberColumnFilter'},
        {'field': 'bronze', 'filter': 'agNumberColumnFilter'},
        {'field': 'total', 'filter': 'agNumberColumnFilter'},
    ]

    defaultColDef = {
        'editable': True,
        'sortable': True,
        'flex': 1,
        'minWidth': 100,
        'filter': True,
        'resizable': True,
    }

    app.layout = html.Div(
        [
            dag.AgGrid(
                id="grid",
                columnDefs=columnDefs,
                rowData=rowData,
                defaultColDef=defaultColDef
            ),
        ]
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "23")

    dash_duo.find_element('.ag-header-cell[aria-colindex="3"] span[data-ref="eFilterButton"]').click()

    dash_duo.find_element('.ag-filter label:nth-child(2)').click()

    grid.wait_for_cell_text(0, 0, "27")

    dash_duo.find_element('.ag-filter label:nth-child(1)').click()

    grid.wait_for_cell_text(0, 0, "23")


# test filterParams.textFormatter, filterParams.textMatcher and filterParams.filterOptions.predicate functions
def test_fi004_custom_filter(dash_duo):
    app = Dash(__name__)

    df = pd.read_json('https://www.ag-grid.com/example-assets/olympic-winners.json', convert_dates=False)

    columnDefs = [
        {
            "field": "athlete",
            "filterParams": {"textFormatter": {"function": "myTextFormatter(params)"}},
        },
        {
            "field": "country",
            "filterParams": {"textMatcher": {"function": "myTextMatcher(params)"}},
        },
        {
            "field": "athlete",
            "filterParams": {
                "filterOptions": [
                    {
                        "displayKey": 'nameStartsWith',
                        "displayName": 'Name starts with',
                        "predicate": {"function": "startWith"},
                        "numberOfInputs": 1,
                    },
                ],
            },
        },
    ]

    app.layout = html.Div(
        [
            dag.AgGrid(
                id="grid",
                rowData=df.to_dict("records"),
                columnDefs=columnDefs,
                columnSize="sizeToFit",
                defaultColDef={"filter": True, "floatingFilter": True}
            ),
        ]
    )

    dash_duo.start_server(app)
    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Michael Phelps")

    # Test textFormatter
    grid.set_filter(0, "bjo")
    grid.wait_for_cell_text(0, 0, "Björn Lind")

    # Remove filter
    grid.set_filter(0, "")
    grid.wait_for_cell_text(0, 0, "Michael Phelps")

    # Test textMatcher
    grid.set_filter(1, "sean")
    grid.wait_for_cell_text(0, 1, "South Africa")

    # Remove filter
    grid.set_filter(1, "")
    grid.wait_for_cell_text(0, 0, "Michael Phelps")

    # Test filterOptions
    grid.set_filter(2, "c")
    grid.wait_for_cell_text(0, 2, "Natalie Coughlin")


# test numberParser and numberFormatter functions in filterParams
def test_fi005_custom_filter(dash_duo):
    app = Dash(__name__)

    rowData = [{"sale": (i - 3) * 100} for i in range(50)]

    columnDefs = [
        {
            "field": "sale",
            "headerName": "Sale",
            "filter": "agNumberColumnFilter",
            "filterParams": {
                "filterOptions": ["greaterThan"],
                "allowedCharPattern": "\\d\\-\\,\\$",
                "numberParser": {"function": "myNumberParser(params)"},
                "numberFormatter": {"function": "myNumberFormatter(params)"},
            },
            "valueFormatter": {
                "function": "d3.formatLocale({'decimal': ',', 'thousands': '.', 'currency': ['$', '']}).format('$,.2f')(params.value)"
            },
        },
    ]

    app.layout = html.Div(
        [
            dag.AgGrid(
                id="grid",
                columnDefs=columnDefs,
                defaultColDef={"floatingFilter": True},
                rowData=rowData,
                columnSize="sizeToFit",
            ),
        ]
    )

    dash_duo.start_server(app)
    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "−$300,00")

    # Test numberParser and numberFormatter
    grid.set_filter(0, "$100,5")
    grid.wait_for_cell_text(0, 0, "$200,00")

def test_fi006_custom_filter(dash_duo):
    app = Dash(__name__)

    df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
    )

    columnDefs = [
        {"field": "athlete",
        "filter": "agMultiColumnFilter",
                "filterParams": {
                    "filters": [
                        {"filter": "agTextColumnFilter"},
                        {"filter": "agSetColumnFilter"} # Example with Set Filter
                    ]
                }},
        {"field": "country"},
        {
            "field": "date",
            "filter": "agMultiColumnFilter",
            "filterParams": {
                "filters": [
                    {
                        "filter": "agSetColumnFilter",
                        'filterParams': {'excelMode': 'windows', 'buttons': ['apply', 'reset'],
                        }
                    },
                    {
                        "filter": "agDateColumnFilter",
                        'filterParams': {
                            'excelMode': 'windows',
                            'buttons': ['apply', 'reset'],
                            'comparator': {'function': 'dateFilterComparator'},
                        }
                    },
                ],

            },
        },
    ]


    app.layout = html.Div(
        [
            dag.AgGrid(
                id="date-filter-example",
                enableEnterpriseModules=True,
                columnDefs=columnDefs,
                rowData=df.to_dict("records"),
                defaultColDef={"flex": 1, "minWidth": 150, "floatingFilter": True},
                dashGridOptions={"animateRows": False}
            ),
        ],
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "date-filter-example")

    grid.wait_for_cell_text(0, 0, "Michael Phelps")

    # Test Set Filter - click filter button on date column
    dash_duo.find_element('.ag-floating-filter[aria-colindex="3"] button').click()

    # Uncheck "Select All"
    dash_duo.find_element('.ag-set-filter-list .ag-set-filter-item .ag-checkbox-input').click()

    # Select "24/08/2008"
    dash_duo.wait_for_element('.ag-set-filter-list .ag-virtual-list-item', timeout=10)
    set_filter_items = dash_duo.find_elements('.ag-set-filter-list .ag-virtual-list-item')
    checkboxes = dash_duo.find_elements('.ag-set-filter-list .ag-virtual-list-item .ag-checkbox-input')

    for i, item in enumerate(set_filter_items):
        if "24/08/2008" in item.text:
            checkboxes[i].click()
            break

    # Apply
    dash_duo.find_element('button[data-ref="applyFilterButton"]').click()
    grid.wait_for_cell_text(0, 2, "24/08/2008")

    # Reset
    dash_duo.find_element('.ag-floating-filter[aria-colindex="3"] button').click()
    dash_duo.find_element('button[data-ref="resetFilterButton"]').click()

    # Test Date Filter - click filter button again
    dash_duo.find_element('.ag-floating-filter[aria-colindex="3"] button').click()

    # Type date
    date_input = dash_duo.find_element('.ag-filter-wrapper .ag-date-filter input[class="ag-input-field-input ag-text-field-input"]')
    date_input.click()
    date_input.send_keys("08/24/2008")

    # Apply
    apply_buttons = dash_duo.find_elements('button[data-ref="applyFilterButton"]')
    apply_buttons[1].click()
    grid.wait_for_cell_text(0, 2, "24/08/2008")