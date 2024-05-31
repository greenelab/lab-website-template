import json
from urllib.request import Request, urlopen
from util import *
from manubot.cite.handlers import prefix_to_handler as manubot_prefixes


def main(entry):
    """
    receives single list entry from orcid data file
    returns list of sources to cite
    """

    # orcid api
    endpoint = "https://pub.orcid.org/v3.0/$ORCID/works"
    headers = {"Accept": "application/json"}

    # get id from entry
    _id = get_safe(entry, "orcid", "")
    if not _id:
        raise Exception('No "orcid" key')

    # query api
    @log_cache
    @cache.memoize(name=__file__, expire=1 * (60 * 60 * 24))
    def query(_id):
        url = endpoint.replace("$ORCID", _id)
        request = Request(url=url, headers=headers)
        response = json.loads(urlopen(request).read())
        return get_safe(response, "group", [])

    response = query(_id)

    # list of sources to return
    sources = []

    # go through response structure and pull out ids e.g. doi:1234/56789
    for work in response:
        # get list of ids
        ids = []
        for summary in get_safe(work, "work-summary", []):
            ids = ids + get_safe(summary, "external-ids.external-id", [])

        # find first id of particular "relationship" type
        _id = next(
            (
                id
                for id in ids
                if get_safe(id, "external-id-relationship", "")
                in ["self", "version-of", "part-of"]
            ),
            ids[0] if len(ids) > 0 else None,
        )

        if _id == None:
            continue

        # get id and id-type from response
        id_type = get_safe(_id, "external-id-type", "")
        id_value = get_safe(_id, "external-id-value", "")

        # create source
        source = {"id": f"{id_type}:{id_value}"}

        # if not an id type that Manubot can cite, keep citation details
        if id_type not in manubot_prefixes:
            # get summaries
            summaries = get_safe(work, "work-summary", [])

            # get first summary with defined sub-value
            def first(get_func):
                return next(
                    (value for value in map(get_func, summaries) if value), None
                )

            # get title
            title = first(lambda s: get_safe(s, "title.title.value", ""))

            # get publisher
            publisher = first(lambda s: get_safe(s, "journal-title.value", ""))

            # get date
            date = (
                get_safe(work, "last-modified-date.value")
                or first(lambda s: get_safe(s, "last-modified-date.value"))
                or get_safe(work, "created-date.value")
                or first(lambda s: get_safe(s, "created-date.value"))
                or 0
            )

            # get link
            link = first(lambda s: get_safe(s, "url.value", ""))

            # keep available details
            if title:
                source["title"] = title
            if publisher:
                source["publisher"] = publisher
            if date:
                source["date"] = format_date(date)
            if link:
                source["link"] = link

        # copy fields from entry to source
        source.update(entry)

        # add source to list
        sources.append(source)

    return sources
