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


dagfuncs.filterParams = {
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
};