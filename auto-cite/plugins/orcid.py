import logging
from urllib.request import Request, urlopen
import json
from util import *


# orcid api
endpoint = "https://pub.orcid.org/v2.0/$ORCID/works"
headers = {"Accept": "application/json"}


def main(data):
    # list of sources to return
    all_sources = []

    # error exit flag
    will_exit = False

    for index, entry in enumerate(data):
        # show progress
        log(
            f"ORCID {index + 1} of {len(data)} - {entry.get('orcid', '[no ORCID]')}",
            3,
            "cyan",
        )

        # get id
        id = entry.get("orcid")
        if not id:
            log('No "orcid" key', 3, "red")
            will_exit = True
            continue

        # query api to get dois from orcid
        try:
            url = endpoint.replace("$ORCID", id)
            request = Request(url=url, headers=headers)
            response = json.loads(urlopen(request).read())
        # if problem with orcid lookup
        except Exception as e:
            log(e, 3, "red")
            will_exit = True
            continue

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
                log(source.get("id", "[no ID]"), 3)

                # copy fields from entry to source
                source.update(entry)

                # add source to collection
                all_sources.append(source)

    # exit at end of loop if error occurred
    if will_exit:
        log("One or more ORCIDs failed", 3, "red")
        exit(1)

    # return flat list of sources
    return all_sources
