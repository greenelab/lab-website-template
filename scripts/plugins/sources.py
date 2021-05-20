from util import *


def main(data):
    # list of sources to return
    all_sources = []

    for entry in data:
        # show progress
        log(entry.get("id", "-"), 3, "white")

        # add each entry to collection
        all_sources.append(entry)

    # return flat list of sources
    return all_sources
