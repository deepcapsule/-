# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:22:51 2019

@author: wangchx
"""

from node import Node
from abstractbag import AbstractBag


class LinkedBag(AbstractBag):
    """A link-based bag implementation."""
    
    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the 
        contents of sourceCollection, if it's present."""
        self._items = None
        AbstractBag.__init__(self, sourceCollection)
    
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._items
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next
                  
    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = None
    
    def add(self, item):
        """Adds item to self."""
        # Check array memory here and increase it if necessary
        self._items = Node(item, self._items)
        self._size += 1
    
    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise if necessary
        if item not in self:
            raise KeyError(str(item) + " not in bag")
        # Search for the node containing the target item
        # probe will point to the target node, and trailer
        # will point to the one before it, if it exists
        probe = self._items
        trailer = None
        for targetItem in self:
            if targetItem == item:
                break
            trailer = probe
            probe = probe.next
        
        # Unclock the node to be deleted, either the first one
        # or the one thereafter
        if probe == self._items:
            self._items = self._items.next
        else:
            trailer.next = probe.next
        # Decrement logical size
        self._size -= 1