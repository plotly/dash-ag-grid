# Dash AG Grid [![PyPi Version](https://img.shields.io/pypi/v/dash-ag-grid.svg)](https://pypi.org/project/dash-ag-grid/)

Dash AG Grid is a Dash component wrapper for the AG Grid JavaScript package, enabling you to display AG Grid components natively in your Dash app.

The underlying AG Grid JavaScript package is a third-party software component developed by [AG Grid Ltd](http://www.ag-grid.com/). Many features are available for free in the AG Grid [Community version](https://github.com/ag-grid/ag-grid). Some features require a paid subscription to the AG Grid Enterprise version ([more info available here](https://www.ag-grid.com/license-pricing.php)). Both the community and enterprise versions are included in this component, but the enterprise features require you to provide a valid AG Grid license key. The demos which use Enterprise features are clearly marked.

<div align="center">
  <a href="https://dash.plotly.com/project-maintenance">
    <img src="https://dash.plotly.com/assets/images/maintained-by-plotly.png" width="400px" alt="Maintained by Plotly">
  </a>
</div>


### Documentation
Please see the [Plotly Dash AG Grid Documentation](https://dash.plotly.com/dash-ag-grid).

### Quick Start

`pip install dash-ag-grid`

This basic grid has the following features enabled by default:
- Alpine theme
- Sort
- Resize, reorder and pin columns
- Boolean values rendered as check boxes
- Row animation on sort

```python

import dash_ag_grid as dag
from dash import Dash
import pandas as pd

app = Dash()

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/space-mission-data.csv")

app.layout = dag.AgGrid(
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
)

app.run(debug=True)
```

<img src="https://github.com/AnnMarieW/dash-ag-grid-examples/assets/72614349/74fe86e1-eb54-4dec-915f-d692f2c8cead" width="1000"/>


### AG Grid Community Features
Here are a few of the AG Grid Community features available:

- Column Interactions (resize, reorder, and pin columns)
- Column Spanning
- Column Grouping
- Pagination
- Sorting
- Row Selection
- Row Reordering
- Row Spanning
- Pinned Rows
- Full Width Rows

- Cell data types with automatic type inference
- Custom Filtering
- Cell Editing

- Provided components including number editors, date picker, select editor, text editor, large text editor
- Custom Components in cells - add your own components such as buttons, graphs, indicators, markdown and more
- Tooltips in cells and headers

- Provided themes with light/dark versions
- Customizable themes
- Figma Design System to design and customize themes

- Format Cell Data
- Conditional formatting

- Data Export to CSV
- Keyboard Navigation
- Accessibility support
- Localization



### AG Grid Enterprise features
Here are a few of the features available in AG Grid Enterprise.  See the AG Grid docs for more information.

- Grouping / Aggregation 
- Advanced Filtering
- Records Lazy Loading 
- Server-Side Records Operations 
- Hierarchical Data Support & Tree View 
- Data Export to Excel 
- Excel-like Pivoting 
- Copy / Paste
- Sparklines

### See a [live demo](https://www.ag-grid.com/example/) of AG Grid Community and Enterprise Features

---------



<img src="https://github.com/AnnMarieW/dash-ag-grid-examples/assets/72614349/0c7319e4-0ebd-437a-bbdc-1091ec7ae325" width="1000"/>

### Contributing 

We welcome contributions to `dash-ag-grid`.  Please see our [contributing guide](https://github.com/plotly/dash-ag-grid/blob/main/CONTRIBUTING.md) for more information.

