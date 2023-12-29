export default function debounce(fn, wait, onDebounce) {
    let lastTimestamp = 0;
    let handle;

    return (...args) => {
        const now = Date.now();
        const delay = Math.min(now - lastTimestamp, wait);

        if (onDebounce) {
            onDebounce(...args)
        }
        if (handle) {
            clearTimeout(handle);
        }

        handle = setTimeout(() => {
            fn(...args);
            lastTimestamp = Date.now();
        }, delay);
    };
}
