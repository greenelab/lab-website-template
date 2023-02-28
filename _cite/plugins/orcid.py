import json
from urllib.request import Request, urlopen
from util import *


def main(entry):
    """
    receives single list entry from orcid data file
    returns list of sources to cite
    """

    # orcid api
    endpoint = "https://pub.orcid.org/v2.0/$ORCID/works"
    headers = {"Accept": "application/json"}

    # get id from entry
    id = entry.get("orcid")
    if not id:
        raise Exception('No "orcid" key')

    # query api
    @log_cache
    @cache.memoize(name=__file__, expire=1 * (60 * 60 * 24))
    def query():
        url = endpoint.replace("$ORCID", id)
        request = Request(url=url, headers=headers)
        response = json.loads(urlopen(request).read())
        return response.get("group")

    response = query()

    # list of sources to return
    sources = []

    # go through response structure and pull out ids e.g. doi:1234/56789
    for work in response:
        for id in work["external-ids"]["external-id"]:
            # get id and id-type from response
            id_type = id["external-id-type"]
            id_value = id["external-id-value"]

            # create source
            source = {"id": f"{id_type}:{id_value}"}

            # copy fields from entry to source
            source.update(entry)

            # add source to list
            sources.append(source)

    return sources
