// tooltips plugin
// shows a popup of text on hover/focus of an element

// create tooltip listener on any element with a data-tooltip attribute
const createTooltips = () => {
  // make sure tippy library available
  if (typeof tippy === "undefined") return;

  // add tooltip to elements
  tippy("[data-tooltip]", {
    content: (element) => {
      const content = element.getAttribute("data-tooltip");
      // add aria label for screen readers
      element.setAttribute("aria-label", content);
      // remove tooltip attribute to mark element as already-tooltipped
      element.removeAttribute("data-tooltip");
      return content;
    },
  });
};

// start script
window.addEventListener("load", createTooltips);
window.addEventListener("tagsfetched", createTooltips);
