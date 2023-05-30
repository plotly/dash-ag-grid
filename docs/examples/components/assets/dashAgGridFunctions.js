var dagfuncs = (window.dashAgGridFunctions = window.dashAgGridFunctions || {});

dagfuncs.DatePicker = class {
    // gets called once before the renderer is used
    init(params) {
        // create the cell
        this.eInput = document.createElement('input');
        this.eInput.value = params.value;
        this.eInput.classList.add('ag-input');
        this.eInput.style.height = 'var(--ag-row-height)';
        this.eInput.style.fontSize = 'calc(var(--ag-font-size) + 1px)';

        // https://jqueryui.com/datepicker/
        $(this.eInput).datepicker({
            dateFormat: 'dd/mm/yy',
            onSelect: () => {
                this.eInput.focus();
            },
        });
    }

    // gets called once when grid ready to insert the element
    getGui() {
        return this.eInput;
    }

    // focus and select can be done after the gui is attached
    afterGuiAttached() {
        this.eInput.focus();
        this.eInput.select();
    }

    // returns the new value after editing
    getValue() {
        return this.eInput.value;
    }

    // any cleanup we need to be done here
    destroy() {
        // but this example is simple, no cleanup, we could
        // even leave this method out as it's optional
    }

    // if true, then this editor will appear in a popup
    isPopup() {
        // and we could leave this method out also, false is the default
        return false;
    }
};

// Used in the conditional rendering example
dagfuncs.moodOrGender = function (params) {
    var dagcomponentfuncs = window.dashAgGridComponentFunctions;
    const moodDetails = {
        component: dagcomponentfuncs.MoodRenderer,
    };
    const genderDetails = {
        component: dagcomponentfuncs.GenderRenderer,
    };
    if (params.data) {
        if (params.data.type === 'gender') return genderDetails;
        else if (params.data.type === 'mood') return moodDetails;
    }
    return undefined;
};

dagfuncs.NumberInput = class {
    // gets called once before the renderer is used
    init(params) {
        // create the cell
        this.eInput = document.createElement('input');
        this.eInput.value = params.value;
        this.eInput.style.height = 'var(--ag-row-height)';
        this.eInput.style.fontSize = 'calc(var(--ag-font-size) + 1px)';
        this.eInput.style.borderWidth = 0;
        this.eInput.style.width = '95%';
        this.eInput.type = 'number';
        this.eInput.min = params.min;
        this.eInput.max = params.max;
        this.eInput.step = params.step || 'any';
        this.eInput.required = params.required;
        this.eInput.placeholder = params.placeholder || '';
        this.eInput.name = params.name;
        this.eInput.disabled = params.disabled;
        this.eInput.title = params.title || '';
    }

    // gets called once when grid ready to insert the element
    getGui() {
        return this.eInput;
    }

    // focus and select can be done after the gui is attached
    afterGuiAttached() {
        this.eInput.focus();
        this.eInput.select();
    }

    // returns the new value after editing
    getValue() {
        return this.eInput.value;
    }

    // any cleanup we need to be done here
    destroy() {
        // but this example is simple, no cleanup, we could
        // even leave this method out as it's optional
    }

    // if true, then this editor will appear in a popup
    isPopup() {
        // and we could leave this method out also, false is the default
        return false;
    }
};

// Used in the cell editor dropdown example
//  dynamicOptions function is for providing different options based on data in a different column
//  Use this in the cellEditorParams
dagfuncs.dynamicOptions = function (params) {
    const selectedCountry = params.data.country;
    if (selectedCountry === 'United States') {
        return {
            options: ['Boston', 'Chicago', 'San Francisco'],
        };
    } else {
        return {
            options: ['Montreal', 'Vancouver', 'Calgary'],
        };
    }
};

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

//  dcc.Dropdown component - cell editor
//  Note - DO NOT USE this component - dropdown options are not visible at the bottom of the grid
//         See community discussion https://community.plotly.com/t/using-dash-core-components-dropdown-as-an-ag-grid-cell-editor/
dagfuncs.DCC_Dropdown = class {
    // gets called once before the renderer is used
    init(params) {
        // create the cell
        this.params = params;
        this.ref = React.forwardRef();

        // function for when Dash is trying to send props back to the component / server
        var setProps = (props) => {
            if (props.value) {
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
            React.createElement(window.dash_core_components.Dropdown, {
                options: params.options,
                value: params.value,
                multi: params.multi,
                placeholder: params.placeholder,
                disabled: params.disabled,
                optionHeight: params.optionHeight,
                maxHeight: params.maxHeight,
                className: params.className,
                style: {width: params.column.actualWidth},
                ref: this.ref,
                setProps,
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
        // mousedown event
        const clickEvent = new MouseEvent('mousedown', {
            view: window,
            bubbles: true,
        });

        // needed to delay and allow the component to render
        setTimeout(() => {
            var inp = this.eInput.getElementsByClassName('Select-value')[0];
            inp.tabIndex = '1';

            // disables keyboard event
            this.params.colDef.suppressKeyboardEvent = (params) => {
                const gridShouldDoNothing = params.editing;
                return gridShouldDoNothing;
            };
            // shows dropdown options
            inp.dispatchEvent(clickEvent);
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
