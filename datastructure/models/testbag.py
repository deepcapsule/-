# -*- coding: utf-8 -*-
"""
File: testbag.py
Created on Tue Mar  5 11:19:07 2019

@author: wangchx
"""

from arraybag import ArrayBag
from linkedbag import LinkedBag

def test(bagType):
    """Expects a bag type as an argument and use some tests
    on objects of that type."""
    lyst = [2019, 3, 5, 11, 24]
    print("The list of items added is: ", lyst)
    b1 = bagType(lyst)
    print("Expect 5: ", len(b1))
    print("Expect the bag's string: ", b1)
    print("Expect True: ", 2019 in b1)
    print("Expect False: ", 2018 in b1)
    print("Expect the items on separate lines: ")
    for item in b1:
        print(item)
    b1.clear()
    print("Expect {}: ", b1)
    b1.add(30)
    b1.remove(30)
    print("Expect {}: ", b1)
    b1 = bagType(lyst)
    b2 = bagType(b1)
    print("Expect True: ", b1 == b2)
    print("Expect False: ", b1 is b2)
    print("Expect two of each item: ", b1 + b2)
    for item in lyst:
        b1.remove(item)
    print("Expect {}: ", b1)
    print("Expect crash with KeyErroe: ")
    b2.remove(100)
    
# test(ArrayBag)
test(ArrayBag)