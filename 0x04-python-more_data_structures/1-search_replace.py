#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nu_list = list(map(lambda x: replace if x == search else x, my_list))
    return (nu_list)
