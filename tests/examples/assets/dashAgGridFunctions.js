var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};
dagfuncs.Round = function (v, a = 2) {
    return Math.round(v * (10 ** a)) / (10 ** a)
}

dagfuncs.toFixed = function (v, a = 2) {
    return Number(v).toFixed(a)
}

dagfuncs.myTextFormatter = (text) => {
    if (text == null) return null;
    return text
        .toLowerCase()
        .replace(/[àáâãäå]/g, 'a')
        .replace(/æ/g, 'ae')
        .replace(/ç/g, 'c')
        .replace(/[èéêë]/g, 'e')
        .replace(/[ìíîï]/g, 'i')
        .replace(/ñ/g, 'n')
        .replace(/[òóôõö]/g, 'o')
        .replace(/œ/g, 'oe')
        .replace(/[ùúûü]/g, 'u')
        .replace(/[ýÿ]/g, 'y');
}

function contains(target, lookingFor) {
    return target && target.indexOf(lookingFor) >= 0;
}

dagfuncs.myTextMatcher = ({value, filterText}) => {
    const aliases = {
        usa: "united states",
        holland: "netherlands",
        niall: "ireland",
        sean: "south africa",
        alberto: "mexico",
        john: "australia",
        xi: "china",
    };
    const literalMatch = contains(value, filterText || "");
    return literalMatch || contains(value, aliases[filterText || ""]);
}

dagfuncs.myNumberParser = (text) => {
    return text === null ? null : parseFloat(text.replace(",", ".").replace("$", ""));
}
dagfuncs.myNumberFormatter = (value) => {
    return value === null ? null : value.toString().replace(".", ",");
}

dagfuncs.startWith = ([filterValues], cellValue) => {
    const name = cellValue ? cellValue.split(" ")[1] : ""
    return name && name.toLowerCase().indexOf(filterValues.toLowerCase()) === 0
}

dagfuncs.quickFilterMatcher = (quickFilterParts, rowQuickFilterAggregateText) => {
    return quickFilterParts.every(part => rowQuickFilterAggregateText.match(part));
}

dagfuncs.dateParser = (value) => {
    if (value == null || value === '') {
        return undefined;
    }
    const dateParts = value.split('/');
    return dateParts.length === 3
        ? new Date(
            parseInt(dateParts[2]),
            parseInt(dateParts[1]) - 1,
            parseInt(dateParts[0])
        )
        : undefined;
}
dagfuncs.dateFormatter = (value) => {
    if (value == null) {
        return undefined;
    }
    const date = String(value.getDate());
    const month = String(value.getMonth() + 1);
    return `${date.length === 1 ? '0' + date : date}/${
        month.length === 1 ? '0' + month : month
    }/${value.getFullYear()}`;
}

dagfuncs.dataTypeDefinitions = {
    percentage: {
        baseDataType: "number",
        extendsDataType: "number",
        valueFormatter: (params) => params.value == null ? '' : (Math.round(params.value * 1000) / 10).toFixed(1) + '%'
    },

    dateString: {
        baseDataType: 'dateString',
        extendsDataType: 'dateString',
        valueParser: (params) => {
            return params.newValue != null &&
            !!params.newValue.match(/\d{2}\/\d{2}\/\d{4}/)
                ? params.newValue
                : null
        },
        valueFormatter: (params) => {
            return params.value == null ? '' : params.value
        },
        dataTypeMatcher: (value) => {
            return typeof value === 'string' && !!value.match(/\d{2}\/\d{2}\/\d{4}/)
        },
        dateParser: (value) => {
            if (value == null || value === '') {
                return undefined;
            }
            const dateParts = value.split('/');
            return dateParts.length === 3
                ? new Date(
                    parseInt(dateParts[2]),
                    parseInt(dateParts[1]) - 1,
                    parseInt(dateParts[0])
                )
                : undefined;
        },
        dateFormatter: (value) => {
            if (value == null) {
                return undefined;
            }
            const date = String(value.getDate());
            const month = String(value.getMonth() + 1);
            return `${date.length === 1 ? '0' + date : date}/${
                month.length === 1 ? '0' + month : month
            }/${value.getFullYear()}`;
        },
    },
};
