# "ORCID" auto-cite plugin
# takes orcid.yaml as input, returns list of sources to be cited as output

# packages
from urllib.request import Request, urlopen
import json
from util import *

def main():
    # input filename
    filename = "../_data/orcid.yaml"

    # load input data
    data = load_data(filename, strict=False)

    # ORCID API
    endpoint = 'https://pub.orcid.org/v2.0/$ID/works'
    headers = { 'Accept': 'application/json' }

    # process each entry in input
    def process(entry):
        # query for ORCID
        url = endpoint.replace("$ID", entry["id"])
        request = Request(url=url, headers=headers)
        response = json.loads(urlopen(request).read())
        
        # go through response structure and pull out e.g. doi:1234/56789
        works = response["group"]
        new_entry = []
        for work in works:
            for id in work["external-ids"]["external-id"]:
                id_type = id["external-id-type"]
                id_value = id["external-id-value"]
                new_entry.append({ "id": f'{id_type}:{id_value}' })

        print(f"Found {len(new_entry)} sources")
        return new_entry

    # resulting sources
    return process_data(data, process)
