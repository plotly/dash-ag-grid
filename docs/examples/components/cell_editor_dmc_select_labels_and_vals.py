"""
Labels and Values different
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import dash_mantine_components as dmc

app = Dash(__name__)

city_options = [
    {"label": "New York City", "value": "NYC", "disabled": True},
    {"label": "Seattle", "value": "SEA"},
    {"label": "San Francisco", "value": "SFO"},
]

things_to_do_options = [
    {"label": "Restaurants", "value": "Restaurants", "group": "Dining"},
    {"label": "Movies", "value": "Movies", "group": "Entertainment"},
    {"label": "Diners", "value": "Diners", "group": "Dining"},
    {"label": "Theater", "value": "Theater", "group": "Entertainment"},
    {"label": "Coffee Shops", "value": "Coffee Shops", "group": "Dining"},
    {"label": "Sporting Events", "value": "Sporting Events", "group": "Entertainment"},
]


columnDefs = [
    {
        "field": "country",
        "editable": False,
    },
    {
        "field": "city",
        "cellEditor": {"function": "DMC_Select"},
        "cellEditorParams": {
            "options": city_options,
            "placeholder": "Select a City",
        },
        "valueFormatter": {
            "function": "filterArray(params.colDef.cellEditorParams.options, params.value)[0] ? "
            "filterArray(params.colDef.cellEditorParams.options, params.value, 'label').toString() "
            ": 'invalid'"
        },
        "cellEditorPopup": True,
    },
    {
        "headerName": "Things To Do",
        "field": "things_to_do",
        "cellEditor": {"function": "DMC_Select"},
        "cellEditorParams": {
            "options": things_to_do_options,
        },
        "cellEditorPopup": True,
    },
]

rowData = [
    {"country": "United States", "city": "SFO", "things_to_do": "Restaurants"},
    {"country": "United States", "city": "NYC", "things_to_do": "Coffee Shops"},
    {"country": "United States", "city": "SEA", "things_to_do": "Theater"},
]


app.layout = html.Div(
    [
        dcc.Markdown("Grid with dmc.Select Options -- Groupings and Labels"),
        dag.AgGrid(
            id="cell-editor-dmc-grid2",
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="responsiveSizeToFit",
            defaultColDef={"editable": True,  "minWidth": 100}
        ),
        html.Div(id="cell-editor-dmc-output2"),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("cell-editor-dmc-output2", "children"),
    Input("cell-editor-dmc-grid2", "cellValueChanged"),
)
def selected(changed):
    return f"You have selected {changed}"


if __name__ == "__main__":
    app.run_server(debug=True)




"""
Add this to the dashAgGridFunctions.js file in the assets folder

----------------

var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};


// Used in the cell editor dropdown examples
//     filterArray function displays the label instead of the value when the dropdown options contain both
//     Use this in a valueFormatter
dagfuncs.filterArray = function (array, condition, col = null) {
    newArray = array.filter((t) => condition.includes(t.value));
    if (!col) {
        return newArray;
    } else {
        var values = [];
        newArray.map((t) => values.push(t[col]));
        return values;
    }
};

// cell editor custom component  - dmc.Select
dagfuncs.DMC_Select = class {
    // gets called once before the renderer is used
    init(params) {
        // create the cell
        this.params = params;

        // function for when Dash is trying to send props back to the component / server
        var setProps = (props) => {
            if (typeof props.value != typeof undefined) {
                // updates the value of the editor
                this.value = props.value;

                // re-enables keyboard event
                delete params.colDef.suppressKeyboardEvent;

                // tells the grid to stop editing the cell
                params.api.stopEditing();

                // sets focus back to the grid's previously active cell
                this.prevFocus.focus();
            }
        };
        this.eInput = document.createElement('div');

        // renders component into the editor element
        ReactDOM.render(
            React.createElement(window.dash_mantine_components.Select, {
                data: params.options,
                value: params.value,
                setProps,
                style: {width: params.column.actualWidth-2,  ...params.style},
                className: params.className,
                clearable: params.clearable,
                searchable: params.searchable || true,
                creatable: params.creatable,
                debounce: params.debounce,
                disabled: params.disabled,
                filterDataOnExactSearchMatch:
                    params.filterDataOnExactSearchMatch,
                limit: params.limit,
                maxDropdownHeight: params.maxDropdownHeight,
                nothingFound: params.nothingFound,
                placeholder: params.placeholder,
                required: params.required,
                searchValue: params.searchValue,
                shadow: params.shadow,
                size: params.size,            
                styles: params.styles,
                switchDirectionOnFlip: params.switchDirectionOnFlip,
                variant: params.variant,            
            }),
            this.eInput
        );

        // allows focus event
        this.eInput.tabIndex = '0';

        // sets editor value to the value from the cell
        this.value = params.value;
    }

    // gets called once when grid ready to insert the element
    getGui() {
        return this.eInput;
    }

    focusChild() {
        // needed to delay and allow the component to render
        setTimeout(() => {
            var inp = this.eInput.getElementsByClassName(
                'mantine-Select-input'
            )[0];
            inp.tabIndex = '1';

            // disables keyboard event
            this.params.colDef.suppressKeyboardEvent = (params) => {
                const gridShouldDoNothing = params.editing;
                return gridShouldDoNothing;
            };
            // shows dropdown options
            inp.focus();
        }, 100);
    }

    // focus and select can be done after the gui is attached
    afterGuiAttached() {
        // stores the active cell
        this.prevFocus = document.activeElement;

        // adds event listener to trigger event to go into dash component
        this.eInput.addEventListener('focus', this.focusChild());

        // triggers focus event
        this.eInput.focus();
    }

    // returns the new value after editing
    getValue() {
        return this.value;
    }

    // any cleanup we need to be done here
    destroy() {
        // sets focus back to the grid's previously active cell
        this.prevFocus.focus();
    }
};


"""