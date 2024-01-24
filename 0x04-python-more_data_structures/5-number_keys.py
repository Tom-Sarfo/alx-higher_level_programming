#!/usr/bin/python3
def number_keys(a_dictionary):
    val = 0
    list_kys = list(a_dictionary.keys())

    for i in list_kys:
        val += 1

    return (val)
