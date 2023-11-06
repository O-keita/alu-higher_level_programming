#!/usr/bin/python3

def element_at(my_list, idx):
    if 0 <= idx > len(my_list):
        return None
    else: 
        return "Element {:d} is at index {}".format(idx, my_list[idx])
