#!/usr/bin/python3
def uppercase(str):
    result = ""
    words = ""
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
            char_str = words.join(uppercase_char)

            print("{}".format(char_str), end = "")
        else:
            print("{}".format(char))
print(uppercase("hello world"))
