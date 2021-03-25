# import packages
import sys
import os
import json
import yaml
import subprocess
from datetime import datetime
from yaml.loader import SafeLoader

####################
# variables
####################

# input and output files
input_file = "research.yaml"
output_file = "research-output.yaml"
current_dir = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(current_dir, input_file)
output_path = os.path.join(current_dir, output_file)

# input papers
input_papers = []

# existing output papers
output_papers = []

# new output papers
new_papers = []

# default paper date, year month day
default_date = [1900, 1, 1]

# colors for logging
palette = {
    "white": "\033[97m",
    "red": "\033[91m",
    "blue": "\033[94m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "reset": "\033[0m"
}

# flag for "done with errors"
with_errors = False

####################
# functions, classes
####################

def log(message, color="white"):
    """
    log wih color
    """
    print(f"{palette[color]}{message}{palette['reset']}")

def exit(message):
    """
    log and exit
    """
    log(message, "red")
    sys.exit(1)

class SafeLineLoader(SafeLoader):
    """
    yaml loader with line numbering
    https://stackoverflow.com/questions/13319067/parsing-yaml-return-with-line-number
    """
    def construct_mapping(self, node, deep=False):
        mapping = super().construct_mapping(node, deep=deep)
        if node.start_mark.column == 2:
            mapping["__line_number__"] = node.start_mark.line + 1
        return mapping

def date_part(citation, index):
    """
    get date parts from Manubot citation
    """
    try:
        return citation.get("issued").get("date-parts")[0][index]
    except Exception:
        return default_date[index]

def clean_date(date):
    """
    format date string with leading 0's
    """
    try:
        return datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
    except Exception:
        return "-".join(str(part) for part in default_date)

####################
# setup
####################

# allow printing ANSI color codes
os.system("")

# check that input file exists
if not os.path.isfile(input_path):
    exit(f"Can't find {input_file}")

# try to open input file
try:
    with open(input_path, encoding="utf8") as file:
        # try to parse input file as yaml
        try:
            input_papers = yaml.load(file, Loader=SafeLineLoader)
        except Exception:
            exit(f"Can't parse {input_file}. Make sure it's valid YAML.")
except Exception:
    exit(f"Can't open {input_file}")

# check that top level of input yaml is list/array
if type(input_papers) != list:
    exit(f"{input_file} not in expected format")

# try to open existing output file and parse as yaml
try:
    with open(output_path, encoding="utf8") as file:
        output_papers = yaml.load(file, Loader=SafeLineLoader)
        if type(output_papers) != list:
            raise Exception()
except Exception:
    output_papers = []

####################
# generate citations
####################

# go through input papers
for input_index, input_paper in enumerate(input_papers):
    # show progress
    log("------------------------------------------------------------")
    log("")
    log(f"Paper {input_index + 1} of {len(input_papers)}")
    log(f"Line number {input_paper.get('__line_number__')}")

    # catch errors in processing paper
    try:

        # check that paper entry is dictionary/object
        if type(input_paper) != dict:
            raise Exception("Entry not in expected format. Skipping.")

        # get paper entry identifier
        input_id = input_paper.get("id")
        if not input_id:
            raise Exception("Entry has no id field. Skipping.")
        log(input_id)
        log("")

        # find duplicate entries
        for duplicate_index, duplicate_paper in enumerate(input_papers):
            if duplicate_paper.get("id") == input_id:
                # don't count first instance of id as duplicate
                if input_index > duplicate_index:
                    raise Exception("Entry is a duplicate. Skipping.")

        # find same paper in existing output
        existing_paper = None
        for output_paper in output_papers:
            if type(output_paper) == dict and output_paper.get("id") == input_id:
                existing_paper = output_paper
                break

        # if already in output, use existing paper to save time
        if existing_paper:
            log("Already in output. Using existing citation.", "blue")
            log("")
            new_papers.append(existing_paper)

        # if not already in output, run Manubot to get citation info
        else:
            log("Running Manubot to generate citation")
            log("")

            # run Manubot and get results as json
            try:
                commands = ["manubot", "cite", input_id, '--log-level=ERROR']
                output = subprocess.Popen(commands, stdout=subprocess.PIPE)
                citation = json.loads(output.communicate()[0])[0]
            except Exception:
                log("")
                raise Exception("Manubot could not generate citation")

            # new paper info, with only needed info from citation
            new_paper = {}

            # title
            new_paper["title"] = citation.get("title", "")

            # authors
            new_paper["authors"] = []
            for author in citation.get("author", []):
                given = author.get("given", "")
                family = author.get("family", "")
                new_paper["authors"].append(given + " " + family)

            # publisher
            container = citation.get("container-title", "")
            collection = citation.get("collection-title", "")
            publisher = citation.get("publisher", "")
            new_paper["publisher"] = container or publisher or collection

            # date
            year = date_part(citation, 0)
            month = date_part(citation, 1)
            day = date_part(citation, 2)
            new_paper["date"] = f"{year}-{month}-{day}"

            # link
            new_paper["link"] = citation.get("URL", "")

            # add new paper to list
            new_papers.append(new_paper)

            log("Citation generated", "green")
            log("")

    # catch errors
    except Exception as message:
        log(message, "red")
        log("")
        with_errors = True

####################
# finish up
####################

log("------------------------------------------------------------")
log("")

# go through new output papers
for new_index, new_paper in enumerate(new_papers):
    # merge properties from input paper into new output paper
    new_paper.update(input_papers[new_index])
    # delete __line_number__ field
    del new_paper["__line_number__"]
    # ensure date in proper format for correct date sorting
    new_paper["date"] = clean_date(new_paper.get("date"))

# write new list of papers to output file
try:
    with open(output_path, mode="w") as file:
        yaml.dump(new_papers, file, default_flow_style=False, sort_keys=False)
except Exception:
    exit(f"Can't save {output_file}")

if with_errors:
    log("Done, with errors", "yellow")
else:
    log("Done!", "green")
