#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for item in my_list:
        if item % 2 == 0:
            return "{} is divisible by 2".format(item)
            
        elif item % 2 ==1:
            return "{} is not divisible by 2".format(item)
        else:
            return my_list
