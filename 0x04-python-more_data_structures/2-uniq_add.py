#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_sum = 0

    gen_set = set()

    gen_set = set(my_list)

    for item in gen_set:
        uniq_sum += item

    return (uniq_sum)
