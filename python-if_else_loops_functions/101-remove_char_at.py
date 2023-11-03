#!/usr/bin/python3
def remove_char_at(s, n):
    if 0 <= n < len(s):
        return s[:n] + s[n+1:]
    else:
        return s  # If n is out of range, return the original string

result_string = remove_char_at(original_string, 3)
