var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

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