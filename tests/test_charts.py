import dash_ag_grid as dag
from dash import Dash, html
from . import utils


def _make_chart_grid(**extra_props):
    return dag.AgGrid(
        id="grid",
        columnDefs=[{"field": "make"}, {"field": "model"}, {"field": "price"}],
        rowData=[
            {"make": "Toyota", "model": "Celica", "price": 35000},
            {"make": "Ford", "model": "Mondeo", "price": 32000},
            {"make": "Porsche", "model": "Boxster", "price": 72000},
        ],
        **extra_props,
    )


def _make_basic_grid(**extra_props):
    return dag.AgGrid(
        id="grid",
        columnDefs=[{"field": "make"}, {"field": "model"}, {"field": "price"}],
        rowData=[
            {"make": "Toyota", "model": "Celica", "price": 35000},
            {"make": "Ford", "model": "Mondeo", "price": 32000},
            {"make": "Porsche", "model": "Boxster", "price": 72000},
        ],
        **extra_props,
    )


def test_charts001_enables_enterprise_charts_modules_with_true(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div(
        [_make_chart_grid(enableEnterpriseModules=True, dashEnableCharts=True)]
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")
    grid.wait_for_cell_text(0, 0, "Toyota")

    assert not any(
        "AG Grid: error #200" in entry.get("message", "")
        for entry in dash_duo.get_logs()
    )


def test_charts002_enables_enterprise_charts_modules(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div(
        [
            _make_chart_grid(
                enableEnterpriseModules=True,
                dashEnableCharts="enterprise",
            )
        ]
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")
    grid.wait_for_cell_text(0, 0, "Toyota")

    assert not any(
        "AG Grid: error #200" in entry.get("message", "")
        for entry in dash_duo.get_logs()
    )


def test_charts003_keeps_enterprise_grid_without_charts(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([_make_basic_grid(enableEnterpriseModules=True)])

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")
    grid.wait_for_cell_text(0, 0, "Toyota")


def test_charts004_rejects_charts_on_community_grid(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([_make_chart_grid(dashEnableCharts=True)])

    dash_duo.start_server(app)

    assert any(
        "dashEnableCharts is only supported when enableEnterpriseModules is true."
        in entry.get("message", "")
        for entry in dash_duo.get_logs()
    )


def test_charts005_rejects_enablecharts_without_dashenablecharts(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div(
        [_make_chart_grid(dashGridOptions={"enableCharts": True})]
    )

    dash_duo.start_server(app)

    assert any(
        "enableCharts is set, but chart modules are not loaded."
        in entry.get("message", "")
        for entry in dash_duo.get_logs()
    )


def test_charts006_rejects_conflicting_enablecharts_false(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div(
        [
            _make_chart_grid(
                enableEnterpriseModules=True,
                dashEnableCharts=True,
                dashGridOptions={"enableCharts": False},
            )
        ]
    )

    dash_duo.start_server(app)

    assert any(
        "dashEnableCharts cannot be combined with dashGridOptions.enableCharts=false."
        in entry.get("message", "")
        for entry in dash_duo.get_logs()
    )


def test_charts007_accepts_charts_license_key_prop(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div(
        [
            _make_chart_grid(
                enableEnterpriseModules=True,
                dashEnableCharts="enterprise",
                licenseKey="grid-key",
                chartsLicenseKey="charts-key",
            )
        ]
    )

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")
    grid.wait_for_cell_text(0, 0, "Toyota")
