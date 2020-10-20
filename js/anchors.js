// anchors plugin
// creates clickable icon next to each heading that links to that section

// create section links next to each heading 1 through 4
const createAnchors = () => {
  // for each heading
  const headings = document.querySelectorAll("h1, h2, h3, h4");
  for (const heading of headings) {
    // create anchor link
    const link = document.createElement("a");
    link.classList.add("fas", "fa-link", "fa-sm", "anchor");
    link.href = "#" + heading.id;
    heading.append(link);

    // if heading 1 or 2, move id from heading to parent section instead
    // why? see /_includes/content.html
    if (heading.matches("h1, h2")) {
      let section = heading.closest("section");
      if (section) {
        section.id = heading.id;
        heading.id = "";
      }
    }
  }
};

// glow section when user navigates to it
const onHashChange = () => {
  const id = window.location.hash.replace("#", "");
  let element = document.getElementById(id);
  if (!element) return;
  element.setAttribute("data-glow", "true");
  window.setTimeout(() => element.removeAttribute("data-glow"), 2000);
};

// start script and add triggers
window.addEventListener("load", createAnchors);
window.addEventListener("load", onHashChange);
window.addEventListener("hashchange", onHashChange);
