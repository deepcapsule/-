# -*- coding: utf-8 -*-
"""
File: scanner.py
Created on Wed Mar 20 16:45:28 2019

@author: wangchx
"""
from treetoken import Token

class Scanner(object):
    """扫描器"""
    
    def __init__(self, expr):
        self._expr = self._deal(expr)
        self._cursor = 0
        
    def get(self):
        if self._cursor < len(self._expr):
            token = Token(self._expr[self._cursor])
            return token
        
    def tonext(self):
        if self._cursor < len(self._expr):
            self._cursor += 1
    
    def first(self):
        if self._cursor >= len(self._expr):
            self._cursor = 0
            
    def __str__(self):
        return ' '.join(self._expr)
        
    def _deal(self, expression):
        lyst = list()
        digits = ''
        for item in expression:
            if item.isdigit():
                digits += item
            elif item.isspace():
                continue
            else:
                if digits:
                    lyst.append(digits)
                    digits = ''
                if item in ('(', ')', '+', '-', '*', '/'):
                    lyst.append(item)
                else:
                    raise ValueError("bad symbol in input: " + item)
        if digits:
            lyst.append(digits)
            digits = ''
        return lyst
    
        
    