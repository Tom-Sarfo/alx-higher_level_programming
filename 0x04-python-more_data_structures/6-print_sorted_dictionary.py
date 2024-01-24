#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    key_items = []

    for key in a_dictionary.keys():
        key_items.append(key)

    key_items = sorted(key_items)

    for item in key_items:
        print("{}: {}".format(item, a_dictionary[item]))
