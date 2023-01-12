from bs4 import BeautifulSoup
import json
import re
import requests
import sys


MODE = "GRID"
if len(sys.argv) == 2 and sys.argv[1] == "--col-defs":
    MODE = "COL"


DASH_PROPS = """
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Dash-assigned callback that gets fired when the input changes
     */
    setProps: PropTypes.func,

    /**
     * The children of this component
     */
    children: PropTypes.node,

    /**
     * The CSS style for the component
     */
     style: PropTypes.object,

    /**
     * Used to allow user interactions in this component to be persisted when
     * the component - or the page - is refreshed. If `persisted` is truthy and
     * hasn't changed from its previous value, a `value` that the user has
     * changed while using the app will keep that change, as long as
     * the new `value` also matches what was given originally.
     * Used in conjunction with `persistence_type`.
     */
    persistence: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.string,
        PropTypes.number,
    ]),

    /**
     * Properties whose user interactions will persist after refreshing the
     * component or the page. Since only `value` is allowed this prop can
     * normally be ignored.
     */
    persisted_props: PropTypes.arrayOf(PropTypes.oneOf(['value'])),

    /**
     * Where persisted user changes will be stored:
     * memory: only kept in memory, reset on page refresh.
     * local: window.localStorage, data is kept after the browser quit.
     * session: window.sessionStorage, data is cleared once the browser quit.
     */
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),
"""

# Several props do not exist in the documentation or are custom, add them manually
GRID_PROPS = """
    /**
     * Size the columns automatically or to fit their contents
     */
    columnSize: PropTypes.oneOf(['sizeToFit', 'autoSizeAll']),

    /**
     * The ag-grid provided theme to use. More info here: https://www.ag-grid.com/javascript-grid/themes-provided/
     */
    theme: PropTypes.oneOf([
        'alpine',
        'balham',
        'material',
        'bootstrap',
    ]),

    /**
     * Serverside model data request object.
     * See https://www.ag-grid.com/react-grid/server-side-model-datasource/
     */
    getRowsRequest: PropTypes.shape({
        /**
         * for Infinite Scroll (i.e. Partial Store) only, first row requested
         */
        startRow: PropTypes.number,

        /**
         * for Infinite Scroll (i.e. Partial Store) only, last row requested
         */
        endRow: PropTypes.number,

        /**
         * row group columns
         */
        rowGroupCols: PropTypes.arrayOf(PropTypes.shape({
            id: PropTypes.string,
            displayName: PropTypes.string,
            field: PropTypes.string,
            aggFunc: PropTypes.string,
        })),

        /**
         * value columns
         */
        valueCols: PropTypes.arrayOf(PropTypes.shape({
            id: PropTypes.string,
            displayName: PropTypes.string,
            field: PropTypes.string,
            aggFunc: PropTypes.string,
        })),

        /**
         * pivot columns
         */
        pivotCols: PropTypes.arrayOf(PropTypes.shape({
            id: PropTypes.string,
            displayName: PropTypes.string,
            field: PropTypes.string,
            aggFunc: PropTypes.string,
        })),

        /**
         * true if pivot mode is one, otherwise false
         */
        pivotMode: PropTypes.bool,

        /**
         * what groups the user is viewing
         */
        groupKeys: PropTypes.arrayOf(PropTypes.string),

        /**
         * if filtering, what the filter model is
         */
        filterModel: PropTypes.any,

        /**
         * if sorting, what the sort model is
         */
        sortModel: PropTypes.any,
    }),

    /**
     * Serverside model data response object.
     * See https://www.ag-grid.com/react-grid/server-side-model-datasource/
     */
     getRowsResponse: PropTypes.shape({
        /**
         * data retreived from the server
         */
        rowData: PropTypes.arrayOf(PropTypes.any),

        /**
         * for Infinite Scroll (i.e. Partial Store) only, the last row, if known
         */
        rowCount: PropTypes.number,

        /**
         * any extra info for the grid to associate with this load
         */
        storeInfo: PropTypes.any,
     }),
    
    /**
     * License key for ag-grid enterprise. If using Enterprise modules, 
     * enableEnterpriseModules must also be true.
     */
     licenseKey: PropTypes.string,

     /**
     * If True, enable ag-grid Enterprise modules. Recommended to use with licenseKey.
     */
     enableEnterpriseModules: PropTypes.bool,

"""


