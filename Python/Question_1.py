# -*- coding: utf-8 -*-
"""
Name: Sandipto Sanyal
PGID: 12010004
"""

def price(no_of_copies):
    cover_price = 200
    discount_percentage = 0.25
    shipping_cost = {'first_copy': 40,
                     'additional_copies': 10
                     }
    total_wholesale_cost = (cover_price - discount_percentage*cover_price)*no_of_copies + \
    shipping_cost['first_copy'] +  shipping_cost['additional_copies']*(no_of_copies-1)
    return total_wholesale_cost

no_of_copies = 60
print("Total wholesale cost for {} copies = {}".format(no_of_copies,price(no_of_copies)))