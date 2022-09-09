from util import *
from importlib import import_module
from dict_hash import sha256

# config info for input/output files and plugins
config = {}
try:
    config = load_data("../_config.yaml", type_check=False).get("auto-cite")
    if not config:
        raise Exception("Couldn't find auto-cite key in config")
except Exception as e:
    log(e, 3, "red")
    exit(1)

log("Compiling list of sources to cite")

# compile master list of sources from various plugins
sources = []

# error exit flag
will_exit = False

# loop through plugins
for plugin in config.get("plugins", []):
    # get plugin props
    name = plugin.get("name", "[no name]")
    files = plugin.get("input", [])

    # show progress
    log(f"Running {name} plugin")

    # loop through plugin input files
    for file in files:
        # show progress
        log(file, 2)

        plugin_sources = []
        try:
            # get data in file
            data = load_data(file)
            # run plugin
            plugin_sources = import_module(f"plugins.{name}").main(data)
        except Exception as e:
            log(e, 3, "red")
            will_exit = True

        log(f"Got {len(plugin_sources)} sources", 2, "green")

        for source in plugin_sources:
            # include meta info about plugin and source
            source["_plugin"] = name
            source["_input"] = file
            # make unique key for cache matching
            source["_cache"] = sha256(source)
            # add source
            sources.append(source)

# exit at end of loop if error occurred
if will_exit:
    log("One or more input files or plugins failed", 3, "red")
    exit(1)

log("Generating citations for sources")

# load existing citations
citations = []
try:
    citations = load_data(config["output"])
except Exception as e:
    log(e, 2, "yellow")

# error exit flag
will_exit = False

# list of new citations to overwrite existing citations
new_citations = []

# go through sources
for index, source in enumerate(sources):
    # show progress
    log(f"Source {index + 1} of {len(sources)} - {source.get('id', '[no ID]')}", 2)

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
        # if Manubot couldn't cite source
        except Exception as e:
            log(e, 3, "red")
            # if manually-entered source, throw error on cite failure
            if source.get("_plugin") == "sources":
                will_exit = True
            continue
    else:
        # pass source through untouched
        log("Passing source through", 3)

    # merge in properties from input source
    new_citation.update(source)
    # ensure date in proper format for correct date sorting
    new_citation["date"] = clean_date(new_citation.get("date"))

    # remove unwanted keys
    new_citation.pop("_plugin")
    new_citation.pop("_input")

    # add new citation to list
    new_citations.append(new_citation)

# exit at end of loop if error occurred
if will_exit:
    log("One or more sources failed to be cited", 3, "red")
    exit(1)

log("Exporting citations")

# save new citations
try:
    save_data(config["output"], new_citations)
except Exception as e:
    log(e, 2, "red")
    exit(1)

log(f"Exported {len(new_citations)} citations", 2, "green")
