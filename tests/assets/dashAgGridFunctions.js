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

dagfuncs.rowTest = function(params) {
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

    setProps = (props) => {
        if (props.value) {
            setYear(props.value)
        }
    }

    return React.createElement(
        window.dash_core_components.RadioItems,
        {
            options:[
                {'label': 'All', 'value': 'All'},
                {'label': 'Since 2010', 'value': '2010'},
            ],
            value: year,
            setProps
        }
        )
});