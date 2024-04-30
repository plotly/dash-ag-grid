# Change Log for Dash AG Grid

All notable changes to `dash-ag-grid` will be documented in this file.
This project adheres to [Semantic Versioning](https://semver.org/).
Links "DE#nnn" prior to version 2.0 point to the Dash Enterprise closed-source Dash AG Grid repo

## [31.2.0] - 2024-02-25

### Changed
 - [#273](https://github.com/plotly/dash-ag-grid/pull/273) increased the timeout for `getApiAsync` to 2 minutes.
 - [#281](https://github.com/plotly/dash-ag-grid/pull/281) webpack is now designed to build quicker, excludes `node_modules` and uses a different parser
 - [#287](https://github.com/plotly/dash-ag-grid/pull/287) bumping to v`31.2.1` for the grid

### Added
  - [#270](https://github.com/plotly/dash-ag-grid/pull/270)
    - support for `eventListeners` to be added to the grid that get loaded upon `gridReady`
    - `eventListeners` are added upon `gridReady` only, if you need to add or remove other event listeners, please use the `getApi` or `getApiAsync` methods
    - added default for `selectedRows` to be `[]`

### Fixed
  - [#283](https://github.com/plotly/dash-ag-grid/pull/283)
    - `selectedRows` can now be passed along with the `rowData`
      - fixes [#274](https://github.com/plotly/dash-ag-grid/issues/274)
      - fixes [#282](https://github.com/plotly/dash-ag-grid/issues/282)
  - [#287](https://github.com/plotly/dash-ag-grid/pull/287)
    - `aggFuncs` can now be passes as an object from the grid to be mapped to functions
    - fixes [#278](https://github.com/plotly/dash-ag-grid/issues/278)


## [31.0.1] - 2024-02-07

- [#266](https://github.com/plotly/dash-ag-grid/pull/266) Updated README

## [31.0.0] - 2024-02-01

### Added
- [#246](https://github.com/plotly/dash-ag-grid/pull/246/)
  - `grid_version` added to allow developer to see underlying AG Grid version in python
  - Added `quartz` theme native support
  - Added function support for `dateParser`, `dateFormatter`, `quickFilterParser`, `components`, `quickFilterMatcher`, `predicate`, `textFormatter`, `textMatcher`, `numberFormatter`, `numberParser`, `dataTypeMatcher`

### Removed
- [#246](https://github.com/plotly/dash-ag-grid/pull/246/) dropped `getColumnApi` and `getColmunApiAsync` as these are deprecated from the underlying grid.

### Changed
- [#261](https://github.com/plotly/dash-ag-grid/pull/261) The `cellValueChanged` property has changed been changed from a (single) event object to a _list_ of event objects. For multi-cell edits, the list will contain an element per change. In other cases, the list will contain a single element. Fixes [#262](https://github.com/plotly/dash-ag-grid/issues/262)
- [#246](https://github.com/plotly/dash-ag-grid/pull/246/)
  - updating underlying grid version from AG Grid v29 -> v31, with this change, Dash AG Grid will reflect a similar version number to underlying Grid version.
  - `dataTypeDefinitions` now supports full js, partial python with full definitions in js of an object, and objects have parts that are js
  - `columnSize` and `columnState` cannot be currently passed together when grid initializes, the `columnSize` will trump the `columnState`

### Fixed
- [#246](https://github.com/plotly/dash-ag-grid/pull/246/) testing for grid going to destroyed state

## [2.4.0] - 2023-10-17

### Added
- [#243](https://github.com/plotly/dash-ag-grid/pull/243) Added function support for:
  - `getContextMenuItems`, `isRowMaster`, `setPopupParent`, `popupParent`, `filter`
  - iterate through `csvExportParams` and `defaultCsvExportParams` for functions:
    - `getCustomContextBelowRow`, `shouldRowBeSkipped`, `processCellCallback`, `processHeaderCallback`, `processGroupHeaderCallback`, `processRowGroupCallback`

### Fixed
- [#237](https://github.com/plotly/dash-ag-grid/pull/237) Fixed issue with grid components not being passed down to the detail grids
- [#232](https://github.com/plotly/dash-ag-grid/pull/232) Fixed height style to unassign automatically if `domLayout` = 'autoHeight', addresses [#231](https://github.com/plotly/dash-ag-grid/issues/231)

## [2.3.0] - 2023-07-27

### Added
- [#212](https://github.com/plotly/dash-ag-grid/pull/212) Async function for `getApiAsync` and `getColumnApiAsync` for use with grid initializing

### Fixed
- [#226](https://github.com/plotly/dash-ag-grid/pull/226) Fixed issue when using grouped rows with `rowData` and `virtualRowData` populating incorrectly. [#215](https://github.com/plotly/dash-ag-grid/issues/215)

## [2.2.0] - 2023-06-20

### Added
- [#199](https://github.com/plotly/dash-ag-grid/pull/199) Add `scrollTo` prop which allows scrolling to rows and columns.
- [#209](https://github.com/plotly/dash-ag-grid/pull/209) Add `getApi` and `getColumnApi` to `dash_ag_grid` namespace to allow for JS functions to call the grid's API directly

### Fixed
- [210](https://github.com/plotly/dash-ag-grid/pull/210) Fix issue with `columnState` and React 18

### Updated
- [210](https://github.com/plotly/dash-ag-grid/pull/210) Migrate props that use `setProps` from the `render()` to `componentDidUpdate`

## [2.1.0] - 2023-06-02

### Added
- [#201](https://github.com/plotly/dash-ag-grid/pull/201) Add `cellDoubleClicked` prop, which works exactly like `cellClicked`

### Updated
- [#174](https://github.com/plotly/dash-ag-grid/pull/174)
  - `columnState` floats during grid interaction and only gets pushed when sent in a callback
  - `columnDefs` trumps `columnState` if it is pushed in a callback without a `columnState`

- [#207](https://github.com/plotly/dash-ag-grid/pull/207) Update AG Grid from 29.3.3 to 29.3.5, with a few minor bugfixes, see their changelog for [29.3.4](https://www.ag-grid.com/changelog/?fixVersion=29.3.4) and [29.3.5](https://www.ag-grid.com/changelog/?fixVersion=29.3.5). Also other minor dependency updates.

### Fixed
- [#174](https://github.com/plotly/dash-ag-grid/pull/174) Fix [#171](https://github.com/plotly/dash-ag-grid/issues/171): `Markdown` renderer now displays a blank cell rather than writing `undefined` if there is no value

- [#204](https://github.com/plotly/dash-ag-grid/pull/204) `filterOptions` will now work as a regular object

- [#206](https://github.com/plotly/dash-ag-grid/pull/206) Fix [#195](https://github.com/plotly/dash-ag-grid/issues/195) where if the user was to redo the exact same action, callbacks on `cellValueChanged` would not trigger again. Fix by adding `timestamp` into the object, as we have in other event-type props to make them unique.

## [2.0.0] - 2023-05-02

### Removed

- [Overhaul commit](https://github.com/plotly/dash-ag-grid/commit/b888d6ab4fcb4afac187492e8b6c9cf0d0f8842b)
  - Remove `agGridColumns` component due to deprecation in AG Grid v29, use `columnDefs` instead.
  - Remove some hardcoded CSS

- [#132](https://github.com/plotly/dash-ag-grid/pull/132) Remove prop `autoSizeAllColumns`, use the `columnSize` prop instead.

### Added

- [Overhaul commit](https://github.com/plotly/dash-ag-grid/commit/b888d6ab4fcb4afac187492e8b6c9cf0d0f8842b)
  - Add `className` prop for css customization native to AG Grid
  - Add `enable*` props for easier user / dash manipulation, for creating buttons
  - Add overarching `dangerously_allow_code` prop to grid props only provided at render, to keep `columnDefs` from receiving possible updates to execute malicious JavaScript (originally called `dangerously_allow_html` but renamed later)
  - Add `data_previous` and `data_previous_timestamp` props to allow easier change tracking in callbacks
  - Add `dashGridOptions` prop to allow for arbitrary use of AG Grid props not explicitly listed
  - Add `setRowId` prop to allow `rowData` change detection
  - Add `columnState` prop to retrieve the current state of the columns after user interaction

- [#6](https://github.com/plotly/dash-ag-grid/pull/6)
  - Allow strings of functions to be passed as parameters to `valueGetterFunction`, `valueFormatterFunction`. This allows for functions to be parsed even in a strict CSP environment.
  - Add row conditional formatting via `getRowStyle`, acts similar to `cellStyles`
  - Add ability for custom parsing functions to be passed via the namespace `window.dashAgGridFunctions`
  - Allow for `null` to be passed to `columnSize`, to prevent the fit to width or autosize being the only options

- [#28](https://github.com/plotly/dash-ag-grid/pull/28)
  - Allow for other column prop functions to pass without disabling them if `dangerously_allow_code` is not passed
  - Copy over `columnDef` `dangerously_allow_code` to allow for the prop to be placed only on the grid level
  - Keep `params` together instead of splitting into separate keys, to allow for easier transition to using AG Grid docs

- [#39](https://github.com/plotly/dash-ag-grid/pull/39)
  - Allow for `defaultColDef` to be iterated through for functions
  - Add `tooltipComponent` to be altered if it was list as a function object

- [#49](https://github.com/plotly/dash-ag-grid/pull/49) Safely handle more attributes when `dangerously_allow_code` is disabled:
  - Top-level attributes `rowClassRules`, `getRowStyle`, and `getRowClass`
  - Column attributes `cellClass`, `cellStyle`, and `cellClassRules`

- [#67](https://github.com/plotly/dash-ag-grid/pull/67) Function parsing recursive columnDefs
  - Add more functions to be available for parsing
  - Allow for recursively going through `columnDefs` -> `children` and master detail info

- [#76](https://github.com/plotly/dash-ag-grid/pull/76) Add logging function available by default, available via `{"function": "log()"}`

- [#111](https://github.com/plotly/dash-ag-grid/pull/111) Add `filterModel` prop in order to capture the grid's active filters

- [#132](https://github.com/plotly/dash-ag-grid/pull/132)
  - Add new `columnSize` option `responsiveSizeToFit`, which will adjust column sizes based upon grid size and columns added or removed
  - Add `columnSizeOptions` prop to modify the behavior chosen in `columnSize`
  - Add ability to push `columnState` back to grid and replay the settings

- [#145](https://github.com/plotly/dash-ag-grid/pull/145)
  - Support `alignedGrids`
  - Support functions with `tooltipComponentParams`
  - Add `paginationInfo` for read-only info from the grid's pagination
  - Add `paginationGoTo` to navigate to different pages

-[#164](https://github.com/plotly/dash-ag-grid/pull/164) Support passing `selectedRows` functions or ids for performing selections

### Updated
- [Overhaul commit](https://github.com/plotly/dash-ag-grid/commit/b888d6ab4fcb4afac187492e8b6c9cf0d0f8842b)
  - Update AG Grid from v27.x to v29.x - see [AG Grid Changelog](https://www.ag-grid.com/changelog/) for details.
  - Update markdown renderer to use github markdown, and also have the ability to be passed a target for links, to avoid `dangerously_allow_code`
  - Update `requirements.txt` (Python dependencies for demos and docs) to allow the latest packages

- [#39](https://github.com/plotly/dash-ag-grid/pull/39)
  - Change `selectionChanged` to `selectedRows` to make props align with AG Grid
  - Allow `selectedRows` to persist

- [#70](https://github.com/plotly/dash-ag-grid/pull/70) Change `clickData` to `cellRendererData` to more closely line up with what this does

- [#81](https://github.com/plotly/dash-ag-grid/pull/81)
  - Prop clean-up overhaul
  - Remove `cellStyle` from the grid level, allowing more flexibility in customization, and alignment with AG grid
  - Allow for functions, styleConditions and regular dictionaries to be passed to the `cellStyle` on all levels
  - Add `rowId` to `cellClicked` data

- [#132](https://github.com/plotly/dash-ag-grid/pull/132) Change `columnSize` option of `autoSizeAll` -> `autoSize`

- [#145](https://github.com/plotly/dash-ag-grid/pull/145) and [#159](https://github.com/plotly/dash-ag-grid/pull/159) Update AG Grid `29.1.0` -> `29.3.3`

- [#155](https://github.com/plotly/dash-ag-grid/pull/155)
  - Update React to `18.2.0`
  - Update `material-ui` to `@mui` for `rowMenuRenderer`

-[#164](https://github.com/plotly/dash-ag-grid/pull/164) Update `selectedRows` to maintain persistence by utilizing `rowIds` if available

### Fixed
- [Overhaul commit](https://github.com/plotly/dash-ag-grid/commit/b888d6ab4fcb4afac187492e8b6c9cf0d0f8842b)
  - Fix conditional formatting for nested columns
  - Fix issue where columns would not take edits or adjustments due to becoming static

- [#6](https://github.com/plotly/dash-ag-grid/pull/6) Fix props issue for `enableAddRows`

- [#19](https://github.com/plotly/dash-ag-grid/pull/19) Fixed `cellClicked` as reported in [#17](https://github.com/plotly/dash-ag-grid/issues/17)

- [#45](https://github.com/plotly/dash-ag-grid/pull/45) Fix [#44](https://github.com/plotly/dash-ag-grid/issues/44), markdown ignoring `target="_blank"` to open links in a new tab. Now if `dangerously_use_code` is `false`, markdown cells honor `columnDef.linkTarget`, but if `dangerously_use_code` is `true` you MUST use the HTML syntax `<a target="_blank">` to achieve this, markdown syntax `[text](url)` will ignore `columnDef.linkTarget`.

- [#47](https://github.com/plotly/dash-ag-grid/pull/47) Fix `virtualRowData` by setting the default `rowModelType='clientSide'`

- [#81](https://github.com/plotly/dash-ag-grid/pull/81) Fix syncing issue with `rowData`, `virtualRowData` when cell edits and async `rowTransactions` occur

- [#90](https://github.com/plotly/dash-ag-grid/pull/90) Fix `columnState` to be populated once `gridReady`

- [#92](https://github.com/plotly/dash-ag-grid/pull/92) Fix `defaultStyle` when no `styleConditions` is in `cellStyle`

- [#111](https://github.com/plotly/dash-ag-grid/pull/111) Fix templates to only populate when `dangerously_allow_code=True`

- [#132](https://github.com/plotly/dash-ag-grid/pull/132) Fix `columnSize` to update upon interaction

- [#145](https://github.com/plotly/dash-ag-grid/pull/145)
  - Fix `onRowDragEnd` to trigger `virtualRowData` update
  - Fix all `virtualRowData` updates to take into account sorting

- [#155](https://github.com/plotly/dash-ag-grid/pull/155) and [#158](https://github.com/plotly/dash-ag-grid/pull/158)
  - Fix `openGroups` where clearing out the set would cause issues
  - Fix `paginationGoTo` to work with a starting page

- [#161](https://github.com/plotly/dash-ag-grid/pull/161) Fix the default style to be applied even when a style is given from the developer. `style.height` and `style.width` always exist but can be overridden if other values are provided in the `style` prop.

-[#164](https://github.com/plotly/dash-ag-grid/pull/164)
  - Fix `comparator` to not be restricted to just params
  - Fix `paginationGoTo` to allow `0` to be passed

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
