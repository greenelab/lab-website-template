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
    // get props from tag row
    const repo = row.dataset.repo.trim();
    const link = row.dataset.link.trim();

    // get tags from github
    if (!repo) continue;
    const tags = (await fetchTags(repo)) || [];

    // add tag elements to section
    for (const tag of tags) {
      const a = document.createElement("a");
      a.classList.add("tag");
      a.innerHTML = tag;
      a.href = `${link}?search="tag: ${tag}"`;
      row.append(a);
    }

    // delete tags container if empty
    if (!row.innerText.trim()) row.remove();

    // emit "tags done" event for other plugins to listen to
    window.dispatchEvent(new Event("tagsfetched"));
  }
};

const fetchTags = async (repo) => {
  const url = api.replace("REPO", repo);
  return (await (await fetch(url, { headers })).json()).names;
};

// start script
window.addEventListener("load", createTags);
