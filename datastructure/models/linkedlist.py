# -*- coding: utf-8 -*-
"""
File: linkedlist.py
Created on Fri Mar 15 17:07:59 2019

@author: wangchx
"""

from node import TwoWayNode
from abstractlist import AbstractList


class LinkedList(AbstractList):
    """A linked-based list implementation."""
    
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        #Uses a circular struture with a sentinel node
        self._head = TwoWayNode()
        self._head.previous = self._head.next = self._head
        AbstractList.__init__(self, sourceCollection)
        
        # Accessor methods
        def __iter__(self):
            """Supports iteration over a view of self."""
            cursor = self._head.next
            while cursor != self._head:
                yield cursor.data
                cursor = cursor.next
                
        # Helper method returns node at position i
        def _getNode(self, i):
            """Helper method: returns a pointer to the node
            at positon i."""
            if i == len(self):
                return self._head
            if i == len(self) - 1:
                return self._head.previous
            probe = self._head.next
            while i > 0:
                probe = probe.next
                i -= 1
            return probe
        
        #Mutator methods
        def __getitem__(self, i):
            """Precondition: 0 <= i < len(self)
            Returns the item at position i."""
            if i < 0 or i >= len(self):
                raise IndexError("List index out of range")
            return self._getNode(i).data
        
        def __setitem__(self, i, item):
            """Precondition: 0 <= i < len(self)
            Replace the item at position i.
            Raises: IndexError."""
            if i < 0 or i >= len(self):
                raise IndexError("List index out of range")
            self._getNode(i).data = item
            
        def insert(self, i, item):
            """Inserts the item at position i."""
            if i < 0:
                i = 0
            elif i > len(self):
                i = len(self)
            theNode = self._getNode(i)
            newNode = TwoWayNode(item, theNode.previous, theNode)
            theNode.previous.next = newNode
            theNode.previous = newNode
            self._size += 1
            self.incModCount()
            
        def pop(self, i=None):
            """Precondition: 0 <= i < len(self)
            Removes and returns the item at position i.
            If i ins None, i is given a default of len(self) - 1.
            Raises: IndexError."""
            if i == None:
                i = len(self) - 1
            if i < 0 or i >= len(self):
                raise IndexError("List index out of range")
            theNode = self._getNode(i)
            item = theNode.data
            theNode.previous.next = theNode.next
            theNode.next.previous = thenode.previous
            self._size -= 1
            self.incModCount()
            return item
        
            