from packaging.version import parse
import dash_ag_grid as dag


def test_vs001_versioning():
    """
    Test that the major and minor versions of bundled Ag Grid align with
    the major and minor versions of the Python package.

    See CONTRIBUTING.md for more information on versioning this package.
    """
    ag_version = parse(dag.grid_version)
    dash_ag_version = parse(dag.__version__)

    assert (
        ag_version.major == dash_ag_version.major
        and ag_version.minor == dash_ag_version.minor
    )
