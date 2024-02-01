import os as _os, json, re

_basepath = _os.path.dirname(__file__)
_filepath = _os.path.abspath(_os.path.join(_basepath, 'package.json'))
with open(_filepath) as f:
    package = json.load(f)


# grid version must be a valid locked version of the grid, to limit possible unexpected updates and breaking changes
errors = []
for pk in ['ag-grid-community', 'ag-grid-enterprise', 'ag-grid-react']:
    try:
        assert re.match("^\d+[.]\d+[.]\d+$", package['dependencies'][pk])
    except:
        errors.append(f"{pk} - {package['dependencies'][pk]}")
if errors:
    message = "not a valid version of AG-Grid; grid version must be a valid locked version of the grid," \
              " to limit possible unexpected updates and breaking changes\n"
    raise Exception(message + '\n'.join(errors))