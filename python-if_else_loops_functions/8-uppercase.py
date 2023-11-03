#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
            print("{}\n".format(uppercase_char), end='')
        else:
            print("{}\n".format(char), end='')
