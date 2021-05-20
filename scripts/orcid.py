# "ORCID" auto-cite plugin

# packages
from urllib.request import Request, urlopen
import json
from util import *

# files for this plugin to read as input
files = ["../_data/orcid.yaml"]

# orcid api
endpoint = "https://pub.orcid.org/v2.0/$ORCID/works"
headers = {"Accept": "application/json"}


def orcid():
    # collect list of sources for plugin to return
    all_sources = []

    # loop through plugin input files
    for file in files:
        # show progress
        log(file, 2)

        # get metasources in file
        metasources = []
        try:
            metasources = load_data(file)
        except Exception as message:
            log(message, 3, "red")
            exit(1)

        for index, metasource in enumerate(metasources):
            # show progress
            log(
                f"Orcid {index + 1} of {len(metasources)} - {metasource.get('orcid', '-')}",
                2,
            )

            # query api to get dois from orcid
            url = endpoint.replace("$ORCID", metasource.get("orcid", "-"))
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

                    # copy fields from metasource to source
                    source.update(metasource)

                    # show progress
                    log(source.get("id", "-"), 3)

                    # add source to collection
                    all_sources.append(source)

    # return flat list of sources to be cited
    return all_sources
