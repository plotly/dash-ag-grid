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
