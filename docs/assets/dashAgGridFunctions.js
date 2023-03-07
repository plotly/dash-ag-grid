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