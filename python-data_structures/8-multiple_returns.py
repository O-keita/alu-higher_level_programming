#!/usr/bin/python3
def multiple_returns(sentence):
    string_len = len(sentence)
    firt_char = sentence[0]
    my_tuple = ()
    if sentence == "":
        my_tuple[0] = None
        my_tuple[1] = string_len
        return my_tuple
    else:
        my_tuple[0] = string_len
        my_tuple[0] = first_char
        return my_tuple

