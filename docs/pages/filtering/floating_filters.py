
img = "https://user-images.githubusercontent.com/72614349/216128136-440a471a-0383-4262-bdbe-7c95e50faf5a.png)"


txt = """

Floating Filters
Floating Filters are an additional row under the column headers where the user will be able to see and optionally edit the filters associated with each column.

Floating filters are activated by setting the property floatingFilter = true on the colDef:

const columnDefs = [
    // column definition with floating filter enabled
    {
        field: 'country',
        filter: true,
        floatingFilter: true
    }
];


To have floating filters on for all columns by default, you should set floatingFilter on the defaultColDef. You can then disable floating filters on a per-column basis by setting floatingFilter = false on an individual colDef.

Floating filters depend on and co-ordinate with the main column filters. They do not have their own state, but rather display the state of the main filter and set state on the main filter if they are editable. For this reason, there is no API for getting or setting state of the floating filters.

Every floating filter takes a parameter to show/hide automatically a button that will open the main filter.

To see how floating filters work see Floating Filter Components.

The following example shows the following features of floating filters:

- Text filter: has out of the box read/write floating filter (Sport column)
- Set filter: has out of the box read-only floating filter (Country column)
- Date and Number filter: have out of the box read/write floating filters for all filters except when switching to in-range filtering, where the floating filter is read-only (Age and Date columns)
- Columns with buttons containing 'apply' require the user to press Enter on the floating filter for the filter to take effect (Gold column). (Note: this does not apply to floating Date Filters, which are always applied as soon as a valid date is entered.)
- Changes made directly to the main filter are reflected automatically in the floating filters (change any main filter)
- Columns with a custom filter have an automatic read-only floating filter if the custom filter implements the method getModelAsString() (Athlete column)
- The user can configure when to show/hide the button that shows the full filter (Silver and Bronze columns)
- The Year column has a filter, but has the floating filter disabled
- The Total column has no filter and therefore no floating filter either
- Combining suppressMenu = true and filter = false lets you control where the user can access the full filter. In this example suppressMenu = true for all the columns except Year, Silver and Bronze

```
this.state = {
      columnDefs: [
        { field: 'athlete', filter: PersonFilter, suppressMenu: true },
        { field: 'age', filter: 'agNumberColumnFilter', suppressMenu: true },
        { field: 'country', filter: 'agSetColumnFilter', suppressMenu: true },
        {
          field: 'year',
          maxWidth: 120,
          filter: 'agNumberColumnFilter',
          floatingFilter: false,
        },
        {
          field: 'date',
          minWidth: 215,
          filter: 'agDateColumnFilter',
          filterParams: dateFilterParams,
          suppressMenu: true,
        },
        { field: 'sport', suppressMenu: true, filter: 'agTextColumnFilter' },
        {
          field: 'gold',
          filter: 'agNumberColumnFilter',
          filterParams: {
            buttons: ['apply'],
          },
          suppressMenu: true,
        },
        {
          field: 'silver',
          filter: 'agNumberColumnFilter',
          floatingFilterComponentParams: {
            suppressFilterButton: true,
          },
        },
        {
          field: 'bronze',
          filter: 'agNumberColumnFilter',
          floatingFilterComponentParams: {
            suppressFilterButton: true,
          },
        },
        { field: 'total', filter: false },
      ],
      defaultColDef: {
        flex: 1,
        minWidth: 150,
        filter: true,
        sortable: true,
        floatingFilter: true,
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

  irelandAndUk = () => {
    var countryFilterComponent = this.gridApi.getFilterInstance('country');
    countryFilterComponent.setModel({ values: ['Ireland', 'Great Britain'] });
    this.gridApi.onFilterChanged();
  };

  clearCountryFilter = () => {
    var countryFilterComponent = this.gridApi.getFilterInstance('country');
    countryFilterComponent.setModel(null);
    this.gridApi.onFilterChanged();
  };

  destroyCountryFilter = () => {
    this.gridApi.destroyFilter('country');
  };

  endingStan = () => {
    var countryFilterComponent = this.gridApi.getFilterInstance('country');
    var countriesEndingWithStan = countryFilterComponent
      .getFilterKeys()
      .filter(function (value) {
        return value.indexOf('stan') === value.length - 4;
      });
    countryFilterComponent.setModel({ values: countriesEndingWithStan });
    this.gridApi.onFilterChanged();
  };

  printCountryModel = () => {
    var countryFilterComponent = this.gridApi.getFilterInstance('country');
    var model = countryFilterComponent.getModel();
    if (model) {
      console.log('Country model is: ' + JSON.stringify(model));
    } else {
      console.log('Country model filter is not active');
    }
  };

  sportStartsWithS = () => {
    var sportsFilterComponent = this.gridApi.getFilterInstance('sport');
    sportsFilterComponent.setModel({
      type: 'startsWith',
      filter: 's',
    });
    this.gridApi.onFilterChanged();
  };

  sportEndsWithG = () => {
    var sportsFilterComponent = this.gridApi.getFilterInstance('sport');
    sportsFilterComponent.setModel({
      type: 'endsWith',
      filter: 'g',
    });
    this.gridApi.onFilterChanged();
  };

  sportsCombined = () => {
    var sportsFilterComponent = this.gridApi.getFilterInstance('sport');
    sportsFilterComponent.setModel({
      condition2: {
        type: 'endsWith',
        filter: 'g',
      },
      operator: 'AND',
      condition1: {
        type: 'startsWith',
        filter: 's',
      },
    });
    this.gridApi.onFilterChanged();
  };

  ageBelow25 = () => {
    var ageFilterComponent = this.gridApi.getFilterInstance('age');
    ageFilterComponent.setModel({
      type: 'lessThan',
      filter: 25,
      filterTo: null,
    });
    this.gridApi.onFilterChanged();
  };

  ageAbove30 = () => {
    var ageFilterComponent = this.gridApi.getFilterInstance('age');
    ageFilterComponent.setModel({
      type: 'greaterThan',
      filter: 30,
      filterTo: null,
    });
    this.gridApi.onFilterChanged();
  };

  ageBelow25OrAbove30 = () => {
    var ageFilterComponent = this.gridApi.getFilterInstance('age');
    ageFilterComponent.setModel({
      condition1: {
        type: 'greaterThan',
        filter: 30,
        filterTo: null,
      },
      operator: 'OR',
      condition2: {
        type: 'lessThan',
        filter: 25,
        filterTo: null,
      },
    });
    this.gridApi.onFilterChanged();
  };

  ageBetween25And30 = () => {
    var ageFilterComponent = this.gridApi.getFilterInstance('age');
    ageFilterComponent.setModel({
      type: 'inRange',
      filter: 25,
      filterTo: 30,
    });
    this.gridApi.onFilterChanged();
  };

  clearAgeFilter = () => {
    var ageFilterComponent = this.gridApi.getFilterInstance('age');
    ageFilterComponent.setModel(null);
    this.gridApi.onFilterChanged();
  };

  after2010 = () => {
    var dateFilterComponent = this.gridApi.getFilterInstance('date');
    dateFilterComponent.setModel({
      type: 'greaterThan',
      dateFrom: '2010-01-01',
      dateTo: null,
    });
    this.gridApi.onFilterChanged();
  };

  before2012 = () => {
    var dateFilterComponent = this.gridApi.getFilterInstance('date');
    dateFilterComponent.setModel({
      type: 'lessThan',
      dateFrom: '2012-01-01',
      dateTo: null,
    });
    this.gridApi.onFilterChanged();
  };

  dateCombined = () => {
    var dateFilterComponent = this.gridApi.getFilterInstance('date');
    dateFilterComponent.setModel({
      condition1: {
        type: 'lessThan',
        dateFrom: '2012-01-01',
        dateTo: null,
      },
      operator: 'OR',
      condition2: {
        type: 'greaterThan',
        dateFrom: '2010-01-01',
        dateTo: null,
      },
    });
    this.gridApi.onFilterChanged();
  };

  clearDateFilter = () => {
    var dateFilterComponent = this.gridApi.getFilterInstance('date');
    dateFilterComponent.setModel(null);
    this.gridApi.onFilterChanged();
  };

  render() {
    return (
      <div style={{ width: '100%', height: '100%' }}>
        <div
          style={{ height: '100%', display: 'flex', flexDirection: 'column' }}
        >
          <div>
            <span className="button-group">
              <button onClick={() => this.irelandAndUk()}>
                Ireland &amp; UK
              </button>
              <button onClick={() => this.endingStan()}>
                Countries Ending 'stan'
              </button>
              <button onClick={() => this.printCountryModel()}>
                Print Country
              </button>
              <button onClick={() => this.clearCountryFilter()}>
                Clear Country
              </button>
              <button onClick={() => this.destroyCountryFilter()}>
                Destroy Country
              </button>
            </span>
            <span className="button-group">
              <button onClick={() => this.ageBelow25()}>Age Below 25</button>
              <button onClick={() => this.ageAbove30()}>Age Above 30</button>
              <button onClick={() => this.ageBelow25OrAbove30()}>
                Age Below 25 or Above 30
              </button>
              <button onClick={() => this.ageBetween25And30()}>
                Age Between 25 and 30
              </button>
              <button onClick={() => this.clearAgeFilter()}>
                Clear Age Filter
              </button>
            </span>
            <span className="button-group">
              <button onClick={() => this.after2010()}>
                Date after 01/01/2010
              </button>
              <button onClick={() => this.before2012()}>
                Date before 01/01/2012
              </button>
              <button onClick={() => this.dateCombined()}>Date combined</button>
              <button onClick={() => this.clearDateFilter()}>
                Clear Date Filter
              </button>
            </span>
            <span className="button-group">
              <button onClick={() => this.sportStartsWithS()}>
                Sport starts with S
              </button>
              <button onClick={() => this.sportEndsWithG()}>
                Sport ends with G
              </button>
              <button onClick={() => this.sportsCombined()}>
                Sport starts with S and ends with G
              </button>
            </span>
          </div>

          <div style={{ flexGrow: '1', height: '10px' }}>
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
      </div>
    );
  }
}

var dateFilterParams = {
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

### Provided Floating Filters
All the default filters provided by the grid provide their own implementation of a floating filter. All you need to do to enable these floating filters is set the floatingFilter = true column property. The features of the provided floating filters are as follows:

 | Filter  | 	Editable  | 	Description | 
  | ----- | -------- | ----------- | 
 | Text | 	Sometimes | 	Provides a text input field to display the filter value, or a read-only label if read-only. | 
 | Number | 	Sometimes | 	Provides a text input field to display the filter value, or a read-only label if read-only. | 
 | Date	 | Sometimes | 	Provides a date input field to display the filter value, or a read-only label if read-only. | 
 | Set	 | No | 	Provides a read-only label by concatenating all selected values. | 


The floating filters for Text, Number and Date (the simple filters) are editable when the filter has one condition and one value. If the floating filter has a) two conditions or b) zero (custom option) or two ('In Range') values, the floating filter is read-only.

The screen shots below show example scenarios where the provided Number floating filter is editable and read-only.

![image](https://user-images.githubusercontent.com/72614349/216128136-440a471a-0383-4262-bdbe-7c95e50faf5a.png)
"""