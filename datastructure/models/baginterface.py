# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:08:17 2019

@author: wangchx
"""


class BagInterface(object):
    """Interface for all bag types."""
    # Construtor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        pass

    # Acessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0,
        or False otherwise."""
        return True
    
    def __len__(self):
        """Returns the number of items in self."""
        return 0
    
    def __str__(self):
        """Returns the string representation of self."""
        return ""
    
    def __iter__(self):
        """Supports iteration over a view of self."""
        return None
    
    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        return None
    
    def  __eq__(self, other):
        """Returns true if self equals other,
        or False otherwise."""
        return False
        
    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        pass
    
    def add(self, item):
        """Adds item to self."""
        pass
    
    def remove(self,item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        Postcondition: item is removed from self."""
        pass
   
   
    
