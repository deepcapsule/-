# -*- coding: utf-8 -*-
"""
File: minarrayheap.py
Created on Thu Mar 21 14:25:49 2019

@author: wangchx
"""

from abstractcollection import AbstractCollection
from arrays import Array


class MinArrayHeap(AbstractCollection):
    """An array-based heap implementation."""
    
    DEFAULT_CAPACITY = 10
    
    def __init__(self, sourceCollection=None):
        self._items = Array(MinArrayHeap.DEFAULT_CAPACITY)
        AbstractCollection.__init__(self, sourceCollection)
        
    def add(self, item):
        self._items[len(self)] = item
        curPos = len(self)
        self._size += 1
        while curPos > 0:
            parent = (curPos - 1) // 2
            parentItem = self._items[parent]
            if parentItem <= item:
                break
            else:
                self._items[curPos] = parentItem
                self._items[parent] = item
                curPos = parent
                
    def pop(self):
        if self.isEmpty():
            raise Exception("Heap is empty")
        topItem = self._items[0]
        bottomItem = self._items[len(self) - 1]
        if len(self) == 1:
            self._size -= 1
            return bottomItem
        
        def minHeapfy(heap, size, root):
            left = 2*root + 1
            right = 2*root + 2
            smaller = root
            if left < size and heap[smaller] > heap[left]:
                smaller = left
            if right < size and heap[smaller] > heap[right]:
                smaller = right
            if smaller != root:
                heap[root], heap[smaller] = heap[smaller], heap[root]
                minHeapfy(heap, size, smaller)
        
        self._items[0] = bottomItem
        minHeapfy(self._items, len(self) - 1, 0)
        self._size -= 1
        return topItem
                
    def __iter__(self):
        temp = type(self)()
        for i in range(len(self)):
            temp.add(self._items[i])
        while not temp.isEmpty():
            yield temp.pop()
        