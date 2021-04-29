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

# colored logging
def error(message): print(f"\033[91m{message}\033[0m"); exit(1) # red
def warning(message): print(f"\033[93m{message}\033[0m") # yellow
def success(message): print(f"\033[92m{message}\033[0m") # green
def info(message): print(f"\033[94m{message}\033[0m") # blue

# log a section divider
def section():
    print("")

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
def load_data(filename, strict=True):
    section()

    print(f"Loading {filename}")
    
    try:
        # full file path
        path = os.path.join(directory, filename)

        # check if file exists
        if not os.path.isfile(path):
            raise Exception("Can't find file")

        # try to open file
        try:
            file = open(path, encoding="utf8")
        except Exception as message:
            raise Exception(message or "Can't open file")

        # try to parse as yaml
        try:
            with file:
                data = yaml.load(file, Loader=SafeLoader)
        except Exception:
            raise Exception("Can't parse file. Make sure it's valid YAML.")

        # is top level array
        if type(data) != list:
            raise Exception ("Top level is not a list")

        # if no errors, return data
        return data

    # catch any errors
    except Exception as message:
        if strict:
            error(message)
        else:
            warning(message)
            print("Starting from scratch")
            return []

# write yaml data to file
def save_data(filename, data):
    section()

    print(f"Saving {filename}")

    try:
        # full file path
        path = os.path.join(directory, filename)

        # try to open file
        try:
            file = open(path, mode="w")
        except Exception:
            raise Exception("Can't open file for writing")

        # try to save data as yaml
        try:
            with file:
                yaml.dump(data, file, default_flow_style=False, sort_keys=False)
        except Exception:
            raise Exception(f"Can't dump as YAML")

        # write warning note to top of file
        note = "# GENERATED AUTOMATICALLY, DO NOT EDIT"
        try:
            with open(path, 'r') as file:
                data = file.read()
            with open(path, 'w') as file:
                file.write(f"{note}\n\n{data}")
        except Exception:
            raise Exception(f"Can't write to file")

    # catch any errors
    except Exception as message:
        error(message)

# identity function
def identity(yep):
    return yep;

# load, type check, de-duplicate, and process list of data
def process_data(data, process=identity):
    # entry ids already found
    ids = []

    # new processed data to return
    new_data = []

    # loop through data entries
    for index, entry in enumerate(data):
        try:
            section()

            # show progress
            print(f"Entry {index + 1} of {len(data)}")

            # is entry a dictionary
            if type(entry) != dict:
                raise Exception("Entry is not a dictionary")

            # entry id
            id = entry.get("id")

            # does entry have an id field
            if not id:
                raise Exception("Entry has no id field")

            print(id)

            # is entry a duplicate
            if id in ids:
                raise Exception("Entry is a duplicate")

            # add entry id to found list
            ids.append(id)

            # run process on entry
            new_entries = process(entry)

            # add processed entry (or entries, if multiple returned) to new data
            if isinstance(new_entries, list):
                for new_entry in new_entries:
                    new_data.append(new_entry)
            else:
                new_data.append(new_entries)

        # catch any errors         
        except Exception as message:
            warning(message)

    return new_data

# generate citation for source with Manubot
def cite_with_manubot(source):
    print("Running Manubot to generate citation")

    # source id
    id = source.get("id")

    # run Manubot and get results as json
    try:
        commands = ["manubot", "cite", id, '--log-level=ERROR']
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
    success("Citation generated")
    return citation
