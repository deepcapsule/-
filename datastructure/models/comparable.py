# -*- coding: utf-8 -*-
"""
file: comparable
Created on Thu Mar 14 08:49:28 2019

@author: wangchx
"""


class Comparable(object):
    """Wrapper class for items that are not comparable."""
    
    def __init__(self, data, priority = 1):
        self._data = data
        self._priority = priority
        
    def __str__(self):
        """Returns the string rep of the contained datum."""
        return str(self.__data)
    
    def __eq__(self, other):
        """Returns True if the contained priorities are equal
        or False otherwise."""
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self._priority == other._priority
    
    def __lt__(self, other):
        """Returns True if self's priority < other's priority,
        or False otherwise."""
        return self._priority < other._priority
    
    def __le__(self, other):
        """Returns True if self's priority <= other's priority,
        or False otherwise."""
        return self._priority <= other._priority
    
    def getData(self):
        """Returns the contained datum."""
        return self._data
    
    def getPriority(self):
        """Returns the contained priority."""
        return self._priority
    