#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    cpy_list = my_list.copy()

    list_len = len(my_list)

    if idx < 0 or idx >= list_len:
        return (cpy_list)
    else:
        cpy_list[idx] = element

    return (cpy_list)
