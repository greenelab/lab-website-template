import subprocess
import json
import yaml
from yaml.loader import SafeLoader
from pathlib import Path
from datetime import datetime
from rich import print
from diskcache import Cache


# cache for time-consuming network requests
cache = Cache("./_cite/.cache")


# clear expired items from cache
cache.expire()


def log_cache(func):
    """
    decorator to use around memoized function to log if cached or or not
    """

    def wrap(*args):
        key = func.__cache_key__(*args)
        if key in cache:
            log(" (from cache)", level="INFO", newline=False)
        return func(*args)

    return wrap


def log(message="\n--------------------\n", indent=0, level="", newline=True):
    """
    log to terminal, color determined by indent and level
    """

    palette = {
        0: "[orange1]",
        1: "[salmon1]",
        2: "[violet]",
        3: "[sky_blue1]",
        "ERROR": "[white on #F43F5E]",
        "WARNING": "[black on #EAB308]",
        "SUCCESS": "[black on #10B981]",
        "INFO": "[grey70]",
    }
    color = palette.get(level) or palette.get(indent) or "[white]"
    if newline:
        print()
    print(indent * "    " + color + str(message) + "[/]", end="", flush=True)


def label(entry):
    """
    get "label" of dict entry
    """

    return list(entry.keys())[0] + ": " + list(entry.values())[0]


def list_of_dicts(data):
    """
    check if data is list of dicts
    """

    return type(data) == list and all(type(entry) == dict for entry in data)


def format_date(date):
    """
    format date as YYYY-MM-DD, or no date if malformed
    """

    try:
        return datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
    except Exception:
        return ""


def load_data(path):
    """
    read data from yaml or json file
    """

    # convert to path object
    path = Path(path)

    # check if file exists
    if not path.is_file():
        raise Exception("Can't find file")

    # try to open file
    try:
        file = open(path, encoding="utf8")
    except Exception as e:
        raise Exception(e or "Can't open file")

    # try to parse as yaml
    try:
        with file:
            data = yaml.load(file, Loader=SafeLoader)
    except Exception:
        raise Exception("Can't parse file. Make sure it's valid YAML.")

    # if no errors, return data
    return data


def save_data(path, data):
    """
    write data to yaml file
    """

    # convert to path object
    path = Path(path)

    # try to open file
    try:
        file = open(path, mode="w")
    except Exception:
        raise Exception("Can't open file for writing")

    # prevent yaml anchors/aliases (pointers)
    yaml.Dumper.ignore_aliases = lambda *args: True

    # try to save data as yaml
    try:
        with file:
            yaml.dump(data, file, default_flow_style=False, sort_keys=False)
    except Exception:
        raise Exception("Can't save YAML to file")

    # write warning note to top of file
    note = "# DO NOT EDIT, GENERATED AUTOMATICALLY"
    try:
        with open(path, "r") as file:
            data = file.read()
        with open(path, "w") as file:
            file.write(f"{note}\n\n{data}")
    except Exception:
        raise Exception("Can't write to file")


@log_cache
@cache.memoize(name="manubot", expire=90 * (60 * 60 * 24))
def cite_with_manubot(source):
    """
    generate citation data for source with Manubot
    """

    # source id
    id = source.get("id")

    # run Manubot
    try:
        commands = ["manubot", "cite", id, "--log-level=WARNING"]
        output = subprocess.Popen(commands, stdout=subprocess.PIPE).communicate()
    except Exception as e:
        log(e, 3)
        raise Exception("Manubot could not generate citation")

    # parse results as json
    try:
        manubot = json.loads(output[0])[0]
    except Exception:
        raise Exception("Couldn't parse Manubot response")

    # new citation with only needed info
    citation = {}

    # original id
    citation["id"] = id

    # title
    citation["title"] = manubot.get("title", "")

    # authors
    citation["authors"] = []
    for author in manubot.get("author", []):
        given = author.get("given", "")
        family = author.get("family", "")
        citation["authors"].append(given + " " + family)

    # publisher
    container = manubot.get("container-title", "")
    collection = manubot.get("collection-title", "")
    publisher = manubot.get("publisher", "")
    citation["publisher"] = container or publisher or collection or ""

    # extract date part
    def date_part(citation, index):
        try:
            return citation.get("issued").get("date-parts")[0][index]
        except Exception:
            return ""

    # date
    year = date_part(manubot, 0)
    if year:
        # fallbacks for no month or day
        month = date_part(manubot, 1) or "1"
        day = date_part(manubot, 2) or "1"
        citation["date"] = format_date(f"{year}-{month}-{day}")
    else:
        # if no year, consider date missing data
        citation["date"] = ""

    # link
    citation["link"] = manubot.get("URL", "")

    # return citation data
    return citation
