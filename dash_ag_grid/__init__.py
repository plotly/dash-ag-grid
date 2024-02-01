from __future__ import print_function as _

import os as _os
import sys as _sys
import json

import dash as _dash

# noinspection PyUnresolvedReferences
from ._imports_ import *
from ._imports_ import __all__

if not hasattr(_dash, '__plotly_dash') and not hasattr(_dash, 'development'):
    print('Dash was not successfully imported. '
          'Make sure you don\'t have a file '
          'named \n"dash.py" in your current directory.', file=_sys.stderr)
    _sys.exit(1)

_basepath = _os.path.dirname(__file__)
_filepath = _os.path.abspath(_os.path.join(_basepath, 'package-info.json'))
with open(_filepath) as f:
    package = json.load(f)

package_name = package['name'].replace(' ', '_').replace('-', '_')
__version__ = package['version']
grid_version = package['dependencies']['ag-grid-community']

_current_path = _os.path.dirname(_os.path.abspath(__file__))

_this_module = _sys.modules[__name__]

_unpkg = f'https://unpkg.com/dash-ag-grid@{__version__}/dash_ag_grid/'

_js_dist = [
    {
        'relative_package_path': 'dash_ag_grid.min.js',
        'external_url': f'{_unpkg}dash_ag_grid.min.js',
        'namespace': package_name
    },
    {
        'relative_package_path': 'dash_ag_grid.min.js.map',
        'namespace': package_name,
        'external_url': f'{_unpkg}dash_ag_grid.min.js.map',
        'dynamic': True
    },
    {
        'relative_package_path': 'async-community.js',
        'namespace': package_name,
        'external_url': f'{_unpkg}async-community.js',
        'async': True
    },
    {
        'relative_package_path': 'async-community.js.map',
        'namespace': package_name,
        'external_url': f'{_unpkg}async-community.js.map',
        'dynamic': True
    },
    {
        'relative_package_path': 'async-enterprise.js',
        'namespace': package_name,
        'external_url': f'{_unpkg}async-enterprise.js',
        'async': True
    },
    {
        'relative_package_path': 'async-enterprise.js.map',
        'namespace': package_name,
        'external_url': f'{_unpkg}async-enterprise.js.map',
        'dynamic': True
    },
]

_css_dist = []


for _component in __all__:
    setattr(locals()[_component], '_js_dist', _js_dist)
    setattr(locals()[_component], '_css_dist', _css_dist)
