/* 
  shows a popup of text on hover/focus of any element with the data-tooltip
  attribute.
*/

{
  const onLoad = () => {
    // make sure Tippy library available
    if (typeof tippy === "undefined") return;

    // get elements with non-empty tooltips
    const elements = [...document.querySelectorAll("[data-tooltip]")].filter(
      (element) => element.dataset.tooltip.trim() && !element._tippy
    );

    // add tooltip to elements
    tippy(elements, {
      content: (element) => element.dataset.tooltip.trim(),
      delay: [200, 0],
      offset: [0, 20],
      allowHTML: true,
      interactive: true,
      appendTo: () => document.body,
      aria: {
        content: "describedby",
        expanded: null,
      },
      onShow: ({ reference, popper }) => {
        const dark = reference.closest("[data-dark]")?.dataset.dark;
        if (dark === "false") popper.dataset.dark = true;
        if (dark === "true") popper.dataset.dark = false;
      },
      // onHide: () => false, // debug
    });
  };

  // after page loads
  window.addEventListener("load", onLoad);
  // after tags load
  window.addEventListener("tagsfetched", onLoad);
}
