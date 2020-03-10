# -*- coding: utf-8 -*-
"""
File: teststack.py
Created on Mon Mar 11 14:14:49 2019

@author: wangchx
"""

from arraystack import ArrayStack
from linkedstack import LinkedStack

def test(stackType):
    # Test any implementation with the same code
    s = stackType()
    print("Length:",len(s))
    print("Empty:",s.isEmpty())
    print("Push 1-9")
    for i in range(9):
        s.push(i + 1)
    print("Peeking:",s.peek())
    print("Items(bottom to top):",s)
    print("Length:",len(s))
    print("Empty:",s.isEmpty())
    theClone = stackType(s)
    print("Items in clone (bottom to top):",theClone)
    theClone.clear()
    print("Length of clone after clear:",len(theClone))
    print("Push 11")
    s.push(11)
    print("Poping items (top to bottom):", end="")
    while not s.isEmpty():
        print(s.pop(), end=" ")
        print("\nLength:",len(s))
        print("Empty:",s.isEmpty())
            
# test
test(ArrayStack)  