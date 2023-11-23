#!/usr/bin/python3
"""Json sucks"""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file



def main():
    # Load existing items from file or initialize an empty list
    try:
        items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        items = []

    # Add command line arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list to 'add_item.json'
    save_to_json_file(items, 'add_item.json')

    # Print the contents of the file
    print("Contents of 'add_item.json':")
    print(load_from_json_file('add_item.json'))

if __name__ == "__main__":
    main()
