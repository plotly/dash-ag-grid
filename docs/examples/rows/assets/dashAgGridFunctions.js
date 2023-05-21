var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

// Used in Row Spanning Simple Example
dagfuncs.rowSpan = function (params) {
    var athlete = params.data ? params.data.athlete : undefined;
    if (athlete === 'Aleksey Nemov') {
        // have all Aleksey Nemov cells in column athlete of height of 2 rows
        return 2;
    } else if (athlete === 'Ryan Lochte') {
        // have all Ryan Lochte cells in column athlete of height of 4 rows
        return 4;
    } else {
        // all other rows should be just normal
        return 1;
    }
}

// Used in Row Spanning Complex Example
dagfuncs.rowSpanComplex = function (params) {
    if (params.data.show) {
        return 4;
    } else {
        return 1;
    }
}

dagfuncs.numberComparator = function (val1, val2) {
    console.log(val1, val2);
    return val2 - val1
}

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

// Used in the row sorting - post sort example
dagfuncs.postSort = function (params) {
    const rowNodes = params.nodes;
    // here we put Michael Phelps rows on top while preserving the sort order
    let nextInsertPos = 0;
    for (let i = 0; i < rowNodes.length; i++) {
        const athlete = rowNodes[i].data ? rowNodes[i].data.athlete : undefined;
        if (athlete === 'Michael Phelps') {
            rowNodes.splice(nextInsertPos, 0, rowNodes.splice(i, 1)[0]);
            nextInsertPos++;
        }
    }
}
// end row sorting - post sort example

// Used in the row dragging - Custom Row Drag Text example and Custom Row Drag Text with Multiple Draggers example
const hostCities = {2000: "Sydney", 2004: "Athens", 2008: "Beijing", 2012: "London",}

dagfuncs.rowDragText = function (params) {
    const {year} = params.rowNode.data;
    if (year in hostCities) {
        return `${params.defaultTextValue} (${hostCities[year]} Olympics)`
    }
    return params.defaultTextValue;
}

// added for multi draggers
dagfuncs.athleteRowDragText = function (params) {
    return `${params.rowNodes.length} athlete(s) selected`
}
// end row dragging - Custom Row Drag Text example  and Custom Row Drag Text with Multiple Draggers example
