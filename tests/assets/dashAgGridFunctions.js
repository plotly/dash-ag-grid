var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};
dagfuncs.Round = function (v, a = 2) {
    return Math.round(v * (10 ** a)) / (10 ** a)
}

dagfuncs.toFixed = function (v, a = 2) {
    return Number(v).toFixed(a)
}

dagfuncs.addEdits = function (params) {
    if (params.data.changes) {
        var newList = JSON.parse(params.data.changes)
        newList.push(params.colDef.field)
        params.data.changes = JSON.stringify(newList)
    } else {
        params.data.changes = JSON.stringify([params.colDef.field])
    }
    params.data[params.colDef.field] = params.newValue
    return true;
}

dagfuncs.highlightEdits = function (params) {
    if (params.data.changes) {
        if (JSON.parse(params.data.changes).includes(params.colDef.field)) {
            return true
        }
    }
    return false;
}

dagfuncs.rowTest = function (params) {
    if (params.data.make == 'Toyota') {
        return 'testing'
    }
}

dagfuncs.ratioValueGetter = function (params) {
    if (!(params.node && params.node.group)) {
        // no need to handle group levels - calculated in the 'ratioAggFunc'
        return createValueObject(params.data.gold, params.data.silver);
    }
}
dagfuncs.ratioAggFunc = function (params) {
    let goldSum = 0;
    let silverSum = 0;
    params.values.forEach((value) => {
        if (value && value.gold) {
            goldSum += value.gold;
        }
        if (value && value.silver) {
            silverSum += value.silver;
        }
    });
    return createValueObject(goldSum, silverSum);
}

function createValueObject(gold, silver) {
    return {
        gold: gold,
        silver: silver,
        toString: () => `${gold && silver ? gold / silver : 0}`,
    };
}

dagfuncs.ratioFormatter = function (params) {
    if (!params.value || params.value === 0) return '';
    return '' + Math.round(params.value * 100) / 100;
}


dagfuncs.filterParams = () => {
    return {
        filterOptions: [
            'lessThan',
            {
                displayKey: 'lessThanWithNulls',
                displayName: 'Less Than with Nulls',
                predicate: ([filterValue], cellValue) => cellValue == null || cellValue < filterValue,
            },
            'greaterThan',
            {
                displayKey: 'greaterThanWithNulls',
                displayName: 'Greater Than with Nulls',
                predicate: ([filterValue], cellValue) => cellValue == null || cellValue > filterValue,
            },
            {
                displayKey: 'betweenExclusive',
                displayName: 'Between (Exclusive)',
                predicate: ([fv1, fv2], cellValue) => cellValue == null || fv1 < cellValue && fv2 > cellValue,
                numberOfInputs: 2,
            }
        ],
        defaultOption: 'lessThanWithNulls',
    }
};

dagfuncs.getDataPath = function (data) {
    return data.orgHierarchy;
}

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
            dateFormat: 'yy-mm-dd',
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

}

dagfuncs.dateComparator = function (date1, date2) {
    const date1Number = monthToComparableNumber(date1);
    const date2Number = monthToComparableNumber(date2);
    if (date1Number === null && date2Number === null) {
        return 0;
    }
    if (date1Number === null) {
        return -1;
    }
    if (date2Number === null) {
        return 1;
    }
    return date1Number - date2Number;
}

// eg 29/08/2004 gets converted to 20040829
function monthToComparableNumber(date) {
    if (date === undefined || date === null) {
        return null;
    }
    const yearNumber = parseInt(date.split('/')[2]);
    const monthNumber = parseInt(date.split('/')[1]);
    const dayNumber = parseInt(date.split('/')[0]);
    return yearNumber * 10000 + monthNumber * 100 + dayNumber;
}

const {useImperativeHandle, useState, useEffect, forwardRef} = React;

// This example was adapted from https://www.ag-grid.com/react-data-grid/component-filter/
// The only differences are:
// - React.createElement instead of JSX
// - setProps, which all Dash components use to report user interactions,
//     instead of a plain js event handler
dagfuncs.YearFilter = forwardRef((props, ref) => {
    const [year, setYear] = useState('All');

    useImperativeHandle(ref, () => {
        return {
            doesFilterPass(params) {
                return params.data.year >= 2010;
            },

            isFilterActive() {
                return year === '2010'
            },

            // this example isn't using getModel() and setModel(),
            // so safe to just leave these empty. don't do this in your code!!!
            getModel() {
            },

            setModel() {
            }
        }
    });

    useEffect(() => {
        props.filterChangedCallback()
    }, [year]);

    setProps = ({value}) => {
        if (value) {
            setYear(value)
        }
    }

    return React.createElement(
        window.dash_core_components.RadioItems,
        {
            options: [
                {'label': 'All', 'value': 'All'},
                {'label': 'Since 2010', 'value': '2010'},
            ],
            value: year,
            setProps
        }
    )
});

dagfuncs.setBody = () => {
    return document.querySelector('body')
}

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
                style: {width: params.column.actualWidth - 2, ...params.style},
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

