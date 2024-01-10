#!/usr/bin/python3
"""
    Returns Dic --V of an obj (PY data struct)
"""


def from_json_string(my_obj):
    """ import JSON, return Dic --V of parsed JSON """
    import json
    return json.loads(my_obj)
