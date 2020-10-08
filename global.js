// create tooltip listener on any element with a data-tooltip attribute
const createTooltips = () => {
  // create tooltip element
  const tooltip = document.createElement("div");
  tooltip.classList.add("tooltip");
  document.body.append(tooltip);

  // init popper.js library
  let popper = null;
  let options = ({ placement = "top" }) => ({
    placement,
    modifiers: [
      // https://github.com/popperjs/popper-core/issues/1138
      { name: "computeStyles", options: { adaptive: false } },
      { name: "offset", options: { offset: [0, 10] } },
    ],
  });

  // open tooltip after delay
  let timer;
  const delayedOpen = ({ target }) => {
    const delay = target.dataset.delay || 100;
    window.clearTimeout(timer);
    timer = window.setTimeout(() => open({ target }), delay);
  };

  // open tooltip on specified target
  const open = ({ target }) => {
    if (popper) popper.destroy();
    popper = Popper.createPopper(target, tooltip, options(target.dataset));
    tooltip.dataset.show = true;
    tooltip.innerHTML = target.dataset.tooltip;
  };

  // close tooltip
  const close = () => {
    window.clearTimeout(timer);
    tooltip.dataset.show = false;
  };

  // loop through elements with data-tooltip attribute
  const targets = document.querySelectorAll("[data-tooltip]");
  for (const target of targets) {
    target.addEventListener("mouseenter", delayedOpen);
    target.addEventListener("focus", delayedOpen);
    target.addEventListener("mouseleave", close);
    target.addEventListener("blur", close);
  }
};

// add triggers
window.addEventListener("load", createTooltips);

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
  if (element.tagName === "H2") element = element.closest("section");
  if (!element) return;
  element.setAttribute("data-glow", "true");
  window.setTimeout(() => element.removeAttribute("data-glow"), 2000);
};

// add triggers
window.addEventListener("load", createAnchors);
window.addEventListener("load", onHashChange);
window.addEventListener("hashchange", onHashChange);
