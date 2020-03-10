# -*- coding: utf-8 -*-
"""
abstractcollection.py
Created on Wed Mar  6 08:26:51 2019

@author: wangchx
"""

class AbstractCollection(object):
    """An abstractbag implementation."""
    
    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the 
        contents of sourceCollection, if it's present."""
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
        

    # Acessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0,
        or False otherwise."""
        return len(self) == 0
    
    def __len__(self):
        """Returns the number of items in self."""
        return self._size
    
    
    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result
    
    def __str__(self):
        """Returns the string representation of self."""
        return "[" + ", ".join(map(str,self)) + "]"
    
    def  __eq__(self, other):
        """Returns true if self equals other,
        or False otherwise."""
        if self is other:
            return True
        if type(self) != type(other) or \
            len(self) != len(other):
            return False
        otherIter = iter(other)
        for item in self:
            if  item != next(otherIter):
                return False
        return True