COL_PROPS = """
    /**
     * boolean. Set to true to show a checkbox in the header of a column.
     * Default Value: false
     */
    headerCheckboxSelection: PropTypes.bool,

    /**
    * boolean. Set to true for checkbox selections to only affect filtered data.
    * Default Value: false
    */
    headerCheckboxSelectionFilteredOnly: PropTypes.bool,
"""


GRID_URLS = [
    ("GRID PROPS", "https://www.ag-grid.com/react-grid/grid-properties/"),
    ("EVENT PROPS", "https://www.ag-grid.com/react-grid/grid-events/"),
]

COL_URLS = [
    ("COLDEF PROPS", "https://www.ag-grid.com/react-grid/column-properties/"),
]


def print_header(title):
    print(
        """
    /********************************
     * {}
     *******************************/
""".format(
            title
        )
    )


def dequote(s):
    s = re.sub(r"'", "", s)
    s = re.sub(r'"', "", s)
    s = s.strip()
    return s


def parse_value(v):
    try:
        v = json.loads(v)
    except json.decoder.JSONDecodeError:
        pass

    if type(v) == str:
        if v[0] == "[":
            v = re.sub(r"\[", "", v)
            v = re.sub(r"\]", "", v)
            v = [dequote(v) for v in v.split(",")]
        else:
            v = dequote(v)

    return v


def pprinter(string):
    s = str(string)
    return s.replace("False", "false").replace("None", "null")


def process_description(td):
    htmlstr = str(td)
    brs = re.sub(r"<br\s?\/?>", "\n", htmlstr).split("\n")

    td_desc = brs.pop(0)
    desc = BeautifulSoup(td_desc, "html.parser").get_text()
    default_value = None
    options = None
    for br in brs:
        if "Default" in br:
            default_value = parse_value(BeautifulSoup(br, "html.parser").code.text)

        elif "Options" in br:
            html_codes = BeautifulSoup(br, "html.parser").find_all("code")
            options = []
            for html_code in html_codes:
                code_value = html_code.text
                options.append(parse_value(code_value))

    return desc, default_value, options


def to_proptypes(value):
    proptype = None
    if type(value) == int:
        proptype = "number"
    elif type(value) == str:
        proptype = "string"
    elif type(value) == bool:
        proptype = "bool"
    elif type(value) == list:
        proptype = f"oneOf({value})"
    else:
        proptype = "any"

    return f"PropTypes.{proptype}"


def print_comment_sentences(comment, pad="    "):
    words = comment.split(" ")
    while len(words) > 0:
        line = " *"
        while len(words) and len(line) < 80:
            line += " " + words.pop(0)
        print(pad + line)


if __name__ == "__main__":

    if MODE == "GRID":
        urls = GRID_URLS
    else:
        urls = COL_URLS

    pad = "    "

    if MODE == "GRID":
        print("DashAgGrid.propTypes = {")
    else:
        print("DashAgGridColumn.propTypes = {")

    print_header("DASH PROPS")

    print(DASH_PROPS)

    print_header("CUSTOM PROPS")

    if MODE == "GRID":
        print(GRID_PROPS)
    else:
        print(COL_PROPS)

    for (prop_category, url) in urls:

        print_header(prop_category)

        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        for table in soup.find_all("table"):

            if MODE == "COL":
                print_header(table.previous_element)

            tbody = table.tbody
            for row in tbody.find_all("tr"):
                tds = row.find_all("td")
                if len(tds) != 2:
                    continue

                # Some props have <br> as there are more than
                # one name per property. Take the first
                tdstr = str(tds[0])
                if "<br" in tdstr:
                    first = re.sub(r"<br\s?\/?>", "\n", tdstr).split("\n")[0]
                    prop = BeautifulSoup(first, "html.parser").get_text()
                else:
                    prop = tds[0].get_text()

                # Skip callback / function prop types
                if "(" and ")" in prop:
                    continue

                desc, default_value, options = process_description(tds[1])

                if options is not None:
                    if default_value in options:
                        default_value = options

                print(pad + "/**")
                print_comment_sentences(desc, pad=pad)
                if default_value is not None:
                    print(pad + f" * Default Value: {pprinter(default_value)}")
                print(pad + " */")
                print(f"{pad}{prop}: {pprinter(to_proptypes(default_value))},")
                print()

    print("};")
