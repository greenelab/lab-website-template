// create section links next to each heading of certain type
const createAnchors = () => {
  const headers = document.querySelectorAll("h2, h3, h4");
  for (const header of headers) {
    const link = document.createElement("a");
    link.classList.add("anchor");
    link.innerHTML = '<i class="fas fa-link fa-sm"></i>';
    link.href = "#" + header.id;
    header.appendChild(link);
  }
};

// glow section when user navigates to it
const onHashChange = () => {
  const id = window.location.hash.replace("#", "");
  let element = document.getElementById(id);
  if (!element) return;
  if (element.tagName === "H2") element = element.closest("section");
  if (!element) return;
  element.setAttribute("data-glow", "true");
  window.setTimeout(() => element.removeAttribute("data-glow"), 2000);
};

// start script and add triggers
window.addEventListener("load", createAnchors);
window.addEventListener("load", onHashChange);
window.addEventListener("hashchange", onHashChange);
