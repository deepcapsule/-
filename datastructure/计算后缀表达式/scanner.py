# -*- coding: utf-8 -*-
"""
File: scanner.py
Created on Tue Mar 12 10:10:45 2019

@author: wangchx
"""

class Scanner(object):
    
    def __init__(self, sourceStr):
        self._handledStr = sourceStr.split()
        self._size = len(self._handledStr)
        self._index = 0
        
    def hasNext(self):
        return self._index < self._size
    
    def next(self):
        if self.hasNext():
            self._index += 1
            return self._handledStr[self._index - 1]
        else:
            raise AttributeError('It is empty')
            
