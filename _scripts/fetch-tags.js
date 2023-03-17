/*
  fetches tags (aka "topics") from a given GitHub repo and adds them to row of
  tag buttons. specify repo in data-repo attribute on row.
*/

{
  const onLoad = async () => {
    // get tag rows with specified repos
    const rows = document.querySelectorAll("[data-repo]");

    // for each repo
    for (const row of rows) {
      // get props from tag row
      const repo = row.dataset.repo.trim();
      const link = row.dataset.link.trim();

      // get tags from github
      if (!repo) continue;
      let tags = await fetchTags(repo);

      // filter out tags already present in row
      let existing = [...row.querySelectorAll(".tag")].map((tag) =>
        window.normalizeTag(tag.innerText)
      );
      tags = tags.filter((tag) => !existing.includes(normalizeTag(tag)));

      // add tags to row
      for (const tag of tags) {
        const a = document.createElement("a");
        a.classList.add("tag");
        a.innerHTML = tag;
        a.href = `${link}?search="tag: ${tag}"`;
        a.dataset.tooltip = `Show items with the tag "${tag}"`;
        row.append(a);
      }

      // delete tags container if empty
      if (!row.innerText.trim()) row.remove();
    }

    // emit "tags done" event for other scripts to listen for
    window.dispatchEvent(new Event("tagsfetched"));
  };

  // after page loads
  window.addEventListener("load", onLoad);

  // GitHub topics endpoint
  const api = "https://api.github.com/repos/REPO/topics";
  const headers = new Headers();
  headers.set("Accept", "application/vnd.github+json");

  // get tags from GitHub based on repo name
  const fetchTags = async (repo) => {
    const url = api.replace("REPO", repo);
    try {
      const response = await (await fetch(url)).json();
      if (response.names) return response.names;
      else throw new Error(JSON.stringify(response));
    } catch (error) {
      console.groupCollapsed("GitHub fetch tags error");
      console.log(error);
      console.groupEnd();
      return [];
    }
  };
}
