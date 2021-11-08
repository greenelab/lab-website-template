// tooltips plugin
// shows a popup of text on hover/focus of an element

// create tooltip listener on any element with a data-tooltip attribute
const createTooltips = () => {
  // make sure tippy library available
  if (typeof tippy === "undefined") return;

  tippy("[data-tooltip]", {
    content: (element) => {
      const content = element.getAttribute("data-tooltip");
      element.setAttribute("aria-label", content);
      return content;
    },
  });
};

// start script
window.addEventListener("load", createTooltips);
