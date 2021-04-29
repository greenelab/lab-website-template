# auto-cite core runner

# packages
from util import *

# auto-cite plugins
from orcid import main as orcid
from sources import main as sources

# filename for output citations
filename = "../_data/citations.yaml"

# plugin order
plugins = [orcid, sources]

section()

info("Compiling sources")

# compile input sources from various plugins
sources = []
for plugin in plugins:
    for entry in plugin():
        sources.append(entry)

section()

info("Generating citations")

# load existing citations
citations = load_data(filename, strict=False)

# list of new citations to overwrite existing citations
new_citations = []

# go through input sources
def process(source):
    # find same source in existing citations
    cached = find_match(source, citations)

    if cached:
        # use existing citation to save time
        info("Using existing citation")
        new_citations.append(cached)

    else:
        # use Manubot to generate new citation
        new_citations.append(cite_with_manubot(source))

process_data(sources, process)

section()

# go through new citations
for citation in new_citations:
    # merge in properties from input source
    citation.update(find_match(citation, sources))

    # ensure date in proper format for correct date sorting
    citation["date"] = clean_date(citation.get("date"))

# save new citations
save_data(filename, new_citations)

# finish
section()
success("Done!")
