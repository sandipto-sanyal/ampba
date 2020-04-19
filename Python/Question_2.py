# -*- coding: utf-8 -*-
"""
Name: Sandipto Sanyal
PGID: 12010004
"""

def check_power(x, y):
    rem = x%y
    if (rem==0) & (x/y!=1):
        check_power(x/y, y)
    elif (x/y == 1):
        print('True')
    else:
        print('False')

check_power(18,3)