dagfuncs.contextTest = (params) => {
    var result = [
        {
            // custom item
            name: 'Alert ' + params.value,
            action: () => {
                window.alert('Alerting about ' + params.value);
            },
            cssClasses: ['redFont', 'bold'],
        },
        'copy',
        'separator',
        'chartRange',
    ];
    return result;
};

// FOR test_custom_filter.py
dagfuncs.myTextFormatter = (text) => {
    if (text == null) return null;
    return text
        .toLowerCase()
        .replace(/[àáâãäå]/g, 'a')
        .replace(/æ/g, 'ae')
        .replace(/ç/g, 'c')
        .replace(/[èéêë]/g, 'e')
        .replace(/[ìíîï]/g, 'i')
        .replace(/ñ/g, 'n')
        .replace(/[òóôõö]/g, 'o')
        .replace(/œ/g, 'oe')
        .replace(/[ùúûü]/g, 'u')
        .replace(/[ýÿ]/g, 'y');
}

function contains(target, lookingFor) {
    return target && target.indexOf(lookingFor) >= 0;
}

dagfuncs.myTextMatcher = ({value, filterText}) => {
    const aliases = {
        usa: "united states",
        holland: "netherlands",
        niall: "ireland",
        sean: "south africa",
        alberto: "mexico",
        john: "australia",
        xi: "china",
    };
    const literalMatch = contains(value, filterText || "");
    return literalMatch || contains(value, aliases[filterText || ""]);
}

dagfuncs.myNumberParser = (text) => {
    return text === null ? null : parseFloat(text.replace(",", ".").replace("$", ""));
}
dagfuncs.myNumberFormatter = (value) => {
    return value === null ? null : value.toString().replace(".", ",");
}
dagfuncs.startWith = ([filterValues], cellValue) => {
    const name = cellValue ? cellValue.split(" ")[1] : ""
    return name && name.toLowerCase().indexOf(filterValues.toLowerCase()) === 0
}
// END test_custom_filter.py

// FOR test_quick_filter.py
dagfuncs.quickFilterMatcher = (quickFilterParts, rowQuickFilterAggregateText) => {
    return quickFilterParts.every(part => rowQuickFilterAggregateText.match(part));
}
// END test_quick_filter.py

// FOR test_cell_data_type_override.py
dagfuncs.dataTypeDefinitions = {
    percentage: {
        baseDataType: "number",
        extendsDataType: "number",
        valueFormatter: (params) => params.value == null ? '' : (Math.round(params.value * 1000) / 10).toFixed(1) + '%'
    },

    dateString: {
        baseDataType: 'dateString',
        extendsDataType: 'dateString',
        valueParser: (params) => {
            return params.newValue != null &&
            !!params.newValue.match(/\d{2}\/\d{2}\/\d{4}/)
                ? params.newValue
                : null
        },
        valueFormatter: (params) => {
            return params.value == null ? '' : params.value
        },
        dataTypeMatcher: (value) => {
            return typeof value === 'string' && !!value.match(/\d{2}\/\d{2}\/\d{4}/)
        },
        dateParser: (value) => {
            if (value == null || value === '') {
                return undefined;
            }
            const dateParts = value.split('/');
            return dateParts.length === 3
                ? new Date(
                    parseInt(dateParts[2]),
                    parseInt(dateParts[1]) - 1,
                    parseInt(dateParts[0])
                )
                : undefined;
        },
        dateFormatter: (value) => {
            if (value == null) {
                return undefined;
            }
            const date = String(value.getDate());
            const month = String(value.getMonth() + 1);
            return `${date.length === 1 ? '0' + date : date}/${
                month.length === 1 ? '0' + month : month
            }/${value.getFullYear()}`;
        },
    },
};

dagfuncs.dateParser = (value) => {
    if (value == null || value === '') {
        return undefined;
    }
    const dateParts = value.split('/');
    return dateParts.length === 3
        ? new Date(
            parseInt(dateParts[2]),
            parseInt(dateParts[1]) - 1,
            parseInt(dateParts[0])
        )
        : undefined;
}
dagfuncs.dateFormatter = (value) => {
    if (value == null) {
        return undefined;
    }
    const date = String(value.getDate());
    const month = String(value.getMonth() + 1);
    return `${date.length === 1 ? '0' + date : date}/${
        month.length === 1 ? '0' + month : month
    }/${value.getFullYear()}`;
}
// END test_cell_data_type_override.py

// BEGIN test_event_listeners.py

dagfuncs.showOutput = (params, setGridProps) => {
    const {colId, rowId, rowIndex, value} = params
    cellClicked = {colId, rowId, rowIndex, timestamp: Date.now(), value, contextMenu: true}
    setGridProps({'cellClicked': cellClicked})
}

// END test_event_listeners.py

// BEGIN test_pivot_column_order.py

dagfuncs.sortColumns = (a, b) => b.localeCompare(a)

// BEGIN test_pivot_column_order.py
