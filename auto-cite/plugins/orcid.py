from urllib.request import Request, urlopen
import json
from util import *


# orcid api
endpoint = "https://pub.orcid.org/v2.0/$ORCID/works"
headers = {"Accept": "application/json"}


def main(data):
    # list of sources to return
    all_sources = []

    for index, entry in enumerate(data):
        # show progress
        log(f"Orcid {index + 1} of {len(data)} - {entry.get('orcid', '-')}", 3, "cyan")

        # query api to get dois from orcid
        url = endpoint.replace("$ORCID", entry.get("orcid", "-"))
        request = Request(url=url, headers=headers)
        response = json.loads(urlopen(request).read())

        # go through response structure and pull out ids e.g. doi:1234/56789
        works = response["group"]
        for work in works:
            for id in work["external-ids"]["external-id"]:
                # get id and id-type from response
                id_type = id["external-id-type"]
                id_value = id["external-id-value"]

                # create source
                source = {"id": f"{id_type}:{id_value}"}

                # show progress
                log(source.get("id", "-"), 3)

                # copy fields from entry to source
                source.update(entry)

                # add source to collection
                all_sources.append(source)

    # return flat list of sources
    return all_sources
