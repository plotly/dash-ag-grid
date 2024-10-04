from packaging.version import parse
import dash_ag_grid as dag


"""
Test that the major and minor versions of bundled Ag Grid align with
the major and minor versions of the Python package.

See CONTRIBUTING.md for more information on versioning this package.
"""
ag_version = parse(dag.grid_version)
dash_ag_version = parse(dag.__version__)

if not (ag_version.major == dash_ag_version.major and ag_version.minor == dash_ag_version.minor):
    raise Exception("There is a version mismatch in DAG and AG-Grid, check your package.json and adjust")
try:
    print('DAG version and AG-Grid are in perfect harmony 🎉')
except:
    print('DAG version and AG-Grid are in perfect harmony :)')