# main auto-cite script

# packages
from util import *

# auto-cite plugins
from orcid import orcid as orcid_plugin
from sources import sources as sources_plugin

# filename for output citations
filename = "../_data/citations.yaml"

# plugins to run, in order
plugins = [orcid_plugin, sources_plugin]

log("Compiling list of sources to cite")

# compile master list of sources from various plugins
sources = []
for plugin in plugins:
    log(f"Running {plugin.__name__} plugin")

    plugin_sources = plugin()

    log(f"Got {len(plugin_sources)} sources", 2, "green")

    for source in plugin_sources:
        sources.append(source)

log("Generating citations for sources")

# load existing citations
citations = load_data(filename)

# list of new citations to overwrite existing citations
new_citations = []

# go through sources
for index, source in enumerate(sources):
    # show progress
    log(f"Source {index + 1} of {len(sources)} - {source.get('id', '-')}", 2)

    # find same source in existing citations
    cached = find_match(source, citations)

    if cached:
        # use existing citation to save time
        log("Using existing citation", 3)
        new_citations.append(cached)

    else:
        # use Manubot to generate new citation
        log("Using Manubot to generate new citation", 3)
        new_citations.append(cite_with_manubot(source))

log("Exporting citations")

# go through new citations
for citation in new_citations:
    # merge in properties from input source
    citation.update(find_match(citation, sources))

    # ensure date in proper format for correct date sorting
    citation["date"] = clean_date(citation.get("date"))

log(f"Exported {len(new_citations)} citations", 2, "green")

# save new citations
save_data(filename, new_citations)

log("Done!")
