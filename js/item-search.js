// item search plugin
// pairs with "item search" component
// filters items on page based on what is typed in search box

let searchInput = ".item_search_input"; // search box
let searchCount = ".item_search_count"; // "showing X of N results"
let items = ".card, .citation"; // items to filter

const createSearch = () => {
  // get important elements
  searchInput = document.querySelector(searchInput);
  searchCount = document.querySelector(searchCount);
  items = Array.from(document.querySelectorAll(items));

  // don't run script if necessary elements aren't present
  if (!searchInput || !items.length) return;

  // attach filter function to search box input
  searchInput.addEventListener("input", debounce(filterItems, 50));

  // enable search input to indicate that script has finished loading
  searchInput.removeAttribute("disabled");

  // get url param and search
  loadUrlSearch();
  filterItems();
};

// determine if string is a term (single word) or phrase (quoted multiple words)
const isPhrase = (str) => /\s/g.test(str);

// determine if item should show up in results based on query
const showItem = (item, query) => {
  // if nothing searched, show
  if (!query.length) return true;
  // get item text content
  item = item.innerText.toLowerCase();
  // get arrays of terms and phrases
  let terms = query.filter((string) => !isPhrase(string));
  let phrases = query.filter((string) => isPhrase(string));
  // func to check if string is in item text
  const includes = (string) => item.includes(string);
  // show item if all terms match, and at least one phrase matches
  // pass test if terms or phrases empty
  terms = terms.length ? terms.every(includes) : true;
  phrases = phrases.length ? phrases.some(includes) : true;
  return terms && phrases;
};

// split search string into array of terms and phrases
const parseQuery = (string) =>
  (string.match(/(".*?"|[^"\s]+)(?=\s*|\s*$)/g) || [])
    .map((string) => string.split('"').join("").trim().toLowerCase())
    .filter((string) => string);

// filter items
const filterItems = () => {
  // get search box text
  const query = parseQuery(searchInput.value);

  // reset highlights
  resetHighlights();

  // hide/show items
  let count = 0;
  for (const item of items) {
    if (showItem(item, query)) {
      item.dataset.hide = false;
      // count if shown
      count++;
      // highlight query words
      highlightTerms(item, query);
    } else item.dataset.hide = true;
  }

  // update results info
  if (searchCount)
    searchCount.innerHTML =
      count.toLocaleString() + " of " + items.length.toLocaleString();
};

// reset mark.js highlights
const resetHighlights = () => new Mark(document.body).unmark();

// highlight search terms with mark.js
const highlightTerms = (item, query) => {
  // to avoid slowdown, only highlight if more than a few letters typed in
  for (const string of query)
    if (string.length > 2) {
      new Mark(item).mark(string, {
        separateWordSearch: isPhrase(string) ? false : true,
      });
    }
};

// util func to debounce search box
const debounce = (func, delay) => () => {
  window.clearTimeout(window["item_search_timer"]);
  window["item_search_timer"] = window.setTimeout(func, delay);
};

// populate search box based on url param
const loadUrlSearch = () => {
  const query = new URLSearchParams(window.location.search).get("search") || "";
  if (!query.trim()) return;
  searchInput.value = query;
};

// start script and add triggers
window.addEventListener("load", createSearch);
