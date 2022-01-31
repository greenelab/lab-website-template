// tooltips plugin
// shows a popup of text on hover/focus of an element

// create tooltip listener on any element with a data-tooltip attribute
const createTooltips = () => {
  // make sure tippy library available
  if (typeof tippy === "undefined") return;

  // get elements with non-empty tooltips
  const elements = Array.from(
    document.querySelectorAll("[data-tooltip]")
  ).filter((element) => element.dataset.tooltip.trim());

  // add tooltip to elements
  tippy(elements, {
    content: (element) => {
      const content = element.dataset.tooltip.trim();
      // add aria label for screen readers
      element.setAttribute("aria-label", element.innerText + " - " + content);
      // remove tooltip attribute to mark element as already-tooltipped
      element.removeAttribute("data-tooltip");
      return content;
    },
    delay: [200, 0],
  });
};

// start script
window.addEventListener("load", createTooltips);
window.addEventListener("tagsfetched", createTooltips);
