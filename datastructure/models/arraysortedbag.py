# -*- coding: utf-8 -*-
"""
File: arraysortedbag.py
Created on Tue Mar  5 15:12:38 2019

@author: wangchx
"""

from arraybag import ArrayBag


class ArraySortedBag(ArrayBag):
    """An array-based sorted bag implementation."""
    
    # Constuctor
    def __init__(self, sourceCollection=None):
        """Sets teh initial state of self, which includes
        the contents of sourceCollection, if it's present."""
        ArrayBag.__init__(self, sourceCollection)
        
    # Access methods
    def __contains__(self, item):
        """Returns True if item is in self, or False otherwise."""
        left = 0
        right = len(self) - 1
        while left < right:
            midPoint = (left + right) // 2
            if self._items[midPoint] == item:
                return True
            elif self._items[midPoint] > item:
                right = midPoint
            else:
                left = midPoint
        return False
    
    # Mutator methods
    def add(self, item):
        """Adds item to self."""
        # Empty or last item, call ArrayBag.add
        if self.isEmpty() or item >= self._items[len(self) - 1]:
            ArrayBag.add(self, item)
        else:
            # Resize the array if it is full here
            # Search for first item >= new item
            targetIndex = 0
            while item > self._items[targetIndex]:
                targetIndex += 1
            # Open a hole for new item
            for i in range(len(self), targetIndex, -1):
                self._items[i] = self._items[i - 1]
            # Insert item and update size
            self._items[targetIndex] = item
            self._size += 1