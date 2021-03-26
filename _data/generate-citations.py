# import packages
import sys
import os
import json
import yaml
import subprocess
from datetime import datetime
from yaml.loader import SafeLoader

####################
# settings
####################

# filename for input papers
papers_file = "research.yaml"

# filename for existing citations
citations_file = "research-output.yaml"

# fallback paper date, year month day
default_date = [1900, 1, 1]

####################
# util
####################

# allow printing ANSI color codes
os.system("")

# colors
palette = {
    "red": "\033[91m", # error
    "yellow": "\033[93m", # warning
    "green": "\033[92m", # success
    "blue": "\033[94m", # info
    "reset": "\033[0m" # default
}

# log wih color
def log(message, color="reset"):
    print(f"{palette[color]}{message}{palette['reset']}")

# log a section divider
def section():
    log("")
    log("------------------------------------------------------------")
    log("")

# yaml loader with line numbering
# https://stackoverflow.com/questions/13319067/parsing-yaml-return-with-line-number
class SafeLineLoader(SafeLoader):
    def construct_mapping(self, node, deep=False):
        mapping = super().construct_mapping(node, deep=deep)
        if node.start_mark.column == 2:
            mapping["__line_number__"] = node.start_mark.line + 1
        return mapping

# current working directory
directory = os.path.dirname(os.path.realpath(__file__))

# read file as yaml
def read_yaml(filename):
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
            return yaml.load(file, Loader=SafeLineLoader)
    except Exception:
        raise Exception("Can't parse file. Make sure it's valid YAML.")

# write yaml data to file
def write_yaml(filename, data):
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

    # write warning to top of file
    warning = "# GENERATED AUTOMATICALLY, DO NOT EDIT"
    try:
        with open(path, 'r') as file:
            data = file.read()
        with open(path, 'w') as file:
            file.write(f"{warning}\n\n{data}")
    except Exception:
        raise Exception(f"Can't write to file")

# check that yaml data has expected structure
def check_structure(data):
    # is top level array
    if type(data) != list:
        raise Exception ("Top level of file is not a list")

    # current or most recent line number
    line_number = 1

    # paper ids already found
    ids = []

    for paper in data:
        # is every paper a dictionary
        if type(paper) != dict:
            raise Exception(f"Paper after line {line_number} is not a dictionary")

        # update line number
        line_number = paper.get("__line_number__", line_number)

        # does every paper have an id field
        if not paper.get("id"):
            raise Exception(f"Paper at line {line_number} has no id field")

        # is paper a duplicate
        if paper.get("id") in ids:
            raise Exception(f"Paper at line {line_number} is a duplicate")

        # add paper id to found list
        ids.append(paper.get("id"))

# find item in list that matches entry by id
def find_match(entry, list):
    for item in list:
        if item.get("id") == entry.get("id"):
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


####################
# load and parse
####################

# load papers
log(f"Loading {papers_file}")
try:
    papers = read_yaml(papers_file)
    check_structure(papers)
except Exception as message:
    log(message, "red")
    sys.exit(1)

# load citations
log(f"Loading {citations_file}")
try:
    citations = read_yaml(citations_file)
    check_structure(citations)
except Exception as message:
    log(message, "yellow")
    log("Starting from scratch")
    citations = []

####################
# generate citations
####################

# list of new citations to overwrite existing citations
new_citations = []

# go through input papers
for index, paper in enumerate(papers):
    # show progress
    section()
    log(f"Paper {index + 1} of {len(papers)}")
    log(f"Line number {paper.get('__line_number__')}")

    log("")

    # find same paper in existing citations
    cached = find_match(paper, citations)

    if cached:
        # use existing citation to save time
        log("Already in output. Using existing citation.", "blue")
        new_citations.append(cached)

    else:
        # run Manubot to get citation info
        log("Running Manubot to generate citation")

        # paper id
        paper_id = paper.get("id")

        # run Manubot and get results as json
        try:
            commands = ["manubot", "cite", paper_id, '--log-level=ERROR']
            output = subprocess.Popen(commands, stdout=subprocess.PIPE)
            manubot = json.loads(output.communicate()[0])[0]
        except Exception:
            log("Manubot could not generate citation", "red")
            sys.exit(1)

        # new citation info, with only needed info from Manubot
        citation = {}

        # original id
        citation["id"] = paper_id

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
        new_citations.append(citation)

        log("Citation generated", "green")

####################
# finish up
####################

section()

# go through new output papers
for citation in new_citations:
    # merge properties from input paper into new output paper
    citation.update(find_match(citation, papers))

    # delete __line_number__ field
    del citation["__line_number__"]

    # ensure date in proper format for correct date sorting
    citation["date"] = clean_date(citation.get("date"))

# save new citations
log(f"Saving {citations_file}")
try:
    write_yaml(citations_file, new_citations)
except Exception as message:
    log(message, "red")
    sys.exit(1)

# done
log("")
log("Done!", "green")
