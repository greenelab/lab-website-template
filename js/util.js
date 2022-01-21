// normalize tag string to lower-case, single-space-separated, trimmed, etc
// (for purposes of comparing content/meaning of strings)
const normalizeString = (string) =>
  string
    .replaceAll(/^"|"$/g, "")
    .toLowerCase()
    .split(/\s|-|,/g)
    .map((word) => word.trim())
    .filter((word) => word)
    .join(" ");

// run a function after a delay
const debounce = (func, delay, key) => {
  window.clearTimeout(window[key]);
  window[key] = window.setTimeout(func, delay);
};
