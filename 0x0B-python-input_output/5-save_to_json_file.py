#!/usr/bin/python3
"""
    writes to .txt fle in JSON format
"""


def save_to_json_file(my_obj, filename):
    """ import JSON and writes converted str """
    import json
    with open(filename, 'w', encoding="UTF8") as my_file:
        my_file.write(json.dumps(my_obj))
