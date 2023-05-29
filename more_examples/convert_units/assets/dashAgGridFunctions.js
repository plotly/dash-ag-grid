var dagfuncs = (window.dashAgGridFunctions = window.dashAgGridFunctions || {});

dagfuncs.bytes = () => {
    return {
        allowedCharPattern: '\\d(.)+\\(?:B|KB|MB|GB|TB|PB)',
        numberParser: (text) => {
            if (text == null) {
                return null;
            } else {
                const pattern = /(^[0-9.]+)?([BKMGT]?B)$/i;
                const match = text.match(pattern);
                if (match) {
                    const number = parseFloat(match[1]);
                    const unit = match[2].toUpperCase();
                    const units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB'];
                    const multiplier = Math.pow(1024, units.indexOf(unit));
                    return number * multiplier;
                } else {
                    return text;
                }
            }
        },
    };
};

dagfuncs.convertUnits = function (x) {
    const units = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB'];
    if (isNaN(x)) {
        return 'N/A';
    } else {
        const unitIndex = Math.min(
            Math.floor(Math.log2(x) / 10),
            units.length - 1
        );
        const convertedValue = x / 2 ** (10 * unitIndex);
        return `${convertedValue.toFixed(2)}${units[unitIndex]}`;
    }
};
