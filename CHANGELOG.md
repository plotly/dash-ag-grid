# Change Log for Dash AG Grid

All notable changes to `dash-ag-grid` will be documented in this file.
This project adheres to [Semantic Versioning](https://semver.org/).
Links "DE#nnn" prior to version 2.0 point to the Dash Enterprise closed-source Dash AG Grid repo

## [2.0.0]

### Removed

### Added

### Updated

### Fixed

## [Unreleased] - 2023-01-23
_More additional functions and security measures_:
- allowing for strings of functions to be passed as parameters to `valueGetterFunction`, `valueFormatterFunction`
  - this allows for functions to be parsed even when the app is completely locked down, (meta tags, etc)
- added row conditional formatting via `getRowStyle` acts similar to `cellStyles`
- added ability for custom parsing functions to be passed via the namespace `window.dashAgGridFunctions`
- allowed for `null` to be passed to `columnSize`, to prevent the fit to width or autosize being the only options
- fixed props issue for `enableAddRows`


## [Unreleased] - 2023-01-20
_Major overhaul of dash-ag-grid_:
- bringing ag-grid from version v27.x to v29.x+
- added secondary `agGridEnterprise.react.js` as additional importing `ag-grid-enterprise` due to all-modules no longer supported
- updating props for breaking changes due to version update
- adding props for easier user / dash manipulation (enable... props ) for creating buttons
- removing `agGridColumns` due to deprecation and removal due to v29
- added `className` support for css customization native to ag-grid (removed hardcoded styling as well)
- added overarching `dangerously_allow_html` to grid props only provided at render, to keep `columnDefs` from receiving possible updates to show unsafe html
- added `data_previous` and `data_previous_timestamp` to allow for use with user change logs
- added `dashGridOptions` to allow for arbitrary use of props not explicitly listed
- added `setRowId` for allowing `rowData` change detection to work
- added prop `columnState` to allow for pulling the current state of the columns after user interaction, necessary for saving layouts outside of snapshots
- fixed issue where conditional formatting was not applied to nested columns
- fixed issue where columns would not take edits or adjustments due to becoming static
- updated `markdownRenderer.js` to use github markdown, and also have the ability to be passed a target for links, to avoid `dangerously_allow_html`
- updated `requirements.txt` to pull the latest packages

## [1.3.2] - 2023-01-13

### Updated

- [DE#146](https://github.com/plotly/dash-ag-grid-closed/pull/146) Update DashAgGrid component to be async.

## [1.3.1] - 2022-05-05

### Fixed

- [DE#129](https://github.com/plotly/dash-ag-grid-closed/pull/129) Rebuild with latest dash component generator for Py3.6 compatibility

## [1.3.0] - 2022-05-03

### Removed

- [DE#126](https://github.com/plotly/dash-ag-grid-closed/pull/126) AG Grid v27 drops support for IE11

### Updated

- [DE#126](https://github.com/plotly/dash-ag-grid-closed/pull/126) Update AG Grid to v27.2.1.

### Added

- [DE#125](https://github.com/plotly/dash-ag-grid-closed/pull/125) Enable sparklines
- [DE#124](https://github.com/plotly/dash-ag-grid-closed/pull/124) Add Sidebar support
- [DE#87](https://github.com/plotly/dash-ag-grid-closed/pull/87) Add `virtualRowData` for accessing filtered data

### Fixed

- [DE#105](https://github.com/plotly/dash-ag-grid-closed/pull/105) and [DE#108](https://github.com/plotly/dash-ag-grid-closed/pull/108) Update column widths when table is resized or a callback changes `columnDefs`.
- [DE#96](https://github.com/plotly/dash-ag-grid-closed/pull/96) Persist filters when `rowData` changes
- [DE#90](https://github.com/plotly/dash-ag-grid-closed/pull/90) and [DE#86](https://github.com/plotly/dash-ag-grid-closed/pull/86) Improved selections algorithm
- [DE#88](https://github.com/plotly/dash-ag-grid-closed/pull/88) Persist row groupings when `rowData` changes

## [1.2.1] - 2021-11-23

- Selections fixes by @ndrezn in [DE#78](https://github.com/plotly/dash-ag-grid-closed/pull/78)
- Add 2.0 support by @ndrezn in [DE#82](https://github.com/plotly/dash-ag-grid-closed/pull/82)
- Request & response for master detail by @ndrezn in [DE#79](https://github.com/plotly/dash-ag-grid-closed/pull/79)
- Update look of docs

## [1.2.0] - 2021-10-27

- [DE#72](https://github.com/plotly/dash-ag-grid-closed/pull/72): Support for master/detail grid https://www.ag-grid.com/javascript-data-grid/master-detail/

## [1.1.2] - 2021-10-16

- [DE#69](https://github.com/plotly/dash-ag-grid-closed/pull/69): Improve support for persistence with `selectionChanged`.

## [1.1.1] - 2021-09-21

- Fix issue with `selectionChanged` write support

## [1.1.0] - 2021-09-21

- Adds support for `persistence`
- Adds support for exporting data as `CSV`/`excel`
- Adds support for column reset

## [1.0.0] - 2021-06-01

This release is as `v1.0.0` as it indicates production-ready, and changes the API for infinite scroll.

### Fixed

-   [DE#47](https://github.com/plotly/dash-ag-grid-closed/pull/47) Fix issues with infinite scroll support

## [0.2.0] - 2021-05-21

### Added

-   [DE#43](https://github.com/plotly/dash-ag-grid-closed/pull/43) Add row menus support
-   [DE#42](https://github.com/plotly/dash-ag-grid-closed/pull/43) Add support for DDK theming
-   [DE#38](https://github.com/plotly/dash-ag-grid-closed/pull/38) Add Markdown support

### Changed

-   [DE#37](https://github.com/plotly/dash-ag-grid-closed/pull/37) Remove build artifacts from tracking
-   [DE#45](https://github.com/plotly/dash-ag-grid-closed/pull/45) Make download link a `dcc.Download` component in docs

## [0.1.0] - 2021-05-03

### Added

-   [DE#28](https://github.com/plotly/dash-ag-grid-closed/pull/28) Add cell styling support

### Changed

-   [DE#31](https://github.com/plotly/dash-ag-grid-closed/pull/31) Allow users to pass in Enterprise key and control whether Enterprise or Community modules are enabled
-   [DE#30](https://github.com/plotly/dash-ag-grid-closed/pull/30) New demo illustrating how to generate a popup from a table
-   [DE#29](https://github.com/plotly/dash-ag-grid-closed/pull/29) New demo illustrating how to download the dataset from a grid as a CSV file
-   [DE#27](https://github.com/plotly/dash-ag-grid-closed/pull/27) Use DDK and GDWC for demo app

## [0.0.1] - 2021-04-12

## Added

-   [DE#8](https://github.com/plotly/dash-ag-grid-closed/pull/8) Add support for selections
-   [DE#9](https://github.com/plotly/dash-ag-grid-closed/pull/9) Add support for checkboxes
-   [DE#11](https://github.com/plotly/dash-ag-grid-closed/pull/11) Improve editing support
-   [DE#14](https://github.com/plotly/dash-ag-grid-closed/pull/14) Autosizing for columns
-   [DE#16](https://github.com/plotly/dash-ag-grid-closed/pull/16) Infinite scroll support
-   [DE#19](https://github.com/plotly/dash-ag-grid-closed/pull/19) Add API demo/documentation

## Changed

-   [DE#7](https://github.com/plotly/dash-ag-grid-closed/pull/7) Fix start script to run locally
-   [DE#15](https://github.com/plotly/dash-ag-grid-closed/pull/15) Style property
-   [DE#20](https://github.com/plotly/dash-ag-grid-closed/pull/20) Default to ag-grid Enterprise
