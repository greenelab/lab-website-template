import json
from urllib.request import Request, urlopen
from util import *
from manubot.cite.handlers import prefix_to_handler as manubot_citable


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

    # filter id by some criteria. return true to accept, false to reject.
    def filter_id(_id):
        # is id of certain "relationship" type
        relationships = ["self", "version-of", "part-of"]
        if not get_safe(_id, "external-id-relationship", "") in relationships:
            return False

        id_type = get_safe(_id, "external-id-type", "")

        # is id of certain type
        # types = ["doi"]
        # if id_type not in types:
        #     return False

        # is id citable by manubot
        if id_type not in manubot_citable:
            return False

        return True

    # prefer some ids over others by some criteria. return lower number to prefer more.
    def sort_id(_id):
        id_type = get_safe(_id, "external-id-type", "")
        types = [
            "doi",
            # "arxiv",
            # "url",
        ]
        return index_of(types, id_type)

    # go through each source
    for work in response:
        # list of ids in source
        ids = []

        # use "work-summary" field instead of top-level "external-ids" to reflect author-selected preferred sources
        for summary in get_safe(work, "work-summary", []):
            ids = ids + get_safe(summary, "external-ids.external-id", [])

        # filter ids by criteria
        ids = list(filter(filter_id, ids))
        # sort ids by criteria
        ids.sort(key=sort_id)

        # pick first available id
        _id = ids[0] if len(ids) > 0 else None

        # id parts
        id_type = get_safe(_id, "external-id-type", "")
        id_value = get_safe(_id, "external-id-value", "")

        # create source
        source = {}

        # if id citable by manubot
        if id_type and id_value and id_type in manubot_citable:
            # id to cite with manubot
            source = {"id": f"{id_type}:{id_value}"}

        # if not citable by manubot, keep citation details from orcid
        else:
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
