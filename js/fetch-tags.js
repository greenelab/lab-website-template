// fetch tags plugin
// fetches tags (aka "topics") from a given GitHub repo and adds them to row

// specify repo in data-repo attribute

// github endpoint for getting tags of a certain repo
const api = "https://api.github.com/repos/REPO/topics";
// NOTE: the github api to get repo "topics (tags) is still in preview
const headers = { Accept: "application/vnd.github.mercy-preview+json" };

// fetch and add github tags to any tag section with a specified repo
const createTags = async () => {
  // get tag rows with specified repos
  const rows = Array.from(document.querySelectorAll("[data-repo]"));

  // for each repo
  for (const row of rows) {
    const tags = await fetchTags(row.dataset.repo);

    // add tag elements to section
    for (const tag of tags) {
      const span = document.createElement("span");
      span.classList.add("tag");
      span.innerHTML = tag;
      row.append(span);
    }
  }
};

const fetchTags = async (repo) => {
  const url = api.replace("REPO", repo);
  return (await (await fetch(url, { headers })).json()).names;
};

// start script
window.addEventListener("load", createTags);
