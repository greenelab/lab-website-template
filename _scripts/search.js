/*
  filters components on page based on url or search box.
  syntax: term1 term2 "full phrase 1" "full phrase 2" "tag: tag 1"
  match if: all terms AND at least one phrase AND at least one tag
*/

import { normalizeString, debounce } from "./util.js";

// components to filter
const componentSelector = ".card, .citation, .post-excerpt";
// search box element
const searchBoxSelector = ".search-box";
// results info box element
const infoBoxSelector = ".search-info";
// tags element
const tagSelector = ".tag";

// split search query into terms, phrases, and tags
const splitQuery = (query) => {
  // split into parts, preserve quotes
  const parts = query.match(/(".*?"|[^"\s]+)(?=\s*|\s*$)/g) || [];

  // bins
  const terms = [];
  const phrases = [];
  const tags = [];

  // put parts into bins
  for (let part of parts) {
    if (part.includes('"')) {
      part = normalizeString(part);
      if (part.indexOf("tag:") === 0) tags.push(part.replace(/tag:\s*/, ""));
      else phrases.push(part);
    } else {
      terms.push(normalizeString(part));
    }
  }

  return { terms, phrases, tags };
};

// get tooltip contents of element
const getTooltips = (element) =>
  [element, ...element.querySelectorAll("[data-tooltip]")]
    .map((element) => element.dataset.tooltip)
    .join(" ");

// determine if component should show up in results based on query
const componentMatches = (component, { terms, phrases, tags }) => {
  // tag elements within component
  const componentTags = [...component.querySelectorAll(".tag")];

  // check if text content exists in component
  const hasText = (string) =>
    normalizeString(component.innerText).includes(string) ||
    normalizeString(getTooltips(component)).includes(string);
  // check if text matches a tag in component
  const hasTag = (string) =>
    componentTags.some((tag) => normalizeString(tag.innerText) === string);

  // match logic
  return (
    (terms.every(hasText) || !terms.length) &&
    (phrases.some(hasText) || !phrases.length) &&
    (tags.some(hasTag) || !tags.length)
  );
};

// loop through components, hide/show based on query, and return results info
const filterComponents = (parts) => {
  let components = document.querySelectorAll(componentSelector);

  // results info
  let x = 0;
  let n = components.length;
  let tags = parts.tags;

  // filter components
  for (const component of components) {
    if (componentMatches(component, parts)) {
      component.style.display = "";
      x++;
      highlightTerms(component, parts);
    } else {
      component.style.display = "none";
    }
  }

  return [x, n, tags];
};

// reset highlights
const resetHighlights = () => {
  // make sure Mark library available
  if (typeof Mark === "undefined") return;

  new Mark(document.body).unmark();
};

// highlight search terms in component
const highlightTerms = async (component, { terms, phrases }) => {
  // make sure Mark library available
  if (typeof Mark === "undefined") return;

  // highlight terms
  // to avoid slowdown, only highlight if more than a few letters searched
  for (const term of terms)
    if (term.length > 2)
      new Mark(component).mark(term, { separateWordSearch: true });

  // highlight phrases
  for (const phrase of phrases)
    if (phrase.length > 2)
      new Mark(component).mark(phrase, { separateWordSearch: false });
};

// update search box based on query
const updateSearchBox = (query = "") => {
  const boxes = document.querySelectorAll(searchBoxSelector);

  for (const box of boxes) {
    const input = box.querySelector("input");
    const button = box.querySelector("button");
    const icon = box.querySelector("button i");
    input.value = query;
    icon.className = input.value.length
      ? "icon fa-solid fa-xmark"
      : "icon fa-solid fa-magnifying-glass";
    button.disabled = input.value.length ? false : true;
  }
};

// update info box based on query and results
const updateInfoBox = (query, x, n) => {
  const boxes = document.querySelectorAll(infoBoxSelector);

  if (query.trim()) {
    // show all info boxes
    boxes.forEach((info) => (info.style.display = ""));

    // info template
    let info = "";
    info += `Showing ${x.toLocaleString()} of ${n.toLocaleString()} results<br>`;
    info += "<a href='./'>Clear search</a>";

    // set info HTML string
    boxes.forEach((el) => (el.innerHTML = info));
  }
  // if nothing searched
  else {
    // hide all info boxes
    boxes.forEach((info) => (info.style.display = "none"));
  }
};

// update tags based on query
const updateTags = (query) => {
  const { tags } = splitQuery(query);
  document.querySelectorAll(tagSelector).forEach((tag) => {
    // set active if tag is in query
    if (tags.includes(normalizeString(tag.innerText)))
      tag.setAttribute("data-active", "");
    else tag.removeAttribute("data-active");
  });
};

// run search with query
const runSearch = (query = "") => {
  resetHighlights();
  const parts = splitQuery(query);
  const [x, n] = filterComponents(parts);
  updateSearchBox(query);
  updateInfoBox(query, x, n);
  updateTags(query);
};

// update url based on query
const updateUrl = (query = "") => {
  const url = new URL(window.location);
  let params = new URLSearchParams(url.search);
  params.set("search", query);
  url.search = params.toString();
  window.history.replaceState(null, null, url);
};

// search based on url param
const searchFromUrl = () => {
  const query = new URLSearchParams(window.location.search).get("search") || "";
  runSearch(query);
};

// when user types into search box
const debouncedRunSearch = debounce(runSearch, 1000);
window.onSearchInput = (target) => {
  debouncedRunSearch(target.value);
  updateUrl(target.value);
};

// when user clears search box with button
window.onSearchClear = () => {
  runSearch();
  updateUrl();
};

// after page loads
window.addEventListener("load", searchFromUrl);
// after tags load
window.addEventListener("tagsfetched", searchFromUrl);
