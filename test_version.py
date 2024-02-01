import os as _os, json

_basepath = _os.path.dirname(__file__)
_filepath = _os.path.abspath(_os.path.join(_basepath, 'package.json'))
with open(_filepath) as f:
    package = json.load(f)

grid_version = package['dependencies']['ag-grid-community']
# grid version must be a valid locked version of the grid, to limit possible unexpected updates and breaking changes

try:
    if int(grid_version[0]) > 0:
        pass
except:
    print("not a valid version of AG-Grid; grid version must be a valid locked version of the grid, to limit possible unexpected updates and breaking changes")
    raise