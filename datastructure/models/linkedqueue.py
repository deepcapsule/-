# -*- coding: utf-8 -*-
"""
File: linkedqueue.py
Created on Tue Mar 12 16:52:52 2019

@author: wangchx
"""

from abstractcollection import AbstractCollection
from node import Node


class LinkedQueue(AbstractCollection):
    """Link-based queue implementation."""
    
    # Constructor
    def __init__(self, sourceCollection=None):
        self._front = None
        self._rear = None
        AbstractCollection.__init__(self, sourceCollection)
        
    # Acessors
    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from front to rear of queue."""
        def visitNodes(node):
            if not node is None:
                visitNodes(node.next)
                tempList.append(node.data)
        tempList = list()
        visitNodes(self._front)
        return iter(tempList)
    
    def peek(self):
        """Returns the item at front of the queue.
        Precondition: the queue is not empty."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        return self._front.data
    
    # Mutators
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._front = None
        self._rear = None

    def add(self, newItem):
        """Adds newItem to the rear of the queue."""
        newNode = Node(newItem)
        if self.isEmpty():
            self._front = newNode
        else:
            self._rear.next = newNode
        self._rear = newNode
        self._size += 1
        
    def pop(self):
        """Removes and returns the item at front of the queue.
        Preconditon: the queue is not empty."""
        # Check preconditon here
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        oldItem = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return oldItem