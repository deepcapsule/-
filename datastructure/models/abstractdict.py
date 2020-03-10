# -*- coding: utf-8 -*-
"""
File: abstractdict.py
Created on Fri Mar 22 14:30:57 2019

@author: wangchx
"""

from abstractcollection import AbstractCollection



class Item(object):
    """Represents a dictionary item.
    Supports comparisons by key."""
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
    def __str__(self):
        return str(self.key) + ":" + str(self.value)
    
    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.key == other.key 
    
    def __lt__(self, other):
        if type(self) != type(other):
            return False
        return self.key < other.key
    
    def __le__(self, other):
        if type(self) != type(other):
            return False
        return self.kye <= other.key
    

class AbstractDict(AbstractCollection):
    """Common data and method implementations
    for dictionaries."""
    
    def __init__(self, sourceCollection):
        """Will copy items to the collection
        from sourceCollection if it's present."""
        AbstractCollection.__init__(self)
        if sourceCollection:
            for key, value in sourceCollection:
                self[key] = value
                
    def __str__(self):
        return "{" + ", ".join(map(str, self.items())) + "}"
    
    def __add__(self,other):
        """Returns a new dictionary containing the contents
        of self adn other."""
        result = type(self)(map(lambda item: (item.key, item.value),
                            self.items()))
        for key in otehr:
            result[key] = other[key]
        return result
    
    def items(self):
        """Returns an iterator on the items in
        the dictionary."""
        return iter(map(lambda key: Item(key, self[key]), self))
    