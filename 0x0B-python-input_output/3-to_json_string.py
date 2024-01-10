#!/usr/bin/python3
"""
    Returns JSON rep of a str obj
"""


def to_json_string(my_obj):
    """ import JSON and return JSOn version of obj """
    import json
    return json.dumps(my_obj)
