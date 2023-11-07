#!/usr/bin/python3
def search_replace(my_list, search, replace):
    index_search = my_list.index(search)
    new_list = my_list[:]
    if search in my_list:
        new_list[index_search] = replace
        return new_list
    else:
        return my_list
