#!/usr/bin/python3
new_list = []
def divisible_by_2(my_list=[]):
    for item in my_list:
        if item % 2 == 0:
            return "{} is divisible by 2".format(item)
            
        else:
            return "{} is not divisible by 2".format(item)
