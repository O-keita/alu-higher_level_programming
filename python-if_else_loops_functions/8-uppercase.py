#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
            print("{}".format(uppercase_char), end='' + "\n")
        else:
            print("{}".format(char), end='' + "\n")
