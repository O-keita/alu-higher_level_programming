#!/usr/bin/python3
def common_elements(set_1, set_2):
    result = []
    for items in set_1:
        if items in set_2:
            result.append(items)
    return result
