from util import *
from importlib import import_module
from dict_hash import sha256

# config info for input/output files and plugins
config = {}
try:
    config = load_data("../_config.yaml", type_check=False).get("auto-cite")
    if not config:
        raise Exception("Couldn't find auto-cite key in config")
except Exception as message:
    log(message, 3, "red")
    exit(1)

log("Compiling list of sources to cite")

# compile master list of sources from various plugins
sources = []

# loop through plugins
for plugin in config.get("plugins", []):
    # get plugin props
    name = plugin.get("name", "-")
    files = plugin.get("input", "")

    # show progress
    log(f"Running {name} plugin")

    # loop through plugin input files
    for file in files:
        # show progress
        log(file, 2)

        # get data in file
        data = []
        try:
            data = load_data(file)
        except Exception as message:
            log(message, 3, "red")
            exit(1)

        # run plugin
        plugin_sources = import_module(f"plugins.{name}").main(data)

        log(f"Got {len(plugin_sources)} sources", 2, "green")

        for source in plugin_sources:
            # make unique key for cache matching
            source["_cache"] = sha256({**source, "plugin": name, "input": file})
            # add source
            sources.append(source)

log("Generating citations for sources")

# load existing citations
citations = []
try:
    citations = load_data(config["output"])
except Exception as message:
    log(message, 2, "yellow")

# list of new citations to overwrite existing citations
new_citations = []

# go through sources
for index, source in enumerate(sources):
    # show progress
    log(f"Source {index + 1} of {len(sources)} - {source.get('id', 'No ID')}", 2)

    # new citation for source
    new_citation = {}

    # find same source in existing citations
    cached = get_cached(source, citations)

    if cached:
        # use existing citation to save time
        log("Using existing citation", 3)
        new_citation = cached

    elif source.get("id", "").strip():
        # use Manubot to generate new citation
        log("Using Manubot to generate new citation", 3)
        try:
            new_citation = cite_with_manubot(source)
        except Exception as message:
            log(message, 3, "red")
            exit(1)
    else:
        # pass source through untouched
        log("Passing source through", 3)

    # merge in properties from input source
    new_citation.update(source)
    # ensure date in proper format for correct date sorting
    new_citation["date"] = clean_date(new_citation.get("date"))

    # add new citation to list
    new_citations.append(new_citation)

log("Exporting citations")

# save new citations
try:
    save_data(config["output"], new_citations)
except Exception as message:
    log(message, 2, "red")
    exit(1)

log(f"Exported {len(new_citations)} citations", 2, "green")
