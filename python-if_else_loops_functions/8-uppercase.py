#!/usr/bin/python3
def uppercase(s):
    result = []
    for char in s:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_char = char
        result.append(uppercase_char)
    print(''.join(result))
input_string = "Hello, World!"
uppercase(input_string)
