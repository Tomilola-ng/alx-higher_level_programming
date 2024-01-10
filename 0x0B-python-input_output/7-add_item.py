#!/usr/bin/python3
"""  Load, add, save """
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


try:
    my_json = load_from_json_file("add_item.json")
except Exception:
    my_json = []

for arg in sys.argv[1:]:
    my_json.append(arg)
save_to_json_file(my_json, "add_item.json")
