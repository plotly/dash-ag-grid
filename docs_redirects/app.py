"""
This app is hosted at https://dashaggrid.pythonanywhere.com/
It redirects the links from the preliminary dash-ag-grid docs (docs/app.py) to the dash-docs

"""
from dash import Dash, html
import flask

base = "https://dash.plotly.com/dash-ag-grid/"
redirect_map = {
    "/": base,
    "/clientside-data/overview": base + "client-side-data",
    "/clientside-data/updating-data": base + "client-side-data-updating",

    "/columns/column-definitions": base + "column-definitions",
    "/columns/column-groups": base + "column-groups",
    "/columns/column-headers": base + "column-headers",
    "/columns/column-moving": base + "column-moving",
    "/columns/column-pinning": base + "column-pinning",
    "/columns/column-sizing": base + "column-sizing",
    "/columns/column-spanning": base + "column-spanning",
    "/columns/column-state": base + "column-state",
    "/columns/updating-definitions": base + "updating-column-definitions",

    "/components/cell-editor-components": base + "cell-editor-components",
    "/components/cell-renderer": base + "cell-renderer-components",
    "/components/many-components-one-column": base + "many-renderer-components",
    "/components/markdown": base + "markdown-component",
    "/components/overlay": base + "overlay-component",
    "/components/row-menu": base + "row-menu",
    "/components/tooltip": base + "tooltips",

    "/editing/cell-editors": base + "cell-editors",
    "/editing/editing-callbacks": base + "editing-and-callbacks",
    "/editing/full-row": base + "editing-full-row",
    "/editing/overview": base + "cell-editing",
    "/editing/provided-cell-editors": base + "provided-cell-editors",
    "/editing/start-stop-editing": base + "start-stop-editing",
    "/editing/undo-redo": base + "undo-redo-edits",

    "/enterprise/aggegation-conditional-formatting": base + "enterprise-row-aggregation",
    "/enterprise/aggegation-custom-functions": base + "enterprise-aggregation-custom-functions",
    "/enterprise/enabling-enterprise": base + "enterprise-ag-grid",
    "/enterprise/group-cell-renderer": base + "enterprise-group-cell-renderer",
    "/enterprise/master-detail": base + "enterprise-master-detail",
    "/enterprise/pivot": base + "enterprise-pivot",
    "/enterprise/row-groupings": base + "enterprise-row-grouping",
    "/enterprise/sidebar": base + "enterprise-sidebar",
    "/enterprise/sparkline": base + "enterprise-sparklines",
    "/enterprise/tree-data": base + "enterprise-tree-data",

    "/filtering/column-filters-overview": base + "column-filters",
    "/filtering/date-filter": base + "date-filters",
    "/filtering/filter-callbacks": base + "callback-filters",
    "/filtering/floating-filters": base + "floating-filters",
    "/filtering/number-filter": base + "number-filters",
    "/filtering/quick-filter": base + "quick-filters",
    "/filtering/text-filter": base + "text-filters",

    "/getting-started/beyond-the-basics": base + "javascript-and-the-grid",
    "/getting-started/migration-guide": base + "migration-guide",
    "/getting-started/quickstart": base + "getting-started",
    "/getting-started/reference": base + "reference",
    "/getting-started/troubleshooting": base + "troubleshooting",

    "/import-export/clipboard": base + "clipboard",
    "/import-export/export-data-as-csv": base + "export-data-csv",

    "/layout/borders": base + "styling-borders",
    "/layout/cell-styling": base + "styling-cells",
    "/layout/color-font": base + "styling-color-font",
    "/layout/grid-size": base + "grid-size",
    "/layout/headers": base + "styling-headers",
    "/layout/row-styling": base + "styling-rows",
    "/layout/selections": base + "styling-selections",
    "/layout/themes": base + "styling-themes",

    "/other-examples/crossfilter": base + "crossfilter",
    "/other-examples/popup-from-cell-click": base + "popups",
    "/other-examples/virtual-row-data": base + "virtual-row-data",

    "/persistence/persistence": base + "persistence",

    "/rendering/change-cell-renderers": base + "change-cell-renderers",
    "/rendering/value-formatters-custom-functions": base + "custom-functions-value-formatters",
    "/rendering/value-formatters-intro": base + "value-formatters",
    "/rendering/value-formatters-with-d3-format": base + "d3-value-formatters",
    "/rendering/value-getters": base + "value-getters",

    "/rows/row-dragging": base + "row-dragging",
    "/rows/row-height": base + "row-height",
    "/rows/row-ids": base + "row-ids",
    "/rows/row-pinning": base + "row-pinning",
    "/rows/row-sorting": base + "row-sorting",
    "/rows/row-spanning": base + "row-spanning",

    "/scrolling/aligned-grids": base + "aligned-grids",
    "/scrolling/infinite-scroll": base + "infinite-scroll",
    "/scrolling/pagination": base + "pagination",
    "/scrolling/scroll-to": base + "scroll-to",
    "/scrolling/scrolling-performance": base + "scrolling-performance",

    "/selection/cell-selection": base + "cell-selection",
    "/selection/range-selection": base + "enterprise-ag-grid",
    "/selection/select-everything-or-filtered": base + "checkbox-row-selection#header-checkbox-using-filters-and-pagination",
    "/selection/selection-checkbox": base + "checkbox-row-selection",
    "/selection/selection-multiple-click": base + "row-selection-multiple-on-click",
    "/selection/selection-multiple": base + "row-selection-multiple",
    "/selection/selection-single": base + "row-selection-single",
    "/selection/text-selection": base + "text-selection",

    "/serverside-data/infinite-row-model": base + "infinite-row-model",
    "/serverside-data/row-models": base + "row-models",

}

app = Dash(__name__)

app.layout = html.Div("no layout")


@app.server.before_request
def redirect():
    return flask.redirect(redirect_map.get(flask.request.path, base))


if __name__ == "__main__":
    app.run_server(debug=True)
