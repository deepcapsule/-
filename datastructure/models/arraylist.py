# -*- coding: utf-8 -*-
"""
File: arraylist.py
Created on Fri Mar 15 15:07:54 2019

@author: wangchx
"""

from arrays import Array
from abstractlist import AbstractList
from arraylistiterator import ArrayListIterator


class ArrayList(AbstractList):
    """An array-based list implementation."""
    
    DEFAULT_CAPACITY = 20
    
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the 
        contents of sourceCollection, if it's present."""
        self._items = Array(ArrayList.DEFAULT_CAPACITY)
        AbstractList.__init__(self, sourceCollection)
        
    # Acessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1
            
    def __getitem__(self, i):
        """Precondition: 0 <= i < len(self)
        Returns the item at position i.
        Raise: IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        return self._items[i]
    
    # Mutator methods
    def __setitem__(self, i, item):
        """Precondition: 0 <= i <len(self)
        Replace the item at position i.
        Raise: IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        self._items[i] = item
        
    def insert(self, i, item):
        """Inserts the item at position i."""
        # Resize array here if necessary
        if i < 0:
            i = 0
        elif i > len(self):
            i = len(self)
        if i < len(self):
            for j in range(len(self), i, -1):
                self._items[j] = self._items[j - 1]
        self._items[i] = item
        self._size += 1
        self.incModCount()
        
    def pop(self, i=None):
        """Precondition: 0 <= i < len(self).
        Removes and returns the item at position i.
        if i is None, i is given a default of len(self)-1.
        Raises: IndexError."""
        if i is None:
            i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        item = self._items[i]
        for j in range(i, len(self) - 1):
            self._items[j] = self._items[j + 1]
        self._size -= 1
        self.incModCount()
        #Resize array here is necessary
        return item
    
    def listIterator(self):
        """Returns a list iterator."""
        return ArrayListIterator(self)