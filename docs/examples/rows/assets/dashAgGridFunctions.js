

var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

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