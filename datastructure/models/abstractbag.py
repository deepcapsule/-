# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:38:31 2019

@author: wangchx
"""
from abstractcollection import AbstractCollection


class AbstractBag(AbstractCollection):
    """An abstractbag implementation."""
    
    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the 
        contents of sourceCollection, if it's present."""
        AbstractCollection.__init__(self, sourceCollection)
   
    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str,self)) + "}"
     
    def  __eq__(self, other):
        """Returns true if self equals other,
        or False otherwise."""
        if self is other:
            return True
        if type(self) != type(other) or \
            len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True
