
filter_images= "https://user-images.githubusercontent.com/72614349/216053251-89ff7290-118b-4521-8ddf-42851cd0eb36.png"

"""
# Simple Filters
The grid provides three Simple Filters for filtering strings, numbers and dates.

Each of the filters works in a similar way. This page describes the common parts of the Simple Filters.

### Example: Simple Filters
The example below demonstrates all three Simple Filters working. Note the following:

- The Athlete column has a Text Filter.
- The Age column has a Number Filter.
- `filter=False` is set on the Total column to disable the filter.
Example: Provided Simple

```
```

### Simple Filter Parts
Each Simple Filter follows the same layout. The only layout difference is the type of input field presented to the user: for Text and Number Filters a text field is displayed, whereas for Date Filters a date picker field is displayed.

img

### Filter Options
Each filter provides a dropdown list of filter options to select from. Each filter option represents a filtering strategy, e.g. 'equals', 'not equals', etc.

Each filter's default Filter Options are listed below, as well as information on Defining Custom Filter Options.

### Filter Value
Each filter option takes zero (a possibility with custom options), one (for most) or two (for 'in range') values. The value type depends on the filter type, e.g. the Date Filter takes Date values.

### Condition 1 and Condition 2
Each filter initially only displays Condition 1. When the user completes the Condition 1 section of the filter, Condition 2 becomes visible.

### Join Operator
The Join Operator decides how Condition 1 and Condition 2 are joined, using either AND or OR.

### Simple Filters Parameters
Simple Filters are configured though the filterParams attribute of the column definition:


- filterOptions Array of filter options to present to the user. See Filter Options. 
- defaultOption (string) The default filter option to be selected.
- defaultJoinOperator - By default, the two conditions are combined using AND. You can change this default by setting this property. Options: AND, OR
- suppressAndOrCondition -If true, the filter will only allow one condition. Default: false
- alwaysShowBothConditions By default, only one condition is shown, and a second is made visible once a first condition
 has been entered. Set this to `True` to always show both conditions. In this case the second condition will be
  disabled until a first condition has been entered. Default: false
- filterPlaceholder -Placeholder text for the filter textbox
- buttons - Specifies the buttons to be shown in the filter, in the order they should be displayed in. The options are:
    - 'apply': If the Apply button is present, the filter is only applied after the user hits the Apply button.
    - 'clear': The Clear button will clear the (form) details of the filter without removing any active filters on the column.
    - 'reset': The Reset button will clear the details of the filter and any active filters on that column.
    - 'cancel': The Cancel button will discard any changes that have been made to the filter in the UI, restoring the applied model.
- closeOnApply -boolean If the Apply button is present, the filter popup will be closed immediately when the Apply or Reset button is clicked if this is set to true. Default: false
- debounceMs -number Overrides the default debounce time in milliseconds for the filter. Defaults are TextFilter and NumberFilter: 500ms. (These filters have text field inputs, so a short delay before the input is formatted and the filtering applied is usually appropriate).
- readOnly -boolean If set to true, disables controls in the filter to mutate its state. Normally this would be used in conjunction with the Filter API. See Read-only Filter UI. Default: false


### Example: Simple Filter Options
The following example demonstrates those configuration options that can be applied to any Simple Filter.

- The Athlete column shows a Text Filter with default behavior for all options.
- The Country column shows a Text Filter with filterOptions set to show a different list of available options, and defaultOption set to change the default option selected.
- The Age column has a Number Filter with alwaysShowBothConditions set to true so that both condition are always shown. The defaultJoinOperator is also set to 'OR' rather than the default ('AND').
- The Date column has a Date Filter with suppressAndOrCondition set to true, so that only the first condition is shown.


```
columnDefs: [
        { field: 'athlete' },
        {
          field: 'country',
          filterParams: {
            filterOptions: ['contains', 'startsWith', 'endsWith'],
            defaultOption: 'startsWith',
          },
        },
        {
          field: 'age',
          filter: 'agNumberColumnFilter',
          filterParams: {
            alwaysShowBothConditions: true,
            defaultJoinOperator: 'OR',
          },
          maxWidth: 100,
        },
        {
          field: 'date',
          filter: 'agDateColumnFilter',
          filterParams: filterParams,
        },
      ],
      defaultColDef: {
        flex: 1,
        minWidth: 150,
        filter: true,
      },
      rowData: null,
    };
  }

  onGridReady = (params) => {
    this.gridApi = params.api;
    this.gridColumnApi = params.columnApi;

    const updateData = (data) => params.api.setRowData(data);

    fetch('https://www.ag-grid.com/example-assets/olympic-winners.json')
      .then((resp) => resp.json())
      .then((data) => updateData(data));
  };

  render() {
    return (
      <div style={{ width: '100%', height: '100%' }}>
        <div
          style={{
            height: '100%',
            width: '100%',
          }}
          className="ag-theme-alpine"
        >
          <AgGridReact
            columnDefs={this.state.columnDefs}
            defaultColDef={this.state.defaultColDef}
            onGridReady={this.onGridReady}
            rowData={this.state.rowData}
          />
        </div>
      </div>
    );
  }
}

var filterParams = {
  suppressAndOrCondition: true,
  comparator: (filterLocalDateAtMidnight, cellValue) => {
    var dateAsString = cellValue;
    if (dateAsString == null) return -1;
    var dateParts = dateAsString.split('/');
    var cellDate = new Date(
      Number(dateParts[2]),
      Number(dateParts[1]) - 1,
      Number(dateParts[0])
    );
    if (filterLocalDateAtMidnight.getTime() === cellDate.getTime()) {
      return 0;
    }
    if (cellDate < filterLocalDateAtMidnight) {
      return -1;
    }
    if (cellDate > filterLocalDateAtMidnight) {
      return 1;
    }
    return 0;
  },
  browserDatePicker: true,
};

```

| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

### Simple Filter Options
Each simple filter presents a list of options to the user. The list of options for each filter are as follows:

| Option Name  | 	Option Key	 | Supported Filters  | 
| ------------ | --------------- | ----------------- |  
| Equals  | 	equals	 | Text, Number, Date | 
| Not Equals | 	notEqual	 | Text, Number, Date | 
| Contains	 | contains	 | Text | 
| Not Contains | 	notContains	 | Text | 
| Starts With	 | startsWith	 | Text | 
| Ends With	 | endsWith	 | Text | 
| Less Than	 | lessThan	 | Number, Date | 
| Less Than or Equal | 	lessThanOrEqual	 | Number | 
| Greater Than | 	greaterThan	 | Number, Date | 
| Greater Than or Equal	 | greaterThanOrEqual	 | Number | 
| In Range	 | inRange	 | Number, Date | 
| Blank	 | blank	Text,  | Number, Date | 
| Not blank | 	notBlank	 | Text, Number, Date | 
| Choose One | 	empty	 | Text, Number, Date | 

Note that the empty filter option is primarily used when creating Custom Filter Options. When 'Choose One' is displayed, the filter is not active.

### Default Filter Options
Each of the filter types has the following default options and default selected option.

 | Filter  | 	Default List of Options	 | Default Selected Option | 
  | ------ | -------------------------- | ------------------------ | 
 | Text	 | Contains, Not Contains, Equals, Not Equals, Starts With, Ends With.	 | Contains | 
 | Number  | 	Equals, Not Equals, Less Than, Less Than or Equal, Greater Than, Greater Than or Equal, In Range.	 | Equals | 
 | Date  | 	Equals, Greater Than, Less Than, Not Equals, In Range.	 | Equals | 



The following example demonstrates several custom filter options:

The Athlete column contains four custom filter options managed by a Text Filter:

- Starts with "A" and Starts with "N" have no inputs; their predicate function is provided zero values.
- Regular Expression has one input; its predicate function is provided one value.
- Between (Exclusive) has two inputs; its predicate function is provided two values.

The Age column contains five custom filter options managed by a Number Filter:

- Even Numbers, Odd Numbers and Blanks have no inputs; their predicate function is provided zero values.
- Age 5 Years Ago has one input; its predicate function is provided one value.
- Between (Exclusive) has two inputs; its predicate function is provided two values.
- Choose One is a built-in option and acts as an inactive filter option.
- The suppressAndOrCondition=true option is used to suppress the join operator panel and condition 2.

The Date column contains three custom filter options managed by a Date Filter:

- Equals (with Nulls) has one inputs; its predicate function is provided one value.
- Leap Year has no inputs; its predicate function is provided zero values.
- Between (Exclusive) has two inputs; its predicate function is provided two values.
- NOTE: a custom comparator is still required for the built-in date filter options, i.e. equals.

The Country column includes:

- a custom * Not Equals (No Nulls) * filter which also removes null values.
- it also demonstrates how localisation can be achieved via the gridOptions.getLocaleText(params) callback function, where the default value is replaced for the filter option 'notEqualNoNulls'.

Saving and restoring custom filter options via api.getFilterModel() and api.setFilterModel() can be tested using the provided buttons.


```
columnDefs: [
        {
          field: 'athlete',
          filterParams: containsFilterParams,
        },
        {
          field: 'age',
          minWidth: 120,
          filter: 'agNumberColumnFilter',
          filterParams: filterParams,
        },
        {
          field: 'date',
          filter: 'agDateColumnFilter',
          filterParams: equalsFilterParams,
        },
        {
          field: 'country',
          filterParams: notEqualsFilterParams,
        },
        { field: 'gold', filter: 'agNumberColumnFilter' },
        { field: 'silver', filter: 'agNumberColumnFilter' },
        { field: 'bronze', filter: 'agNumberColumnFilter' },
        { field: 'total', filter: false },
      ],
      defaultColDef: {
        flex: 1,
        minWidth: 150,
        sortable: true,
        filter: true,
      },
      getLocaleText: (params) => {
        if (params.key === 'notEqualNoNulls') {
          return '* Not Equals (No Nulls) *';
        }
        return params.defaultValue;
      },
      rowData: null,
    };
  }

  onGridReady = (params) => {
    this.gridApi = params.api;
    this.gridColumnApi = params.columnApi;

    const updateData = (data) => {
      this.setState({ rowData: data });
    };

    fetch('https://www.ag-grid.com/example-assets/small-olympic-winners.json')
      .then((resp) => resp.json())
      .then((data) => updateData(data));
  };

  printState = () => {
    var filterState = this.gridApi.getFilterModel();
    console.log('filterState: ', filterState);
  };

  saveState = () => {
    window.filterState = this.gridApi.getFilterModel();
    console.log('filter state saved');
  };

  restoreState = () => {
    this.gridApi.setFilterModel(window.filterState);
    console.log('filter state restored');
  };

  resetState = () => {
    this.gridApi.setFilterModel(null);
    console.log('column state reset');
  };

  render() {
    return (
      <div style={{ width: '100%', height: '100%' }}>
        <div className="example-wrapper">
          <div style={{ marginBottom: '5px' }}>
            <button onClick={() => this.printState()}>Print State</button>
            <button onClick={() => this.saveState()}>Save State</button>
            <button onClick={() => this.restoreState()}>Restore State</button>
            <button onClick={() => this.resetState()}>Reset State</button>
          </div>

          <div
            style={{
              height: '100%',
              width: '100%',
            }}
            className="ag-theme-alpine"
          >
            <AgGridReact
              columnDefs={this.state.columnDefs}
              defaultColDef={this.state.defaultColDef}
              getLocaleText={this.state.getLocaleText}
              onGridReady={this.onGridReady}
              rowData={this.state.rowData}
            />
          </div>
        </div>
      </div>
    );
  }
}

var filterParams = {
  filterOptions: [
    'empty',
    {
      displayKey: 'evenNumbers',
      displayName: 'Even Numbers',
      predicate: (_, cellValue) => cellValue != null && cellValue % 2 === 0,
      numberOfInputs: 0,
    },
    {
      displayKey: 'oddNumbers',
      displayName: 'Odd Numbers',
      predicate: (_, cellValue) => cellValue != null && cellValue % 2 !== 0,
      numberOfInputs: 0,
    },
    {
      displayKey: 'blanks',
      displayName: 'Blanks',
      predicate: (_, cellValue) => cellValue == null,
      numberOfInputs: 0,
    },
    {
      displayKey: 'age5YearsAgo',
      displayName: 'Age 5 Years Ago',
      predicate: ([fv1], cellValue) =>
        cellValue == null || cellValue - 5 === fv1,
      numberOfInputs: 1,
    },
    {
      displayKey: 'betweenExclusive',
      displayName: 'Between (Exclusive)',
      predicate: ([fv1, fv2], cellValue) =>
        cellValue == null || (fv1 < cellValue && fv2 > cellValue),
      numberOfInputs: 2,
    },
  ],
  suppressAndOrCondition: true,
};
var containsFilterParams = {
  filterOptions: [
    'contains',
    {
      displayKey: 'startsA',
      displayName: 'Starts With "A"',
      predicate: (_, cellValue) =>
        cellValue != null && cellValue.indexOf('A') === 0,
      numberOfInputs: 0,
    },
    {
      displayKey: 'startsN',
      displayName: 'Starts With "N"',
      predicate: (_, cellValue) =>
        cellValue != null && cellValue.indexOf('N') === 0,
      numberOfInputs: 0,
    },
    {
      displayKey: 'regexp',
      displayName: 'Regular Expression',
      predicate: ([fv1], cellValue) =>
        cellValue == null || new RegExp(fv1, 'gi').test(cellValue),
      numberOfInputs: 1,
    },
    {
      displayKey: 'betweenExclusive',
      displayName: 'Between (Exclusive)',
      predicate: ([fv1, fv2], cellValue) =>
        cellValue == null || (fv1 < cellValue && fv2 > cellValue),
      numberOfInputs: 2,
    },
  ],
};
var equalsFilterParams = {
  filterOptions: [
    'equals',
    {
      displayKey: 'equalsWithNulls',
      displayName: 'Equals (with Nulls)',
      predicate: ([filterValue], cellValue) => {
        if (cellValue == null) return true;
        var parts = cellValue.split('/');
        var cellDate = new Date(
          Number(parts[2]),
          Number(parts[1] - 1),
          Number(parts[0])
        );
        return cellDate.getTime() === filterValue.getTime();
      },
    },
    {
      displayKey: 'leapYear',
      displayName: 'Leap Year',
      predicate: (_, cellValue) => {
        if (cellValue == null) return true;
        const year = Number(cellValue.split('/')[2]);
        return year % 4 === 0 && year % 200 !== 0;
      },
      numberOfInputs: 0,
    },
    {
      displayKey: 'betweenExclusive',
      displayName: 'Between (Exclusive)',
      predicate: ([fv1, fv2], cellValue) => {
        if (cellValue == null) return true;
        var parts = cellValue.split('/');
        var cellDate = new Date(
          Number(parts[2]),
          Number(parts[1] - 1),
          Number(parts[0])
        );
        return (
          cellDate.getTime() > fv1.getTime() &&
          cellDate.getTime() < fv2.getTime()
        );
      },
      numberOfInputs: 2,
    },
  ],
  comparator: (filterLocalDateAtMidnight, cellValue) => {
    var dateAsString = cellValue;
    if (dateAsString == null) return -1;
    var dateParts = dateAsString.split('/');
    var cellDate = new Date(
      Number(dateParts[2]),
      Number(dateParts[1]) - 1,
      Number(dateParts[0])
    );
    if (filterLocalDateAtMidnight.getTime() === cellDate.getTime()) {
      return 0;
    }
    if (cellDate < filterLocalDateAtMidnight) {
      return -1;
    }
    if (cellDate > filterLocalDateAtMidnight) {
      return 1;
    }
    return 0;
  },
  browserDatePicker: true,
};
var notEqualsFilterParams = {
  filterOptions: [
    'notEqual',
    {
      displayKey: 'notEqualNoNulls',
      displayName: 'Not Equals without Nulls',
      predicate: ([filterValue], cellValue) => {
        if (cellValue == null) return false;
        return cellValue.toLowerCase() !== filterValue.toLowerCase();
      },
    },
  ],
};


```


### Blank Cells (Date and Number Filters)
If the row data contains blanks (i.e. null or undefined), by default the row won't be included in filter results. To change this, use the filter params includeBlanksInEquals, includeBlanksInLessThan, includeBlanksInGreaterThan and includeBlanksInRange. For example, the code snippet below configures a filter to include null for equals, but not for less than, greater than or in range:

```
const filterParams = {
    includeBlanksInEquals: true,
    includeBlanksInLessThan: false,
    includeBlanksInGreaterThan: false,
    includeBlanksInRange: false,
};

```
In the following example you can filter by age or date and see how blank values are included. Note the following:

- Columns Age and Date have both null and undefined values resulting in blank cells.
- Toggle the controls on the top to see how includeBlanksInEquals, includeBlanksInLessThan, includeBlanksInGreaterThan and includeBlanksInRange impact the search result.


AMW - Snippet?  app has radio buttons on the top
```
var filterParams = {
  comparator: (filterLocalDateAtMidnight, cellValue) => {
    var dateAsString = cellValue;
    if (dateAsString == null) return -1;
    var dateParts = dateAsString.split('/');
    var cellDate = new Date(
      Number(dateParts[2]),
      Number(dateParts[1]) - 1,
      Number(dateParts[0])
    );

    if (filterLocalDateAtMidnight.getTime() === cellDate.getTime()) {
      return 0;
    }

    if (cellDate < filterLocalDateAtMidnight) {
      return -1;
    }

    if (cellDate > filterLocalDateAtMidnight) {
      return 1;
    }
    return 0;
  },
  includeBlanksInEquals: false,
  includeBlanksInLessThan: false,
  includeBlanksInGreaterThan: false,
  includeBlanksInRange: false,
};

const columnDefs = [
  { field: 'athlete' },
  {
    field: 'age',
    maxWidth: 120,
    filter: 'agNumberColumnFilter',
    filterParams: {
      includeBlanksInEquals: false,
      includeBlanksInLessThan: false,
      includeBlanksInGreaterThan: false,
      includeBlanksInRange: false,
    },
  },
  {
    field: 'date',
    filter: 'agDateColumnFilter',
    filterParams: filterParams,
  },
  {
    headerName: 'Description',
    valueGetter: '"Age is " + data.age + " and Date is " + data.date',
    minWidth: 340,
  },
];

const gridOptions = {
  columnDefs: columnDefs,
  defaultColDef: {
    flex: 1,
    minWidth: 100,
    filter: true,
    resizable: true,
  },
};

function changeNull(toChange, value) {
  switch (toChange) {
    case 'equals':
      columnDefs[1].filterParams.includeBlanksInEquals = value;
      columnDefs[2].filterParams.includeBlanksInEquals = value;
      break;
    case 'lessThan':
      columnDefs[1].filterParams.includeBlanksInLessThan = value;
      columnDefs[2].filterParams.includeBlanksInLessThan = value;
      break;
    case 'greaterThan':
      columnDefs[1].filterParams.includeBlanksInGreaterThan = value;
      columnDefs[2].filterParams.includeBlanksInGreaterThan = value;
      break;
    case 'inRange':
      columnDefs[1].filterParams.includeBlanksInRange = value;
      columnDefs[2].filterParams.includeBlanksInRange = value;
      break;
  }

  var filterModel = gridOptions.api.getFilterModel();

  gridOptions.api.setColumnDefs(columnDefs);
  gridOptions.api.destroyFilter('age');
  gridOptions.api.destroyFilter('date');
  gridOptions.api.setFilterModel(filterModel);
}

// setup the grid after the page has finished loading
document.addEventListener('DOMContentLoaded', function () {
  var gridDiv = document.querySelector('#myGrid');
  new agGrid.Grid(gridDiv, gridOptions);

  gridOptions.api.setRowData([
    {
      athlete: 'Alberto Gutierrez',
      age: 36,
      country: 'Spain',
      year: '2017',
      date: null,
      sport: 'Squash',
      gold: 1,
      silver: 0,
      bronze: 0,
    },
    {
      athlete: 'Niall Crosby',
      age: 40,
      country: 'Spain',
      year: '2017',
      date: undefined,
      sport: 'Running',
      gold: 1,
      silver: 0,
      bronze: 0,
    },
    {
      athlete: 'Sean Landsman',
      age: null,
      country: 'Rainland',
      year: '2017',
      date: '25/10/2016',
      sport: 'Running',
      gold: 0,
      silver: 0,
      bronze: 1,
    },
    {
      athlete: 'Robert Clarke',
      age: undefined,
      country: 'Raveland',
      year: '2017',
      date: '25/10/2016',
      sport: 'Squash',
      gold: 0,
      silver: 0,
      bronze: 1,
    },
  ]);
});


```


### Data Updates
Grid data can be updated in a number of ways, including:

- Cell Editing.
- Updating Data.
- Clipboard Operations. (enterprise)
Simple filters are not affected by data changes, as is demonstrated by the following example:

-Perform some filtering using the configured simple filters, such as filtering by Age equals 24.
-Click the Jumble Ages button to update the grid data by jumbling values in the Age column between rows.
-Observe that filters remain unchanged, but the displayed rows change to those now assigned an age of 24.

```
this.state = {
      columnDefs: [
        { field: 'athlete' },
        { field: 'age', filter: 'agNumberColumnFilter', maxWidth: 100 },
        {
          field: 'date',
          filter: 'agDateColumnFilter',
          filterParams: filterParams,
        },
        { field: 'total', filter: false },
      ],
      defaultColDef: {
        flex: 1,
        minWidth: 150,
        filter: true,
      },
      rowData: null,
    };
  }

  onGridReady = (params) => {
    this.gridApi = params.api;
    this.gridColumnApi = params.columnApi;

    const updateData = (data) => {
      fetchedData = data.slice(0, 9);
      params.api.setRowData(fetchedData);
    };

    fetch('https://www.ag-grid.com/example-assets/olympic-winners.json')
      .then((resp) => resp.json())
      .then((data) => updateData(data));
  };

  jumbleData = () => {
    if (fetchedData) {
      const ages = fetchedData.map((d) => d.age);
      // Force reload by mutating fetched data - jumble the ages.
      const jumbledData = fetchedData.map((d) => {
        const randomAgeIndex = Math.round(Math.random() * (ages.length - 1));
        return { ...d, age: ages.splice(randomAgeIndex, 1)[0] };
      });
      this.gridApi.setRowData(jumbledData);
    }
  };

  render() {
    return (
      <div style={{ width: '100%', height: '100%' }}>
        <div className="example-wrapper">
          <div style={{ marginBottom: '5px' }}>
            <button onClick={() => this.jumbleData()}>Jumble Ages</button>
          </div>

          <div
            style={{
              height: '100%',
              width: '100%',
            }}
            className="ag-theme-alpine"
          >
            <AgGridReact
              columnDefs={this.state.columnDefs}
              defaultColDef={this.state.defaultColDef}
              onGridReady={this.onGridReady}
              rowData={this.state.rowData}
            />
          </div>
        </div>
      </div>
    );
  }
}

var filterParams = {
  comparator: (filterLocalDateAtMidnight, cellValue) => {
    var dateAsString = cellValue;
    if (dateAsString == null) return -1;
    var dateParts = dateAsString.split('/');
    var cellDate = new Date(
      Number(dateParts[2]),
      Number(dateParts[1]) - 1,
      Number(dateParts[0])
    );
    if (filterLocalDateAtMidnight.getTime() === cellDate.getTime()) {
      return 0;
    }
    if (cellDate < filterLocalDateAtMidnight) {
      return -1;
    }
    if (cellDate > filterLocalDateAtMidnight) {
      return 1;
    }
    return 0;
  },
  browserDatePicker: true,
};
var fetchedData;

```

### Style Header on Filter
Each time a filter is applied to a column the CSS class ag-header-cell-filtered is added to the header. This can be used for adding style to headers that are filtered.

In the example below, we've added some styling to ag-header-cell-filtered, so when you filter a column you will notice the column header change.

CSS

```
.ag-header-cell-filtered {
  background-color: #1b6d85 !important;
  color: #fff !important;
}

.ag-header-cell-filtered span {
  color: #fff !important;
}

```


```
 this.state = {
      columnDefs: [
        { field: 'athlete' },
        { field: 'age', maxWidth: 120 },
        { field: 'country' },
        { field: 'year', maxWidth: 120 },
        { field: 'sport' },
        { field: 'gold' },
        { field: 'silver' },
        { field: 'bronze' },
        { field: 'total' },
      ],
      defaultColDef: {
        flex: 1,
        minWidth: 150,
        filter: true,
        resizable: true,
      },
      rowData: null,
    };
  }

  onGridReady = (params) => {
    this.gridApi = params.api;
    this.gridColumnApi = params.columnApi;

    const updateData = (data) => params.api.setRowData(data);

    fetch('https://www.ag-grid.com/example-assets/olympic-winners.json')
      .then((resp) => resp.json())
      .then((data) => updateData(data));
  };

  render() {
    return (
      <div style={{ width: '100%', height: '100%' }}>
        <div
          style={{
            height: '100%',
            width: '100%',
          }}
          className="ag-theme-alpine"
        >
          <AgGridReact
            columnDefs={this.state.columnDefs}
            defaultColDef={this.state.defaultColDef}
            onGridReady={this.onGridReady}
            rowData={this.state.rowData}
          />
        </div>
      </div>
    );
  }
}

```



### Customising Filter Placeholder Text
Filter placeholder text can be customised on a per column basis using filterParams.filterPlaceholder within the grid option columnDefs. The placeholder can be either a string or a function as shown in the snippet below:
```
const columnDefs = [
    {
        field: 'age',
        filter: 'agNumberColumnFilter',
        filterParams: {
            filterPlaceholder: 'Age...'
        }
    },
    {
        field: 'total',
        filter: 'agNumberColumnFilter',
        filterParams: {
            filterPlaceholder: (params) => {
                const { filterOption, placeholder } = params;
                return `${filterOption} ${placeholder}`;
            }
        }
    }
];
```
When filterPlaceholder is a function, the parameters are made up of the following:

`filterOptionKey` ISimpleFilterModelType The filter option key
`filterOption` string The filter option name as localised text 
`placeholder` string The default placeholder text




The following example shows the various ways of specifying filter placeholders. Click on the filter menu for the different columns in the header row to see the following:

- Athlete column shows the default placeholder of Filter... with no configuration
- Country column shows the string Country... for all filter options
- Sport column shows the filter option key with the default placeholder eg, for the Contains filter option, it shows contains - Filter.... The filter option keys are listed in the table above.
- Total column shows the filter option name with the suffix total eg, for the Equals filter option, it shows Equals total. The filter option names are listed in the table above.

```
his.state = {
      columnDefs: [
        {
          field: 'athlete',
        },
        {
          field: 'country',
          filter: 'agTextColumnFilter',
          filterParams: {
            filterPlaceholder: 'Country...',
          },
        },
        {
          field: 'sport',
          filter: 'agTextColumnFilter',
          filterParams: {
            filterPlaceholder: (params) => {
              const { filterOptionKey, placeholder } = params;
              return `${filterOptionKey} - ${placeholder}`;
            },
          },
        },
        {
          field: 'total',
          filter: 'agNumberColumnFilter',
          filterParams: {
            filterPlaceholder: (params) => {
              const { filterOption } = params;
              return `${filterOption} total`;
            },
          },
        },
      ],
      defaultColDef: {
        flex: 1,
        sortable: true,
        filter: true,
      },
      rowData: null,
    };
  }

  onGridReady = (params) => {
    this.gridApi = params.api;
    this.gridColumnApi = params.columnApi;

    const updateData = (data) => params.api.setRowData(data);

    fetch('https://www.ag-grid.com/example-assets/olympic-winners.json')
      .then((resp) => resp.json())
      .then((data) => updateData(data));
  };

  render() {
    return (
      <div style={{ width: '100%', height: '100%' }}>
        <div
          style={{
            height: '100%',
            width: '100%',
          }}
          className="ag-theme-alpine"
        >
          <AgGridReact
            columnDefs={this.state.columnDefs}
            defaultColDef={this.state.defaultColDef}
            rowData={this.state.rowData}
            onGridReady={this.onGridReady}
          />
        </div>
      </div>
    );
  }
}
```

"""




