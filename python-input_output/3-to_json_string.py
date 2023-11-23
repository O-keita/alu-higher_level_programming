#!/usr/bin/python3
"""3-to_json_string.py"""
import json


def to_json_string(my_obj):
    """ returning the json rep of a file"""

    json_rep = json.dumps(my_obj)
    return json_rep
