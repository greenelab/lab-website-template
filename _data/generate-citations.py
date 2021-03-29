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

# colored logging
def error(message): print(f"\033[91m{message}\033[0m"); sys.exit(1) # red
def warning(message): print(f"\033[93m{message}\033[0m") # yellow
def success(message): print(f"\033[92m{message}\033[0m") # green
def info(message): print(f"\033[94m{message}\033[0m") # blue

# log a section divider
def section():
    print("")
    print("------------------------------------------------------------")
    print("")

# yaml loader with line numbering
# https://stackoverflow.com/questions/13319067/parsing-yaml-return-with-line-number
class SafeLineLoader(SafeLoader):
    def construct_mapping(self, node, deep=False):
        mapping = super().construct_mapping(node, deep=deep)
        if node.start_mark.column == 2:
            mapping["_line_"] = node.start_mark.line + 1
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

    # write warning note to top of file
    note = "# GENERATED AUTOMATICALLY, DO NOT EDIT"
    try:
        with open(path, 'r') as file:
            data = file.read()
        with open(path, 'w') as file:
            file.write(f"{note}\n\n{data}")
    except Exception:
        raise Exception(f"Can't write to file")

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


####################
# load and parse
####################

section()

# load papers
print(f"Loading {papers_file}")
try:
    papers = read_yaml(papers_file)
    # is top level array
    if type(papers) != list:
        raise Exception ("Top level is not a list")
except Exception as message:
    error(message)

# load citations
print(f"Loading {citations_file}")
try:
    citations = read_yaml(citations_file)
    # is top level array
    if type(citations) != list:
        raise Exception ("Top level is not a list")
except Exception as message:
    warning(message)
    print("Starting from scratch")
    citations = []

####################
# generate citations
####################

# list of new citations to overwrite existing citations
new_citations = []

# paper ids already found
ids = []

# go through input papers
for index, paper in enumerate(papers):
    try:
        section()

        # show progress
        print(f"Paper {index + 1} of {len(papers)}")

        # is entry a dictionary
        if type(paper) != dict:
            print("")
            raise Exception("Entry is not a dictionary")

        # show line number in yaml for reference
        print(f"Line number {paper.get('_line_', '???')}")
        print("")

        # paper id
        paper_id = paper.get("id")

        # does entry have an id field
        if not paper_id:
            raise Exception("Entry has no id field")

        # is entry a duplicate
        if paper_id in ids:
            raise Exception("Entry is a duplicate")

        # add paper id to found list
        ids.append(paper_id)

        # find same paper in existing citations
        cached = find_match(paper, citations)

        if cached:
            # use existing citation to save time
            info("Using existing citation")
            new_citations.append(cached)

        else:
            # run Manubot to get citation info
            print("Running Manubot to generate citation")

            # run Manubot and get results as json
            try:
                commands = ["manubot", "cite", paper_id, '--log-level=ERROR']
                output = subprocess.Popen(commands, stdout=subprocess.PIPE)
                manubot = json.loads(output.communicate()[0])[0]
            except Exception:
                raise Exception("Manubot could not generate citation")

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

            success("Citation generated")

    # catch any errors and exit            
    except Exception as message:
        error(message)

####################
# finish up
####################

section()

# go through new citations
for citation in new_citations:
    # merge in properties from input paper
    citation.update(find_match(citation, papers))

    # delete line number field
    del citation["_line_"]

    # ensure date in proper format for correct date sorting
    citation["date"] = clean_date(citation.get("date"))

# save new citations
print(f"Saving {citations_file}")
try:
    write_yaml(citations_file, new_citations)
except Exception as message:
    error(message)

section()

# done
success("Done!")
