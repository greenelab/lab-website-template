# a script to automatically generate citations for papers the research list component

# before running:
# install python                    https://www.python.org/downloads/
# install pip                       https://pip.pypa.io/en/stable/installing/
# install manubot                   https://github.com/manubot/manubot#installation

import sys
import os
import json
import yaml
import subprocess
from datetime import datetime

# input and output files
current_dir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(current_dir, "research-input.yml")
output_file = os.path.join(current_dir, "research-output.yml")

# load input papers as yaml
try:
    with open(input_file, encoding="utf8") as file:
        input_papers = yaml.load(file, Loader=yaml.FullLoader)
except Exception:
    print("Problem with input file.")
    sys.exit(1)

# load existing output papers as yaml
try:
    with open(output_file, encoding="utf8") as file:
        output_papers = yaml.load(file, Loader=yaml.FullLoader)
except Exception:
    output_papers = []

# get citation metadata for each paper
new_papers = []
for index, input_paper in enumerate(input_papers, start=1):
    # show progress
    print("\n------------------------------")
    print(f"Paper {index} of {len(input_papers)}")
    print("------------------------------\n")

    # if input paper already exists in output, use that citation info to save time
    matches = [p for p in output_papers if p.get("id", "") == input_paper.get("id", "")]
    if len(matches) > 0:
        print("Paper already in output. Using existing citation.")
        new_papers.append(matches[0])

    # otherwise, run manubot to get new citation metadata
    else:
        print("Paper not in output. Running Manubot to generate citation.\n")
        commands = ["manubot", "cite", input_paper["id"], "--log-level", "DEBUG"]
        output = subprocess.Popen(commands, stdout=subprocess.PIPE)
        citation = json.loads(output.communicate()[0])[0]

        # take only the needed info from the citation
        new_paper = {}
        # output_ title
        new_paper["title"] = citation.get("title", "")
        # output_ authors
        new_paper["authors"] = []
        for author in citation.get("author", []):
            new_author = author.get("given", "") + " " + author.get("family", "")
            new_paper["authors"].append(new_author)
        # output_ publisher
        new_paper["publisher"] = citation.get("container-title", citation.get("publisher", citation.get("collection-title", "")))
        # output_ date
        date_parts = citation.get("issued").get("date-parts")[0]
        date_parts += (3 - len(date_parts)) * [1] # default month and day to 1
        new_paper["date"] = "-".join([str(part) for part in date_parts])
        # output_ link
        new_paper["link"] = citation.get("URL", "")
        # add to list
        new_papers.append(new_paper)

# merge any extra properties specified in the input papers into the final output
print("\nCopying additional metadata from input to output.")
for index, new_paper in enumerate(new_papers):
    new_paper.update(input_papers[index])
    # ensure date in proper format (w/ leading 0's) for correct date sorting
    new_paper["date"] = datetime.strptime(new_paper["date"], "%Y-%m-%d").strftime("%Y-%m-%d")

# write new list of papers to output file
with open(output_file, mode="w") as file:
    yaml.dump(new_papers, file, default_flow_style=False, sort_keys=False)
