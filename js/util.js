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
