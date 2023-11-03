#!/usr/bin/python3
def remove_char_at(s, n):
    if 0 <= n < len(s):
        return s[:n] + s[n+1:]
    else:
        return s  # If n is out of range, return the original string

# Example usage:
original_string = "Hello, World"
result_string = remove_char_at(original_string, 3)
print(result_string)  # Output: "Helo, World"
