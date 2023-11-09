#!/usr/bin/python3
def roman_to_int(roman_string):
    match roman_string:
        case "I":
            return 1
        case None:
            return 0
