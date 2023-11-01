#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_char = char
        print(uppercase_char, end='')
    print()

# Test the function
input_string = "Hello, World!"
uppercase(input_string)

