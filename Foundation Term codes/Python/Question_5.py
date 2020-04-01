# -*- coding: utf-8 -*-
"""
Name: Sandipto Sanyal
PGID: 12010004
"""

def is_triangle(a,b,c):
    if ((a+b >c) & (b+c > a) & (c+a >b)):
        print("Yes")
    else:
        print("No")
        
is_triangle(3,4,5)
is_triangle(1,2,3)