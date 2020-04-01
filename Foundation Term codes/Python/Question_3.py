# -*- coding: utf-8 -*-
"""
Name: Sandipto Sanyal
PGID: 12010004
"""

def GCD(a, b, c):
    list_of_integers = [a, b, c]
    minimum_no = min(list_of_integers)
    gcd = 1
    for i in range(1,minimum_no+1):
        divisibility_condition = (a%i==0) & (b%i==0) & (c%i==0)
        if divisibility_condition:
            gcd = i
    return gcd

print(GCD(18,12,24))