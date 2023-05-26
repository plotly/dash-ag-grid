var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

// Used in the column spanning simple example
dagfuncs.simpleSpanning = function (params) {
    const country = params.data.country;
    if (country === 'Russia') {
        // have all Russia cells in column country of width of 2 columns
        return 2;
    } else if (country === 'United States') {
        // have all United States cells in column country of width of 4 columns
        return 4;
    } else {
        // all other rows should be just normal
        return 1;
    }
}
// end column spanning simple example

// Used in the column spanning complex example
function isHeaderRow(params) {
    return params.data.section === 'big-title';
}

function isQuarterRow(params) {
    return params.data.section === 'quarters';
}

dagfuncs.janColSpan = function (params) {
    if (isHeaderRow(params)) {
        return 6;
    } else if (isQuarterRow(params)) {
        return 3;
    } else {
        return 1;
    }
}

dagfuncs.aprColSpan = function (params) {
    if (isQuarterRow(params)) {
        return 3;
    } else {
        return 1;
    }
}

// end column spanning complex example