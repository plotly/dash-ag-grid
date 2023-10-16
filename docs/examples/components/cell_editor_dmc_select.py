"""
Grid with dcc.Dropdown component as a cell editor
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import dash_mantine_components as dmc

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)


columnDefs = [
    {
        "field": "country",
        "cellEditor": {"function": "DMC_Select"},
        "cellEditorParams": {
            "options": df.country.unique(),
            "clearable": True,
            "placeholder": "Select Country",
            "shadow": "xl",
        },
        "cellEditorPopup": True,
        "singleClickEdit": True,
    },
    {"field": "year"},
    {"field": "athlete"},
    {"field": "age"},
    {"field": "date"},
    {
        "field": "sport",
        "cellEditor": {"function": "DMC_Select"},
        "cellEditorParams": {
            "options": df.sport.unique(),
            "creatable": True,
            "clearable": False,
            "shadow": "xl",
        },
        "cellEditorPopup": True,
        "singleClickEdit": True,
    },
    {"field": "total"},
]

defaultColDef = {
    "resizable": True,
    "sortable": True,
    "filter": True,
    "minWidth": 100,
    "editable": True,
}


app.layout = html.Div(
    [
        dcc.Markdown(
            "This grid has Dash Mantine Components dmc.Select in the Country and Sport columns"
        ),
        dag.AgGrid(
            id="cell-editor-dmc-grid",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="responsiveSizeToFit",
            defaultColDef=defaultColDef,
        ),
        html.Div(id="cell-editor-dmc-output"),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("cell-editor-dmc-output", "children"),
    Input("cell-editor-dmc-grid", "cellValueChanged"),
)
def selected(changed):
    return f"You have selected {changed}"


if __name__ == "__main__":
    app.run_server(debug=True)


"""
Add this to the dashAgGridFunctions.js file in the assets folder

----------------

var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

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