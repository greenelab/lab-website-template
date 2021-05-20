# "sources" auto-cite plugin

from util import *

# files for this plugin to read as input
files = ["../_data/sources.yaml"]


def sources():
    # collect list of sources for plugin to return
    all_sources = []

    # loop through plugin input files
    for file in files:
        # show progress
        log(file, 2)

        # get sources in file
        sources = load_data(file)

        for source in sources:
            # show progress
            log(source.get("id", "-"), 3, "white")

            # add each source to collection
            all_sources.append(source)

    # return flat list of sources to be cited
    return all_sources
