#!/usr/bin/python3
"""
    create Dic from .JSON file
"""


def load_from_json_file(filename):
    """ import JSON, write to .txt file"""
    import json
    with open(filename, "r", encoding="UTF8") as my_json:
        return json.load(my_json)
