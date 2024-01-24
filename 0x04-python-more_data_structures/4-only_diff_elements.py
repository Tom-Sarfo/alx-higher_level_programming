#!/usr/bin/python3

def only_diff_elements(set_1, set_2):

    uniq_list = []

    for item_1 in set_1:
        for item_2 in set_2:
            if item_1 not in set_2:
                uniq_list.append(item_1)
            if item_2 not in set_1:
                uniq_list.append(item_2)

    comp_set = set(uniq_list)

    return (comp_set)
