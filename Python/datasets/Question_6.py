# -*- coding: utf-8 -*-
"""
Name: Sandipto Sanyal
PGID: 12010004
"""

def any_uppercase1(s): 
    for c in s:
        if c.isupper(): 
            return True
        else:
            return False
        
def any_uppercase2(s):
    for c in s:
        if 'c'.isupper():
            return 'True'
        else:
            return 'False'

def any_uppercase3(s):
    for c in s:
        flag = c.isupper()
    return flag

def any_uppercase4(s):
    flag = False
    for c in s:
        flag = flag or c.isupper()
    return flag

def any_uppercase5(s):
    for c in s:
        if not c.isupper():
            return False
    return True

test1 = "this Is a test"
test2 = "THISISATEST"
print(any_uppercase5(test2))