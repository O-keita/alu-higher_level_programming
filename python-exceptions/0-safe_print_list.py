#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_list = my_list[:x]
    try:
        for num in num_lsit:
            print("{}".format(num), end='')
    except:
        print("There is an error")
