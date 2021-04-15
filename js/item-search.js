// item search plugin
// filters items on page based on url or search box
// syntax: term1 term2 "full phrase 1" "full phrase 2" "tag: tag 1"

// items to filter
const itemQuery = ".card, .citation, .post_excerpt";
// search box element
const boxQuery = ".search_box input";
// results info element
const infoQuery = ".search_info";

// normalize tag string to lower-case, single-space-separated, trimmed, etc
const cleanTag = (tag) =>
  tag
    .toLowerCase()
    .split(/\s|-|,|tag:/g)
    .map((w) => w.trim())
    .filter((w) => w)
    .join(" ");

// split search query into terms, phrases, and tags
const splitQuery = (query) => {
  // split into parts by spaces but preserve quoted sub-strings
  const parts = (query.match(/(".*?"|[^"\s]+)(?=\s*|\s*$)/g) || [])
    .map((string) => string.trim().toLowerCase())
    .filter((string) => string);

  // bins
  const terms = [];
  const phrases = [];
  const tags = [];

  // put parts into bins
  for (let part of parts) {
    if (part.includes('"')) {
      part = part.split('"').join("");
      if (part.indexOf("tag:") === 0) tags.push(cleanTag(part));
      else phrases.push(part);
    } else {
      terms.push(part);
    }
  }

  return { terms, phrases, tags };
};

// determine if item should show up in results based on query
const showItem = (item, { terms, phrases, tags }) => {
  // tag elements within item
  const itemTags = Array.from(item.querySelectorAll(".tag"));

  // check if text content exists in item
  const hasText = (string) => item.innerText.toLowerCase().includes(string);
  // check if text matches a tag in item
  const hasTag = (string) =>
    itemTags.some((tag) => cleanTag(tag.innerText) === string);

  // show item if it has:
  // all terms AND at least one phrase AND at least one tag
  return (
    (terms.every(hasText) || !terms.length) &&
    (phrases.some(hasText) || !phrases.length) &&
    (tags.some(hasTag) || !tags.length)
  );
};

// util func to debounce search
const debounce = (func, delay) => (...args) => {
  window.clearTimeout(window.item_search_timer);
  window.item_search_timer = window.setTimeout(() => func(...args), delay);
};

// search and filter items
const searchItems = debounce((query) => {
  // split query into parts
  const parts = splitQuery(query);

  // reset highlights
  resetHighlights();

  // hide/show items
  let count = 0;
  const items = document.querySelectorAll(itemQuery);
  for (const item of items) {
    if (showItem(item, parts)) {
      item.dataset.hide = false;
      // count if shown
      count++;
      // highlight query words
      highlightTerms(item, parts);
    } else {
      item.dataset.hide = true;
    }
  }

  // update search box
  const updateBox = (element) => (element.value = query);
  document.querySelectorAll(boxQuery).forEach(updateBox);

  // update results info
  const updateInfo = (element) => {
    element.innerHTML = element.dataset.text
      .replace(/\X/g, count.toLocaleString())
      .replace(/\N/g, items.length.toLocaleString());
    element.dataset.hide = false;
  };
  document.querySelectorAll(infoQuery).forEach(updateInfo);
}, 200);

// reset mark.js highlights
const resetHighlights = () => new Mark(document.body).unmark();

// highlight search terms with mark.js
const highlightTerms = (item, { terms, phrases, tags }) => {
  // to avoid slowdown, only highlight if more than a few letters searched
  for (const term of terms)
    if (term.length > 2)
      new Mark(item).mark(term, { separateWordSearch: true });
  for (const phrase of phrases)
    if (phrase.length > 2)
      new Mark(item).mark(phrase, { separateWordSearch: false });
};

// search based on url param
const urlSearch = () => {
  const query = new URLSearchParams(window.location.search).get("search") || "";
  searchItems(query.trim());
};

// start script and add triggers
window.addEventListener("load", urlSearch);
window.addEventListener("tagsfetched", urlSearch);
