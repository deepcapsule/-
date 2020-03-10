# -*- coding: utf-8 -*-
"""
File: arrayqueue.py 
Created on Wed Mar 13 08:42:54 2019

@author: wangchx
"""

from abstractcollection import AbstractCollection
from arrays import Array


class ArrayQueue(AbstractCollection):
    """An array-based circle queue implementation."""
    
    # Class Variable
    # 循环队列，最大长度为20，其中一个位置闲置不存数据,用来被尾指针指向
    DEFAULT_CAPACITY = 21
    
    # Constructor
    def __init__(self, sourceCollection=None):
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)
        self._front = 0
        self._rear = 0
        AbstractCollection.__init__(self, sourceCollection)
        
    # Acessors
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._front
        while cursor != self._rear:
            yield self._items[cursor]
            cursor += 1
            if cursor >= ArrayQueue.DEFAULT_CAPACITY:
                cursor = 0
    
    def peek(self):
        """Returns the item at front of the queue.
        Precondition: the queue is not empty."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        return self._items[self._front]
    
    # Mutators
    def clear(self):
        """Make self become empty."""
        self._size = self._front = self._rear = 0
        
    def add(self, newItem):
        """Adds newItem to the rear of the queue."""
        newRear = self._rear + 1
        if newRear >= ArrayQueue.DEFAULT_CAPACITY:
            newRear = 0
        if newRear == self._front:
            raise AttributeError("The queue is full.")
        self._items[self._rear] = newItem
        self._rear = newRear
        self._size += 1
        
    def pop(self):
        """Removes and returns the item at front of the queue.
        Preconditon: the queue is not empty."""
        # Check preconditon here
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        oldItem = self._items[self._front]
        self._front += 1
        if self._front >= ArrayQueue.DEFAULT_CAPACITY:
            self._front = 0
        self._size -= 1
        return oldItem
        