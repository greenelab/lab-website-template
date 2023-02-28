import os
from serpapi import GoogleSearch
from util import *


def main(entry):
    """
    receives single list entry from google-scholar data file
    returns list of sources to cite
    """

    # get id from entry
    id = entry.get("gsid")
    if not id:
        raise Exception('No "gsid" key')

    # get api key
    api_key = os.environ.get("GOOGLE_SCHOLAR_API_KEY")
    if not api_key:
        raise Exception('No "GOOGLE_SCHOLAR_API_KEY" env var')

    # serp api
    params = {
        "engine": "google_scholar_author",
        "author_id": id,
        "api_key": api_key,
        "num": 100,
    }

    # query api
    @log_cache
    @cache.memoize(name=__file__, expire=1 * (60 * 60 * 24))
    def query():
        return GoogleSearch(params).get_dict().get("articles", [])

    response = query()

    # list of sources to return
    sources = []

    # go through response and format sources
    for work in response:

        # create source
        source = {}

        # format source fields
        source["id"] = work.get("citation_id", "")
        source["title"] = work.get("title", "")
        source["authors"] = list(map(str.strip, work.get("authors", "").split(",")))
        source["publisher"] = work.get("publication", "")
        source["date"] = work.get("year", "") + "-01-01"
        source["link"] = work.get("link", "")

        # copy fields from entry to source
        source.update(entry)

        # add source to list
        sources.append(source)

    return sources
