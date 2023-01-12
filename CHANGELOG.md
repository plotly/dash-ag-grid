# Change Log for Dash AG Grid

All notable changes to `dash-ag-grid` will be documented in this file.
This project adheres to [Semantic Versioning](https://semver.org/).

## [1.3.1] - 2022-05-05

### Fixed

- [#129](https://github.com/plotly/dash-ag-grid/pull/129) Rebuild with latest dash component generator for Py3.6 compatibility

## [1.3.0] - 2022-05-03

### Removed

- [#126](https://github.com/plotly/dash-ag-grid/pull/126) AG Grid v27 drops support for IE11

### Updated

- [#126](https://github.com/plotly/dash-ag-grid/pull/126) Update AG Grid to v27.2.1.

### Added

- [#125](https://github.com/plotly/dash-ag-grid/pull/125) Enable sparklines
- [#124](https://github.com/plotly/dash-ag-grid/pull/124) Add Sidebar support
- [#87](https://github.com/plotly/dash-ag-grid/pull/87) Add `virtualRowData` for accessing filtered data

### Fixed

- [#105](https://github.com/plotly/dash-ag-grid/pull/105) and [#108](https://github.com/plotly/dash-ag-grid/pull/108) Update column widths when table is resized or a callback changes `columnDefs`.
- [#96](https://github.com/plotly/dash-ag-grid/pull/96) Persist filters when `rowData` changes
- [#90](https://github.com/plotly/dash-ag-grid/pull/90) and [#86](https://github.com/plotly/dash-ag-grid/pull/86) Improved selections algorithm
- [#88](https://github.com/plotly/dash-ag-grid/pull/88) Persist row groupings when `rowData` changes

## [1.2.1] - 2021-11-23

- Selections fixes by @ndrezn in [#78](https://github.com/plotly/dash-ag-grid/pull/78)
- Add 2.0 support by @ndrezn in [#82](https://github.com/plotly/dash-ag-grid/pull/82)
- Request & response for master detail by @ndrezn in [#79](https://github.com/plotly/dash-ag-grid/pull/79)
- Update look of docs

## [1.2.0] - 2021-10-27

- [#72](https://github.com/plotly/dash-ag-grid/pull/72): Support for master/detail grid https://www.ag-grid.com/javascript-data-grid/master-detail/

## [1.1.2] - 2021-10-16

- [#69](https://github.com/plotly/dash-ag-grid/pull/69): Improve support for persistence with `selectionChanged`.

## [1.1.1] - 2021-09-21

- Fix issue with `selectionChanged` write support

## [1.1.0] - 2021-09-21

- Adds support for `persistence`
- Adds support for exporting data as `CSV`/`excel`
- Adds support for column reset

## [1.0.0] - 2021-06-01

This release is as `v1.0.0` as it indicates production-ready, and changes the API for infinite scroll.

### Fixed

-   [#47](https://github.com/plotly/dash-ag-grid/pull/47) Fix issues with infinite scroll support

## [0.2.0] - 2021-05-21

### Added

-   [#43](https://github.com/plotly/dash-ag-grid/pull/43) Add row menus support
-   [#42](https://github.com/plotly/dash-ag-grid/pull/43) Add support for DDK theming
-   [#38](https://github.com/plotly/dash-ag-grid/pull/38) Add Markdown support

### Changed

-   [#37](https://github.com/plotly/dash-ag-grid/pull/37) Remove build artifacts from tracking
-   [#45](https://github.com/plotly/dash-ag-grid/pull/45) Make download link a `dcc.Download` component in docs

## [0.1.0] - 2021-05-03

### Added

-   [#28](https://github.com/plotly/dash-ag-grid/pull/28) Add cell styling support

### Changed

-   [#31](https://github.com/plotly/dash-ag-grid/pull/31) Allow users to pass in Enterprise key and control whether Enterprise or Community modules are enabled
-   [#30](https://github.com/plotly/dash-ag-grid/pull/30) New demo illustrating how to generate a popup from a table
-   [#29](https://github.com/plotly/dash-ag-grid/pull/29) New demo illustrating how to download the dataset from a grid as a CSV file
-   [#27](https://github.com/plotly/dash-ag-grid/pull/27) Use DDK and GDWC for demo app

## [0.0.1] - 2021-04-12

## Added

-   [#8](https://github.com/plotly/dash-ag-grid/pull/8) Add support for selections
-   [#9](https://github.com/plotly/dash-ag-grid/pull/9) Add support for checkboxes
-   [#11](https://github.com/plotly/dash-ag-grid/pull/11) Improve editing support
-   [#14](https://github.com/plotly/dash-ag-grid/pull/14) Autosizing for columns
-   [#16](https://github.com/plotly/dash-ag-grid/pull/16) Infinite scroll support
-   [#19](https://github.com/plotly/dash-ag-grid/pull/19) Add API demo/documentation

## Changed

-   [#7](https://github.com/plotly/dash-ag-grid/pull/7) Fix start script to run locally
-   [#15](https://github.com/plotly/dash-ag-grid/pull/15) Style property
-   [#20](https://github.com/plotly/dash-ag-grid/pull/20) Default to ag-grid Enterprise
