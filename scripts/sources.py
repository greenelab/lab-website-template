# "sources" auto-cite plugin
# takes sources.yaml as input, returns list of sources to be cited as output

from util import *

def main():
    return process_data(load_data("../_data/sources.yaml"))
