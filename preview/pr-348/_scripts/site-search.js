/*
  for site search component. searches site/domain via google.
*/

{
  // when user submits site search form/box
  window.onSiteSearchSubmit = (event) => {
    event.preventDefault();
    const google = "https://www.google.com/search?q=site:";
    const site = window.location.origin;
    const query = event.target.elements.query.value;
    window.location = google + site + " " + query;
  };
}
