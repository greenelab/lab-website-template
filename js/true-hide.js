// true hide plugin

// css "display: none" removes an element from the document flow, but does not
// remove it from the dom. the result is that css selectors like ":first-child"
// still take "display: none" elements into account. this fixes that by actually
// removing the node from the dom. this is hacky. use with care.

// store to hold removed nodes for later re-insertion
const nodeStore = {};
// counter to create unique ids for nodes
let nodeId = 0;
// id prefix to avoid collision with comments outside of this plugin
const prefix = "true-hide-";

// hide all elements that match query
const trueHide = (query) => {
  // loop through elements matching query
  const elements = document.querySelectorAll(query);
  for (const element of elements) {
    // replace node with comment
    const comment = document.createComment(prefix + nodeId);
    element.parentNode.insertBefore(comment, element.nextSibling);
    const node = element.parentElement.removeChild(element);

    // add node to list of removed nodes
    nodeStore[nodeId] = node;
    nodeId++;
  }
};

// show previously hidden elements that match query
const trueShow = (query) => {
  // loop through previously removed nodes
  for (const [id, node] of Object.entries(nodeStore)) {
    // ignore nodes that don't match query
    if (!node.matches(query)) continue;

    // loop through comments
    const comments = document.createNodeIterator(
      document.body,
      NodeFilter.SHOW_COMMENT
    );
    while (comments.nextNode()) {
      // comment node
      const comment = comments.referenceNode;

      // if comment matches removed node, replace comment with node
      if (comment.textContent === prefix + id) {
        comment.parentNode.insertBefore(node, comment);
        comment.remove();
        delete nodeStore[id];
      }
    }
  }
};
