#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    results = []  # Create an empty list to store the results
    for item in range(len(my_list)):
        if my_list[item] % 2 == 0:
            results.append(True)
        else:
            results.append(False)
    return results
