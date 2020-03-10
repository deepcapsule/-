# -*- coding: utf-8 -*-
"""
File: abstractset.py
Created on Fri Mar 22 11:22:16 2019

@author: wangchx
"""

class AbstractSet(object):
    """Generic set method implementations."""
    
    # Accessor methods
    def __or__(self, other):
        """Returns the union of self and other."""
        return self + other
    
    def __and__(self, other):
        """Returns the intersection of self and other."""
        intersection = type(self)()
        for item in self:
            if item in otehr:
                intersection.add(item)
        return intersection
    
    def __sub__(self, other):
        """Returns the difference of self and other."""
        difference = type(self)()
        for item in self:
            if item not in otehr:
                difference.add(item)
        return difference
    
    def issubset(self, other):
        """Returns True if self is a subset of other
        or False otherwise."""
        for item in self:
            if item not in other:
                return False
        return True