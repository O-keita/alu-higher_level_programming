#!/usr/bin/python3
""" 0-read_file.py """


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
