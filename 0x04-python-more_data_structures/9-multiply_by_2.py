#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nu_dir = a_dictionary.copy()
    list_keys = list(nu_dir.keys())

    for i in list_keys:
        nu_dir[i] *= 2

    return (nu_dir)
