// search plugin
// supports site search component which searches site/domain via google

// when submits site search form/box
const onSiteSearchSubmit = (event) => {
  event.preventDefault();
  const google = "https://www.google.com/search?q=site:";
  const site = window.location.origin;
  const query = event.target.elements.query.value;
  window.location = google + site + " " + query;
};
