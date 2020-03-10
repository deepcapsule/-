# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 13:56:43 2019

@author: wangchx
"""


from arrays import Array

class Grid(object):
    """Represents a two-dimensional array."""
    
    def __init__(self, rows, columns, fillValue = None):
        self._data = Array(rows)
        for row in range(rows):
            self._data[row] = Array(columns,fillValue)
            
    def getHeight(self):
        """Returns the number of rows."""
        return len(self._data)
    
    def getWidth(self):
        """Return the number of columns."""
        return(len(self._data[0]))
    
    def __getitem__(self,index):
        """Supports two-dimensional indexing with [row][column]."""
        return self._data[index]
    
    def __str__(self):
        """Returns a string representation of the grid."""
        result = ""
        for row in range(self.getHeight()):
            for column in range(self.getWidth()):
                result += str(self._data[row][column]) + " "
            result += '\n'
        return result
    