import dash_ag_grid

def test_gv001_grid_version():
    assert dash_ag_grid.grid_version == dash_ag_grid.package['dependencies']['ag-grid-community']