#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    add_score = 0

    sum_weight = 0

    for score, weight in my_list:
        add_score += score * weight

        sum_weight += weight

    if sum_weight == 0:
        return 0
    else:
        return add_score / sum_weight
