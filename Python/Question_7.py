# -*- coding: utf-8 -*-
"""
Name: Sandipto Sanyal
PGID: 12010004
"""

def cumulative_sum(t):
    cumul_list = [] # it stores the cumulative sums of elements
    last_cum_no = 0 # it will update the last updated cumulative sum
    for elem in t:
        # append sum of each element to cumul_list
        cumul_list.append(last_cum_no + elem)
        last_cum_no = cumul_list[-1] # access the last uploaded sum and update the last_cum_no
    return cumul_list

print(cumulative_sum([10,12,15,20,36]))