#!/usr/bin/python3
"""6-load_from_json_file.py"""
import json


def load_from_json_file(filename):
    """ creating object from json"""

    with open(filename, 'w', encoding='utf-8') as file:

        return json.load(file)
