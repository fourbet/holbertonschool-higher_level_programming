#!/usr/bin/python3
""" Project: Python Input-Output """
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

lists = [item for item in sys.argv]
lists = lists[1:]

try:
    previous_list = load_from_json_file("add_item.json")
except:
    previous_list = []
for item in lists:
    previous_list.append(item)
save_to_json_file(previous_list, "add_item.json")
