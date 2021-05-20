# common functions for auto-citations

# import packages
from sys import exit
import os
import subprocess
import json
import yaml
from yaml.loader import SafeLoader
from datetime import datetime

# current working directory
directory = os.path.dirname(os.path.realpath(__file__))

# fallback year, month, day
default_date = [1900, 1, 1]

# allow printing ANSI color codes on Windows
os.system("")

# colors for logging
palette = {
    "white": "\033[97m",
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "purple": "\033[95m",
    "cyan": "\033[96m",
    "reset": "\033[0m",
}

# level colors
levels = {1: "purple", 2: "cyan", 3: "white"}

# colored logging
def log(message="", level=1, color=""):
    if not color:
        color = levels[level]

    if color != "white":
        print("")

    if level == 1:
        message = message.upper()

    print(f"{(level - 1) * '  '}{palette[color]}{message}{palette['reset']}")


# find item in list that matches entry by id
def find_match(entry, list):
    for item in list:
        if type(item) == dict and item.get("id") == entry.get("id"):
            return item
    return {}


# get date parts from Manubot citation
def date_part(citation, index):
    try:
        return citation.get("issued").get("date-parts")[0][index]
    except Exception:
        return default_date[index]


# format date string with leading 0's
def clean_date(date):
    try:
        return datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
    except Exception:
        return "-".join(str(part) for part in default_date)


# read data from yaml file
def load_data(filename, type_check=True):
    # full file path
    path = os.path.join(directory, filename)

    # check if file exists
    if not os.path.isfile(path):
        raise Exception(f"Can't find {filename}")

    # try to open file
    try:
        file = open(path, encoding="utf8")
    except Exception as message:
        raise Exception(message or f"Can't open {filename}")

    # try to parse as yaml
    try:
        with file:
            data = yaml.load(file, Loader=SafeLoader)
    except Exception:
        raise Exception(f"Can't parse {filename}. Make sure it's valid YAML.")

    if type_check:
        # is top level array
        if type(data) != list:
            raise Exception(f"Top level of {filename} is not a list")

        # is each entry a dict
        for entry in data:
            if type(entry) != dict:
                raise Exception(f"Not all entries in {filename} are dictionaries")

    # if no errors, return data
    return data


# write yaml data to file
def save_data(filename, data):
    # full file path
    path = os.path.join(directory, filename)

    # try to open file
    try:
        file = open(path, mode="w")
    except Exception:
        raise Exception(f"Can't open {filename} for writing")

    # try to save data as yaml
    try:
        with file:
            yaml.dump(data, file, default_flow_style=False, sort_keys=False)
    except Exception:
        raise Exception(f"Can't dump {filename} as YAML")

    # write warning note to top of file
    note = "# GENERATED AUTOMATICALLY, DO NOT EDIT"
    try:
        with open(path, "r") as file:
            data = file.read()
        with open(path, "w") as file:
            file.write(f"{note}\n\n{data}")
    except Exception:
        raise Exception(f"Can't write to {filename}")


# generate citation for source with Manubot
def cite_with_manubot(source):
    # source id
    id = source.get("id")

    # run Manubot and get results as json
    try:
        commands = ["manubot", "cite", id, "--log-level=ERROR"]
        output = subprocess.Popen(commands, stdout=subprocess.PIPE)
        manubot = json.loads(output.communicate()[0])[0]
    except Exception:
        raise Exception("Manubot could not generate citation")

    # new citation info, with only needed info from Manubot
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
    citation["publisher"] = container or publisher or collection

    # date
    year = date_part(manubot, 0)
    month = date_part(manubot, 1)
    day = date_part(manubot, 2)
    citation["date"] = f"{year}-{month}-{day}"

    # link
    citation["link"] = manubot.get("URL", "")

    # add new citation to list
    return citation
