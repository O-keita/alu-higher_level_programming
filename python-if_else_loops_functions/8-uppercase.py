#!/usr/bin/python3
#uppercase
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
            result += uppercase_char
        else:
            result += char
    print("{}".format(result), end='')
