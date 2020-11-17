// card search plugin
// pairs with "card search" component
// filters cards on page based on what is typed in search box

let searchInput;
let searchCount;
let cards;
let hide;

const createSearch = () => {
  // get important elements
  searchInput = document.querySelector(".card_search_input");
  searchCount = document.querySelector(".card_search_count");
  cards = Array.from(document.querySelectorAll(".card"));
  hide = Array.from(document.querySelectorAll(".card_search_hide"));

  // don't run script if necessary elements aren't present
  if (!searchInput || !cards.length) return;

  // attach filter function to search box input
  searchInput.addEventListener("input", debounce(filterCards, 50));

  // get url param and search
  loadUrlSearch();
  filterCards();
};

// determine if string is a term (single word) or phrase (quoted multiple words)
const isPhrase = (str) => /\s/g.test(str);

// determine if card should show up in results based on query
const showCard = (card, query) => {
  // if nothing searched, show
  if (!query.length) return true;
  // get card text content
  card = card.innerText.toLowerCase();
  // get arrays of terms and phrases
  let terms = query.filter((string) => !isPhrase(string));
  let phrases = query.filter((string) => isPhrase(string));
  // func to check if string is in card text
  const includes = (string) => card.includes(string);
  // show card if all terms match, and at least one phrase matches
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

// filter cards
const filterCards = () => {
  // get search box text
  const query = parseQuery(searchInput.value);

  // reset highlights
  resetHighlights();

  // hide/show cards
  let count = 0;
  for (const card of cards) {
    if (showCard(card, query)) {
      card.dataset.hide = false;
      // count if shown
      count++;
      // highlight query words
      highlightTerms(card, query);
    } else card.dataset.hide = true;
  }

  // hide any elements marked with data-search-hide if there was any filtering
  const anyFiltering = count < cards.length;
  hide.forEach((heading) => (heading.dataset.hide = anyFiltering));

  // update results info
  if (searchCount)
    searchCount.innerHTML =
      count.toLocaleString() + " of " + cards.length.toLocaleString();
};

// reset mark.js highlights
const resetHighlights = () => new Mark(document.body).unmark();

// highlight search terms with mark.js
const highlightTerms = (card, query) => {
  // to avoid slowdown, only highlight if more than a few letters typed in
  for (const string of query)
    if (string.length > 2) {
      new Mark(card).mark(string, {
        separateWordSearch: isPhrase(string) ? false : true,
      });
    }
};

// util func to debounce search box
const debounce = (func, delay) => () => {
  window.clearTimeout(window["card_search_timer"]);
  window["card_search_timer"] = window.setTimeout(func, delay);
};

// populate search box based on url param
const loadUrlSearch = () => {
  const query = new URLSearchParams(window.location.search).get("search") || "";
  if (!query.trim()) return;
  searchInput.value = query;
};

// start script and add triggers
window.addEventListener("load", createSearch);
