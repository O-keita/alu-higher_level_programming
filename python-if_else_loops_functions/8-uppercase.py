#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
            result += uppercase_char
        else:
            result += char
    return result

input_str = "Hello, World!"
output_str = uppercase(input_str)
print(output_str)
