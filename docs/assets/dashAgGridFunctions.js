var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.Round = function(v, a=2) {
    return Math.round(v * (10**a)) / (10**a)
}

dagfuncs.toFixed = function(v, a=2) {
    return Number(v).toFixed(a)
}

dagfuncs.addEdits = function(params) {
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

dagfuncs.highlightEdits = function(params) {
    if (params.data.changes) {
    if (JSON.parse(params.data.changes).includes(params.colDef.field))
        {return true}
    }
    return false;
}


dagfuncs.Intl = Intl

dagfuncs.EUR = function(number) {
  return Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(number);
}


dagfuncs.JPY = function(number) {
  return Intl.NumberFormat('ja-JP', { style: 'currency', currency: 'JPY' }).format(number)
}


dagfuncs.USD = function(number) {
  return Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(number);
}


dagfuncs.CAD = function(number) {
  return Intl.NumberFormat('en-CA', { style: 'currency', currency: 'CAD', currencyDisplay: 'code' }).format(number);
}


dagfuncs.PercentageFilna = function(number, filna="") {
    if (isNaN(number)){
        return filna
    }
    return Intl.NumberFormat("en-US", {style: "percent"}).format(number)
}



dagfuncs.MoneyFilna = function(number, filna="") {
    if (isNaN(number)){
        return filna
    }
    return Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(number);
}


// Used in the row spanning example
dagfuncs.rowSpan = function(params) {
  var athlete = params.data ? params.data.athlete : undefined;
  if (athlete === 'Aleksey Nemov') {
    // have all Russia age columns width 2
    return 2;
  } else if (athlete === 'Ryan Lochte') {
    // have all United States column width 4
    return 4;
  } else {
    // all other rows should be just normal
    return 1;
  }
}


// used in the Enterprise Aggregation Custom Functions example

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



// Used in the column spanning example
function isHeaderRow(params) {
  return params.data.section === 'big-title';
}
function isQuarterRow(params) {
  return params.data.section === 'quarters';
}

dagfuncs.janColSpan = function(params) {
    if (isHeaderRow(params)) {
      return 6;
    } else if (isQuarterRow(params)) {
      return 3;
    } else {
      return 1;
    }
}

dagfuncs.aprColSpan = function(params) {
    if (isQuarterRow(params)) {
      return 3;
    } else {
      return 1;
    }
}
// end column spanning example


// used in the cell editor example

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

}


// used in the tree data example
dagfuncs.getDataPath = function (data) {
    return data.orgHierarchy;
}



// used in cell editors dynamic options example
dagfuncs.dynamicOptions = function(params) {
    const selectedCountry = params.data.country;
    if (selectedCountry === 'United States') {
        return {
            values: ['Boston', 'Chicago', 'San Francisco'],
        };
    } else {
        return {
            values: ['Montreal', 'Vancouver', 'Calgary']
        };
    }
}



// Used in the conditional rendering example
dagfuncs.moodOrGender = function (params) {
  var dagcomponentfuncs = window.dashAgGridComponentFunctions
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
}


// Custom number input - used in Editing/cell editors example
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
    this.eInput.type = "number";
    this.eInput.min = params.min;
    this.eInput.max = params.max;
    this.eInput.step = params.step || "any";
    this.eInput.required =  params.required;
    this.eInput.placeholder =  params.placeholder || "";
    this.eInput.name = params.name;
    this.eInput.disabled = params.disabled;
    this.eInput.title = params.title || ""
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


// Used in the layout & Style cell styling heatmap example
function rgbToHex(r, g, b) {
    return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
};

dagfuncs.heatMap = function (props) {
    const min = props.colDef.cellRendererParams.min;
    const max = props.colDef.cellRendererParams.max;
    const val = props.value;

    if(val) {
        if(val > 0) {
            g = 255;
            r = b = Math.round(255 * (1 - val / max));
        }
        else {
            r = 255;
            g = b = Math.round(255 * (1 - val / min));
        };

        return {
            backgroundColor: rgbToHex(r, g, b),
            color: 'black',
        }
    }
    else {
        return {};
    }
};
// end



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
                style: {width: params.column.actualWidth},
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
                style: params.style,
                styles: params.styles,
                switchDirectionOnFlip: params.switchDirectionOnFlip,
                variant: params.variant,
                zIndex: params.zIndex,
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
// end dmc.Select




// Used in the row sorting custom comparator example
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
  return (yearNumber * 10000) + (monthNumber * 100) + dayNumber;
}
// end custom comparator example


