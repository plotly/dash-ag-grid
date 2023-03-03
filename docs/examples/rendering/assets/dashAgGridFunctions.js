

var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

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

