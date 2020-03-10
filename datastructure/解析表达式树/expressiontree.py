# -*- coding: utf-8 -*-
"""
File: expressiontree.py
Created on Thu Mar 21 09:15:28 2019

@author: wangchx
"""


class LeafNode(object):
    """Represents an integer."""
    
    def  __init__(self, data):
        self._data  = data
        
    def postfix(self):
        return str(self)
    
    def prefix(self):
        return str(self)
    
    def infix(self):
        return  str(self)
    
    def value(self):
        return self._data
    
    def __str__(self):
        return str(self._data)
    

class InteriorNode(object):
    """Represent an operator and its two oprands."""
    
    def __init__(self, op, leftPer, rightOper):
        self._oprator = op
        self._leftOperand = leftPer
        self._rightOperand = rightOper
        
    def postfix(self):
        return self._leftOperand.postfix() + ' ' + \
                self._rightOperand.postfix() + ' ' + \
                self._oprator
                
    def prefix(self):
        return self._oprator + ' ' + \
                self._leftOperand.prefix() + ' ' + \
                self._rightOperand.prefix()
                
    def infix(self):
        return '(' + self._leftOperand.infix() + ' ' + \
                self._oprator + ' ' + \
                self._rightOperand.infix() + ')'
    def value(self):
        def recurse(op, lo, ro):
            result = None
            if op == '+':
                result = lo.value() + ro.value()
            elif op == '-':
                result = lo.value() - ro.value()
            elif op == '*':
                result = lo.value() * ro.value()
            elif op == '/':
                result = lo.value() / ro.value()
            return result
        return recurse(self._oprator, self._leftOperand,
                       self._rightOperand)
        
        
