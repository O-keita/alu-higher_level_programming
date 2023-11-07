#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = []

    for items in set_1:
        if items not in set_2:
            result.append(items)
    for items in set_2:
        if items not in set_1:
            result.append(items)
    return result
