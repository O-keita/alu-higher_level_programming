#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
            words_split = uppercase_char.split()
            words = "\n".join(words_split)
            print("{}".format(words), end='')
        else:
            print("{}".format(char), end='')
