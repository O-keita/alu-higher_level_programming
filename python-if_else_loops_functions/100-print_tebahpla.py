#!/usr/bin/python3
for char_code in range(ord('z'), ord('a') - 1, -1):
    char = chr(char_code)
    if char_code % 2 == 1:
        char = char.upper() if char.islower() else char.lower()
    print("{}".format(char), end='')

# Output: zYxWvUtSrQpOnMlKjIhGfEdCbA
