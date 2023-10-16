var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};


// Used in the layout & Style cell styling heatmap example
function rgbToHex(r, g, b) {
    return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
};

dagfuncs.heatMap = function (props) {
    const min = props.colDef.cellRendererParams.min;
    const max = props.colDef.cellRendererParams.max;
    const val = props.value;

    if(val) {
        if(val > 0) {
            g = 255;
            r = b = Math.round(255 * (1 - val / max));
        }
        else {
            r = 255;
            g = b = Math.round(255 * (1 - val / min));
        };

        return {
            backgroundColor: rgbToHex(r, g, b),
            color: 'black',
        }
    }
    else {
        return {};
    }
};
// end