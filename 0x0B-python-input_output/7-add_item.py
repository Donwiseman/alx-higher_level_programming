#!/usr/bin/python3
"""Creates a pythn list from command line arguments and saves as JSON file"""

import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

save_file = "add_item.json"
try:
    json_list = load_from_json_file(save_file)
except Exception:
    json_list = []

if len(sys.argv) > 1:
    for index, arg in enumerate(sys.argv):
        if index > 0:
            json_list.append(arg)

save_to_json_file(json_list, save_file)
