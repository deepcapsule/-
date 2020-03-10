# -*- coding: utf-8 -*-
"""
File: treetoken.py
Created on Wed Mar 20 16:22:11 2019

@author: wangchx
"""


class Token(object):
    
    UNKNOW = 0
    
    INT = 1
    
    PLUS = 3
    MINUS = 4
    MUL = 5
    DIV = 6
    
    L_PAR = 7
    R_PAR = 8
    
    def __init__(self, value):
        """initial"""
        self._value = value
        self._type = self._makeType(value)
        if self._type == Token.INT:
            self._value = int(value)
            
    def getValue(self):
        return self._value
    
    def getType(self):
        return self._type
    
    def __str__(self):
        return str(self._value)
    
    def _makeType(self, value):
        if type(value) == int or value.isdigit():
            return Token.INT
        elif value == '+':
            return Token.PLUS
        elif value == '-':
            return Token.MINUS
        elif value == '*':
            return Token.MUL
        elif value == '/':
            return Token.DIV
        elif value == '(':
            return Token.L_PAR
        elif value == ')':
            return Token.R_PAR
        else:
            return Token.UNKNOW
