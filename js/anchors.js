// create section links next to each heading 1 through 4
const createAnchors = () => {
  // for each heading
  const headings = document.querySelectorAll("h1, h2, h3, h4");
  for (const heading of headings) {
    // creat anchor link
    const link = document.createElement("a");
    link.classList.add("anchor");
    link.innerHTML = '<i class="fas fa-link fa-sm"></i>';
    link.href = "#" + heading.id;

    // if heading 1 or 2 (see _includes/content.html)
    if (heading.matches("h1, h2")) {
      // move id from heading to parent section instead
      let section = heading.closest("section");
      if (section) {
        section.id = heading.id;
        heading.id = "";
      }

      // if no icon in heading already
      if (!heading.querySelector("i"))
        // add invisible link icon to other side to keep heading text centered
        heading.innerHTML =
          '<i class="fas fa-link fa-sm" style="visibility: hidden;"></i>' +
          heading.innerHTML;
    }

    // append anchor to heading
    heading.appendChild(link);
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
