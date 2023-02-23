// normalize string for purposes of comparing content/meaning
export const normalizeString = (string) =>
  string
    .replaceAll(/^"|"$/g, "")
    .toLowerCase()
    .split(/\s|-|,/g)
    .map((word) => word.trim())
    .filter((word) => word)
    .join(" ");

// return func that runs after delay
export const debounce = (callback, delay = 250) => {
  let timeout;
  return (...args) => {
    window.clearTimeout(timeout);
    timeout = window.setTimeout(() => callback(...args), delay);
  };
};
